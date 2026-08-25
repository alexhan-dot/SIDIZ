"""Rebuild the T90 template's scroll sections on the ported KR sections.

Replaces the hand-written scroll banner / card sections with the KR ports, so
the pinned-text-while-cards-scroll behaviour is driven by the Korean script,
and attaches the 360 frame sets to the PDP head.
"""

import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
TPL = ROOT / "theme" / "templates" / "product.t90.json"
SPIN = ROOT / "data" / "products" / "t90" / "spin-360.json"

CDN = "https://kr.sidiz.com/cdn/shop"


def vid(h, name):
    return f"{CDN}/videos/c/vp/{h}/{name}"


def poster(h):
    return f"{CDN}/files/preview_images/{h}.thumbnail.0000000000_small.jpg"


# KR colour code -> AU Colour option value
SPIN_COLOURS = {
    "4B1LMN": "Grey",
    "4B6BKM": "Black",
    "AQUATEX": "Cream Beige",
    "L941AC": "Shadow Grey",
    "L945AC": "Tan Brown",
    "L738AC": "Dry Rose",
    "L735LC": "Daisy Yellow",
    "L744AC": "Greyish Mint",
    "L734CR": "Teal Blue",
    "L734AC": "Deep Navy",
}

ERGO_BANNER = {
    "type": "sidiz-wb-scroll-banner",
    "settings": {
        "heading": "Optimised for performance<br>PROGRESSIVE MOVEMENT",
        "tag": "Change posture without breaking focus",
        "subheading": "Ergonomic design that responds<br>to how you move",
        "description": "<p>Designed so your concentration holds even when your posture drifts through a long stretch of work.</p><p>Twist your upper body or lean to one side and the T90 responds smoothly, keeping your back and lower back supported.</p>",
        "video_url": vid("f4fa01b56d86461cb0e5ac85b06cf5a4", "f4fa01b56d86461cb0e5ac85b06cf5a4.HD-1080p-7.2Mbps-36706544.mp4"),
        "poster_url": poster("f4fa01b56d86461cb0e5ac85b06cf5a4"),
        "video_url_mobile": vid("fac91c41ce534f4483c545eb022e0bfa", "fac91c41ce534f4483c545eb022e0bfa.HD-1080p-7.2Mbps-36941802.mp4"),
        "poster_url_mobile": poster("fac91c41ce534f4483c545eb022e0bfa"),
        "alt": "SIDIZ T90 responding as the sitter shifts posture",
    },
}

ERGO_CARDS = {
    "type": "sidiz-wb-scroll-card-list",
    "blocks": {
        "c1": {
            "type": "card",
            "settings": {
                "title": "Perfect Fitting Lumbar Support",
                "description": "<p>SIDIZ's own patented mechanism supports the curve of your lower back in any posture, adapting to your body.</p><p>Built to keep your lower back comfortable through long working sessions.</p>",
                "note": "<p>Korean Patent No. 10-2468097</p>",
                "video_url": vid("9f691510fc054903b2ea38f1a54a49de", "9f691510fc054903b2ea38f1a54a49de.HD-720p-4.5Mbps-36706916.mp4"),
                "poster_url": poster("9f691510fc054903b2ea38f1a54a49de"),
                "alt": "Perfect Fitting Lumbar Support adapting to the sitter's lower back",
            },
        },
        "c2": {
            "type": "card",
            "settings": {
                "title": "Flexible backrest",
                "description": "<p>A flexible backrest structure that responds naturally as you move.</p><p>It reduces the load on your back and lower back over long periods of sitting, for comfortable support throughout the day.</p>",
                "video_url": vid("87deb204b2244ed492b2727d98af48ac", "87deb204b2244ed492b2727d98af48ac.HD-720p-4.5Mbps-36706917.mp4"),
                "poster_url": poster("87deb204b2244ed492b2727d98af48ac"),
                "alt": "Flexible backrest of the SIDIZ T90 responding to movement",
            },
        },
        "c3": {
            "type": "card",
            "settings": {
                "title": "High Comfort Foam",
                "description": "<p>Soft memory foam combined with 100% MDI foam for a comfortable cushioned feel.</p><p>It supports your shoulders and upper body so leaning in any direction still feels stable.</p>",
                "video_url": vid("7583e174aa384a91a8954321a6bdda70", "7583e174aa384a91a8954321a6bdda70.HD-720p-4.5Mbps-36706919.mp4"),
                "poster_url": poster("7583e174aa384a91a8954321a6bdda70"),
                "alt": "High Comfort Foam cushioning in the SIDIZ T90 backrest",
            },
        },
    },
    "block_order": ["c1", "c2", "c3"],
    "settings": {},
}

