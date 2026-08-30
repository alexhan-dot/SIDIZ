"""Compose product.fungus.json.

FUNGUS is the multipurpose stool: image hero, a two-option compare (the KR
Tottenham-edition option and the leather guidance are both dropped - the
collab is excluded pending sign-off and no leather is sold), the
360-and-move view, four use-case tiles and a compact tail with a
four-drawing spec across the stool and castor bases.
"""

import copy
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
KR = "https://kr.sidiz.com/cdn/shop"


def img(name):
    return f"{KR}/files/{name}"


base = json.loads((ROOT / "theme/templates/product.t50-2.json").read_text(encoding="utf-8"))
B = base["sections"]

S = {}

S["sticky_nav"] = copy.deepcopy(B["sticky_nav"])
S["sticky_nav"]["blocks"] = {
    "n1": {"type": "link", "settings": {"label": "Options", "anchor": "options"}},
    "n2": {"type": "link", "settings": {"label": "Freedom to move", "anchor": "move"}},
    "n3": {"type": "link", "settings": {"label": "Uses", "anchor": "uses"}},
    "n4": {"type": "link", "settings": {"label": "Specifications", "anchor": "specifications"}},
}
S["sticky_nav"]["block_order"] = ["n1", "n2", "n3", "n4"]

S["pdp_head"] = copy.deepcopy(B["pdp_head"])
S["pdp_head"]["blocks"]["i1"]["settings"]["value"] = "SIDIZ FUNGUS Multipurpose Stool"
S["pdp_head"]["blocks"]["i2"]["settings"]["value"] = "Stool"
S["pdp_head"]["blocks"]["i3"]["settings"]["value"] = "Fabric, sponge, plastic"
S["pdp_head"]["blocks"]["i4"]["settings"]["value"] = "Watery Blue\nCharcoal\nBrick Orange\nGrey\nBlue\nAsh Green"
S["pdp_head"]["settings"]["subtitle"] = (
    "Fun with us: a mushroom-shaped stool that turns 360 degrees and carries by its "
    "handle - side chair, dresser stool and sofa stool in one."
)

S["hero"] = {
    "type": "sidiz-pdp-hero",
    "settings": {
        "subtitle": "<em class=\"caps\">Fun with us</em>",
        "subtitle_colour": "#ffffff",
        "heading": "FUNGUS",
        "heading_colour": "#ffffff",
        "text_align": "center",
        "header_scheme": "dark",
        "image_url": img("FUNGUS_HEAD_a3137f0a-90ea-4f6c-98f3-05d60f1afd67.jpg"),
        "image_url_mobile": img("FUNGUS_Head_M.jpg"),
        "alt": "The mushroom-shaped SIDIZ FUNGUS stool",
        "description": (
            "<p>With its distinctive mushroom-inspired design, the FUNGUS earns its place "
            "all through the day - as a side chair, a dresser stool, a sofa stool and "
            "more.</p>"
        ),
        "description_colour": "#000000",
        "description_align": "left",
        "product_type": "default",
    },
}

S["options"] = {
    "type": "sidiz-option-compare",
    "blocks": {
        "o1": {"type": "option", "settings": {
            "title": "FUNGUS Stool",
            "description": "The stool on glides",
            "images": img("FUNGUS_Option1.jpg") + "," + img("FUNGUS_Option1-1.jpg"),
            "colours": "#87999b,#36393b,#b56a4d,#c4c8cb,#6b8199,#9aa694",
            "alt": "The SIDIZ FUNGUS stool"}},
        "o2": {"type": "option", "settings": {
            "title": "FUNGUS Castors",
            "description": "The stool on durable nylon castors",
            "images": img("FUNGUS_Option2.jpg") + "," + img("FUNGUS_Option2-1.jpg"),
            "colours": "#87999b,#36393b,#b56a4d,#c4c8cb,#6b8199,#9aa694",
            "alt": "The SIDIZ FUNGUS on castors"}},
    },
    "block_order": ["o1", "o2"],
    "settings": {"heading": "The FUNGUS option for you"},
}

S["move_view"] = {
    "type": "sidiz-product-view-vertical",
    "settings": {
        "heading": "Free to go wherever the day does",
        "description": (
            "<p>Useful all through the house, the FUNGUS moves easily and turns freely - "
            "the all-rounder of stools.</p>"
        ),
        "image_url": img("FUNGUS_01.jpg"),
        "alt": "The FUNGUS moving between rooms",
    },
    "blocks": {
        "b1": {"type": "feature", "settings": {
            "title": "A 360-degree swivel seat",
            "description": "<p>The seat turns with your movement, in any direction.</p>",
            "image_url": img("FUNGUS_01-1.jpg"),
            "alt": "The FUNGUS seat swivelling"}},
        "b2": {"type": "feature", "settings": {
            "title": "A handle made for moving",
            "description": "<p>A handle at the seat's edge carries it comfortably from room to room.</p>",
            "image_url": img("FUNGUS_01-2.jpg"),
            "alt": "Carrying the FUNGUS by its handle"}},
        "b3": {"type": "feature", "settings": {
            "title": "Even freer to move",
            "description": "<p>Durable nylon castors roll it wherever it is needed. *Castor version.</p>",
            "image_url": img("FUNGUS_01-3.jpg"),
            "alt": "The FUNGUS rolling on its castors"}},
    },
    "block_order": ["b1", "b2", "b3"],
}

