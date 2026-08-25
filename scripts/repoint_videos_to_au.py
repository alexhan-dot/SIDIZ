"""Repoint the T90 template from the KR CDN to the AU store's own media.

Every video URL in the template still pointed at kr.sidiz.com. Now that the
files live in the AU store, each is swapped for its Shopify-hosted equivalent
along with the matching full-resolution poster frame.

The mapping goes KR content hash -> external_video_id (recorded at upload time)
-> AU hash and best rendition (read back from the Files API).
"""

import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
TPL = ROOT / "theme" / "templates" / "product.t90.json"
RESULTS = ROOT / "data" / "products" / "t90" / "video-upload-results.json"
AU_MAP = ROOT / "data" / "products" / "t90" / "video-au-map.json"

CDN = "https://cdn.shopify.com"
FILES = "https://cdn.shopify.com/s/files/1/0692/6689/9266/files"


def main():
    results = json.loads(RESULTS.read_text(encoding="utf-8"))
    au = json.loads(AU_MAP.read_text(encoding="utf-8"))

    # KR hash -> (AU hash, rendition)
    lookup = {}
    for r in results:
        entry = au.get(r["external_video_id"])
        if entry:
            lookup[r["hash"]] = (entry[0], entry[1], r["external_video_id"])

    tpl = TPL.read_text(encoding="utf-8")
    before = tpl

    swapped_video, swapped_poster, unmatched = 0, 0, set()

    # video URLs
    def video_sub(match):
        nonlocal swapped_video
        kr_hash = match.group(1)
        hit = lookup.get(kr_hash)
        if not hit:
            unmatched.add(kr_hash)
            return match.group(0)
        au_hash, rendition, ext_id = hit
        swapped_video += 1
        return f"{CDN}/videos/c/vp/{au_hash}/{au_hash}.{rendition}-{ext_id}.mp4"

    tpl = re.sub(
        r"https://kr\.sidiz\.com/cdn/shop/videos/c/vp/([0-9a-f]{32})/[^\"]+?\.mp4",
        video_sub,
        tpl,
    )

    # poster URLs — the AU preview frame is full resolution, no _small suffix
    def poster_sub(match):
        nonlocal swapped_poster
        kr_hash = match.group(1)
        hit = lookup.get(kr_hash)
        if not hit:
            unmatched.add(kr_hash)
            return match.group(0)
        au_hash = hit[0]
        swapped_poster += 1
        return f"{FILES}/preview_images/{au_hash}.thumbnail.0000000000.jpg"

    tpl = re.sub(
        r"https://kr\.sidiz\.com/cdn/shop/files/preview_images/([0-9a-f]{32})\.thumbnail\.\d+(?:_small)?\.jpg",
        poster_sub,
        tpl,
    )

    TPL.write_text(tpl, encoding="utf-8")

    remaining = len(re.findall(r"kr\.sidiz\.com/cdn/shop/videos", tpl))
    still_kr = len(re.findall(r"kr\.sidiz\.com", tpl))

    print(f"video URLs repointed : {swapped_video}")
    print(f"poster URLs repointed: {swapped_poster}")
    print(f"changed              : {'yes' if tpl != before else 'no'}")
    print(f"KR video URLs left   : {remaining}")
    print(f"KR references left   : {still_kr}  (images not yet migrated)")
    if unmatched:
        print(f"\nunmatched hashes ({len(unmatched)}):")
        for h in sorted(unmatched):
            print("   " + h)


if __name__ == "__main__":
    main()