ARM_BANNER = {
    "type": "sidiz-wb-scroll-banner",
    "settings": {
        "heading": "",
        "tag": "Move without limits, so you can think from every angle",
        "subheading": "Panorama 4D armrests<br>that support every posture",
        "description": "<p>Modern work moves between PC, laptop, tablet and phone, which makes the movement of your arms and upper body matter more than it used to.</p><p>The T90's 4D armrests offer a wide adjustment range, supporting your arms and shoulders in whatever posture the task calls for. The movement opens out like a panorama.</p><p>Korean Patent No. 10-2779705</p>",
        "video_url": vid("f2b08a29331a4271b16e9fe5b55b9814", "f2b08a29331a4271b16e9fe5b55b9814.HD-1080p-7.2Mbps-36707422.mp4"),
        "poster_url": poster("f2b08a29331a4271b16e9fe5b55b9814"),
        "alt": "Panorama 4D armrests moving through their full adjustment range",
    },
}

ARM_CARDS = {
    "type": "sidiz-wb-scroll-card-list",
    "blocks": {
        "a1": {
            "type": "card",
            "settings": {
                "title": "4D armrest adjustment",
                "description": "<p>A four-way adjustment system covering armrest height, depth, width and angle.</p><p>Adjustable through 70 mm height, 60 mm depth, 35° laterally and 230° rotation.</p>",
                "video_url": vid("7c4836fa4ed942488ffdf3762cb80769", "7c4836fa4ed942488ffdf3762cb80769.SD-480p-1.0Mbps-36797054.mp4"),
                "poster_url": poster("7c4836fa4ed942488ffdf3762cb80769"),
                "alt": "Adjusting the 4D armrest on the SIDIZ T90",
            },
        },
        "a2": {
            "type": "card",
            "settings": {
                "title": "Tension support design",
                "description": "<p>Calibrated tension gives steady support when you rest your arms.</p><p>It reduces fatigue in the arms and shoulders during keyboard and mouse work.</p>",
                "video_url": vid("8d49c3d03ccf4fbb9abf0c9c775499fa", "8d49c3d03ccf4fbb9abf0c9c775499fa.SD-480p-1.2Mbps-36797055.mp4"),
                "poster_url": poster("8d49c3d03ccf4fbb9abf0c9c775499fa"),
                "alt": "Tension support in the T90 armrest as an arm rests on it",
            },
        },
        "a3": {
            "type": "card",
            "settings": {
                "title": "Silicone armrest pads",
                "description": "<p>Soft silicone reduces pressure where your arms make contact.</p><p>It stays comfortable to the touch through long sessions.</p>",
                "image_url": f"{CDN}/files/f2518d4c4dc36873528bb2b0de569259.png",
                "alt": "Silicone armrest pad on the SIDIZ T90",
            },
        },
    },
    "block_order": ["a1", "a2", "a3"],
    "settings": {},
}

TILT_BANNER = {
    "type": "sidiz-wb-banner",
    "settings": {
        "tag": "A close fit, with nothing leaking your focus",
        "heading": "Zero gap between you and the chair",
        "description": "<p>Perfect Fitting Lumbar Support and the Ultimate Sync Tilt mechanism minimise the gap between your body and the backrest, while backrest and seat move together to hold a stable posture.</p>",
        "align": "left",
        "align_vertical": "bottom",
        "text_colour": "#ffffff",
        "video_url": vid("c7d14500aba741a88dcb8a51148358db", "c7d14500aba741a88dcb8a51148358db.HD-1080p-2.5Mbps-40789349.mp4"),
        "poster_url": poster("c7d14500aba741a88dcb8a51148358db"),
        "alt": "Backrest and seat of the SIDIZ T90 moving together as the sitter reclines",
    },
}