S["use_tiles"] = {
    "type": "sidiz-tile-card-list",
    "blocks": {
        "t1": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "A side chair that makes studying together fun",
            "image_url": img("FUNGUS_1_1__01.jpg"),
            "alt": "The FUNGUS beside a child's desk"}},
        "t2": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "A versatile extra seat for study and office",
            "image_url": img("FUNGUS_1_1__02.jpg"),
            "alt": "The FUNGUS as an office side seat"}},
        "t3": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "A stool that makes the sofa more comfortable",
            "image_url": img("FUNGUS_1_1__03.jpg"),
            "alt": "The FUNGUS beside a sofa"}},
        "t4": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "A compact stool for the dresser",
            "image_url": img("FUNGUS_1_1__04.jpg"),
            "alt": "The FUNGUS at a dresser"}},
    },
    "block_order": ["t1", "t2", "t3", "t4"],
    "settings": {"heading": "Versatile, wherever it lands"},
}

S["goes_with"] = {
    "type": "sidiz-related-products",
    "settings": {"heading": "Goes well with the FUNGUS", "source": "collection", "limit": 4},
}

S["specifications"] = copy.deepcopy(B["specifications"])
S["specifications"]["settings"]["heading"] = "FUNGUS dimensions"
S["specifications"]["settings"]["figures"] = (
    "Maximum load 112 kg. Product weight approximately 5.9 kg (stool) or 6.72 kg (castors)."
)
S["specifications"]["settings"]["caveats"] = (
    "*Measurements may vary by plus or minus 20 mm and 1 kg depending on where and how "
    "they are taken; this is not a fault.<br>*Dimensions are measured with nobody seated."
)
S["specifications"]["blocks"] = {
    "d1": {"type": "drawing", "settings": {
        "image_url": img("MN130_01_2843ca20-7cfb-40a2-b67c-0e4ec6c00d89.jpg"),
        "alt": "Dimension drawing of the FUNGUS stool, front elevation"}},
    "d2": {"type": "drawing", "settings": {
        "image_url": img("MN130_02_cf77088f-7dc3-4cae-8f27-460812192cd6.jpg"),
        "alt": "Dimension drawing of the FUNGUS stool, side elevation"}},
    "d3": {"type": "drawing", "settings": {
        "image_url": img("MN130Y_01_0cec7b4b-3be6-473f-a31a-2f1114b90443.jpg"),
        "alt": "Dimension drawing of the FUNGUS on castors, front elevation"}},
    "d4": {"type": "drawing", "settings": {
        "image_url": img("MN130Y_02_371b5d3c-3830-45cb-af63-f0d334ca098f.jpg"),
        "alt": "Dimension drawing of the FUNGUS on castors, side elevation"}},
}
S["specifications"]["block_order"] = ["d1", "d2", "d3", "d4"]

S["safety_info"] = {
    "type": "sidiz-safety-info",
    "blocks": {
        "n1": {"type": "note", "settings": {
            "title": "Removing stains from the frame",
            "body": "<p>If the frame gets marked, a melamine sponge lifts stains easily. *Rubbing hard can damage the surface.</p>"}},
    },
    "block_order": ["n1"],
    "settings": {"heading": "Care and cautions"},
}

S["reviews"] = copy.deepcopy(B["reviews"])

S["stockists"] = {
    "type": "sidiz-store-info",
    "settings": {
        "heading": "Try one before you decide",
        "description": "Seat feel differs from body to body. Try a FUNGUS in person where you can; otherwise our returns policy is there to fall back on.",
        "link_label": "Find a stockist",
        "link": "/pages/contact",
        "image_url": img("shop_pc.jpg"),
        "alt": "A SIDIZ showroom interior",
    },
}

S["recommend"] = {
    "type": "sidiz-related-products",
    "settings": {
        "heading": "You may also like",
        "link_label": "View all chairs",
        "link": "/collections/all",
        "source": "collection",
        "limit": 4,
    },
}

S["notices"] = copy.deepcopy(B["notices"])

order = [
    "sticky_nav", "pdp_head", "hero", "options",
    "move_view", "use_tiles", "goes_with",
    "specifications", "safety_info",
    "reviews", "stockists", "recommend", "notices",
]
assert set(order) == set(S), set(order) ^ set(S)

out = ROOT / "theme/templates/product.fungus.json"
out.write_text(json.dumps({"sections": S, "order": order}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print("written", out.name, "sections:", len(order))
