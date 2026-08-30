"""Compose product.button.json.

BUTTON is the multi-purpose chair: image hero, four-way option compare
(leather guidance dropped), the support view (one KR block is text-only),
the six-tile option/finish grid and a compact tail. The KR spec section
carries a stub entry with placeholder figures - only the four real
configurations are reproduced.
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
    "n2": {"type": "link", "settings": {"label": "Support", "anchor": "support"}},
    "n3": {"type": "link", "settings": {"label": "Bases and finishes", "anchor": "finishes"}},
    "n4": {"type": "link", "settings": {"label": "Specifications", "anchor": "specifications"}},
    "n5": {"type": "link", "settings": {"label": "FAQ", "anchor": "faq"}},
}
S["sticky_nav"]["block_order"] = ["n1", "n2", "n3", "n4", "n5"]

S["pdp_head"] = copy.deepcopy(B["pdp_head"])
S["pdp_head"]["blocks"]["i1"]["settings"]["value"] = "SIDIZ BUTTON Multi-Purpose Chair"
S["pdp_head"]["blocks"]["i3"]["settings"]["value"] = "Plastic or fabric, sponge, steel"
S["pdp_head"]["settings"]["subtitle"] = (
    "Button up your comfort: a clean, compact multi-purpose chair with a supportive "
    "backrest and four base configurations for dining, living and home-office rooms."
)

S["hero"] = {
    "type": "sidiz-pdp-hero",
    "settings": {
        "subtitle": "<em class=\"caps\">Button up your comfort</em>",
        "subtitle_colour": "#ffffff",
        "heading": "BUTTON",
        "heading_colour": "#ffffff",
        "text_align": "center",
        "header_scheme": "dark",
        "image_url": img("BUTTON_Head.jpg"),
        "image_url_mobile": img("BUTTON_Head_M-0_706c0509-d3ed-4ab1-9efa-0559def75ca1.jpg"),
        "alt": "SIDIZ BUTTON chairs in a living space",
        "description": (
            "<p>The SIDIZ BUTTON is a multi-purpose interior chair whose clean, "
            "uncluttered design settles naturally into any room - dining space, living "
            "room or home office.</p><p>Compact in form yet steady in backrest support "
            "and comfortable to sit in, it is a design chair that satisfies both the "
            "look of a space and the use of it.</p>"
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
            "title": "4-Legs / Castors",
            "description": "The four-leg frame on a mobile castor base",
            "images": img("BUTTON_Option4_9fcca377-97be-4bc4-86ab-d0eb39f7f9a7.jpg") + "," + img("BUTTON_Option4-1_172bd351-81a1-45bb-9875-fb4136209740.jpg"),
            "alt": "The BUTTON 4-legs frame with castors"}},
        "o2": {"type": "option", "settings": {
            "title": "4-Legs / Glides",
            "description": "The four-leg frame on a fixed glide base",
            "images": img("BUTTON_Option3_5f43c212-4269-4a9f-a4c8-c4f0ee772141.jpg") + "," + img("BUTTON_Option3-1_5a03c11d-d66b-44c0-b5b0-e85f87a47c51.jpg"),
            "alt": "The BUTTON 4-legs frame with glides"}},
        "o3": {"type": "option", "settings": {
            "title": "Height Adjustable / Castors",
            "description": "Height adjustment on a mobile castor base",
            "images": img("BUTTON_Option2_7e53c1cb-0171-4e0f-82e4-8d78dab36805.jpg") + "," + img("BUTTON_Option2-1_830d7d50-5f2d-4675-bee9-4b8886cb5f6a.jpg"),
            "alt": "The height-adjustable BUTTON with castors"}},
        "o4": {"type": "option", "settings": {
            "title": "Height Adjustable / Glides",
            "description": "Height adjustment on a fixed glide base",
            "images": img("BUTTON_Option1.jpg") + "," + img("BUTTON_Option1-1.jpg"),
            "alt": "The height-adjustable BUTTON with glides"}},
    },
    "block_order": ["o1", "o2", "o3", "o4"],
    "settings": {"heading": "The BUTTON option for you"},
}

S["support_view"] = {
    "type": "sidiz-product-view-vertical",
    "settings": {
        "heading": "Support that steadies the body",
        "description": (
            "<p>Knowing chairs matters; studying bodies matters as much. The BUTTON's "
            "ergonomic stability holds you firmly, for comfort that stays.</p>"
        ),
        "image_url": img("BUTTON_01.jpg"),
        "alt": "The BUTTON supporting an upright sit",
    },
    "blocks": {
        "b1": {"type": "feature", "settings": {
            "title": "Flexibility that holds through any movement",
            "description": "<p>Elasticity built into the material absorbs the lean and flexes as posture changes, keeping the body's load minimal.</p>"}},
        "b2": {"type": "feature", "settings": {
            "title": "A backrest hole that suits every posture",
            "description": "<p>A design point that lets any build adjust their position at will, adding comfort to whatever posture the moment calls for.</p>",
            "image_url": img("BUTTON_01-2.jpg"),
            "alt": "The BUTTON's backrest hole"}},
        "b3": {"type": "feature", "settings": {
            "title": "A backrest at the right height",
            "description": "<p>High enough to support the upper back comfortably, low enough never to crowd the table it pairs with.</p>",
            "image_url": img("BUTTON_01-3.jpg"),
            "alt": "The BUTTON's backrest height at the table"}},
        "b4": {"type": "feature", "settings": {
            "title": "A generous seat",
            "description": "<p>Roomy enough to sit cross-legged in comfort.</p>",
            "image_url": img("BUTTON_01-4.jpg"),
            "alt": "The BUTTON's generous seat"}},
    },
    "block_order": ["b1", "b2", "b3", "b4"],
}

S["finish_tiles"] = {
    "type": "sidiz-tile-card-list",
    "blocks": {
        "t1": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "4-Legs",
            "description": "<p>The most classic build, easy to style. Steel for durability, with a slim line running to the floor for visual openness.</p>",
            "image_url": img("LINIE_3_2__01.jpg"),
            "alt": "The BUTTON 4-legs base"}},
        "t2": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "Height adjustable",
            "description": "<p>Set the height to different builds and tables, and swivel freely for a wider range of movement.</p>",
            "image_url": img("LINIE_3_2__02_aae8e7db-abb3-4201-8282-1adc6f38b6ba.jpg"),
            "alt": "The height-adjustable BUTTON base"}},
        "t3": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "Glide option",
            "description": "<p>Fixed steadily in place for a sit without wobble.</p>",
            "image_url": img("LINIE_3_2__03.jpg"),
            "alt": "The BUTTON glide option"}},
        "t4": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "Castor option",
            "description": "<p>Soft castors move freely and make it easy to reset your posture.</p>",
            "image_url": img("LINIE_3_2__04.jpg"),
            "alt": "The BUTTON castor option"}},
        "t5": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "Plastic finish",
            "description": "<p>A refined dot-pattern plastic that keeps care easy and blends into any interior.</p>",
            "image_url": img("LINIE_3_2__05.jpg"),
            "alt": "The dot-pattern plastic finish"}},
        "t6": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "Fabric finish",
            "description": "<p>Fabric adds warmth to the BUTTON's design language, and the backrest cover removes easily for a change of look.</p>",
            "image_url": img("LINIE_3_2__06.jpg"),
            "alt": "The fabric finish with its removable cover"}},
    },
    "block_order": ["t1", "t2", "t3", "t4", "t5", "t6"],
    "settings": {"heading": "Choose the BUTTON that fits you"},
}

S["goes_with"] = {
    "type": "sidiz-related-products",
    "settings": {"heading": "Goes well with the BUTTON", "source": "collection", "limit": 4},
}

S["warranty"] = copy.deepcopy(B["warranty"])
S["warranty"]["settings"]["heading"] = "BUTTON | 5-year warranty"
S["warranty"]["settings"]["body"] = (
    "<p>So the journey with your BUTTON continues, SIDIZ provides a 5-year warranty to "
    "customers who complete product registration. Once your chair arrives, register it "
    "before you forget, for more comfortable years ahead.</p>"
)

S["specifications"] = copy.deepcopy(B["specifications"])
S["specifications"]["settings"]["heading"] = "BUTTON dimensions"
S["specifications"]["settings"]["figures"] = (
    "Maximum load 112-125 kg depending on the base; product weight approximately "
    "8.9-9.3 kg."
)
S["specifications"]["blocks"] = {
    "d1": {"type": "drawing", "settings": {
        "image_url": img("MN803G__01_35fe52be-bc78-44ac-8ae2-5d2b41aa6b46.jpg"),
        "alt": "Dimension drawing of the 4-legs BUTTON on glides, front elevation"}},
    "d2": {"type": "drawing", "settings": {
        "image_url": img("MN803G__02_7aff3e0b-1712-40fa-b8c4-5867eb89e607.jpg"),
        "alt": "Dimension drawing of the 4-legs BUTTON on glides, side elevation"}},
    "d3": {"type": "drawing", "settings": {
        "image_url": img("MN803Y__01_2e7d255d-dc40-43c2-822b-5ca63eaf179d.jpg"),
        "alt": "Dimension drawing of the 4-legs BUTTON on castors, front elevation"}},
    "d4": {"type": "drawing", "settings": {
        "image_url": img("MN803Y__02_5203bd59-f841-4429-af18-7b5296559c74.jpg"),
        "alt": "Dimension drawing of the 4-legs BUTTON on castors, side elevation"}},
    "d5": {"type": "drawing", "settings": {
        "image_url": img("MN801E__01_75616010-569d-4b1e-afa0-4170576480a8.jpg"),
        "alt": "Dimension drawing of the height-adjustable BUTTON on glides, front elevation"}},
    "d6": {"type": "drawing", "settings": {
        "image_url": img("MN801E__02_f511f109-dc0a-4b66-a6d3-e543dad51f2b.jpg"),
        "alt": "Dimension drawing of the height-adjustable BUTTON on glides, side elevation"}},
    "d7": {"type": "drawing", "settings": {
        "image_url": img("MN801EY__01_48a9632f-413b-4a18-93fc-84ce5c7afb78.jpg"),
        "alt": "Dimension drawing of the height-adjustable BUTTON on castors, front elevation"}},
    "d8": {"type": "drawing", "settings": {
        "image_url": img("MN801EY__02_e0c4de14-0cae-43b7-9b48-4a89a8239ebf.jpg"),
        "alt": "Dimension drawing of the height-adjustable BUTTON on castors, side elevation"}},
}
S["specifications"]["block_order"] = ["d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8"]

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

S["faq"] = {
    "type": "sidiz-faq",
    "blocks": {
        "q1": {"type": "faq", "settings": {
            "question": "I bought castors - can I switch to glides?",
            "answer": "<p>Yes, castors and fixed glides interchange - contact our support team to arrange it. Note the chair's height changes with the swap, and on the 4-legs frame the leg frames differ between castor and glide fittings, so the frames swap too.</p>"}},
    },
    "block_order": ["q1"],
    "settings": {"heading": "Frequently asked questions", "open_first": True, "background": "#f5f6f7"},
}

S["reviews"] = copy.deepcopy(B["reviews"])

S["stockists"] = {
    "type": "sidiz-store-info",
    "settings": {
        "heading": "Try one before you decide",
        "description": "Seat feel differs from body to body. Try a BUTTON in person where you can; otherwise our returns policy is there to fall back on.",
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
    "support_view", "finish_tiles",
    "goes_with", "warranty", "specifications", "safety_info", "faq",
    "reviews", "stockists", "recommend", "notices",
]
assert set(order) == set(S), set(order) ^ set(S)

out = ROOT / "theme/templates/product.button.json"
out.write_text(json.dumps({"sections": S, "order": order}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print("written", out.name, "sections:", len(order))