TILT_CARDS = {
    "type": "sidiz-wb-card-list",
    "blocks": {
        "t1": {
            "type": "card",
            "settings": {
                "title": "Ultimate Sync Tilt",
                "description": "<p>More than 138 precisely assembled components produce a tilt mechanism that moves close to the way the body does.</p><p>Korean Patent No. 10-1533650 · Co-developed over six years with ITO Design.</p>",
                "align": "left",
                "video_url": vid("20e9455892f343a0bcdb4a7427a961d6", "20e9455892f343a0bcdb4a7427a961d6.SD-480p-1.5Mbps-36797788.mp4"),
                "poster_url": poster("20e9455892f343a0bcdb4a7427a961d6"),
                "alt": "Ultimate Sync Tilt mechanism of the SIDIZ T90 in motion",
            },
        },
        "t2": {
            "type": "card",
            "settings": {
                "title": "Synchronised tilting",
                "description": "<p>The seat tilts along with the backrest as you recline, accounting for the way your legs naturally extend.</p>",
                "align": "left",
                "video_url": vid("1a4364137cb746e18d59275a01a09f3c", "1a4364137cb746e18d59275a01a09f3c.SD-480p-1.5Mbps-36797785.mp4"),
                "poster_url": poster("1a4364137cb746e18d59275a01a09f3c"),
                "alt": "Synchronised tilting: the seat tilts with the backrest",
            },
        },
        "t3": {
            "type": "card",
            "settings": {
                "title": "Multi-limited tilting",
                "description": "<p>Set the range through which the backrest reclines, to taste. The resistance as it returns is adjustable too.</p>",
                "align": "left",
                "video_url": vid("8a2fb37c626a4c8384ebce18397f9807", "8a2fb37c626a4c8384ebce18397f9807.SD-480p-1.5Mbps-36797787.mp4"),
                "poster_url": poster("8a2fb37c626a4c8384ebce18397f9807"),
                "alt": "Multi-limited tilting control setting the backrest recline range",
            },
        },
    },
    "block_order": ["t1", "t2", "t3"],
    "settings": {},
}


def main():
    d = json.loads(TPL.read_text(encoding="utf-8"))
    spins = json.loads(SPIN.read_text(encoding="utf-8"))

    # --- 360 sets on the PDP head -------------------------------------------
    head = d["sections"]["pdp_head"]
    order = [b for b in head["block_order"] if not b.startswith("spin")]
    for code, frames in spins.items():
        colour = SPIN_COLOURS.get(code)
        if not colour:
            continue
        key = "spin" + code.lower()
        head["blocks"][key] = {
            "type": "spin",
            "settings": {
                "colour": colour,
                "frames": ",".join(frames),
                "alt": f"SIDIZ T90 in {colour}, rotated view",
            },
        }
        order.append(key)
    head["block_order"] = order

    # --- scroll sections ----------------------------------------------------
    d["sections"]["ergonomics_banner"] = ERGO_BANNER
    d["sections"]["ergonomics_cards"] = ERGO_CARDS
    d["sections"]["armrests_banner"] = ARM_BANNER
    d["sections"]["armrests_cards"] = ARM_CARDS
    d["sections"]["tilt_banner"] = TILT_BANNER
    d["sections"]["tilt_cards"] = TILT_CARDS
    d["sections"].pop("armrests_gallery", None)

    new_order = []
    for key in d["order"]:
        if key == "armrests_gallery":
            new_order.extend(["armrests_banner", "armrests_cards"])
        else:
            new_order.append(key)
    d["order"] = [k for k in new_order if k in d["sections"]]

    TPL.write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"sections: {len(d['sections'])}  order: {len(d['order'])}")
    print("360 sets attached:", sum(1 for b in head["blocks"] if b.startswith("spin")))
    print("\norder:")
    for k in d["order"]:
        print(f"  {k:22} {d['sections'][k]['type']}")


if __name__ == "__main__":
    main()
