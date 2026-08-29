"""Extract EVERY section's raw HTML from a saved kr.sidiz.com page, in DOM order.

extract_section_html.py pulls one section by name and stops at the first match,
which loses every duplicate (a page can hold three product_wb_banner sections
that all differ). This walks the whole document and writes each section as
NN-name.html so duplicates keep their position and identity.

Usage: python scripts/extract_all_sections.py t60-air
Writes: data/products/<handle>/sections/NN-<section>.html
"""

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]

STRIP = re.compile(r"^(?:template|sections)--\d+__")
SUFFIX = re.compile(r"_[A-Za-z0-9]{6}$")

CHROME = {
    "announcement", "header", "site-menu-sidebar", "footer",
    "popups", "sidebar-complementary",
}


def main():
    handle = sys.argv[1]
    doc = (ROOT / "data" / "kr-raw" / f"page-{handle}.html").read_text(encoding="utf-8")
    out = ROOT / "data" / "products" / handle / "sections"
    out.mkdir(parents=True, exist_ok=True)

    idx = 0
    for m in re.finditer(r'<(\w+)([^>]*id="shopify-section-([^"]+)"[^>]*)>', doc):
        raw_name = m.group(3)
        name = SUFFIX.sub("", STRIP.sub("", raw_name))

        tag = m.group(1)
        start = m.start()
        depth = 0
        pos = start
        pattern = re.compile(rf"</?{tag}\b", re.I)
        while True:
            hit = pattern.search(doc, pos)
            if not hit:
                end = len(doc)
                break
            if doc[hit.start() + 1] == "/":
                depth -= 1
                if depth == 0:
                    end = doc.index(">", hit.start()) + 1
                    break
            else:
                depth += 1
            pos = hit.end()

        idx += 1
        if name in CHROME:
            continue
        dest = out / f"{idx:02d}-{name}.html"
        dest.write_text(doc[start:end], encoding="utf-8")
        print(f"{idx:02d} {name:36} {end - start:>9,} bytes")


if __name__ == "__main__":
    main()
