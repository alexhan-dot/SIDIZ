"""Compose product.molti.json.

MOLTI is the convertible baby chair (floor seat / high chair / desk chair):
image hero, a two-set option compare (leather guidance dropped - no leather
on the MOLTI), the 3-in-1 Hello Baby view, the high-chair-set view, two
image scroll banners (age guide and lifestyle), safety view, two tile lists,
an eight-drawing spec across the four configurations and a three-item FAQ.
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
    "n2": {"type": "link", "settings": {"label": "3-in-1", "anchor": "three-in-one"}},
    "n3": {"type": "link", "settings": {"label": "High chair", "anchor": "high-chair"}},
    "n4": {"type": "link", "settings": {"label": "Safety", "anchor": "safety"}},
    "n5": {"type": "link", "settings": {"label": "Specifications", "anchor": "specifications"}},
    "n6": {"type": "link", "settings": {"label": "FAQ", "anchor": "faq"}},
}
S["sticky_nav"]["block_order"] = ["n1", "n2", "n3", "n4", "n5", "n6"]

S["pdp_head"] = copy.deepcopy(B["pdp_head"])
S["pdp_head"]["blocks"]["i1"]["settings"]["value"] = "SIDIZ MOLTI Convertible Baby Chair"
S["pdp_head"]["blocks"]["i3"]["settings"]["value"] = "Synthetic leather, moulded foam, plastic, wood, steel"
S["pdp_head"]["blocks"]["i4"]["settings"]["value"] = "Soy Milk\nCoral Pink\nAvocado Green"
S["pdp_head"]["settings"]["subtitle"] = (
    "The multi-player baby chair: floor seat, high chair and desk chair in one, "
    "changing with your child from the first sit to the school desk."
)

S["hero"] = {
    "type": "sidiz-pdp-hero",
    "settings": {
        "subtitle": "The multi-player baby chair",
        "subtitle_colour": "#ffffff",
        "heading": "MOLTI",
        "heading_colour": "#ffffff",
        "text_align": "center",
        "header_scheme": "dark",
        "image_url": img("MOLTI_Head_01.jpg"),
        "image_url_mobile": img("MOLTI_Head_01_M-0.jpg"),
        "alt": "The SIDIZ MOLTI in its three configurations",
        "description": (
            "<p>As your child grows, the chair they need keeps changing - which is why "
            "there is MOLTI. A floor seat that cradles the lower back for a first-ever "
            "chair, a high chair that shapes mealtime habits as solids begin, and a desk "
            "chair that holds good posture at the desk.</p><p>One baby chair that changes "
            "along with your child's growth - that is why MOLTI is called the "
            "multi-player.</p>"
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
            "title": "Hello Baby Set",
            "description": "Three chairs in one set",
            "images": img("MOLTI_Option1.jpg") + "," + img("MOLTI_Option1-1.jpg"),
            "colours": "#e8ddc9,#e8a091,#a5b184",
            "alt": "The MOLTI Hello Baby set"}},
        "o2": {"type": "option", "settings": {
            "title": "High Chair Set",
            "description": "Just the essentials for self-feeding",
            "images": img("MOLTI_Option2.jpg") + "," + img("MOLTI_Option2-1.jpg"),
            "colours": "#e8ddc9,#e8a091,#a5b184",
            "alt": "The MOLTI high chair set"}},
    },
    "block_order": ["o1", "o2"],
    "settings": {"heading": "The MOLTI option for your child"},
}

S["play_banner"] = {
    "type": "sidiz-wb-banner",
    "settings": {
        "heading": "Multi-play, freely,<br>matched to growth and the moment",
        "align": "left",
        "title_colour": "#000000",
    },
}

S["hello_view"] = {
    "type": "sidiz-product-view",
    "settings": {
        "tag": "Hello Baby Set",
        "heading": "The 3-in-1 multi-player",
        "description": (
            "<p>For a child growing by the day: a floor seat for babies under six "
            "months, a high chair timed to first solids, and a desk chair that shapes "
            "good posture - all in one set.</p>"
        ),
        "image_url": img("Img_1_9b88d673-2797-480c-8a47-4bc5fd4f4038.jpg"),
        "alt": "The MOLTI Hello Baby set's three configurations",
    },
    "blocks": {
        "b1": {"type": "feature", "settings": {
            "title": "Floor seat",
            "description": "<p>For babies under six months whose lower backs are still gaining strength.</p>",
            "image_url": img("MOLTI_01-1.jpg"),
            "alt": "The MOLTI as a floor seat"}},
        "b2": {"type": "feature", "settings": {
            "title": "High chair",
            "description": "<p>For children starting solids at the table.</p>",
            "image_url": img("MOLTI_01-2.jpg"),
            "alt": "The MOLTI as a high chair"}},
        "b3": {"type": "feature", "settings": {
            "title": "Desk chair",
            "description": "<p>Holding good posture through play and learning.</p>",
            "image_url": img("MOLTI_01-3.jpg"),
            "alt": "The MOLTI as a desk chair"}},
    },
    "block_order": ["b1", "b2", "b3"],
}

S["highchair_view"] = {
    "type": "sidiz-product-view",
    "settings": {
        "tag": "High Chair Set",
        "heading": "A high chair set for the start of self-feeding",
        "description": (
            "<p>Once neck and back strengthen, children start doing things for "
            "themselves. The high chair set carries exactly the functions that stage "
            "needs.</p>"
        ),
        "image_url": img("MOLTI_02_df820c41-8592-44de-bb44-193c73492beb.jpg"),
        "alt": "The MOLTI high chair set at the table",
    },
    "blocks": {
        "b1": {"type": "feature", "settings": {
            "title": "Safety belt and bar",
            "description": "<p>For the safety of children whose movements grow bolder by the week.</p>",
            "image_url": img("MOLTI_02-1.jpg"),
            "alt": "The MOLTI safety belt and bar"}},
        "b2": {"type": "feature", "settings": {
            "title": "One-touch tray",
            "description": "<p>A tray that clips on and off with one touch.</p>",
            "image_url": img("MOLTI_02-2.jpg"),
            "alt": "Removing the MOLTI tray"}},
        "b3": {"type": "feature", "settings": {
            "title": "Kids dining chair",
            "description": "<p>From about age three, remove the accessories and it joins the family table as a dining chair.</p>",
            "image_url": img("MOLTI_02-3.jpg"),
            "alt": "The MOLTI as a kids dining chair"}},
    },
    "block_order": ["b1", "b2", "b3"],
}

S["guide_banner"] = {
    "type": "sidiz-wb-scroll-banner",
    "settings": {
        "heading": "",
        "header_scheme": "light",
        "tag": "",
        "subheading": "The MOLTI guide, month by month",
        "description": "",
        "text_colour": "#000000",
        "image_url": img("molti_0121.jpg"),
        "image_url_mobile": img("molti_0121_mo.jpg"),
        "alt": "The MOLTI configuration guide by age in months",
    },
}

S["lifestyle_banner"] = {
    "type": "sidiz-wb-scroll-banner",
    "settings": {
        "heading": "",
        "header_scheme": "light",
        "tag": "",
        "subheading": "For the child who sits,<br>and the person raising them",
        "description": "",
        "text_colour": "#000000",
        "image_url": img("MOLTI_Img.jpg"),
        "image_url_mobile": img("MOLTI_Img_2.jpg"),
        "alt": "The MOLTI in family life",
    },
}

S["safety_view"] = {
    "type": "sidiz-product-view-vertical",
    "settings": {
        "heading": "Designed around children's safety",
        "description": "",
        "image_url": img("MOLTI_03-0.jpg"),
        "alt": "The MOLTI's safety design",
    },
    "blocks": {
        "b1": {"type": "feature", "settings": {
            "title": "A steady body design",
            "description": "<p>The body rises around the back and both sides, wrapping the child in a settled, secure hold.</p>",
            "image_url": img("MOLTI_03-1.jpg"),
            "alt": "The MOLTI's wrapping body shape"}},
        "b2": {"type": "feature", "settings": {
            "title": "Plush back and seat cushions",
            "description": "<p>Thick, high-resilience sponge wraps hips and back in softness.</p>",
            "image_url": img("MOLTI_03-2.jpg"),
            "alt": "The MOLTI's cushioning"}},
        "b3": {"type": "feature", "settings": {
            "title": "A safety bar and belt, both",
            "description": "<p>Bar and belt together raise the level of safety further still.</p>",
            "image_url": img("MOLTI_03-3.jpg"),
            "alt": "The MOLTI's safety bar and belt"}},
    },
    "block_order": ["b1", "b2", "b3"],
}

S["adjust_tiles"] = {
    "type": "sidiz-tile-card-list",
    "blocks": {
        "t1": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "Four-step back and seat adjustment",
            "description": "<p>Levers on the backrest and seat set backrest height, seat height and seat depth.</p>",
            "image_url": img("MOLTI_1_1__01.jpg"),
            "alt": "Adjusting the MOLTI back and seat"}},
        "t2": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "Five-step footrest",
            "description": "<p>Always steady, matched to the length of your child's legs.</p>",
            "image_url": img("MOLTI_1_1__02.jpg"),
            "alt": "The MOLTI's five-step footrest"}},
        "t3": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "A one-touch, splash-proof tray",
            "description": "<p>The tray that comes on and off most often does it fastest - one touch.</p>",
            "image_url": img("MOLTI_1_1__03.jpg"),
            "alt": "The one-touch MOLTI tray"}},
        "t4": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "Simple inner-seat fitting",
            "description": "<p>The inner seat fits and removes through the backrest lever - no tools.</p>",
            "image_url": img("MOLTI_1_1__04.jpg"),
            "alt": "Fitting the MOLTI inner seat"}},
    },
    "block_order": ["t1", "t2", "t3", "t4"],
    "settings": {"heading": "Simple controls, no tools required"},
}

S["care_tiles"] = {
    "type": "sidiz-tile-card-list",
    "blocks": {
        "t1": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "Stain-resistant synthetic leather",
            "description": "<p>Spilt liquids and food wipe straight off, keeping mealtimes hygienic.</p>",
            "image_url": img("MOLTI_1_1__05.jpg"),
            "alt": "Wiping the MOLTI clean"}},
        "t2": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "A back and seat that separate for cleaning",
            "description": "<p>Both remove completely without tools, so cleaning reaches everywhere.</p>",
            "image_url": img("MOLTI_1_1__06.jpg"),
            "alt": "Separating the MOLTI back and seat"}},
    },
    "block_order": ["t1", "t2"],
    "settings": {"heading": "Materials and design that make upkeep easy"},
}

S["goes_with"] = {
    "type": "sidiz-related-products",
    "settings": {"heading": "Goes well with the MOLTI", "source": "collection", "limit": 4},
}

S["warranty"] = copy.deepcopy(B["warranty"])
S["warranty"]["settings"]["heading"] = "MOLTI | 5-year warranty"
S["warranty"]["settings"]["body"] = (
    "<p>So the journey with your MOLTI continues, SIDIZ provides a 5-year warranty to "
    "customers who complete product registration. Once your chair arrives, register it "
    "before you forget, for more comfortable years ahead.</p>"
)

S["specifications"] = copy.deepcopy(B["specifications"])
S["specifications"]["settings"]["heading"] = "MOLTI dimensions"
S["specifications"]["settings"]["figures"] = (
    "Maximum load 40 kg. Product weight approximately 6.3 kg (floor seat), 7.9 kg "
    "(high chair), 8.5 kg (high chair with inner seat) or 6.3 kg (desk chair)."
)
S["specifications"]["blocks"] = {
    "d1": {"type": "drawing", "settings": {
        "image_url": img("SK500NA_01_f4759bcb-7371-4b5e-842d-6e997bb46c1f.jpg"),
        "alt": "Dimension drawing of the MOLTI floor seat, front elevation"}},
    "d2": {"type": "drawing", "settings": {
        "image_url": img("SK500NA_02_e3ea00e0-05e4-45aa-967c-c33c8295a5d1.jpg"),
        "alt": "Dimension drawing of the MOLTI floor seat, side elevation"}},
    "d3": {"type": "drawing", "settings": {
        "image_url": img("SK500NA_05_f55ab27c-cdff-4f24-8dee-8290b455dc64.jpg"),
        "alt": "Dimension drawing of the MOLTI high chair, front elevation"}},
    "d4": {"type": "drawing", "settings": {
        "image_url": img("SK500NA_06_dcc2e7c8-1738-4643-8c26-11972e40714f.jpg"),
        "alt": "Dimension drawing of the MOLTI high chair, side elevation"}},
    "d5": {"type": "drawing", "settings": {
        "image_url": img("SK500NA_03_36e91585-27c2-4b97-be27-e066336abd21.jpg"),
        "alt": "Dimension drawing of the MOLTI high chair with inner seat, front elevation"}},
    "d6": {"type": "drawing", "settings": {
        "image_url": img("SK500NA_04_64f7a699-a32d-4c49-9fec-dc328d2ef3d6.jpg"),
        "alt": "Dimension drawing of the MOLTI high chair with inner seat, side elevation"}},
    "d7": {"type": "drawing", "settings": {
        "image_url": img("SK500NA_07_4ea3aa02-c7f4-4b1a-81d7-0cb1377c1201.jpg"),
        "alt": "Dimension drawing of the MOLTI desk chair, front elevation"}},
    "d8": {"type": "drawing", "settings": {
        "image_url": img("SK500NA_08_248f2009-7524-43bf-bd18-9f8dfad256dc.jpg"),
        "alt": "Dimension drawing of the MOLTI desk chair, side elevation"}},
}
S["specifications"]["block_order"] = ["d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8"]

S["safety_info"] = {
    "type": "sidiz-safety-info",
    "blocks": {
        "n1": {"type": "note", "settings": {
            "title": "Tray on the desk chair: tipping risk",
            "body": "<p>With the desk-chair legs fitted, using the tray is not recommended - the combination risks tipping. Leave the tray and safety bar off in that configuration.</p>"}},
        "n2": {"type": "note", "settings": {
            "title": "Always fit a base before use",
            "body": "<p>For safe use the body must always be fitted with one of the bases: glides, the long legs or the desk-chair legs.</p>"}},
        "n3": {"type": "note", "settings": {
            "title": "Removing stains from the frame",
            "body": "<p>If the frame gets marked during assembly or use, a melamine sponge lifts stains easily. *Rubbing hard can damage the surface.</p>",
            "image_url": img("BLOCK-EGA-NOTICE.jpg"),
            "alt": "Cleaning the MOLTI frame"}},
    },
    "block_order": ["n1", "n2", "n3"],
    "settings": {"heading": "Care and cautions"},
}

S["faq"] = {
    "type": "sidiz-faq",
    "blocks": {
        "q1": {"type": "faq", "settings": {
            "question": "What is the difference between the Hello Baby set and the High Chair set?",
            "answer": "<p>The Hello Baby set includes everything for all three configurations - floor seat, high chair and desk chair. The High Chair set omits the glides, inner seat and desk-chair legs (the inner seat and desk-chair legs are sold separately).</p>"}},
        "q2": {"type": "faq", "settings": {
            "question": "Until when is the inner seat used?",
            "answer": "<p>The inner seat steadies babies from the time they hold their heads up while their lower backs are still weak - usually to around 12 months, though it varies with each child's development.</p>"}},
        "q3": {"type": "faq", "settings": {
            "question": "The legs look mottled - is that a fault?",
            "answer": "<p>No - the grain pattern on the legs is a natural characteristic of the timber and is not grounds for exchange or return.</p>"}},
    },
    "block_order": ["q1", "q2", "q3"],
    "settings": {"heading": "Frequently asked questions", "open_first": True, "background": "#f5f6f7"},
}

S["reviews"] = copy.deepcopy(B["reviews"])

S["stockists"] = {
    "type": "sidiz-store-info",
    "settings": {
        "heading": "Sit in one before you decide",
        "description": "Seat feel differs from child to child. Try a MOLTI in person where you can; otherwise our returns policy is there to fall back on.",
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
    "sticky_nav", "pdp_head", "hero", "options", "play_banner",
    "hello_view", "highchair_view", "guide_banner", "lifestyle_banner",
    "safety_view", "adjust_tiles", "care_tiles",
    "goes_with", "warranty", "specifications", "safety_info", "faq",
    "reviews", "stockists", "recommend", "notices",
]
assert set(order) == set(S), set(order) ^ set(S)

out = ROOT / "theme/templates/product.molti.json"
out.write_text(json.dumps({"sections": S, "order": order}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print("written", out.name, "sections:", len(order))
