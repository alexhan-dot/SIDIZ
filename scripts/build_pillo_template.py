"""Compose product.pillo.json.

PILLO is the ergonomic floor chair: image hero, fabric-vs-vegan-leather
option compare (leather guidance dropped), the S-Curve ergonomics view, the
considerate-design banner and card list, a finish tile and a compact tail.
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
    "n2": {"type": "link", "settings": {"label": "Ergonomics", "anchor": "ergonomics"}},
    "n3": {"type": "link", "settings": {"label": "Design", "anchor": "design"}},
    "n4": {"type": "link", "settings": {"label": "Specifications", "anchor": "specifications"}},
}
S["sticky_nav"]["block_order"] = ["n1", "n2", "n3", "n4"]

S["pdp_head"] = copy.deepcopy(B["pdp_head"])
S["pdp_head"]["blocks"]["i1"]["settings"]["value"] = "SIDIZ PILLO Ergonomic Floor Chair"
S["pdp_head"]["blocks"]["i3"]["settings"]["value"] = "Fabric or synthetic leather, sponge, plastic"
S["pdp_head"]["blocks"]["i4"]["settings"]["value"] = "Dark Grey\nBeige\nMandarin Orange\nMustard"
S["pdp_head"]["settings"]["subtitle"] = (
    "The start of healthy floor sitting - an S-Curve backrest, flexible tilting and a "
    "thick sponge seat bring ergonomic support down to floor level."
)

S["hero"] = {
    "type": "sidiz-pdp-hero",
    "settings": {
        "subtitle": "The start of healthy floor sitting",
        "subtitle_colour": "#ffffff",
        "heading": "PILLO",
        "heading_colour": "#ffffff",
        "text_align": "center",
        "header_scheme": "dark",
        "image_url": img("Head_vw55.jpg"),
        "image_url_mobile": img("pillo_HEAD_M.jpg"),
        "alt": "The SIDIZ PILLO floor chair in a living space",
        "description": (
            "<p>With ergonomic design and considerate usability, the PILLO makes floor "
            "sitting more comfortable and healthier.</p>"
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
            "title": "Fabric",
            "description": "Fabric seat",
            "images": img("Pillo_option_1.jpg") + "," + img("Pillo_option_1-2.jpg"),
            "colours": "#5a5d60,#d9c9b2,#c96f3f,#c9a13f",
            "alt": "The PILLO with the fabric seat"}},
        "o2": {"type": "option", "settings": {
            "title": "Vegan Leather",
            "description": "Synthetic leather seat",
            "images": img("Pillo_option_2.jpg") + "," + img("Pillo_option_2-1.jpg"),
            "colours": "#5a5d60,#d9c9b2",
            "alt": "The PILLO with the synthetic leather seat"}},
    },
    "block_order": ["o1", "o2"],
    "settings": {"heading": "The PILLO option for you"},
}

S["ergonomics_view"] = {
    "type": "sidiz-product-view-vertical",
    "settings": {
        "heading": "Ergonomics, even on the floor",
        "description": (
            "<p>So floor sitting never costs you posture or comfort, the PILLO carries "
            "ergonomic thinking through every part - easy on the body, hour after hour.</p>"
        ),
        "image_url": img("content_1.jpg"),
        "alt": "The PILLO supporting an upright floor sit",
    },
    "blocks": {
        "b1": {"type": "feature", "settings": {
            "title": "A backrest shaped like the spine",
            "description": "<p>An S-Curve form gives the lower back its most natural support, comfortable through long sittings.</p>",
            "image_url": img("content_2.jpg"),
            "alt": "The PILLO's S-Curve backrest"}},
        "b2": {"type": "feature", "settings": {
            "title": "Flexible backrest tilting",
            "description": "<p>The backrest leans naturally with your movement, keeping lumbar fatigue to a minimum.</p>",
            "image_url": img("content_3.jpg"),
            "alt": "The PILLO backrest tilting"}},
        "b3": {"type": "feature", "settings": {
            "title": "A thick sponge seat",
            "description": "<p>Generous sponge with a latex-like cushioning for a settled, comfortable sit.</p>",
            "image_url": img("content_4.jpg"),
            "alt": "The PILLO's thick sponge seat"}},
        "b4": {"type": "feature", "settings": {
            "title": "A springy, fresh double-raschel back",
            "description": "<p>Two layers of mesh double the spring and durability while keeping the airflow.</p>",
            "image_url": img("content_5.jpg"),
            "alt": "The double-raschel mesh backrest"}},
    },
    "block_order": ["b1", "b2", "b3", "b4"],
}

S["design_banner"] = {
    "type": "sidiz-wb-banner",
    "settings": {
        "heading": "Design that keeps caring",
        "description": (
            "<p>Considerate detail for when the PILLO is in use, when it is put away - "
            "and for everything after.</p>"
        ),
        "align": "left",
        "title_colour": "#ffffff",
        "description_colour": "#ffffff",
        "image_url": img("article_1_eb918cb9-cf3a-4745-9e18-b9c3137b1369.jpg"),
        "image_url_mobile": img("pillo_Type_B-2_M.jpg"),
        "alt": "The PILLO folded away neatly",
    },
}

S["design_cards"] = {
    "type": "sidiz-wb-card-list",
    "blocks": {
        "c1": {"type": "card", "settings": {
            "title": "Glides made for real floors",
            "title_colour": "#000000",
            "description": "<p>Felt glides minimise friction, sparing floors from scratches and rooms from noise.</p>",
            "description_colour": "#7c8084",
            "image_url": img("article1.jpg"),
            "alt": "The PILLO's felt glides"}},
        "c2": {"type": "card", "settings": {
            "title": "A folding backrest that saves space",
            "title_colour": "#000000",
            "description": "<p>Folds flat to slide under a desk or stand against the wall. *Fits floor desks 280 mm and higher.</p>",
            "description_colour": "#7c8084",
            "image_url": img("article2.jpg"),
            "alt": "The PILLO folded for storage"}},
        "c3": {"type": "card", "settings": {
            "title": "A replaceable seat",
            "title_colour": "#000000",
            "description": "<p>The seat swaps easily, keeping the chair like new for years. *Available through our support team.</p>",
            "description_colour": "#7c8084",
            "image_url": img("article3.jpg"),
            "alt": "Replacing the PILLO seat"}},
    },
    "block_order": ["c1", "c2", "c3"],
    "settings": {"heading": ""},
}

S["finish_tiles"] = {
    "type": "sidiz-tile-card-list",
    "blocks": {
        "t1": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "Fabric seat",
            "description": "<p>Soft and snug to sit on, in a choice of four colours to suit your taste and space.</p>",
            "image_url": img("article2_1.jpg"),
            "alt": "The PILLO fabric seat colours"}},
    },
    "block_order": ["t1"],
    "settings": {"heading": "A finish to suit your taste"},
}

S["goes_with"] = {
    "type": "sidiz-related-products",
    "settings": {"heading": "Goes well with the PILLO", "source": "collection", "limit": 4},
}

S["specifications"] = copy.deepcopy(B["specifications"])
S["specifications"]["settings"]["heading"] = "PILLO dimensions"
S["specifications"]["settings"]["figures"] = "Product weight approximately 4.4 kg."
S["specifications"]["settings"]["caveats"] = (
    "*Measurements may vary by plus or minus 20 mm and 1 kg depending on where and how "
    "they are taken; this is not a fault.<br>*Dimensions are measured with nobody seated."
)
S["specifications"]["blocks"]["d1"]["settings"].update({
    "image_url": img("M090_01.jpg"),
    "alt": "Dimension drawing of the SIDIZ PILLO, front elevation"})
S["specifications"]["blocks"]["d2"]["settings"].update({
    "image_url": img("M090_02.jpg"),
    "alt": "Dimension drawing of the SIDIZ PILLO, side elevation"})

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
        "description": "Seat feel differs from body to body. Try a PILLO in person where you can; otherwise our returns policy is there to fall back on.",
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
    "ergonomics_view", "design_banner", "design_cards", "finish_tiles",
    "goes_with", "specifications", "safety_info",
    "reviews", "stockists", "recommend", "notices",
]
assert set(order) == set(S), set(order) ^ set(S)

out = ROOT / "theme/templates/product.pillo.json"
out.write_text(json.dumps({"sections": S, "order": order}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print("written", out.name, "sections:", len(order))
