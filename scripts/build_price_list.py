"""Convert kr.sidiz.com KRW prices to AUD, rounded UP to end in 99.

Rule as directed: KRW -> AUD at the live rate, then round up so the price
ends in 99.

Because a flat "end in 99" rule distorts cheap spare parts (a $19 armpad would
become $99), sub-$100 items are also given an "end in 9" figure so the choice
between the two is explicit rather than silently applied.

Writes: data/pricing/price-list.csv  (one row per variant)
        data/pricing/price-summary.csv (one row per product)
"""

import csv
import json
import math
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "pricing"

# Current AU retail, read from the live sidiz.au store on 2026-08-25.
AU_LIVE = {
    "t50-2": 499, "t50": 499, "t50-air-2": 729, "t80": 1029,
    "gc-pro": 1599, "ringo-gen2": 359,
}


def up99(aud):
    """Round up to the next whole dollar ending in 99 (99, 199, 299...)."""
    return math.ceil((aud - 99) / 100) * 100 + 99


def up9(aud):
    """Round up to the next whole dollar ending in 9 (9, 19, 29...)."""
    return math.ceil((aud - 9) / 10) * 10 + 9


def main():
    OUT.mkdir(parents=True, exist_ok=True)

    fx = json.load(open(ROOT / "data" / "kr-raw" / "fx.json", encoding="utf-8"))
    rate = fx["rates"]["AUD"]
    asof = fx["time_last_update_utc"]

    variants = list(csv.DictReader(
        open(ROOT / "data" / "kr-catalogue" / "variants.csv", encoding="utf-8")))
    products = list(csv.DictReader(
        open(ROOT / "data" / "kr-catalogue" / "products.csv", encoding="utf-8")))

    rows = []
    for v in variants:
        if not v["price_krw"]:
            continue
        krw = float(v["price_krw"])
        raw = krw * rate
        # Confirmed rule: end in 99 at $100 and above, end in 9 below $100.
        final = up9(raw) if raw < 100 else up99(raw)
        rows.append({
            "product_handle": v["product_handle"],
            "product_title_ko": v["product_title_ko"],
            "variant_title_ko": v["variant_title_ko"],
            "sku": v["sku"],
            "price_krw": int(krw),
            "aud_raw": round(raw, 2),
            "aud_final": final,
            "rule": "x9" if raw < 100 else "x99",
            "band": "under $100" if raw < 100 else "$100+",
        })

    with open(OUT / "price-list.csv", "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    # product-level summary + comparison against live AU pricing
    summary = []
    by_handle = {}
    for r in rows:
        by_handle.setdefault(r["product_handle"], []).append(r)

    for p in products:
        h = p["handle"]
        rs = by_handle.get(h)
        if not rs:
            continue
        lo = min(r["aud_final"] for r in rs)
        hi = max(r["aud_final"] for r in rs)
        live = AU_LIVE.get(h, "")
        delta = f"{(lo - live) / live * 100:+.0f}%" if live else ""
        summary.append({
            "handle": h,
            "title_ko": p["title_ko"],
            "krw_min": p["price_krw_min"],
            "aud_final_min": lo,
            "aud_final_max": hi,
            "au_live_price": live,
            "change_vs_live": delta,
        })

    with open(OUT / "price-summary.csv", "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(summary[0].keys()))
        w.writeheader()
        w.writerows(summary)

    under = [r for r in rows if r["band"] == "under $100"]
    print(f"rate: 1 KRW = {rate} AUD   (as of {asof})")
    print(f"variants priced      : {len(rows)}")
    print(f"  under $100 raw     : {len(under)}  <- flat x99 rule inflates these")
    print(f"  $100+              : {len(rows) - len(under)}")
    print()
    print("Repricing impact on models already selling on sidiz.au:")
    for s in summary:
        if s["au_live_price"]:
            print(f"  {s['title_ko'][:26]:26} ${s['au_live_price']:>5} -> "
                  f"${s['aud_final_min']:>5}   {s['change_vs_live']}")


if __name__ == "__main__":
    main()
