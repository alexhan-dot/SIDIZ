"""Extract one section's raw HTML from a saved kr.sidiz.com page, verbatim.

Reconstructing a section from its stylesheet means guessing the markup, and a
guess that is 95% right still renders wrong. This pulls the real HTML so the
Liquid can be built by substituting dynamic values into the actual DOM instead.

Usage: python scripts/extract_section_html.py t90 configurator
Writes: data/products/<handle>/sections/<section>.html
"""

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]

STRIP = re.compile(r"^(?:template|sections)--\d+__")
SUFFIX = re.compile(r"_[A-Za-z0-9]{6}$")


def main():
    handle = sys.argv[1] if len(sys.argv) > 1 else "t90"
    want = sys.argv[2] if len(sys.argv) > 2 else "configurator"

    doc = (ROOT / "data" / "kr-raw" / f"page-{handle}.html").read_text(encoding="utf-8")

    # Find the opening tag of the section wrapper, then walk to its matching close.
    for m in re.finditer(r'<(\w+)([^>]*id="shopify-section-([^"]+)"[^>]*)>', doc):
        raw_name = m.group(3)
        name = SUFFIX.sub("", STRIP.sub("", raw_name))
        if name != want:
            continue

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

        html = doc[start:end]
        out = ROOT / "data" / "products" / handle / "sections"
        out.mkdir(parents=True, exist_ok=True)
        dest = out / f"{name}.html"
        dest.write_text(html, encoding="utf-8")

        print(f"{name}: {len(html):,} bytes -> {dest.relative_to(ROOT)}")
        print(f"  wrapper: <{tag} {m.group(2).strip()[:120]}>")
        return

    print(f"section '{want}' not found")
    raise SystemExit(1)


if __name__ == "__main__":
    main()
