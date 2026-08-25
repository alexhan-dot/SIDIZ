"""Print a condensed DOM skeleton for extracted KR sections.

Collapses whitespace, strips inline <style> blocks and shortens asset URLs, so
a section's structure fits on screen and can be transcribed into Liquid.

Usage: python scripts/skeleton.py t90 product_warranty product_spec ...
"""

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]


def condense(doc, limit):
    doc = re.sub(r"<style data-shopify>.*?</style>", "", doc, flags=re.S)
    doc = re.sub(r"<!--.*?-->", "", doc, flags=re.S)
    doc = re.sub(r"\s+", " ", doc)
    # shorten long asset urls but keep the tail so the file is identifiable
    doc = re.sub(r'(src|poster|href)="[^"]*?([^/"]{0,30})"', r'\1="…\2"', doc)
    doc = re.sub(r'srcset="[^"]*"', 'srcset="…"', doc)
    doc = re.sub(r'(sizes|loading|decoding|preload|playsinline|autoplay|loop|muted)="[^"]*"', "", doc)
    doc = doc.replace("> <", "><").replace("><", ">\n<")
    lines = [l.rstrip() for l in doc.split("\n") if l.strip()]
    return "\n".join(lines[:limit])


def main():
    handle = sys.argv[1] if len(sys.argv) > 1 else "t90"
    names = sys.argv[2:] or ["product_warranty"]
    limit = 60
    src = ROOT / "data" / "products" / handle / "sections"

    for name in names:
        f = src / f"{name}.html"
        if not f.exists():
            print(f"\n########## {name}: not extracted")
            continue
        print(f"\n########## {name} ##########")
        print(condense(f.read_text(encoding="utf-8"), limit))


if __name__ == "__main__":
    main()
