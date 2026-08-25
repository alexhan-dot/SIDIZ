"""Plan the migration of the T90 videos into the AU store's Files.

Reads every video referenced by the T90 template, matches it to the local
download, and produces the stagedUploadsCreate input with an English SEO
filename and alt text for each.

Writes: data/products/t90/video-upload-plan.json
"""

import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
TPL = ROOT / "theme" / "templates" / "product.t90.json"
MEDIA = ROOT / "data" / "products" / "t90" / "media"
OUT = ROOT / "data" / "products" / "t90" / "video-upload-plan.json"

# hash -> (english filename stem, alt text)
NAMES = {
    "f4fa01b56d86461cb0e5ac85b06cf5a4": ("sidiz-t90-progressive-movement", "SIDIZ T90 responding as the sitter shifts posture"),
    "fac91c41ce534f4483c545eb022e0bfa": ("sidiz-t90-progressive-movement-mobile", "SIDIZ T90 responding as the sitter shifts posture"),
    "9f691510fc054903b2ea38f1a54a49de": ("sidiz-t90-perfect-fitting-lumbar-support", "Perfect Fitting Lumbar Support adapting to the sitter's lower back"),
    "87deb204b2244ed492b2727d98af48ac": ("sidiz-t90-flexible-backrest", "Flexible backrest of the SIDIZ T90 responding to movement"),
    "7583e174aa384a91a8954321a6bdda70": ("sidiz-t90-high-comfort-foam", "High Comfort Foam cushioning in the SIDIZ T90 backrest"),
    "f2b08a29331a4271b16e9fe5b55b9814": ("sidiz-t90-panorama-4d-armrests", "Panorama 4D armrests moving through their full adjustment range"),
    "7c4836fa4ed942488ffdf3762cb80769": ("sidiz-t90-4d-armrest-adjustment", "Adjusting the 4D armrest on the SIDIZ T90"),
    "8d49c3d03ccf4fbb9abf0c9c775499fa": ("sidiz-t90-armrest-tension-support", "Tension support in the SIDIZ T90 armrest as an arm rests on it"),
    "c7d14500aba741a88dcb8a51148358db": ("sidiz-t90-ultimate-sync-tilt", "Backrest and seat of the SIDIZ T90 moving together as the sitter reclines"),
    "20e9455892f343a0bcdb4a7427a961d6": ("sidiz-t90-ultimate-sync-tilt-mechanism", "Ultimate Sync Tilt mechanism of the SIDIZ T90 in motion"),
    "1a4364137cb746e18d59275a01a09f3c": ("sidiz-t90-synchronised-tilting", "Synchronised tilting: the seat tilts with the backrest"),
    "8a2fb37c626a4c8384ebce18397f9807": ("sidiz-t90-multi-limited-tilting", "Multi-limited tilting control setting the backrest recline range"),
    "99b0646b1da94afaabb47802d23a36db": ("sidiz-t90-headrest", "Headrest of the SIDIZ T90 adjusting for height and angle"),
    "2047af3cd38b4acd8aa30534ca3c9893": ("sidiz-t90-ultra-comfort-foam", "Waterfall front edge of the SIDIZ T90 seat cushion"),
    "e007a4036f70485bb34cb721a0f0b0d9": ("sidiz-t90-forward-tilting", "Forward tilting angles the SIDIZ T90 seat slightly forward"),
    "03ffb1ec5b944830802e8b8782e114be": ("sidiz-t90-headrest-height-and-angle", "Adjusting the headrest height and angle on the SIDIZ T90"),
    "6a3f5402a37241ed90ddf799239bfe27": ("sidiz-t90-tilt-range-and-resistance", "Setting the tilt range and resistance on the SIDIZ T90"),
    "2b43aa4b1ec24573b4f679781c10d4c5": ("sidiz-t90-lumbar-support-height", "Adjusting the lumbar support height on the SIDIZ T90"),
    "785d235698f24e7498fb31b98af73489": ("sidiz-t90-studio-rotation", "SIDIZ T90 shown in a studio setting, rotating slowly"),
    "fa159114e82f43a0bae73474ce27b3d5": ("sidiz-t90-at-a-desk", "SIDIZ T90 in use at a desk, seen from behind"),
    "97efc5a9ffa8402994162a5947f43574": ("sidiz-t90-backrest-detail", "Close detail of the SIDIZ T90 backrest and armrest"),
    "b4c1c34f2a974c4f9865d42a3f40f2dd": ("sidiz-t90-detail-loop", "Detail footage of the SIDIZ T90"),
    "f5fd6a72121f42efad4c0a201f572ed1": ("sidiz-t90-overview-loop", "Overview footage of the SIDIZ T90"),
}


def main():
    tpl = TPL.read_text(encoding="utf-8")
    used = set(re.findall(r"/videos/c/vp/([0-9a-f]{32})/", tpl))

    plan = []
    missing_file, missing_name = [], []

    for path in sorted(MEDIA.glob("*.mp4")):
        h = path.name.split(".")[0]
        if h not in NAMES:
            missing_name.append(path.name)
            continue
        stem, alt = NAMES[h]
        plan.append({
            "hash": h,
            "local": path.name,
            "bytes": path.stat().st_size,
            "filename": f"{stem}.mp4",
            "alt": alt,
            "used_in_template": h in used,
        })

    for h in used:
        if not any(p["hash"] == h for p in plan):
            missing_file.append(h)

    OUT.write_text(json.dumps(plan, indent=1, ensure_ascii=False), encoding="utf-8")

    total = sum(p["bytes"] for p in plan)
    in_use = [p for p in plan if p["used_in_template"]]
    print(f"videos on disk        : {len(plan)}")
    print(f"referenced by template: {len(used)}  (matched {len(in_use)})")
    print(f"total bytes           : {total:,} ({total/1048576:.1f} MB)")
    if missing_name:
        print(f"\nno English name mapped ({len(missing_name)}):")
        for n in missing_name:
            print("   " + n)
    if missing_file:
        print(f"\nreferenced but not downloaded ({len(missing_file)}):")
        for h in missing_file:
            print("   " + h)
    print(f"\n-> {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
