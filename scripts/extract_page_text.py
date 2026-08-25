"""Extract the visible Korean copy from a saved kr.sidiz.com page.

Strips scripts, styles and JSON blobs, then reports the on-page text runs that
contain Hangul. This is the actual translation source for a product page --
and it settles whether Korean copy lives in HTML (cheap to translate) or is
burned into imagery (expensive to recreate).

Usage: python scripts/extract_page_text.py t90
"""

import html
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]

DROP_BLOCKS = re.compile(
    r"<(script|style|noscript|svg|template)\b[^>]*>.*?</\1>", re.S | re.I
)
TAG = re.compile(r"<[^>]+>")
HANGUL = re.compile(r"[가-힣]")
WS = re.compile(r"[ \t ]+")


def main():
    handle = sys.argv[1] if len(sys.argv) > 1 else "t90"
    src = ROOT / "data" / "kr-raw" / f"page-{handle}.html"
    if not src.exists():
        print(f"missing {src}")
        raise SystemExit(1)

    doc = src.read_text(encoding="utf-8")
    doc = DROP_BLOCKS.sub(" ", doc)
    # block-level tags become line breaks so runs stay separate
    doc = re.sub(r"</(p|div|li|h[1-6]|section|br|td|tr|dt|dd)>", "\n", doc, flags=re.I)
    doc = re.sub(r"<br\s*/?>", "\n", doc, flags=re.I)
    doc = TAG.sub(" ", doc)
    doc = html.unescape(doc)

    seen, runs = set(), []
    for line in doc.split("\n"):
        line = WS.sub(" ", line).strip()
        if len(line) < 2 or not HANGUL.search(line):
            continue
        if line in seen:
            continue
        seen.add(line)
        runs.append(line)

    out = ROOT / "data" / "products" / handle
    out.mkdir(parents=True, exist_ok=True)
    dest = out / "kr-copy.txt"
    dest.write_text("\n".join(runs) + "\n", encoding="utf-8")

    chars = sum(len(HANGUL.findall(r)) for r in runs)
    print(f"{handle}: {len(runs)} unique Korean text runs, {chars:,} Hangul characters")
    print(f"-> {dest.relative_to(ROOT)}\n")
    for r in runs[:40]:
        print("  " + r[:110])


if __name__ == "__main__":
    main()
