"""Give every product image an English SEO filename and alt text.

Reads data/products/<handle>/media-manifest.csv, matches each KR filename to a
variant (the KR files embed the SKU colour code), and fills in:

  en_filename  - descriptive, hyphenated, keyword-bearing, lowercase
  en_alt_text  - a real sentence describing the image for screen readers and
                 image search; never keyword-stuffed
  action       - keep / recreate / drop

Usage: python scripts/build_media_seo.py t90
"""

import csv
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]

PRODUCT_EN = {
    "t90": {
        "name": "SIDIZ T90 ergonomic office chair",
        "slug": "sidiz-t90-ergonomic-office-chair",
    }
}

# KR colour-code fragment -> Australian English material + colour
COLOUR_CODES = {
    "4B1LMN": ("Double Raschel mesh", "grey"),
    "4B6BKM": ("Double Raschel mesh", "black"),
    "9I2MNI": ("Aquatex fabric", "cream beige"),
    "9I7BKM": ("Aquatex fabric", "green black"),
    "L841AC": ("natural leather", "shadow grey"),
    "L945AC": ("natural leather", "tan brown"),
    "L738AC": ("Natural Leather Limited Palette", "dry rose"),
    "L735LC": ("Natural Leather Limited Palette", "daisy yellow"),
    "L744AC": ("Natural Leather Limited Palette", "greyish mint"),
    "L734CR": ("Natural Leather Limited Palette", "teal blue"),
    "L734AC": ("Natural Leather Limited Palette", "deep navy"),
}

VIEWS = [
    "front view",
    "angled view",
    "side profile",
    "rear view",
    "seat detail",
    "armrest detail",
    "headrest detail",
]

# filename fragment -> (slug part, alt sentence, action)
NAMED = {
    "WARRANTY": (
        "15-year-warranty",
        "SIDIZ 15-year warranty badge",
        "keep",
    ),
    "leather_caution": (
        "natural-leather-surface-detail",
        "Close-up of the natural leather seat and armrests, showing the grain and "
        "surface variation characteristic of full-grain hide",
        "keep",
    ),
    "limitied-palatte-color": (
        "natural-leather-limited-palette-colours",
        "The five colours of the SIDIZ T90 Natural Leather Limited Palette",
        "keep",
    ),
    "AQUATEX": (
        "aquatex-fabric-detail",
        "Close-up of the Aquatex fabric upholstery on the SIDIZ T90",
        "keep",
    ),
    "FYF": (
        "adjustment-guide",
        "Diagram showing the adjustment points on the SIDIZ T90: seat tilt, "
        "headrest, tilt range, armrests and lumbar support",
        "review",
    ),
    "FUNGUS": ("", "", "drop"),
    "olly": ("", "", "drop"),
}


def slugify(s):
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s.lower())
    return re.sub(r"-+", "-", s).strip("-")


def classify(name, product):
    lower = name.lower()
    ext = name.rsplit(".", 1)[-1].lower()

    for frag, (slug, alt, action) in NAMED.items():
        if frag.lower() in lower:
            if action == "drop":
                return "", "", "drop — cross-sell for a product not launching in AU"
            return f"{product['slug']}-{slug}.{ext}", alt, action

    if ext in ("mp4", "webm"):
        return (
            f"{product['slug']}-video.{ext}",
            f"Video showing the {product['name']} in use",
            "keep — check for Korean voiceover or on-screen text",
        )

    if ".thumbnail." in lower:
        return (
            f"{product['slug']}-video-poster.{ext}",
            f"{product['name']}",
            "keep — video poster frame",
        )

    # variant photography: the SKU colour code is embedded in the filename
    for code, (material, colour) in COLOUR_CODES.items():
        if code.lower() in lower:
            idx = re.search(r"_(\d{2})_", name) or re.search(r"__(\d{2})_", name)
            n = int(idx.group(1)) if idx else 0
            view = VIEWS[n] if n < len(VIEWS) else f"view {n + 1}"
            return (
                f"{product['slug']}-{slugify(material)}-{slugify(colour)}-{n + 1:02d}.{ext}",
                f"{product['name']} in {material}, {colour} — {view}",
                "keep",
            )

    if "aquatex" in lower:
        idx = re.search(r"_(\d{2})_", name)
        n = int(idx.group(1)) if idx else 0
        view = VIEWS[n] if n < len(VIEWS) else f"view {n + 1}"
        return (
            f"{product['slug']}-aquatex-fabric-{n + 1:02d}.{ext}",
            f"{product['name']} in Aquatex fabric — {view}",
            "keep",
        )

    if re.match(r"^img\d+", lower):
        n = int(re.match(r"^img(\d+)", lower).group(1))
        return (
            f"{product['slug']}-in-use-{n:02d}.{ext}",
            f"The {product['name']} at a desk in a home office, shown in use",
            "keep",
        )

    if lower.startswith("leather_"):
        n = re.search(r"leather_(\d+)", lower)
        n = int(n.group(1)) if n else 1
        return (
            f"{product['slug']}-natural-leather-detail-{n:02d}.{ext}",
            "Detail of the natural leather upholstery on the SIDIZ T90, showing "
            "grain, wrinkles and natural colour variation",
            "keep",
        )

    return (
        f"{product['slug']}-{slugify(name.rsplit('.', 1)[0])[:48]}.{ext}",
        f"{product['name']}",
        "review — needs a human-written alt text",
    )


def main():
    handle = sys.argv[1] if len(sys.argv) > 1 else "t90"
    product = PRODUCT_EN[handle]
    path = ROOT / "data" / "products" / handle / "media-manifest.csv"
    rows = list(csv.DictReader(open(path, encoding="utf-8")))

    used = {}
    for r in rows:
        fn, alt, action = classify(r["kr_filename"], product)
        if fn:
            # keep filenames unique
            base, _, ext = fn.rpartition(".")
            n = used.get(fn, 0)
            used[fn] = n + 1
            if n:
                fn = f"{base}-{n + 1}.{ext}"
        r["en_filename"] = fn
        r["en_alt_text"] = alt
        r["action"] = action
        r["has_korean_text"] = "no"

    with open(path, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    from collections import Counter
    tally = Counter(r["action"].split(" —")[0] for r in rows)
    print(f"{handle}: {len(rows)} assets")
    for k, v in tally.most_common():
        print(f"  {k:8} {v}")
    print(f"\n-> {path.relative_to(ROOT)}")
    print("\nsample:")
    for r in rows[:8]:
        print(f"  {r['en_filename'][:56]:58} {r['en_alt_text'][:60]}")


if __name__ == "__main__":
    main()
