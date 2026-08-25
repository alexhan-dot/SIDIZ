"""Harvest the kr.sidiz.com theme's public CSS/JS/font assets.

The KR theme's Liquid source is not downloadable without admin access, but its
compiled stylesheets, scripts and webfonts are served publicly from the Shopify
CDN. Those give us the real design tokens and component styles to rebuild
against.

Writes into data/kr-theme/assets/ and prints a manifest summary.
"""

import pathlib
import re
import sys
import time
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "kr-raw"
OUT = ROOT / "data" / "kr-theme" / "assets"

UA = "Mozilla/5.0 (compatible; SIDIZ-AU-migration/1.0)"

PAGES = [
    "https://kr.sidiz.com/",
    "https://kr.sidiz.com/products/t60",
    "https://kr.sidiz.com/products/t80-headrest",
    "https://kr.sidiz.com/products/t60-re-life",
    "https://kr.sidiz.com/collections/work",
    "https://kr.sidiz.com/pages/brand-story-1",
    "https://kr.sidiz.com/pages/history",
    "https://kr.sidiz.com/pages/find-your-chair",
    "https://kr.sidiz.com/pages/compare",
    "https://kr.sidiz.com/pages/easy-repair",
    "https://kr.sidiz.com/blogs/s-culture",
    "https://kr.sidiz.com/cart",
]

ASSET_RE = re.compile(r'["\'(]((?://|https://)[^"\'()\s]*?/cdn/shop/t/\d+/assets/[^"\'()\s]+)')
FONT_RE = re.compile(r'url\(["\']?([^"\')]+\.(?:woff2?|otf|ttf))["\']?\)', re.I)


def fetch(url, binary=False):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
    return data if binary else data.decode("utf-8", errors="replace")


def norm(u):
    if u.startswith("//"):
        u = "https:" + u
    return u.split("?")[0]


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    urls = set()

    for page in PAGES:
        cache = RAW / ("page-" + re.sub(r"\W+", "_", page.split("kr.sidiz.com")[1] or "index").strip("_") + ".html")
        try:
            html = cache.read_text(encoding="utf-8") if cache.exists() else fetch(page)
            if not cache.exists():
                cache.write_text(html, encoding="utf-8")
                time.sleep(1)
        except Exception as exc:  # noqa: BLE001
            print(f"  page failed {page}: {exc}", file=sys.stderr)
            continue
        found = {norm(u) for u in ASSET_RE.findall(html)}
        urls |= found
        print(f"{page:52} {len(found):>3} assets")

    css = sorted(u for u in urls if u.endswith(".css"))
    js = sorted(u for u in urls if u.endswith(".js"))
    other = sorted(u for u in urls if not u.endswith((".css", ".js")))

    print(f"\nunique assets: {len(urls)}  (css {len(css)}, js {len(js)}, other {len(other)})")

    fonts = set()
    saved = 0
    for u in css + js + other:
        name = u.rsplit("/", 1)[-1]
        dest = OUT / name
        if dest.exists():
            continue
        try:
            body = fetch(u, binary=True)
        except Exception as exc:  # noqa: BLE001
            print(f"  skip {name}: {exc}", file=sys.stderr)
            continue
        dest.write_bytes(body)
        saved += 1
        if u.endswith(".css"):
            for f in FONT_RE.findall(body.decode("utf-8", errors="replace")):
                fonts.add(norm(f if f.startswith(("http", "//")) else
                              u.rsplit("/", 1)[0] + "/" + f.lstrip("./")))
        time.sleep(0.2)

    print(f"downloaded {saved} assets -> {OUT.relative_to(ROOT)}")
    if fonts:
        print(f"\nwebfonts referenced ({len(fonts)}):")
        for f in sorted(fonts):
            print("  " + f)
    (OUT.parent / "asset-manifest.txt").write_text(
        "\n".join(sorted(urls)) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
