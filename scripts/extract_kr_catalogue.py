"""Extract the kr.sidiz.com catalogue from the public Shopify JSON feeds.

Produces:
  data/kr-catalogue/variants.csv   - one row per variant (SKU-level working sheet)
  data/kr-catalogue/products.csv   - one row per product (page-level working sheet)
  data/kr-catalogue/bodies/*.html  - raw Korean body_html per product, for translation
"""

import csv
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "kr-raw"
OUT = ROOT / "data" / "kr-catalogue"
BODIES = OUT / "bodies"


def load(name):
    with open(RAW / name, encoding="utf-8") as fh:
        return json.load(fh)


def text_of(html):
    """Rough plain-text length probe — used only to size the translation job."""
    txt = re.sub(r"<[^>]+>", " ", html or "")
    txt = re.sub(r"&[a-z]+;|&#\d+;", " ", txt)
    return re.sub(r"\s+", " ", txt).strip()


def korean_chars(s):
    return len(re.findall(r"[가-힣]", s))


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    BODIES.mkdir(parents=True, exist_ok=True)

    products = load("products.json")["products"]
    collections = {c["handle"]: c for c in load("collections.json")["collections"]}

    prod_rows, var_rows = [], []

    for p in products:
        handle = p["handle"]
        body = p.get("body_html") or ""
        plain = text_of(body)

        (BODIES / f"{handle}.html").write_text(body, encoding="utf-8")

        prices = [int(float(v["price"])) for v in p["variants"] if v.get("price")]
        prod_rows.append({
            "handle": handle,
            "title_ko": p["title"],
            "product_type": p.get("product_type", ""),
            "vendor": p.get("vendor", ""),
            "tags": "|".join(p.get("tags", [])),
            "options": "|".join(o["name"] for o in p.get("options", [])),
            "variant_count": len(p["variants"]),
            "image_count": len(p.get("images", [])),
            "price_krw_min": min(prices) if prices else "",
            "price_krw_max": max(prices) if prices else "",
            "body_chars": len(plain),
            "body_korean_chars": korean_chars(plain),
            "published_at": p.get("published_at") or "",
            "url": f"https://kr.sidiz.com/products/{handle}",
        })

        for v in p["variants"]:
            var_rows.append({
                "product_handle": handle,
                "product_title_ko": p["title"],
                "variant_title_ko": v.get("title", ""),
                "sku": v.get("sku", ""),
                "option1": v.get("option1") or "",
                "option2": v.get("option2") or "",
                "option3": v.get("option3") or "",
                "price_krw": v.get("price", ""),
                "compare_at_krw": v.get("compare_at_price") or "",
                "available": v.get("available", ""),
                "grams": v.get("grams", ""),
            })

    def write(path, rows):
        with open(path, "w", encoding="utf-8", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
            w.writeheader()
            w.writerows(rows)

    write(OUT / "products.csv", prod_rows)
    write(OUT / "variants.csv", var_rows)

    total_ko = sum(r["body_korean_chars"] for r in prod_rows)
    empty = [r["handle"] for r in prod_rows if r["body_chars"] == 0]

    print(f"products      : {len(prod_rows)}")
    print(f"variants      : {len(var_rows)}")
    print(f"collections   : {len(collections)}")
    print(f"korean chars in product bodies: {total_ko:,}")
    print(f"products with empty body      : {len(empty)}")
    if empty:
        print("  " + ", ".join(empty[:10]))


if __name__ == "__main__":
    main()
