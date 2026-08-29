"""Compose product.t20.json.

T20's KR page is its own shape (intro row BEFORE the hero, two scroll-banner +
card-list pairs, a home-to-office media banner, a business-enquiry link row and
a gen1-vs-gen2 tile comparison), so this builds the template fresh, borrowing
only the family-standard tail sections from product.t50-2.json.
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

S = {}

S["sticky_nav"] = copy.deepcopy(B["sticky_nav"])
S["sticky_nav"]["blocks"] = {
    "n1": {"type": "link", "settings": {"label": "Overview", "anchor": "about"}},
    "n2": {"type": "link", "settings": {"label": "Comfort", "anchor": "comfort"}},
    "n3": {"type": "link", "settings": {"label": "For business", "anchor": "business"}},
    "n4": {"type": "link", "settings": {"label": "Compare", "anchor": "compare"}},
    "n5": {"type": "link", "settings": {"label": "Adjustment", "anchor": "adjustment-guide"}},
    "n6": {"type": "link", "settings": {"label": "Specifications", "anchor": "specifications"}},
    "n7": {"type": "link", "settings": {"label": "FAQ", "anchor": "faq"}},
}
S["sticky_nav"]["block_order"] = ["n1", "n2", "n3", "n4", "n5", "n6", "n7"]

S["pdp_head"] = copy.deepcopy(B["pdp_head"])
S["pdp_head"]["blocks"]["i1"]["settings"]["value"] = "SIDIZ T20 Ergonomic Office Chair"
S["pdp_head"]["blocks"]["i3"]["settings"]["value"] = "Fabric, moulded foam, plastic, steel"
S["pdp_head"]["blocks"]["i4"]["settings"]["value"] = "Off White\nMid Grey\nSmoke Black"
del S["pdp_head"]["blocks"]["f3"]
S["pdp_head"]["block_order"] = ["f1", "f2", "i1", "i2", "i3", "i4", "i5"]
S["pdp_head"]["settings"]["subtitle"] = (
    "The supernormal chair: expert presets, a 4-step backrest lock and a Cloud Foam seat - "
    "ergonomic comfort without complicated adjustment."
)

S["intro"] = {
    "type": "sidiz-product-row",
    "settings": {
        "heading": "SIDIZ T20 Ergonomic Office Computer Chair",
        "body": (
            "<ul><li><strong>Supernormal design</strong> - expert presets create an ergonomic "
            "sitting position immediately, with no fiddly setup.</li>"
            "<li><strong>4-step backrest lock</strong> - fix the recline within 105-125 degrees, "
            "from focused work through to rest.</li>"
            "<li><strong>Cloud Foam seat + ergonomic headrest</strong> - scooping minimises "
            "thigh pressure, and the headrest supports the nape at any contact point.</li>"
            "<li><strong>Easy Repair + 5-year warranty</strong> - part-level replacement and a "
            "long warranty for lasting value.</li>"
            "<li><strong>A work chair for home and business alike</strong> - one entry-level "
            "ergonomic chair covering home office, study and workplace.</li></ul>"
        ),
        "align": "left",
        "background": "#ffffff",
        "text_colour": "#000000",
    },
}

S["hero"] = {
    "type": "sidiz-pdp-hero",
    "settings": {
        "subtitle": "<em class=\"caps\">Less is more</em><br>The supernormal chair, focused on the essentials",
        "subtitle_colour": "#ffffff",
        "heading": "T20",
        "heading_colour": "#ffffff",
        "text_align": "center",
        "header_scheme": "dark",
        "video_url": vid("ca6af8d9ca7e402f8b66cc2b0be24feb", "HD-1080p-7.2Mbps", "41014010"),
        "poster_url": poster("ca6af8d9ca7e402f8b66cc2b0be24feb"),
        "video_url_mobile": vid("0eac5fb3a248488f8e879f7be0c8b883", "HD-1080p-7.2Mbps", "41014009"),
        "poster_url_mobile": poster("0eac5fb3a248488f8e879f7be0c8b883"),
        "alt": "SIDIZ T20 supernormal ergonomic office chair in motion",
        "description": (
            "<p>The SIDIZ T20 is a supernormal ergonomic office chair focused on the "
            "essentials. A 4-step backrest lock, Cloud Foam seat and ergonomic headrest "
            "deliver comfort without complicated adjustment.</p><p>A steady sit for home "
            "offices, study and workplaces - and the right first ergonomic chair.</p>"
        ),
        "description_colour": "#000000",
        "description_align": "left",
        "product_type": "default",
    },
}

S["about"] = {
    "type": "sidiz-content-row",
    "settings": {
        "width": "wide",
        "media_side": "above",
        "text_align": "left",
        "anchor_id": "about",
        "heading": "What is the SIDIZ T20?",
        "body": (
            "<p>A minimal design that suits any space, carrying only the functions that "
            "matter, on an ergonomic foundation. The backrest lock sets the chair to the "
            "moment, and from secondary students to first-time SIDIZ buyers it is an easy "
            "office chair to choose.</p>"
        ),
        "background": "#ffffff",
        "text_colour": "#000000",
        "padding_block": 80,
    },
}

S["supernormal_banner"] = {
    "type": "sidiz-wb-scroll-banner",
    "settings": {
        "heading": "",
        "header_scheme": "light",
        "tag": "The supernormal chair, focused on the essentials",
        "tag_colour": "#000000",
        "tag_background": "#eaedf0",
        "subheading": "A practical work chair<br>with only the functions you need",
        "description": (
            "<p>The T20 carries minimal adjustment. A few simple controls make it feel "
            "fitted to you, from moments of deep focus to moments of rest.</p>"
        ),
        "text_colour": "#757575",
        "video_url": vid("191efc71976f437a98810e4285cc4c15", "HD-1080p-7.2Mbps", "41014072"),
        "poster_url": poster("191efc71976f437a98810e4285cc4c15"),
        "video_url_mobile": vid("adb1d34a3924461795364ccc48ee6161", "HD-1080p-7.2Mbps", "41014066"),
        "poster_url_mobile": poster("adb1d34a3924461795364ccc48ee6161"),
        "alt": "The SIDIZ T20 in a calm workspace",
    },
}

S["fit_cards"] = {
    "type": "sidiz-wb-card-list",
    "blocks": {
        "c1": {"type": "card", "settings": {
            "title": "Chair and headrest height that adjust to your build",
            "title_colour": "#000000",
            "description_colour": "#7c8084",
            "video_url": vid("8095649bdcd648b1928a3982e74a93d4", "SD-480p-0.9Mbps", "41014067"),
            "poster_url": poster("8095649bdcd648b1928a3982e74a93d4"),
            "alt": "Adjusting the T20 chair and headrest height"}},
        "c2": {"type": "card", "settings": {
            "title": "Easy tilting tension",
            "title_colour": "#000000",
            "description": "<p>Four steps of tilting tension, set to your build and taste.</p>",
            "description_colour": "#7c8084",
            "image_url": img("T20_01-2_09c24698-26b6-4df5-ba37-70081df5cf3f.jpg"),
            "alt": "The T20 tilting tension control"}},
        "c3": {"type": "card", "settings": {
            "title": "Focus to rest: 4-step backrest lock",
            "title_colour": "#000000",
            "description": "<p>Fix the backrest at the angle you want, for steady immersion or an easy rest.</p>",
            "description_colour": "#7c8084",
            "image_url": img("T20_01-3.jpg"),
            "alt": "The T20 backrest locked at an angle"}},
    },
    "block_order": ["c1", "c2", "c3"],
    "settings": {"heading": "The essentials of a chair that fits"},
}

S["comfort_banner"] = {
    "type": "sidiz-wb-scroll-banner",
    "settings": {
        "heading": "Design built for optimal comfort",
        "heading_colour": "#000000",
        "header_scheme": "dark",
        "tag": "The supernormal chair, focused on the essentials",
        "tag_colour": "#000000",
        "tag_background": "#eaedf0",
        "subheading": "Comfort designed<br>into every contact point",
        "description": (
            "<p>Ever removed a headrest that never sat right, or had a long seat press "
            "behind your knees? The T20's expert-designed preset delivers comfort you feel "
            "without touching a thing.</p>"
        ),
        "text_colour": "#ffffff",
        "video_url": vid("fd2a7f5a6ffc4786abfbe1d9a0fa3624", "HD-1080p-3.3Mbps", "40956439"),
        "poster_url": poster("fd2a7f5a6ffc4786abfbe1d9a0fa3624"),
        "video_url_mobile": vid("b7906d553fd543bd85374b7b6c83fc5f", "HD-1080p-4.8Mbps", "40956440"),
        "poster_url_mobile": poster("b7906d553fd543bd85374b7b6c83fc5f"),
        "alt": "The T20's preset comfort in use",
    },
}

S["comfort_cards"] = {
    "type": "sidiz-wb-card-list",
    "blocks": {
        "c1": {"type": "card", "settings": {
            "title": "A headrest comfortable at any point",
            "title_colour": "#000000",
            "description": "<p>An ergonomic shape that supports wherever the back of your head or neck lands.</p>",
            "description_colour": "#7c8084",
            "video_url": vid("b1263fd05f114e24b4adda9ac9b11642", "SD-480p-1.5Mbps", "40616915"),
            "poster_url": poster("b1263fd05f114e24b4adda9ac9b11642"),
            "alt": "The T20 headrest supporting different positions"}},
        "c2": {"type": "card", "settings": {
            "title": "Cloud Foam, a step more comfortable",
            "title_colour": "#000000",
            "description": "<p>SIDIZ scooping maximises compression, considered right down to where the seat meets the back of your legs.</p>",
            "description_colour": "#7c8084",
            "video_url": vid("0c7eafe7c30f400288356224357d4f52", "SD-480p-1.5Mbps", "40616916"),
            "poster_url": poster("0c7eafe7c30f400288356224357d4f52"),
            "alt": "The Cloud Foam seat compressing"}},
        "c3": {"type": "card", "settings": {
            "title": "A steady armrest pad",
            "title_colour": "#000000",
            "description": "<p>A generous area and firm material that supports the arms reliably.</p>",
            "description_colour": "#7c8084",
            "video_url": vid("2f95f20b864b4eef928f3beb6e3eb76a", "SD-480p-1.5Mbps", "40616917"),
            "poster_url": poster("2f95f20b864b4eef928f3beb6e3eb76a"),
            "alt": "The T20 armrest pad"}},
    },
    "block_order": ["c1", "c2", "c3"],
    "settings": {"heading": ""},
}

S["office_banner"] = {
    "type": "sidiz-wb-banner",
    "settings": {
        "header_scheme": "dark",
        "tag": "Optimised for the workplace as much as the home",
        "tag_colour": "#000000",
        "tag_background": "#eaedf0",
        "heading": "From home to office<br>the same standard of comfort",
        "title_colour": "#ffffff",
        "description": (
            "<p>Worried about after-sales care once you buy? The T20 eases what comes "
            "after, with part-level Easy Repair and a 5-year warranty.</p>"
        ),
        "description_colour": "#ffffff",
        "align": "left",
        "image_url": img("T20_05-1_a894de61-3900-41a6-9b82-5bcdb7338355.jpg"),
        "image_url_mobile": img("Head_M_b93afb2d-da1a-4cdc-b850-b7e03df12f84.jpg"),
        "alt": "The SIDIZ T20 in an office environment",
    },
}

S["office_cards"] = {
    "type": "sidiz-wb-card-list",
    "blocks": {
        "c1": {"type": "card", "settings": {
            "title": "9 to 6, comfort that lasts all day",
            "title_colour": "#000000",
            "description": "<p>Quiet, smooth castors and ergonomic design tuned for working focus.</p>",
            "description_colour": "#7c8084",
            "image_url": img("T20_05-2.jpg"),
            "alt": "T20 chairs in a working office"}},
        "c2": {"type": "card", "settings": {
            "title": "A smart choice for operations too",
            "title_colour": "#000000",
            "description": "<p>Easy Repair part replacement and the 5-year warranty keep upkeep simple.</p>",
            "description_colour": "#7c8084",
            "image_url": img("T20_05-3.jpg"),
            "alt": "Easy Repair parts for the T20"}},
        "c3": {"type": "card", "settings": {
            "title": "Volume orders for teams",
            "title_colour": "#000000",
            "description": "<p>Fitting out an office? Talk to us about volume pricing.</p>",
            "description_colour": "#7c8084",
            "image_url": img("T20_05-4.jpg"),
            "alt": "Rows of T20 chairs in a fitted-out office"}},
    },
    "block_order": ["c1", "c2", "c3"],
    "settings": {"heading": ""},
}

S["business_link"] = {
    "type": "sidiz-content-row",
    "settings": {
        "width": "wide",
        "media_side": "above",
        "text_align": "center",
        "anchor_id": "business",
        "heading": "Business customer enquiries",
        "cta_label": "Contact us",
        "cta_link": "/pages/contact",
        "background": "#ffffff",
        "text_colour": "#000000",
        "padding_block": 56,
    },
}

S["compare_tiles"] = {
    "type": "sidiz-tile-card-list",
    "blocks": {
        "t1": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "From straight lines to a minimal, softened form",
            "description": "<p>Generation 1: clean lines and a sharp silhouette. Generation 2: a rounded, minimal language across every part.</p>",
            "image_url": img("Img_1_1_bb1c4656-82a9-4c40-8ade-1e4e96a2e489.jpg"),
            "alt": "The T20 generation 1 and 2 side by side"}},
        "t2": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "Light Sync Tilt, easier to adjust",
            "description": "<p>Generation 1's tension lever sat centre-under the seat; generation 2 adjusts without bending down, with nothing protruding.</p>",
            "image_url": img("Img_1_1__2.jpg"),
            "alt": "The generation 2 tilt adjustment"}},
        "t3": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "A headrest that is easier to live with",
            "description": "<p>Generation 1 locked with a lever; generation 2 is comfortable at any contact point and adjusts from where you sit.</p>",
            "image_url": img("Img_1_1__3.jpg"),
            "alt": "The generation 2 headrest"}},
        "t4": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "A seat for longer, easier sitting",
            "description": "<p>Generation 1: compact and firm. Generation 2: roomier, more comfortable, and Easy Repair-replaceable.</p>",
            "image_url": img("Img_1_1__4.jpg"),
            "alt": "The generation 2 seat"}},
    },
    "block_order": ["t1", "t2", "t3", "t4"],
    "settings": {"heading": "T20, generation 1 and 2 compared"},
}

S["find_your_fit"] = {
    "type": "sidiz-find-your-fit",
    "blocks": {
        "s1": {"type": "adjustment", "settings": {
            "title": "Chair height",
            "description": "<p>Set to your body frame.</p>",
            "image_url": img("FYF_01.jpg"),
            "alt": "Adjusting the T20 chair height"}},
        "s2": {"type": "adjustment", "settings": {
            "title": "Headrest height / angle",
            "description": "<p>Ease the load on your head and neck.</p>",
            "image_url": img("FYF_02.jpg"),
            "alt": "Adjusting the T20 headrest"}},
        "s3": {"type": "adjustment", "settings": {
            "title": "Tilting tension / backrest lock",
            "description": "<p>Choose how the backrest moves and holds.</p>",
            "image_url": img("FYF_03.jpg"),
            "alt": "Adjusting the T20 tilt and backrest lock"}},
    },
    "block_order": ["s1", "s2", "s3"],
    "settings": {
        "heading": "T20 adjustment guide",
        "subtitle": "FIND YOUR FIT. Set it up for your body",
        "guide_label": "USER GUIDE",
        "guide_link": "/pages/user-guide",
    },
}

S["goes_with"] = {
    "type": "sidiz-related-products",
    "settings": {"heading": "Goes well with the T20", "source": "collection", "limit": 4},
}

S["easy_repair"] = copy.deepcopy(B["easy_repair"])
S["easy_repair"]["settings"]["heading"] = "T20 | EASY REPAIR"
S["easy_repair"]["settings"]["subtitle"] = "Repair it, keep it longer"
S["easy_repair"]["settings"]["description"] = (
    "<p>Even after long use, buy just the part you need and swap it in to keep the chair "
    "like new.</p>"
)

S["warranty"] = copy.deepcopy(B["warranty"])
S["warranty"]["settings"]["heading"] = "T20 | 5-year warranty"
S["warranty"]["settings"]["body"] = (
    "<p>So the journey with your T20 continues, SIDIZ provides a 5-year warranty to "
    "customers who complete product registration. Once your chair arrives, register it "
    "before you forget, for more comfortable years ahead.</p>"
)

S["specifications"] = copy.deepcopy(B["specifications"])
S["specifications"]["settings"]["heading"] = "T20 dimensions"
S["specifications"]["settings"]["figures"] = "Maximum load 125 kg / product weight approximately 15.5 kg."
S["specifications"]["blocks"]["d1"]["settings"].update({
    "image_url": img("T20-2_01_6b011859-3f21-4896-a267-ea8ea1e36b8c.jpg"),
    "alt": "Dimension drawing of the SIDIZ T20, front elevation"})
S["specifications"]["blocks"]["d2"]["settings"].update({
    "image_url": img("T20-2_02_58937322-e61d-497b-9d5e-c1fdbc4f69d9.jpg"),
    "alt": "Dimension drawing of the SIDIZ T20, side elevation"})

S["safety_info"] = copy.deepcopy(B["safety_info"])

S["faq"] = {
    "type": "sidiz-faq",
    "blocks": {
        "q1": {"type": "faq", "settings": {
            "question": "Can I buy the headrest or seat separately?",
            "answer": "<p>Yes. When a part needs replacing, buy the matching Easy Repair part and swap it in easily.</p>"}},
        "q2": {"type": "faq", "settings": {
            "question": "How far does the backrest recline, and can it lock?",
            "answer": "<p>The backrest reclines up to 125 degrees, and its angle locks in three positions: 105, 113 and 121 degrees.</p>"}},
        "q3": {"type": "faq", "settings": {
            "question": "The tension will not adjust with the backrest locked at step 2 or 3",
            "answer": "<p>That is by design - the tension lever is fixed while the backrest is locked reclined. Return the backrest upright to step 1 and adjust the tension without leaning on it.</p>"}},
        "q4": {"type": "faq", "settings": {
            "question": "Who is the T20 for?",
            "answer": "<p>Anyone after a first ergonomic chair without complicated controls - from secondary students to home-office and workplace use. Expert presets do the fitting for you.</p>"}},
    },
    "block_order": ["q1", "q2", "q3", "q4"],
    "settings": {"heading": "Frequently asked questions", "open_first": True, "background": "#f5f6f7"},
}

S["reviews"] = copy.deepcopy(B["reviews"])

S["stockists"] = {
    "type": "sidiz-store-info",
    "settings": {
        "heading": "Sit in one before you decide",
        "description": "Seat feel differs from body to body. Try a T20 in person where you can; otherwise our returns policy is there to fall back on.",
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
    "sticky_nav", "pdp_head", "intro", "hero", "about",
    "supernormal_banner", "fit_cards", "comfort_banner", "comfort_cards",
    "office_banner", "office_cards", "business_link", "compare_tiles",
    "find_your_fit", "goes_with", "easy_repair", "warranty",
    "specifications", "safety_info", "faq", "reviews", "stockists",
    "recommend", "notices",
]
assert set(order) == set(S), set(order) ^ set(S)

out = ROOT / "theme/templates/product.t20.json"
out.write_text(json.dumps({"sections": S, "order": order}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print("written", out.name, "sections:", len(order))
