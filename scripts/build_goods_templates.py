"""Compose product.the-p-bag.json and product.multispray-infinity.json.

The two goods pages are short: image hero, intro row, a few product views and
an FAQ. Neither KR page carries warranty, Easy Repair or store sections, and
the KR store-scenting line in the spray FAQ is phrased as the Korean stores
they are.
"""

import copy
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
KR = "https://kr.sidiz.com/cdn/shop"


def vid(id_, variant, n):
    return f"{KR}/videos/c/vp/{id_}/{id_}.{variant}-{n}.mp4"


def poster(id_):
    return f"{KR}/files/preview_images/{id_}.thumbnail.0000000000_small.jpg"


def img(name):
    return f"{KR}/files/{name}"


base = json.loads((ROOT / "theme/templates/product.t50-2.json").read_text(encoding="utf-8"))
B = base["sections"]


def tail(name):
    return {
        "reviews": copy.deepcopy(B["reviews"]),
        "recommend": {
            "type": "sidiz-related-products",
            "settings": {
                "heading": "You may also like",
                "link_label": "View all products",
                "link": "/collections/all",
                "source": "collection",
                "limit": 4,
            },
        },
        "notices": copy.deepcopy(B["notices"]),
    }


# ---------------------------------------------------------------- P-BAG
S = {}
S["pdp_head"] = copy.deepcopy(B["pdp_head"])
S["pdp_head"]["blocks"]["i1"]["settings"]["value"] = "SIDIZ The Progressive Bag"
S["pdp_head"]["blocks"]["i2"]["settings"]["value"] = "Bag"
S["pdp_head"]["blocks"]["i3"]["settings"]["value"] = "DuPont Tyvek (high-density polyethylene)"
S["pdp_head"]["blocks"]["i5"]["settings"]["value"] = "See product care notes"
S["pdp_head"]["settings"]["warranty_value"] = "-"
S["pdp_head"]["block_order"] = ["f1", "f2", "i1", "i2", "i3", "i5"]
S["pdp_head"]["settings"]["subtitle"] = (
    "A reusable everyday bag in 100 per cent recyclable Tyvek - light as paper, "
    "tough enough to retire the single-use shopping bag."
)

S["hero"] = {
    "type": "sidiz-pdp-hero",
    "settings": {
        "subtitle": "<em class=\"caps\">To sit is to progress</em>",
        "subtitle_colour": "#ffffff",
        "heading": "THE PROGRESSIVE BAG",
        "heading_colour": "#ffffff",
        "text_align": "center",
        "header_scheme": "dark",
        "image_url": img("Head_15060548-648e-41fc-9d8c-9e731b761934.jpg"),
        "image_url_mobile": img("Head_M_ed367a6d-ccdf-40bf-af35-6305df458796.jpg"),
        "alt": "The SIDIZ Progressive Bag carried over a shoulder",
        "description": (
            "<p>Beyond good chairs and the act of sitting, SIDIZ proposes a sustainable "
            "lifestyle that coexists with the planet. Made from 100 per cent recyclable "
            "Tyvek, the Progressive Bag is light as paper yet powerfully durable - a "
            "long-term companion in place of the single-use shopping bag.</p><p>Small "
            "acts add up: SIDIZ leads the circulation of resources and considered "
            "consumption toward a sustainable future.</p>"
        ),
        "description_colour": "#000000",
        "description_align": "left",
        "product_type": "default",
    },
}

S["intro"] = {
    "type": "sidiz-product-row",
    "settings": {
        "heading": "SIDIZ The Progressive Bag: the Eco-Lifestyle Reusable Bag",
        "body": (
            "<ul><li><strong>Eco-friendly Tyvek</strong> - DuPont high-density "
            "polyethylene, 100 per cent recyclable and burning without leaving harmful "
            "residues, easing the load on the planet.</li>"
            "<li><strong>High durability and water resistance</strong> - light as paper "
            "but hard to tear, and unbothered by water, so rain and everyday mess hold "
            "no fear.</li>"
            "<li><strong>A comfort shoulder strap</strong> - generously long for a "
            "stable, comfortable carry, hour after hour.</li>"
            "<li><strong>Easy, compact storage</strong> - room for pouches, wallets and "
            "A4 documents or books, folding flat when the day is done.</li></ul>"
            "<p>A daily side bag, an eco shopping bag, a commuting sub-bag - a "
            "reusable bag for a lighter, more sustainable everyday.</p>"
        ),
        "align": "left",
        "background": "#ffffff",
        "text_colour": "#000000",
    },
}

