"""Wire the newly ported KR sections into the T90 template.

Covers the mismatch list in order: intro row, adjustment grid, warranty,
specifications and the contact / after-sales block.
"""

import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
TPL = ROOT / "theme" / "templates" / "product.t90.json"
CDN = "https://kr.sidiz.com/cdn/shop"


def vid(h, name):
    return f"{CDN}/videos/c/vp/{h}/{name}"


def poster(h):
    return f"{CDN}/files/preview_images/{h}.thumbnail.0000000000_small.jpg"


def img(name):
    return f"{CDN}/files/{name}"


INTRO = {
    "type": "sidiz-product-row",
    "settings": {
        "heading": "SIDIZ T90 Ergonomic Office Chair",
        "align": "center",
        "background": "#ffffff",
        "text_colour": "#000000",
        "body": (
            "<ul>"
            "<li><strong>Ergonomic office chair</strong> – a premium work chair designed around long hours of computer use</li>"
            "<li><strong>Panorama 4D armrests</strong> – height, depth, width and angle adjustment for a wide range of working postures</li>"
            "<li><strong>Perfect Fitting Lumbar Support</strong> – steady lower-back support shaped to your body</li>"
            "<li><strong>Flexible backrest</strong> – a backrest that responds naturally as you move</li>"
            "<li><strong>Optimised for office, work-from-home and multi-device environments</strong></li>"
            "</ul>"
        ),
    },
}

FYF = {
    "type": "sidiz-find-your-fit",
    "blocks": {
        "f1": {"type": "adjustment", "settings": {
            "title": "To suit your body",
            "description": "<p>Seat height / seat depth</p>",
            "image_url": img("T90_FYF_01_cb1091a9-08dc-4187-9996-a30a129a887e.jpg"),
            "alt": "Adjusting seat height and depth on the SIDIZ T90"}},
        "f2": {"type": "adjustment", "settings": {
            "title": "For moments that need focus",
            "description": "<p>Seat tilt</p>",
            "image_url": img("T90_FYF_02_5247389b-d4ad-41e9-8e5b-97981b030bc5.jpg"),
            "alt": "Adjusting seat tilt on the SIDIZ T90"}},
        "f3": {"type": "adjustment", "settings": {
            "title": "To ease the load on head and neck",
            "description": "<p>Headrest height / angle</p>",
            "video_url": vid("03ffb1ec5b944830802e8b8782e114be", "03ffb1ec5b944830802e8b8782e114be.SD-480p-1.5Mbps-41125900.mp4"),
            "poster_url": poster("03ffb1ec5b944830802e8b8782e114be"),
            "alt": "Adjusting the headrest height and angle on the SIDIZ T90"}},
        "f4": {"type": "adjustment", "settings": {
            "title": "So the backrest reclines the way you want",
            "description": "<p>Tilt range / resistance</p>",
            "video_url": vid("6a3f5402a37241ed90ddf799239bfe27", "6a3f5402a37241ed90ddf799239bfe27.SD-480p-1.5Mbps-37256343.mp4"),
            "poster_url": poster("6a3f5402a37241ed90ddf799239bfe27"),
            "alt": "Setting the tilt range and resistance on the SIDIZ T90"}},
        "f5": {"type": "adjustment", "settings": {
            "title": "To rest shoulders and arms",
            "description": "<p>Armrest height / depth / angle / tilt</p>",
            "image_url": img("T90_FYF_05.jpg"),
            "alt": "Adjusting the 4D armrests on the SIDIZ T90"}},
        "f6": {"type": "adjustment", "settings": {
            "title": "To support your lower back",
            "description": "<p>Lumbar support height</p>",
            "video_url": vid("2b43aa4b1ec24573b4f679781c10d4c5", "2b43aa4b1ec24573b4f679781c10d4c5.SD-480p-1.5Mbps-37256396.mp4"),
            "poster_url": poster("2b43aa4b1ec24573b4f679781c10d4c5"),
            "alt": "Adjusting the lumbar support height on the SIDIZ T90"}},
    },
    "block_order": ["f1", "f2", "f3", "f4", "f5", "f6"],
    "settings": {
        "heading": "T90 adjustment guide",
        "subtitle": "FIND YOUR FIT. Set it up for your body",
        "guide_label": "USER GUIDE",
        "guide_link": "/pages/user-guide",
    },
}

WARRANTY = {
    "type": "sidiz-warranty",
    "settings": {
        "heading": "T90 | 15-year warranty",
        "body": "<p>So the value of your T90 keeps going, SIDIZ provides a 15-year warranty to customers who complete product registration.</p><p>Register your product once it arrives, before it slips your mind.</p>",
        "note": "<p>*Warranty periods vary by component.</p>",
        "register_label": "Register your product",
        "register_link": "/pages/product-registration",
        "show_acl": True,
        "image_url": img("WARRANTY_15.jpg"),
        "alt": "SIDIZ 15-year warranty badge",
    },
}

SPEC = {
    "type": "sidiz-spec",
    "blocks": {
        "d1": {"type": "drawing", "settings": {
            "image_url": img("T90HLDA2KK_01.jpg"),
            "alt": "Dimension drawing of the SIDIZ T90, front elevation, in millimetres"}},
        "d2": {"type": "drawing", "settings": {
            "image_url": img("T90HLDA2KK_02.jpg"),
            "alt": "Dimension drawing of the SIDIZ T90, side elevation, in millimetres"}},
    },
    "block_order": ["d1", "d2"],
    "settings": {
        "heading": "T90 dimensions",
        "figures": "• Maximum load: 125 kg &nbsp;&nbsp; • Product weight: approx. 28.7 kg",
        "caveats": (
            "*Measurements may vary by ±20 mm and ±1 kg depending on where and how they are taken; "
            "this is not a fault.<br>"
            "*Dimensions are measured with nobody seated.<br>"
            "*Seat height is measured from the centre of the seat."
        ),
    },
}

CONTACT = {
    "type": "sidiz-contact-notice",
    "blocks": {
        "c1": {"type": "notice", "settings": {
            "title": "Product, delivery, service and returns",
            "body": "<p>support@sidiz.au</p><p>Monday to Friday, 9:00 am – 5:00 pm AEST<br>Closed weekends and public holidays</p>"}},
        "c2": {"type": "notice", "settings": {
            "title": "Warranty and faulty returns",
            "body": "<p>Warranty period: up to 15 years from purchase, with product registration.</p><p>SIDIZ components are warranted from one year up to 15 years depending on the part. See the <a href=\"/pages/warranty\">warranty terms</a> for detail.</p><p>Nothing here limits your rights under the Australian Consumer Law, including your right to a repair, replacement or refund where goods are not of acceptable quality.</p>"}},
    },
    "block_order": ["c1", "c2"],
    "settings": {
        "heading": "Contact centre",
        "background": "#eaedf0",
        "title_colour": "#000000",
        "text_colour": "#434548",
    },
}


def main():
    d = json.loads(TPL.read_text(encoding="utf-8"))
    s = d["sections"]

    s["intro"] = INTRO
    s["find_your_fit"] = FYF
    s["warranty"] = WARRANTY
    s["specifications"] = SPEC
    s["notices"] = CONTACT

    # The contact block belongs at the foot of the page, as on kr.sidiz.com.
    order = [k for k in d["order"] if k != "notices"] + ["notices"]
    d["order"] = [k for k in order if k in s]

    TPL.write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    for k in d["order"]:
        print(f"  {k:20} {s[k]['type']}")


if __name__ == "__main__":
    main()
