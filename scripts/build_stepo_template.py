"""Compose product.stepo-footrest.json.

STEPO is the ergonomic footrest: image hero, a two-option compare (leather
guidance dropped - no leather on the STEPO), the ergonomic-design view, the
padded-cover view, the cover fitting guide (KR's product_assembly_guide here
is a real fitting guide, not reviews - gotcha 3), four use-case tiles and a
compact tail with the step-stool warning kept.
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
    "n2": {"type": "link", "settings": {"label": "Design", "anchor": "design"}},
    "n3": {"type": "link", "settings": {"label": "Cover", "anchor": "cover"}},
    "n4": {"type": "link", "settings": {"label": "Uses", "anchor": "uses"}},
    "n5": {"type": "link", "settings": {"label": "Specifications", "anchor": "specifications"}},
    "n6": {"type": "link", "settings": {"label": "FAQ", "anchor": "faq"}},
}
S["sticky_nav"]["block_order"] = ["n1", "n2", "n3", "n4", "n5", "n6"]

S["pdp_head"] = copy.deepcopy(B["pdp_head"])
S["pdp_head"]["blocks"]["i1"]["settings"]["value"] = "SIDIZ STEPO Ergonomic Footrest"
S["pdp_head"]["blocks"]["i2"]["settings"]["value"] = "Footrest"
S["pdp_head"]["blocks"]["i3"]["settings"]["value"] = "Fabric, plastic"
S["pdp_head"]["blocks"]["i4"]["settings"]["value"] = "Charcoal Grey\nBeige\nMint Green\nGrey"
S["pdp_head"]["settings"]["subtitle"] = (
    "The posture mate: when feet do not fully reach the floor, the STEPO settles them "
    "at the right height and angle to complete an upright sit."
)

S["hero"] = {
    "type": "sidiz-pdp-hero",
    "settings": {
        "subtitle": "The posture mate",
        "subtitle_colour": "#ffffff",
        "heading": "STEPO",
        "heading_colour": "#ffffff",
        "text_align": "center",
        "header_scheme": "dark",
        "image_url": img("STEPO_Head.jpg"),
        "image_url_mobile": img("STEPO_Head_M.jpg"),
        "alt": "Feet resting on the SIDIZ STEPO footrest",
        "description": (
            "<p>When feet do not fully reach the floor, posture drifts. Let the STEPO "
            "settle your feet steadily and complete an upright sit.</p>"
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
            "title": "Standard",
            "description": "The STEPO as it comes",
            "images": img("STEPO_Option1.jpg") + "," + img("STEPO_Option1-1.jpg"),
            "colours": "#989b98",
            "alt": "The standard SIDIZ STEPO"}},
        "o2": {"type": "option", "settings": {
            "title": "Padded Cover",
            "description": "With the padded fabric cover fitted",
            "images": img("STEPO_Option2.jpg") + "," + img("STEPO_Option2-1.jpg"),
            "colours": "#4a4a4d,#d9c9b2,#a8c1b4",
            "alt": "The SIDIZ STEPO with its padded cover"}},
    },
    "block_order": ["o1", "o2"],
    "settings": {"heading": "The STEPO option for you"},
}

S["design_view"] = {
    "type": "sidiz-product-view-vertical",
    "settings": {
        "heading": "Ergonomic design for upright posture",
        "description": (
            "<p>SIDIZ ergonomics keep the STEPO steady and comfortable however the "
            "posture or situation changes.</p>"
        ),
        "image_url": img("STEPO_01-0_1215c474-f2ef-41f1-bba0-608b10bc0a76.jpg"),
        "alt": "The STEPO's ergonomic form",
    },
    "blocks": {
        "b1": {"type": "feature", "settings": {
            "title": "23 cm, made for rest",
            "description": "<p>The height that lets you raise your legs and truly rest.</p>",
            "image_url": img("STEPO_01-1.jpg"),
            "alt": "The STEPO's 23 cm height"}},
        "b2": {"type": "feature", "settings": {
            "title": "13 degrees, made for posture",
            "description": "<p>The angle that spreads the load coming into the lower body.</p>",
            "image_url": img("STEPO_01-2_0fdfffca-ae5a-4e8f-93fa-bb60bb359ea8.jpg"),
            "alt": "The STEPO's 13 degree angle"}},
        "b3": {"type": "feature", "settings": {
            "title": "Non-slip pads, made for stability",
            "description": "<p>Grippy pads keep it planted, never sliding away underfoot.</p>",
            "image_url": img("STEPO_01-3.jpg"),
            "alt": "The STEPO's non-slip pads"}},
    },
    "block_order": ["b1", "b2", "b3"],
}

S["cover_view"] = {
    "type": "sidiz-product-view-vertical",
    "settings": {
        "heading": "Fresh and cosy, under one cover",
        "description": (
            "<p>The cover makes upkeep easy and the surface fresh - and its padding adds "
            "cosiness on top.</p>"
        ),
        "image_url": img("STEPO_02_1d909b54-1b11-4951-a6c3-49eee1c74944.jpg"),
        "alt": "The STEPO with its padded cover",
    },
    "blocks": {
        "b1": {"type": "feature", "settings": {
            "title": "Fresh in summer, cosy in winter",
            "description": "<p>Double-raschel fabric from premium upholstery brings airflow and durability in one weave.</p>",
            "image_url": img("STEPO_02-1.jpg"),
            "alt": "The double-raschel cover fabric"}},
        "b2": {"type": "feature", "settings": {
            "title": "Easy to look after",
            "description": "<p>Water- and stain-resistant finishes keep care simple, and the cover machine-washes when it needs it.</p>",
            "image_url": img("STEPO_02-2.jpg"),
            "alt": "Washing the STEPO cover"}},
    },
    "block_order": ["b1", "b2"],
}

S["cover_guide"] = {
    "type": "sidiz-tile-card-list",
    "blocks": {
        "t1": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "Step 1",
            "description": "<p>Slot the strip in with its groove facing the fabric pocket.</p>",
            "image_url": img("Img_1_1__01.jpg"),
            "alt": "Fitting the cover strip"}},
        "t2": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "Step 2",
            "description": "<p>Fit the strip into the top board, then fold the fabric over the back.</p>",
            "image_url": img("Img_1_1__02.jpg"),
            "alt": "Folding the fabric over"}},
        "t3": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "Step 3",
            "description": "<p>Pass the fabric's end through the gap between the first and second tiers, in the order shown.</p>",
            "image_url": img("Img_1_1__03.jpg"),
            "alt": "Passing the fabric through the tiers"}},
        "t4": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "Step 4",
            "description": "<p>Fasten the fabric's end to the velcro underneath.</p>",
            "image_url": img("Img_1_1__04.jpg"),
            "alt": "Fastening the cover to the velcro"}},
    },
    "block_order": ["t1", "t2", "t3", "t4"],
    "settings": {"heading": "Fitting the cover"},
}

S["use_tiles"] = {
    "type": "sidiz-tile-card-list",
    "blocks": {
        "t1": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "When focus matters",
            "description": "<p>Spreading the pressure that gathers in the lower body helps concentration hold.</p>",
            "image_url": img("STEPO_1_1__01.jpg"),
            "alt": "The STEPO under a desk"}},
        "t2": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "When a child is still growing",
            "description": "<p>For children whose feet do not reach the floor, it builds the habit of upright sitting.</p>",
            "image_url": img("STEPO_1_1__02.jpg"),
            "alt": "A child's feet on the STEPO"}},
        "t3": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "When it is time to rest",
            "description": "<p>Stretch your legs out or rest your feet up in comfort.</p>",
            "image_url": img("STEPO_1_1__03.jpg"),
            "alt": "Resting with the STEPO"}},
        "t4": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "When shoes need a home",
            "description": "<p>With shoes off, the space beneath the footrest keeps them.</p>",
            "image_url": img("STEPO_1_1__04.jpg"),
            "alt": "Shoes stored under the STEPO"}},
    },
    "block_order": ["t1", "t2", "t3", "t4"],
    "settings": {"heading": "One STEPO, many uses"},
}

S["goes_with"] = {
    "type": "sidiz-related-products",
    "settings": {"heading": "Goes well with the STEPO", "source": "collection", "limit": 4},
}

S["specifications"] = copy.deepcopy(B["specifications"])
S["specifications"]["settings"]["heading"] = "STEPO dimensions"
S["specifications"]["settings"]["figures"] = "Maximum load 65 kg / product weight approximately 2.2 kg."
S["specifications"]["settings"]["caveats"] = (
    "*Measurements may vary by plus or minus 20 mm and 1 kg depending on where and how "
    "they are taken; this is not a fault.<br>*Dimensions are measured with nobody seated."
)
S["specifications"]["blocks"]["d1"]["settings"].update({
    "image_url": img("SB01F1_01_46a485bb-823a-4f5e-8f03-aaa387bba990.jpg"),
    "alt": "Dimension drawing of the SIDIZ STEPO, front elevation"})
S["specifications"]["blocks"]["d2"]["settings"].update({
    "image_url": img("SB01F1_02_e6e935e3-8a8f-4286-bba3-e06cdece4e6d.jpg"),
    "alt": "Dimension drawing of the SIDIZ STEPO, side elevation"})

S["safety_info"] = {
    "type": "sidiz-safety-info",
    "blocks": {
        "n1": {"type": "note", "settings": {
            "title": "Not a step stool",
            "body": "<p>The STEPO carries up to 65 kg on its second tier, but it is not a step stool - standing on it is dangerous.</p>"}},
        "n2": {"type": "note", "settings": {
            "title": "Washing the cover",
            "body": "<p>Wash gently at 40 degrees. Oxygen bleach may be used. Iron between 80 and 120 degrees if needed. Dry cleaning is fine. Dry flat, in the shade.</p>"}},
        "n3": {"type": "note", "settings": {
            "title": "Removing stains from the frame",
            "body": "<p>If the frame gets marked, a melamine sponge lifts stains easily. *Rubbing hard can damage the surface.</p>"}},
    },
    "block_order": ["n1", "n2", "n3"],
    "settings": {"heading": "Care and cautions"},
}

S["faq"] = {
    "type": "sidiz-faq",
    "blocks": {
        "q1": {"type": "faq", "settings": {
            "question": "From what height can it be used?",
            "answer": "<p>The STEPO is designed for everyone, from young children to adults.</p>"}},
        "q2": {"type": "faq", "settings": {
            "question": "Can I buy the padded cover on its own?",
            "answer": "<p>Yes - to buy or replace just the cover, contact our support team.</p>"}},
    },
    "block_order": ["q1", "q2"],
    "settings": {"heading": "Frequently asked questions", "open_first": True, "background": "#f5f6f7"},
}

S["reviews"] = copy.deepcopy(B["reviews"])

S["stockists"] = {
    "type": "sidiz-store-info",
    "settings": {
        "heading": "Try one before you decide",
        "description": "Fit differs from body to body. Try a STEPO in person where you can; otherwise our returns policy is there to fall back on.",
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
    "design_view", "cover_view", "cover_guide", "use_tiles",
    "goes_with", "specifications", "safety_info", "faq",
    "reviews", "stockists", "recommend", "notices",
]
assert set(order) == set(S), set(order) ^ set(S)

out = ROOT / "theme/templates/product.stepo-footrest.json"
out.write_text(json.dumps({"sections": S, "order": order}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print("written", out.name, "sections:", len(order))
