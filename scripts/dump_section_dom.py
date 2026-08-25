"""Print the DOM skeleton of one section from a saved kr.sidiz.com page.

Strips text and attributes down to tag + class + a short text hint, so the
structure of a section can be read and rebuilt faithfully.

Usage: python scripts/dump_section_dom.py t90 configurator [max_depth]
"""

import html
import pathlib
import re
import sys
from html.parser import HTMLParser

ROOT = pathlib.Path(__file__).resolve().parents[1]

VOID = {"img", "br", "hr", "input", "source", "meta", "link", "path", "use", "circle"}
SKIP = {"script", "style", "noscript", "svg", "path", "defs", "clipPath"}


class Skeleton(HTMLParser):
    def __init__(self, max_depth):
        super().__init__(convert_charrefs=True)
        self.depth = 0
        self.max_depth = max_depth
        self.skip_depth = None
        self.lines = []
        self.pending = None

    def handle_starttag(self, tag, attrs):
        if self.skip_depth is not None:
            return
        if tag in SKIP:
            self.skip_depth = self.depth
            return

        a = dict(attrs)
        cls = a.get("class", "")
        cls = re.sub(r"\s+", ".", cls.strip())
        bits = []
        if cls:
            bits.append("." + cls)
        for key in ("type", "role", "aria-label", "data-type", "name"):
            if a.get(key):
                bits.append(f'{key}="{a[key][:40]}"')
        if tag == "img" and a.get("src"):
            bits.append("src=" + a["src"].rsplit("/", 1)[-1][:38])
        if tag == "video" and a.get("src"):
            bits.append("video=" + a["src"].rsplit("/", 1)[-1][:38])

        if self.depth <= self.max_depth:
            self.lines.append("  " * self.depth + f"<{tag} " + " ".join(bits))
        if tag not in VOID:
            self.depth += 1

    def handle_endtag(self, tag):
        if self.skip_depth is not None:
            if tag in SKIP and self.depth == self.skip_depth:
                self.skip_depth = None
            return
        if tag not in VOID:
            self.depth = max(0, self.depth - 1)

    def handle_data(self, data):
        if self.skip_depth is not None:
            return
        text = re.sub(r"\s+", " ", html.unescape(data)).strip()
        if len(text) > 1 and self.depth <= self.max_depth + 1:
            self.lines.append("  " * self.depth + "· " + text[:74])


def main():
    handle = sys.argv[1] if len(sys.argv) > 1 else "t90"
    want = sys.argv[2] if len(sys.argv) > 2 else "configurator"
    depth = int(sys.argv[3]) if len(sys.argv) > 3 else 7

    doc = (ROOT / "data" / "kr-raw" / f"page-{handle}.html").read_text(encoding="utf-8")
    parts = re.split(r'id="shopify-section-([^"]+)"', doc)

    for i in range(1, len(parts), 2):
        name = re.sub(r"^(?:template|sections)--\d+__", "", parts[i])
        name = re.sub(r"_[A-Za-z0-9]{6}$", "", name)
        if name != want:
            continue
        body = parts[i + 1]
        parser = Skeleton(depth)
        parser.feed(body)
        print(f"===== {name} =====")
        print("\n".join(parser.lines))
        return

    print(f"section '{want}' not found")


if __name__ == "__main__":
    main()