S["brand_banner"] = {
    "type": "sidiz-wb-banner",
    "settings": {
        "heading": "Sit, and become yourself<br><em class=\"caps\">To sit is to progress</em>",
        "align": "left",
        "title_colour": "#000000",
    },
}

S["brand_view"] = {
    "type": "sidiz-product-view-vertical",
    "settings": {
        "heading": "",
        "description": (
            "<p>SIDIZ goes beyond making good chairs to talk about the people and lives "
            "above them. Sitting, we deliberate, concentrate, try things every which "
            "way, and inch forward. Time spent sitting is our most intense and dynamic "
            "time - and all those seated moments, gathered, make a self. Our sitting is "
            "a journey toward being more ourselves.</p>"
        ),
        "video_url": vid("0084afd6a7ab49fc973de9e37f9da8f8", "HD-1080p-7.2Mbps", "58544034"),
        "poster_url": poster("0084afd6a7ab49fc973de9e37f9da8f8"),
        "alt": "The Progressive Bag in daily life",
    },
    "blocks": {},
    "block_order": [],
}

S["material_view"] = {
    "type": "sidiz-product-view-vertical",
    "settings": {
        "heading": "Light on the day, light on the planet",
        "description": (
            "<p>The Progressive Bag is made from DuPont Tyvek: high-density "
            "polyethylene that recycles fully and burns without leaving harmful "
            "residues. Light, tough, and made with sustainability in mind.</p>"
        ),
        "image_url": img("Img_8f360215-1535-4f13-9d2b-6ba0e76bda44.jpg"),
        "alt": "The Tyvek material up close",
    },
    "blocks": {
        "b1": {"type": "feature", "settings": {
            "title": "A light, tough daily partner",
            "description": "<p>Light as paper but hard to tear, and unbothered by water - useful all through the day.</p>",
            "image_url": img("Img_6a267143-484a-4a41-af56-73ad0e59b7a6.jpg"),
            "alt": "The bag holding its shape in use"}},
        "b2": {"type": "feature", "settings": {
            "title": "Better looking as time passes",
            "description": "<p>Tyvek's paper-like texture gains natural creases with use - character that grows on you.</p>",
            "image_url": img("Img2_224db752-528e-471d-af82-a4689438021a.jpg"),
            "alt": "The natural creases of worn Tyvek"}},
    },
    "block_order": ["b1", "b2"],
}

S["convenience_view"] = {
    "type": "sidiz-product-view-vertical",
    "settings": {
        "heading": "The convenience you keep reaching for",
        "description": (
            "<p>A generously long shoulder strap carries without strain, and the light, "
            "compact body suits a side bag or the shopping run - handy in all the "
            "situations a day brings.</p>"
        ),
        "image_url": img("Img3_d73536dc-ee81-4817-a01e-7b37c1edf5e7.jpg"),
        "alt": "The Progressive Bag worn on the shoulder",
    },
    "blocks": {
        "b1": {"type": "feature", "settings": {
            "title": "Light things, straight in",
            "description": "<p>From pouches to A4 documents, everyday items fit with room to spare.</p>",
            "image_url": img("unnamed.jpg"),
            "alt": "A4 documents sliding into the bag"}},
    },
    "block_order": ["b1"],
}

S["specifications"] = copy.deepcopy(B["specifications"])
S["specifications"]["settings"]["heading"] = "The Progressive Bag dimensions"
S["specifications"]["settings"]["figures"] = ""
S["specifications"]["settings"]["caveats"] = (
    "*Measurements may vary by plus or minus 20 mm depending on how they are taken; "
    "this is not a fault."
)
S["specifications"]["blocks"] = {
    "d1": {"type": "drawing", "settings": {
        "image_url": img("sidiz_dimension_THE_PROGRESSIVE_BAG.jpg"),
        "alt": "Dimension drawing of the SIDIZ Progressive Bag"}},
}
S["specifications"]["block_order"] = ["d1"]

S["faq"] = {
    "type": "sidiz-faq",
    "blocks": {
        "q1": {"type": "faq", "settings": {
            "question": "How do I clean the Tyvek bag?",
            "answer": "<p>Tyvek is water-resistant by nature, so avoid machine washing and dry cleaning. For light marks, wipe gently with running water, a damp cloth or a wet wipe, then air-dry in a well-ventilated, shaded spot and it stays clean for years without damaging the material.</p>"}},
        "q2": {"type": "faq", "settings": {
            "question": "How much does it hold? Does A4 fit?",
            "answer": "<p>The bag folds flat yet holds A4 paper, a small tablet, a cosmetics pouch or a tumbler with room to spare - an ideal size for a light commuting side bag or second bag. See the dimension drawing below for exact measurements.</p>"}},
        "q3": {"type": "faq", "settings": {
            "question": "It looks like crumpled paper - will it tear easily?",
            "answer": "<p>Tyvek's paper-like, analogue texture belies a highly functional material with real tensile strength. It resists tearing from pointed items and everyday knocks, and recovers well from getting wet, keeping its water resistance on rainy days - lighter than paper, tough as leather.</p>"}},
    },
    "block_order": ["q1", "q2", "q3"],
    "settings": {"heading": "Frequently asked questions", "open_first": True, "background": "#f5f6f7"},
}

