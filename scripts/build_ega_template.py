"""Compose product.ega.json.

EGA is the Claudio Bellini multi-purpose chair: image hero, a five-way option
compare (leather guidance dropped), the lineup scroll banner and two-card
list, the ergonomics view, the six-tile base-and-finish grid and a
ten-drawing spec across the five configurations (the KR stub entry with
placeholder figures is dropped; EGA Daily's drawings are kept without
figures the KR page does not state).
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
    "n2": {"type": "link", "settings": {"label": "Lineup", "anchor": "lineup"}},
    "n3": {"type": "link", "settings": {"label": "Ergonomics", "anchor": "ergonomics"}},
    "n4": {"type": "link", "settings": {"label": "Bases and finishes", "anchor": "finishes"}},
    "n5": {"type": "link", "settings": {"label": "Specifications", "anchor": "specifications"}},
    "n6": {"type": "link", "settings": {"label": "FAQ", "anchor": "faq"}},
}
S["sticky_nav"]["block_order"] = ["n1", "n2", "n3", "n4", "n5", "n6"]

S["pdp_head"] = copy.deepcopy(B["pdp_head"])
S["pdp_head"]["blocks"]["i1"]["settings"]["value"] = "SIDIZ EGA Multi-Purpose Chair"
S["pdp_head"]["blocks"]["i3"]["settings"]["value"] = "Fabric or synthetic leather, sponge, plastic, steel"
S["pdp_head"]["settings"]["subtitle"] = (
    "Enjoy genuine comfort anytime: Claudio Bellini's fluid curves and a low, open "
    "backrest, in five base configurations for living, dining and light work."
)

S["hero"] = {
    "type": "sidiz-pdp-hero",
    "settings": {
        "subtitle": "Enjoy Genuine-comfort Anytime!",
        "subtitle_colour": "#ffffff",
        "heading": "EGA",
        "heading_colour": "#ffffff",
        "text_align": "center",
        "header_scheme": "dark",
        "image_url": img("EGA_Head.jpg"),
        "image_url_mobile": img("EGA_Head_M-0.jpg"),
        "alt": "SIDIZ EGA chairs in a living-dining space",
        "description": (
            "<p>The SIDIZ EGA folds the engineering of comfort into a fluid design. "
            "Drawn by the renowned designer Claudio Bellini, its stingray-like curved "
            "frame and low backrest keep even a small room or living space feeling "
            "open.</p><p>A multi-purpose chair that holds the body comfortably, wherever "
            "it stands.</p>"
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
            "images": img("EGA_Option1.jpg") + "," + img("EGA_Option1-1.jpg"),
            "alt": "The EGA 4-legs frame with castors"}},
        "o2": {"type": "option", "settings": {
            "title": "4-Legs / Glides",
            "description": "The four-leg frame on a fixed glide base",
            "images": img("EGA_Option2.jpg") + "," + img("EGA_Option2-1.jpg"),
            "alt": "The EGA 4-legs frame with glides"}},
        "o3": {"type": "option", "settings": {
            "title": "Height Adjustable / Castors",
            "description": "Height adjustment on a mobile castor base",
            "images": img("EGA_Option3.jpg") + "," + img("EGA_Option3-1.jpg"),
            "alt": "The height-adjustable EGA with castors"}},
        "o4": {"type": "option", "settings": {
            "title": "Height Adjustable / Glides",
            "description": "Height adjustment on a fixed glide base",
            "images": img("EGA_Option4.jpg") + "," + img("EGA_Option4-1.jpg"),
            "alt": "The height-adjustable EGA with glides"}},
        "o5": {"type": "option", "settings": {
            "title": "EGA Daily",
            "description": "The home-office base with height adjustment and castors",
            "images": img("Img1_58304cce-df00-4472-958b-1aedad262113.jpg") + "," + img("Img2_28246805-ceb5-4f6b-9e70-1b9c1631222f.jpg"),
            "alt": "The EGA Daily on its home-office base"}},
    },
    "block_order": ["o1", "o2", "o3", "o4", "o5"],
    "settings": {"heading": "The EGA option for you"},
}

S["lineup_banner"] = {
    "type": "sidiz-wb-scroll-banner",
    "settings": {
        "heading": "",
        "header_scheme": "light",
        "tag": "",
        "subheading": "The EGA lineup, from open living-dining<br>to the study and home office",
        "description": (
            "<p>Lighter in open spaces, steadier where you concentrate - the base design "
            "itself is finished to suit the room.</p>"
        ),
        "text_colour": "#000000",
        "image_url": img("Img_33a80ad4-98bb-4b72-90eb-fdd61d7448b5.jpg"),
        "image_url_mobile": img("EGA_m2.jpg"),
        "alt": "The EGA lineup across living spaces",
    },
}

S["lineup_cards"] = {
    "type": "sidiz-wb-scroll-card-list",
    "blocks": {
        "c1": {"type": "card", "settings": {
            "title": "A simple leg design made for the dining space",
            "title_colour": "#000000",
            "description": "<p>Considering the mix of chairs a dining space holds, a simple leg design in high-strength material keeps the impression clean and the sit steady.</p>",
            "description_colour": "#7c8084",
            "image_url": img("Img_4_3_eb94f75e-ca36-481b-90b8-f74b7c0eecf4.jpg"),
            "alt": "The EGA in a dining setting"}},
        "c2": {"type": "card", "settings": {
            "title": "EGA Daily: the light work chair for the home office",
            "title_colour": "#000000",
            "description": "<p>A home-office base and structurally steady form, comfortable through work and study, at home in the study and workspace.</p>",
            "description_colour": "#7c8084",
            "image_url": img("Img_4_3_2_ffa4e9a0-6704-46d5-a283-82665ca08239.jpg"),
            "alt": "The EGA Daily at a home-office desk"}},
    },
    "block_order": ["c1", "c2"],
    "settings": {"header_scheme": "light", "background": "#ffffff"},
}

S["ergonomics_view"] = {
    "type": "sidiz-product-view-vertical",
    "settings": {
        "heading": "Study the body, design the comfort",
        "description": (
            "<p>Ergonomic engineering hidden inside a simple design: knowing chairs "
            "matters, and studying the body matters as much. The EGA's thoroughly "
            "engineered comfort lasts from the moment you sit to the moment you "
            "stand.</p>"
        ),
        "image_url": img("EGA_01_4e88779a-a06a-4ef6-986a-c73422b276a1.jpg"),
        "alt": "The EGA supporting a relaxed sit",
    },
    "blocks": {
        "b1": {"type": "feature", "settings": {
            "title": "A flexible backrest for every movement",
            "description": "<p>A U-shaped frame open at the top meets flexible Climaflex sponge for support that is firm yet soft.</p>",
            "image_url": img("EGA_01-1.jpg"),
            "alt": "The EGA's flexible U-frame backrest"}},
        "b2": {"type": "feature", "settings": {
            "title": "A generous seat",
            "description": "<p>Roomy enough to sit cross-legged in comfort.</p>",
            "image_url": img("Img_270af5b8-4e3d-4df3-abab-1005bffa942a.jpg"),
            "alt": "The EGA's generous seat"}},
        "b3": {"type": "feature", "settings": {
            "title": "A backrest at the right height",
            "description": "<p>High enough to support the upper back comfortably, low enough never to crowd the table it pairs with.</p>",
            "image_url": img("EGA_01-3.jpg"),
            "alt": "The EGA's backrest height at the table"}},
        "b4": {"type": "feature", "settings": {
            "title": "Armrests that steady you",
            "description": "<p>Steady through a change of posture and the moments of sitting down and standing up.</p>",
            "image_url": img("EGA_01-4.jpg"),
            "alt": "The EGA's supportive armrests"}},
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
            "image_url": img("LINIE_3_2__01_2ec94a7d-2da6-43d7-8617-10d7947a6b5a.jpg"),
            "alt": "The EGA 4-legs base"}},
        "t2": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "Height adjustable",
            "description": "<p>Set the height to different builds and tables, and swivel freely for a wider range of movement.</p>",
            "image_url": img("LINIE_3_2__02_c71d3fb1-9080-451d-86d3-9844904cb1bb.jpg"),
            "alt": "The height-adjustable EGA base"}},
        "t3": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "Glide option",
            "description": "<p>Fixed steadily in place for a sit without wobble.</p>",
            "image_url": img("LINIE_3_2__03_05190c7e-30b1-4582-94f3-7f8e4a682f25.jpg"),
            "alt": "The EGA glide option"}},
        "t4": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "Castor option",
            "description": "<p>Soft castors move freely and make it easy to reset your posture.</p>",
            "image_url": img("LINIE_3_2__04_2006eea4-afc9-4e01-9139-d09af5072f6e.jpg"),
            "alt": "The EGA castor option"}},
        "t5": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "Fabric finish",
            "description": "<p>Soft and snug to sit on, in a choice of four colours to suit your taste and space.</p>",
            "image_url": img("LINIE_3_2__05_e91389ef-4def-4899-9a77-5e3ecb7f768e.jpg"),
            "alt": "The fabric-finish EGA"}},
        "t6": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "Vegan leather finish",
            "description": "<p>A refined look that is strong against stains and easy to keep clean.</p>",
            "image_url": img("LINIE_3_2__06_b9ebfe48-c5b3-435a-a86a-308c85539868.jpg"),
            "alt": "The vegan-leather EGA"}},
    },
    "block_order": ["t1", "t2", "t3", "t4", "t5", "t6"],
    "settings": {"heading": "Choose the EGA that fits you"},
}

S["goes_with"] = {
    "type": "sidiz-related-products",
    "settings": {"heading": "Goes well with the EGA", "source": "collection", "limit": 4},
}

S["warranty"] = copy.deepcopy(B["warranty"])
S["warranty"]["settings"]["heading"] = "EGA | 5-year warranty"
S["warranty"]["settings"]["body"] = (
    "<p>So the journey with your EGA continues, SIDIZ provides a 5-year warranty to "
    "customers who complete product registration. Once your chair arrives, register it "
    "before you forget, for more comfortable years ahead.</p>"
)

S["specifications"] = copy.deepcopy(B["specifications"])
S["specifications"]["settings"]["heading"] = "EGA dimensions"
S["specifications"]["settings"]["figures"] = (
    "Maximum load 112-125 kg depending on the base; product weight approximately "
    "8.9-9.3 kg."
)
DRAWINGS = [
    ("TN601FEY_01_71a4bd3d-2107-401f-aed4-cc89767b8b6b.jpg", "4-legs EGA on castors, front elevation"),
    ("TN601FEY_02_0d8f3ede-bcc1-4a2c-a7ed-7f2f36eba019.jpg", "4-legs EGA on castors, side elevation"),
    ("TN603FY_01_75b3de12-fa6c-44a9-839f-1158de6b4101.jpg", "height-adjustable EGA on castors, front elevation"),
    ("TN603FY_02_a61e6229-61cd-4bb3-a8d7-d9b4f938a2d6.jpg", "height-adjustable EGA on castors, side elevation"),
    ("TN601FE_01_2b686019-f72d-415b-b8d1-60d9cf7fc3b2.jpg", "4-legs EGA on glides, front elevation"),
    ("TN601FE_02_e76e84d9-cd32-482a-b64d-0a3e8d2df934.jpg", "4-legs EGA on glides, side elevation"),
    ("TN603FG_01_f6ef4bd1-fe8e-4240-81e0-fc50fe395362.jpg", "height-adjustable EGA on glides, front elevation"),
    ("TN603FG_02_02bf28f5-7263-4a85-b9ac-e20f98d8be70.jpg", "height-adjustable EGA on glides, side elevation"),
    ("EGA_DAILY_01.jpg", "EGA Daily, front elevation"),
    ("EGA_DAILY_02.jpg", "EGA Daily, side elevation"),
]
S["specifications"]["blocks"] = {
    f"d{i+1}": {"type": "drawing", "settings": {
        "image_url": img(name), "alt": f"Dimension drawing of the {alt}"}}
    for i, (name, alt) in enumerate(DRAWINGS)
}
S["specifications"]["block_order"] = [f"d{i+1}" for i in range(len(DRAWINGS))]

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
        "description": "Seat feel differs from body to body. Try an EGA in person where you can; otherwise our returns policy is there to fall back on.",
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
    "lineup_banner", "lineup_cards", "ergonomics_view", "finish_tiles",
    "goes_with", "warranty", "specifications", "safety_info", "faq",
    "reviews", "stockists", "recommend", "notices",
]
assert set(order) == set(S), set(order) ^ set(S)

out = ROOT / "theme/templates/product.ega.json"
out.write_text(json.dumps({"sections": S, "order": order}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print("written", out.name, "sections:", len(order))
