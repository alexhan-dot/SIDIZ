"""Harvest every image and video used on a kr.sidiz.com product page.

Usage:  python scripts/harvest_product_media.py t90 [--baseline t60]

A product page carries ~400 media URLs, most of which are site-wide chrome
(nav icons, footer badges, menu thumbnails). Subtracting the media of a second
product page leaves the media that actually belongs to this product.

Downloads into data/products/<handle>/media/ and writes media-manifest.csv,
the working sheet for the English rebuild: one row per asset with columns for
the new English filename, alt text and the Korean text it carries.
"""

import csv
import json
import pathlib
import re
import sys
import time
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
UA = "Mozilla/5.0 (compatible; SIDIZ-AU-migration/1.0)"

MEDIA_RE = re.compile(
    r'((?://|https://)[a-z0-9.-]+/cdn/shop/[^"\'()\s\\]+?'
    r'\.(?:jpg|jpeg|png|webp|gif|mp4|webm))',
    re.I,
)
SIZE_SUFFIX_RE = re.compile(
    r"_(\d+x\d*|\d*x\d+|small|medium|large|grande|pico|icon|thumb|compact|master)"
    r"(?=\.[a-z0-9]+$)",
    re.I,
)


def fetch(url, binary=False):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=90) as r:
        data = r.read()
    return data if binary else data.decode("utf-8", errors="replace")


def norm(u):
    if u.startswith("//"):
        u = "https:" + u
    return SIZE_SUFFIX_RE.sub("", u.split("?")[0])


def page_html(handle):
    cache = ROOT / "data" / "kr-raw" / f"page-{handle}.html"
    if cache.exists():
        return cache.read_text(encoding="utf-8")
    html = fetch(f"https://kr.sidiz.com/products/{handle}")
    cache.write_text(html, encoding="utf-8")
    time.sleep(1)
    return html


def media_of(handle):
    return {norm(u) for u in MEDIA_RE.findall(page_html(handle))}


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print("usage: harvest_product_media.py <handle> [--baseline <handle>]")
        raise SystemExit(2)

    handle = args[0]
    baseline = args[1] if len(args) > 1 else "t60"

    out = ROOT / "data" / "products" / handle
    media = out / "media"
    media.mkdir(parents=True, exist_ok=True)

    mine = media_of(handle)
    shared = media_of(baseline) if baseline != handle else set()
    specific = sorted(mine - shared)

    product = json.loads(fetch(f"https://kr.sidiz.com/products/{handle}.json"))["product"]
    gallery = {norm(i["src"]) for i in product.get("images", [])}
    # gallery images must always be kept even if the baseline shares them
    specific = sorted(set(specific) | gallery)

    print(f"{handle}: {len(mine)} media on page, {len(shared)} shared with "
          f"{baseline} -> {len(specific)} product-specific")

    rows = []
    for i, url in enumerate(specific, 1):
        name = url.rsplit("/", 1)[-1]
        dest = media / name
        if dest.exists():
            size = dest.stat().st_size
        else:
            try:
                blob = fetch(url, binary=True)
                dest.write_bytes(blob)
                size = len(blob)
                time.sleep(0.15)
            except Exception as exc:  # noqa: BLE001
                print(f"  skip {name}: {exc}", file=sys.stderr)
                continue

        rows.append({
            "order": i,
            "kr_filename": name,
            "kr_url": url,
            "bytes": size,
            "role": "gallery" if url in gallery else "detail",
            # --- filled during the English rebuild ---
            "has_korean_text": "",
            "kr_text_content": "",
            "en_filename": "",
            "en_alt_text": "",
            "en_text_content": "",
            "action": "",
        })

    if not rows:
        print("no media downloaded")
        return

    with open(out / "media-manifest.csv", "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    total = sum(r["bytes"] for r in rows)
    vids = sum(1 for r in rows if r["kr_filename"].lower().endswith((".mp4", ".webm")))
    print(f"downloaded {len(rows)} files ({vids} video), {total/1024/1024:.1f} MB")
    print(f"manifest -> {(out / 'media-manifest.csv').relative_to(ROOT)}")


if __name__ == "__main__":
    main()