S.update(tail("bag"))

order = [
    "pdp_head", "hero", "intro", "brand_banner", "brand_view",
    "material_view", "convenience_view", "specifications", "faq",
    "reviews", "recommend", "notices",
]
assert set(order) == set(S), set(order) ^ set(S)
out = ROOT / "theme/templates/product.the-p-bag.json"
out.write_text(json.dumps({"sections": S, "order": order}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print("written", out.name, "sections:", len(order))

# ---------------------------------------------------------- MULTI SPRAY
S = {}
S["pdp_head"] = copy.deepcopy(B["pdp_head"])
S["pdp_head"]["blocks"]["i1"]["settings"]["value"] = "SIDIZ Multi Spray INFINITY 150 mL"
S["pdp_head"]["blocks"]["i2"]["settings"]["value"] = "Fabric and room spray, 150 mL"
S["pdp_head"]["blocks"]["i3"]["settings"]["value"] = "See packaging for ingredients"
S["pdp_head"]["block_order"] = ["f1", "f2", "i1", "i2", "i3"]
S["pdp_head"]["settings"]["subtitle"] = (
    "A premium fabric deodorising and room spray, blended with Pale Blue Dot - "
    "citrus top notes settling into a soft musk."
)

S["hero"] = {
    "type": "sidiz-pdp-hero",
    "settings": {
        "subtitle": "Premium fabric &amp; room spray",
        "subtitle_colour": "#ffffff",
        "heading": "MULTI SPRAY INFINITY",
        "heading_colour": "#ffffff",
        "text_align": "center",
        "header_scheme": "dark",
        "image_url": img("Head_380b5047-4714-4596-af51-1ca2935decaf.jpg"),
        "image_url_mobile": img("Head_M_1376240a-1e06-4794-9537-36b2bbf3cf8f.jpg"),
        "alt": "The SIDIZ Multi Spray INFINITY bottle",
        "description": (
            "<p>The SIDIZ Multi Spray INFINITY is a premium fabric deodorising and room "
            "spray, made to deepen the immersion of the spaces where you work and "
            "rest.</p>"
        ),
        "description_colour": "#000000",
        "description_align": "left",
        "product_type": "default",
    },
}

S["intro"] = {
    "type": "sidiz-product-row",
    "settings": {
        "heading": "SIDIZ INFINITY Fabric Multi Spray",
        "body": (
            "<ul><li><strong>Deodorising made for fabric and mesh</strong> - excellent "
            "deodorising tuned to chairs, curtains, bedding and other fabric and mesh "
            "surfaces.</li>"
            "<li><strong>A considered scent</strong> - citrus top notes flowing into a "
            "soft musk base, in a distinctive composition.</li>"
            "<li><strong>Sustainable packaging</strong> - a top-grade recyclable clear "
            "PET bottle, a fully removable label and certified eco-friendly paper "
            "packaging.</li></ul>"
        ),
        "align": "left",
        "background": "#ffffff",
        "text_colour": "#000000",
    },
}

S["usage_view"] = {
    "type": "sidiz-product-view",
    "settings": {
        "tag": "Why does a chair brand make a spray?",
        "heading": "Multi-deodorising, from chairs to bedding",
        "description": (
            "<p>Spray lightly two or three times wherever you would like the scent - "
            "bedding, curtains, chairs. The deodorising action keeps fabric and mesh "
            "surfaces fresh.</p><p>*Do not spray directly on the body, or near eyes and "
            "skin. *If discolouration is a concern, test a small hidden area first. "
            "*Do not spray directly onto leather.</p>"
        ),
        "image_url": img("INFINITY_06f660ae-8814-4636-9869-98570faefaee.png"),
        "alt": "Spraying INFINITY onto a mesh chair",
    },
    "blocks": {},
    "block_order": [],
}

S["scent_view"] = {
    "type": "sidiz-product-view-vertical",
    "settings": {
        "heading": "Complete your universe with scent",
        "description": (
            "<p>A long-lasting citrus musk: INFINITY cheers on the boundless "
            "possibility that expands past every boundary. It opens on light citrus "
            "notes and leaves a soft, lingering musk. TOP: bergamot, grapefruit, "
            "orange, lemon, spearmint. MIDDLE: rose, jasmine, geranium, ivy. BASE: "
            "muscone, musk. *10 per cent fragrance concentration; lasts around 4-5 "
            "hours, varying with temperature and environment.</p>"
        ),
        "image_url": img("INFINITY.png"),
        "alt": "The INFINITY scent pyramid",
    },
    "blocks": {
        "b1": {"type": "feature", "settings": {
            "title": "A collaboration with Pale Blue Dot",
            "description": "<p>SIDIZ, proposing the journey toward being yourself, meets Pale Blue Dot, recording travel's moments in scent - a fragrance for adventurers who value experience.</p>",
            "image_url": img("Img2_d90e4475-0a63-4d0c-9be4-90a4de6baa46.jpg"),
            "alt": "The SIDIZ and Pale Blue Dot collaboration"}},
        "b2": {"type": "feature", "settings": {
            "title": "The scent of The Progressive stores",
            "description": "<p>The perfumer's craft and the comfort of chairs, distilled: the mood of SIDIZ's The Progressive stores in Korea, captured as a scent.</p>",
            "image_url": img("Img3_4a445753-bb31-4245-bdc7-ba29bf2b151b.jpg"),
            "alt": "The scent in a Progressive store"}},
    },
    "block_order": ["b1", "b2"],
}

S["packaging_view"] = {
    "type": "sidiz-product-view",
    "settings": {
        "heading": "100 per cent recyclable packaging",
        "description": (
            "<p>Peel the label and the bottle recycles completely - top-grade clear "
            "PET, in a box of certified eco-friendly paper. So the everyday leads on "
            "to the sustainable, SIDIZ keeps the circle turning. *The pump is a "
            "composite material and goes in general waste.</p>"
        ),
        "image_url": img("Img5.jpg"),
        "alt": "The INFINITY bottle and its packaging",
    },
    "blocks": {
        "b1": {"type": "feature", "settings": {
            "title": "A fully removable label",
            "description": "<p>Reuse the bottle any time, and recycle it without fuss.</p>",
            "image_url": img("Img6.jpg"),
            "alt": "Peeling the removable label"}},
        "b2": {"type": "feature", "settings": {
            "title": "Top-grade recyclable PET",
            "description": "<p>No needless finishing to hinder recycling - clear, high-purity material for the best recovery.</p>",
            "image_url": img("Img7.jpg"),
            "alt": "The clear PET bottle"}},
        "b3": {"type": "feature", "settings": {
            "title": "Certified eco-friendly paper",
            "description": "<p>FSC-certified, chlorine-free, acid-free paper from sustainably managed forests.</p>",
            "image_url": img("Img8_6a89a295-db5e-43a0-a6fa-02649f78c39e.jpg"),
            "alt": "The eco-friendly paper box"}},
    },
    "block_order": ["b1", "b2", "b3"],
}

S["faq"] = {
    "type": "sidiz-faq",
    "blocks": {
        "q1": {"type": "faq", "settings": {
            "question": "How do I keep a mesh or fabric chair smelling fresh?",
            "answer": "<p>Spray INFINITY lightly two or three times on the backrest, seat or wherever you would like the scent - it deodorises and keeps mesh and fabric fresh for a long while, and works on bedding and curtains too.</p>"}},
        "q2": {"type": "faq", "settings": {
            "question": "What does it smell like, and how long does it last?",
            "answer": "<p>A premium fragrance blended with Pale Blue Dot at 10 per cent concentration, lasting around 4-5 hours. It opens on light citrus - bergamot and orange - and settles into a calm, steady musk, well suited to home offices and other spaces built for focus.</p>"}},
        "q3": {"type": "faq", "settings": {
            "question": "How do I recycle the empty bottle?",
            "answer": "<p>Peel off the fully removable label and recycle the bottle as clear PET. The spray pump is a composite material and goes in general waste. The box is FSC-certified eco-friendly paper. Do not spray directly onto leather.</p>"}},
    },
    "block_order": ["q1", "q2", "q3"],
    "settings": {"heading": "Frequently asked questions", "open_first": True, "background": "#f5f6f7"},
}

S.update(tail("spray"))

order = [
    "pdp_head", "hero", "intro", "usage_view", "scent_view",
    "packaging_view", "faq", "reviews", "recommend", "notices",
]
assert set(order) == set(S), set(order) ^ set(S)
out = ROOT / "theme/templates/product.multispray-infinity.json"
out.write_text(json.dumps({"sections": S, "order": order}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print("written", out.name, "sections:", len(order))
