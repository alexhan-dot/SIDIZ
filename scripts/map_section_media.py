"""Map every image and video on a KR product page to the section it appears in.

Splitting the saved HTML on the shopify-section wrappers preserves DOM order,
so the output can drive the AU template: each section gets the same media, in
the same sequence, as the Korean page.

Usage: python scripts/map_section_media.py t90
"""

import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]

STRIP = re.compile(r"^(?:template|sections)--\d+__")
SUFFIX = re.compile(r"_[A-Za-z0-9]{6}$")
SIZE = re.compile(r"_(\d+x\d*|\d*x\d+)(?=\.[a-z0-9]+$)", re.I)
MEDIA = re.compile(
    r"(?://|https://)[a-z0-9.-]+/cdn/shop/(?:files|videos)/[^\"'\s()\\]+?"
    r"\.(?:jpg|jpeg|png|webp|mp4)",
    re.I,
)


def norm(u):
    if u.startswith("//"):
        u = "https:" + u
    return SIZE.sub("", u.split("?")[0])


def main():
    handle = sys.argv[1] if len(sys.argv) > 1 else "t90"
    html = (ROOT / "data" / "kr-raw" / f"page-{handle}.html").read_text(encoding="utf-8")

    parts = re.split(r'id="shopify-section-([^"]+)"', html)
    out = []
    for i in range(1, len(parts), 2):
        name = SUFFIX.sub("", STRIP.sub("", parts[i]))
        body = parts[i + 1] if i + 1 < len(parts) else ""
        urls, seen = [], set()
        for u in MEDIA.findall(body):
            u = norm(u)
            if u not in seen:
                seen.add(u)
                urls.append(u)
        out.append({"section": name, "media": urls})

    dest = ROOT / "data" / "products" / handle / "section-media.json"
    dest.write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")

    total = sum(len(s["media"]) for s in out)
    print(f"{handle}: {len(out)} sections, {total} media references")
    print(f"-> {dest.relative_to(ROOT)}\n")
    for s in out:
        if s["media"]:
            first = s["media"][0].rsplit("/", 1)[-1]
            print(f"  {s['section']:32} {len(s['media']):>3}  {first[:46]}")


if __name__ == "__main__":
    main()
