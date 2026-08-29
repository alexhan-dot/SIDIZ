"""Compose product.muuve.json.

MUUVE is a light-work chair page built from lifestyle tile grids and two
light image-backed scroll sections, plus DIY-assembly and part-replacement
views. The KR related-article (S-Culture blog link) section is skipped - no
AU article exists yet. The AI-generated office visuals keep their disclaimer.
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

AI_NOTE = " *AI-generated visual; details may differ from the actual product."

S = {}

S["sticky_nav"] = copy.deepcopy(B["sticky_nav"])
S["sticky_nav"]["blocks"] = {
    "n1": {"type": "link", "settings": {"label": "At home", "anchor": "at-home"}},
    "n2": {"type": "link", "settings": {"label": "At work", "anchor": "at-work"}},
    "n3": {"type": "link", "settings": {"label": "Design", "anchor": "design"}},
    "n4": {"type": "link", "settings": {"label": "Replaceable parts", "anchor": "parts"}},
    "n5": {"type": "link", "settings": {"label": "Assembly", "anchor": "assembly"}},
    "n6": {"type": "link", "settings": {"label": "Specifications", "anchor": "specifications"}},
    "n7": {"type": "link", "settings": {"label": "FAQ", "anchor": "faq"}},
}
S["sticky_nav"]["block_order"] = ["n1", "n2", "n3", "n4", "n5", "n6", "n7"]

S["pdp_head"] = copy.deepcopy(B["pdp_head"])
S["pdp_head"]["blocks"]["i1"]["settings"]["value"] = "SIDIZ MUUVE Light Work Chair"
S["pdp_head"]["blocks"]["i3"]["settings"]["value"] = "Fabric, moulded foam, plastic, steel"
S["pdp_head"]["blocks"]["i4"]["settings"]["value"] = "Dusty Grey\nMid Grey"
S["pdp_head"]["blocks"]["f3"] = {"type": "fact", "settings": {
    "label": "Assembly",
    "value": "Simple DIY assembly - about 15 minutes"}}
if "f3" not in S["pdp_head"]["block_order"]:
    S["pdp_head"]["block_order"] = ["f1", "f2", "f3", "i1", "i2", "i3", "i4", "i5"]
S["pdp_head"]["settings"]["subtitle"] = (
    "A minimal light-work chair that maximises focus without disturbing the room - "
    "for home offices, studies and every light-work moment in between."
)

S["hero"] = {
    "type": "sidiz-pdp-hero",
    "settings": {
        "subtitle": "Move Light, Think Free",
        "subtitle_colour": "#ffffff",
        "heading": "MUUVE",
        "heading_colour": "#ffffff",
        "text_align": "center",
        "header_scheme": "dark",
        "image_url": img("Head_24a9ec81-d8c3-470e-9d2c-b9dc238e6413.jpg"),
        "image_url_mobile": img("MUUVE_m1.jpg"),
        "alt": "SIDIZ MUUVE light work chair in a calm interior",
        "description": (
            "<p>The SIDIZ MUUVE is a light work chair of minimal design that maximises "
            "working focus without disturbing the interior.</p><p>Recommended for home "
            "offices, studies, multi-rooms and living spaces where the room matters as "
            "much as the work.</p>"
        ),
        "description_colour": "#000000",
        "description_align": "left",
        "product_type": "default",
    },
}

S["how_banner"] = {
    "type": "sidiz-content-row",
    "settings": {
        "width": "wide", "media_side": "above", "text_align": "center",
        "heading": "So how do you use a MUUVE?",
        "background": "#ffffff", "text_colour": "#000000", "padding_block": 72,
    },
}

S["home_row"] = {
    "type": "sidiz-content-row",
    "settings": {
        "width": "wide", "media_side": "above", "text_align": "left",
        "anchor_id": "at-home",
        "heading": "Light-work moments with the MUUVE, from home office to living-room study",
        "background": "#ffffff", "text_colour": "#000000", "padding_block": 40,
    },
}

S["home_tiles"] = {
    "type": "sidiz-tile-card-list",
    "blocks": {
        "t1": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "A minimal home-office chair that respects the room",
            "description": "<p>A chair that settles naturally into a carefully styled study or home office. The minimal design and compact silhouette never weigh a space down, keeping even a small room feeling clean.</p>",
            "image_url": img("Img_1_1_6b9dded8-667e-48c8-ad61-990f1561602b.jpg"),
            "alt": "The MUUVE in a styled home office"}},
        "t2": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "A living-room chair with a light footprint",
            "description": "<p>Easy to place in a corner of the living room, at a small table or beside a desk - less floor taken, more harmony kept, and a comfortable place to focus even in a tight space.</p>",
            "image_url": img("Img_1_2.jpg"),
            "alt": "The MUUVE beside a small living-room table"}},
        "t3": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "For light hobbies, from sewing to reading",
            "description": "<p>Suited to the moments you want to concentrate at ease - sewing, reading, journalling, laptop work. Simple design with a comfortable sit carries different hobbies in one place.</p>",
            "image_url": img("Img_1_3.jpg"),
            "alt": "The MUUVE at a hobby table"}},
        "t4": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "A living-room study chair the whole family shares",
            "description": "<p>At home in the living-room study where you read and learn with the kids - not one person's desk chair, but comfortable in the spaces the family shares.</p>",
            "image_url": img("Img_1_4.jpg"),
            "alt": "The MUUVE in a family study space"}},
    },
    "block_order": ["t1", "t2", "t3", "t4"],
    "settings": {"heading": ""},
}

S["office_row"] = {
    "type": "sidiz-content-row",
    "settings": {
        "width": "wide", "media_side": "above", "text_align": "left",
        "anchor_id": "at-work",
        "heading": "A workspace chair with broad reach, from reception to meeting room",
        "background": "#ffffff", "text_colour": "#000000", "padding_block": 40,
    },
}

S["office_tiles"] = {
    "type": "sidiz-tile-card-list",
    "blocks": {
        "t1": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "For receptions where first impressions count",
            "description": f"<p>Well suited to clinics, showrooms and other reception spaces - a clean impression and a comfortable sit complete a composed atmosphere.{AI_NOTE}</p>",
            "image_url": img("AI_MUUVE_01.png"),
            "alt": "MUUVE chairs in a reception space"}},
        "t2": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "Adding ease to consulting spaces",
            "description": f"<p>Blends naturally into consulting and service rooms, creating a relaxed environment for conversation.{AI_NOTE}</p>",
            "image_url": img("AI_MUUVE___02.png"),
            "alt": "MUUVE chairs in a consulting room"}},
        "t3": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "Flexible seating for open spaces",
            "description": f"<p>Applies naturally to shared work areas and collaboration zones where the use of a space keeps changing.{AI_NOTE}</p>",
            "image_url": img("AI_MUUVE_04.png"),
            "alt": "MUUVE chairs in an open collaboration space"}},
        "t4": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "A neat impression for meeting rooms",
            "description": f"<p>Sits cleanly in meeting rooms, supporting the many working sessions that call for focus.{AI_NOTE}</p>",
            "image_url": img("AI_MUUVE_10.png"),
            "alt": "MUUVE chairs around a meeting table"}},
    },
    "block_order": ["t1", "t2", "t3", "t4"],
    "settings": {"heading": ""},
}

S["homeoffice_banner"] = {
    "type": "sidiz-wb-scroll-banner",
    "settings": {
        "heading": "",
        "header_scheme": "light",
        "tag": "",
        "subheading": "The home office you pictured,<br>completed by simple design and usability",
        "description": (
            "<p>A minimal exterior keeps the space light; the functions tucked away keep "
            "the sit comfortable. The finishing touches of light work, held in balance.</p>"
        ),
        "text_colour": "#000000",
        "image_url": img("Img_1_fbe9ef5e-ab34-4138-a72c-05b29b5529a5.jpg"),
        "image_url_mobile": img("MUUVE_m2.jpg"),
        "alt": "The MUUVE completing a home office",
    },
}

S["homeoffice_cards"] = {
    "type": "sidiz-wb-scroll-card-list",
    "blocks": {
        "c1": {"type": "card", "settings": {
            "title": "A backrest that supports the lumbar curve in balance",
            "title_colour": "#000000",
            "description": "<p>It follows your movement and supports without lifting away, for a comfortable, close fit.</p>",
            "description_colour": "#7c8084",
            "video_url": vid("26986ad67dee4f47a56cd7aa5ce01453", "HD-720p-4.5Mbps", "66938350"),
            "poster_url": poster("26986ad67dee4f47a56cd7aa5ce01453"),
            "alt": "The MUUVE backrest flexing with movement"}},
        "c2": {"type": "card", "settings": {
            "title": "A height lever that completes the minimal design",
            "title_colour": "#000000",
            "description": "<p>Adjust the height to your build and space (seat height 445-535 mm), with a lever shaped carefully so it never breaks the simple line.</p>",
            "description_colour": "#7c8084",
            "image_url": img("Img_4_3_9e73e6eb-a7fa-4e7d-8e4f-7eadcd6bb4c1.jpg"),
            "alt": "The MUUVE height-adjustment lever"}},
    },
    "block_order": ["c1", "c2"],
    "settings": {"header_scheme": "light", "background": "#ffffff"},
}

S["dining_view"] = {
    "type": "sidiz-product-view-vertical",
    "settings": {
        "heading": "The chair a more flexible dining space needs",
        "description": (
            "<p>The dining space now hosts everyday light work as well as meals - and "
            "those moments need a chair that completes them comfortably.</p>"
        ),
        "image_url": img("Img_2_45019f01-09d5-4441-884c-c2419039a55a.jpg"),
        "alt": "The MUUVE at a dining table used for light work",
    },
    "blocks": {
        "b1": {"type": "feature", "settings": {
            "title": "A minimal design that soaks into the space",
            "description": "<p>A restrained design and clean silhouette that suit the dining space - and sit well beside the dining chairs you already own.</p>",
            "image_url": img("Img_3_db6e7e56-ced8-4324-bf2a-fb55b6c5639f.jpg"),
            "alt": "The MUUVE beside existing dining chairs"}},
        "b2": {"type": "feature", "settings": {
            "title": "A compact flat base",
            "description": "<p>A flat base with a tidy impression, so the mood of the dining space stays intact.</p>",
            "image_url": img("Img_4_4dabcc41-d3de-4787-bccb-19e379e952cd.jpg"),
            "alt": "The MUUVE's compact flat base"}},
    },
    "block_order": ["b1", "b2"],
}

S["livingstudy_banner"] = {
    "type": "sidiz-wb-scroll-banner",
    "settings": {
        "heading": "",
        "header_scheme": "light",
        "tag": "",
        "subheading": "Comfort for the living-room study<br>the family shares",
        "description": (
            "<p>The living room has become a study where the family thinks and talks "
            "together. The MUUVE makes those light-work moments comfortable.</p>"
        ),
        "text_colour": "#000000",
        "image_url": img("Img_5_f937f509-315e-4126-8d4e-61b77d298149.jpg"),
        "image_url_mobile": img("MUUVE_m3.jpg"),
        "alt": "The MUUVE in a shared living-room study",
    },
}

S["livingstudy_cards"] = {
    "type": "sidiz-wb-scroll-card-list",
    "blocks": {
        "c1": {"type": "card", "settings": {
            "title": "A design that matches any dining chair",
            "title_colour": "#000000",
            "description": "<p>A balanced design that pairs naturally with tables of any mood, and sits without friction beside existing dining chairs.</p>",
            "description_colour": "#7c8084",
            "image_url": img("Img_4_3__2.jpg"),
            "alt": "The MUUVE matched with dining furniture"}},
        "c2": {"type": "card", "settings": {
            "title": "A glide option that keeps the living room quiet",
            "title_colour": "#000000",
            "description": "<p>For open living spaces, a simple glide specification that never draws the eye.</p>",
            "description_colour": "#7c8084",
            "image_url": img("Img_4_3__3.jpg"),
            "alt": "The MUUVE glide base"}},
    },
    "block_order": ["c1", "c2"],
    "settings": {"header_scheme": "light", "background": "#ffffff"},
}

S["repair_view"] = {
    "type": "sidiz-product-view-vertical",
    "settings": {
        "heading": "Replace a part, feel a new chair",
        "description": (
            "<p>A chair chosen after long deliberation should last. The parts that "
            "naturally wear with time are designed to swap out, so the chair keeps "
            "feeling new - easy to replace, made to last.</p>"
        ),
        "image_url": img("Img_6_c7e0dc4e-d059-4518-8238-82a68220a582.jpg"),
        "alt": "The MUUVE with its replaceable parts",
    },
    "blocks": {
        "b1": {"type": "feature", "settings": {
            "title": "A backrest that swaps with one wrench",
            "description": "<p>Slot a wrench into the hidden groove and turn - the backrest comes free and replaces easily. *Parts available through our support team.</p>",
            "video_url": vid("366c8a6cf5e24d769bef6c6f714bf126", "HD-720p-4.5Mbps", "67322851"),
            "poster_url": poster("366c8a6cf5e24d769bef6c6f714bf126"),
            "alt": "Removing the MUUVE backrest with a wrench"}},
        "b2": {"type": "feature", "settings": {
            "title": "A replaceable seat",
            "description": "<p>The seat shows time first; when it wears or stains, replace just the seat and the chair feels new. *Parts available through our support team.</p>",
            "video_url": vid("3b8a88f4ef1f456ea6b0e0a44daa366d", "HD-720p-4.5Mbps", "66939605"),
            "poster_url": poster("3b8a88f4ef1f456ea6b0e0a44daa366d"),
            "alt": "Replacing the MUUVE seat"}},
    },
    "block_order": ["b1", "b2"],
}

S["diy_view"] = {
    "type": "sidiz-product-view-vertical",
    "settings": {
        "heading": "A DIY product you assemble yourself",
        "description": (
            "<p>Before assembling, check every part, then follow the assembly guide on "
            "the top pad.</p>"
        ),
        "image_url": img("Img_7_52e9815a-a3e5-4329-991b-37152edfdee1.jpg"),
        "alt": "The MUUVE parts laid out for assembly",
    },
    "blocks": {
        "b1": {"type": "feature", "settings": {
            "title": "Quick, easy assembly",
            "description": "<p>A simple process that takes about 15 minutes: join the seat and backrest, then fit the base and column.</p>",
            "image_url": img("f809a9ce6c24449bef25486d04f40c8f_12a7e474-841f-47aa-b549-8ec3535c75c7.jpg"),
            "alt": "Assembling the MUUVE"}},
    },
    "block_order": ["b1"],
}

S["warranty"] = copy.deepcopy(B["warranty"])
S["warranty"]["settings"]["heading"] = "MUUVE | 5-year warranty"
S["warranty"]["settings"]["body"] = (
    "<p>So the journey with your MUUVE continues, SIDIZ provides a 5-year warranty to "
    "customers who complete product registration. Once your chair arrives, register it "
    "before you forget, for more comfortable years ahead.</p>"
)

S["specifications"] = copy.deepcopy(B["specifications"])
S["specifications"]["settings"]["heading"] = "MUUVE dimensions"
S["specifications"]["settings"]["figures"] = "Maximum load 125 kg / product weight approximately 9 kg."
S["specifications"]["blocks"] = {
    "d1": {"type": "drawing", "settings": {
        "image_url": img("MUUVE___01.jpg"),
        "alt": "Dimension drawing of the SIDIZ MUUVE with castors, front elevation"}},
    "d2": {"type": "drawing", "settings": {
        "image_url": img("MUUVE___02.jpg"),
        "alt": "Dimension drawing of the SIDIZ MUUVE with castors, side elevation"}},
    "d3": {"type": "drawing", "settings": {
        "image_url": img("MUUVE___01_3b6e6eb7-e118-4112-8630-4d353a7137b7.jpg"),
        "alt": "Dimension drawing of the SIDIZ MUUVE with glides, front elevation"}},
    "d4": {"type": "drawing", "settings": {
        "image_url": img("MUUVE___02_4ce68b62-b0f5-4720-8d21-a4ae9a7c1870.jpg"),
        "alt": "Dimension drawing of the SIDIZ MUUVE with glides, side elevation"}},
}
S["specifications"]["block_order"] = ["d1", "d2", "d3", "d4"]

S["safety_info"] = copy.deepcopy(B["safety_info"])
del S["safety_info"]["blocks"]["n2"]
S["safety_info"]["block_order"] = ["n1"]

S["faq"] = {
    "type": "sidiz-faq",
    "blocks": {
        "q1": {"type": "faq", "settings": {
            "question": "Can I swap between castors and glides?",
            "answer": "<p>Yes - contact our support team to purchase the alternative base parts and swap them yourself. Note that the seat height changes slightly with the swap.</p>"}},
        "q2": {"type": "faq", "settings": {
            "question": "How far does the soft tilting move?",
            "answer": "<p>The soft tilting follows your body through roughly 8 degrees upward and 4 degrees downward. The videos on this page show the movement.</p>"}},
        "q3": {"type": "faq", "settings": {
            "question": "What is the maximum load?",
            "answer": "<p>The MUUVE supports up to 125 kg.</p>"}},
        "q4": {"type": "faq", "settings": {
            "question": "Can the seat and backrest cushions be washed?",
            "answer": "<p>The cushions are not washable, but if they stain or wear with long use, replacements are available through our support team.</p>"}},
    },
    "block_order": ["q1", "q2", "q3", "q4"],
    "settings": {"heading": "Frequently asked questions", "open_first": True, "background": "#f5f6f7"},
}

S["goes_with"] = {
    "type": "sidiz-related-products",
    "settings": {"heading": "Goes well with the MUUVE", "source": "collection", "limit": 4},
}

S["reviews"] = copy.deepcopy(B["reviews"])

S["stockists"] = {
    "type": "sidiz-store-info",
    "settings": {
        "heading": "Sit in one before you decide",
        "description": "Seat feel differs from body to body. Try a MUUVE in person where you can; otherwise our returns policy is there to fall back on.",
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
    "sticky_nav", "pdp_head", "hero", "how_banner",
    "home_row", "home_tiles", "office_row", "office_tiles",
    "homeoffice_banner", "homeoffice_cards", "dining_view",
    "livingstudy_banner", "livingstudy_cards", "repair_view", "diy_view",
    "warranty", "specifications", "safety_info", "faq",
    "goes_with", "reviews", "stockists", "recommend", "notices",
]
assert set(order) == set(S), set(order) ^ set(S)

out = ROOT / "theme/templates/product.muuve.json"
out.write_text(json.dumps({"sections": S, "order": order}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print("written", out.name, "sections:", len(order))
