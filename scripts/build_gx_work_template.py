"""Compose product.gx-work.json for SIDIZ GX (renewed / Joy Explorer page).

KR order: renewal tiles BEFORE the hero, image-backed scroll banner, dark
feature card list, a one-line scroll banner, two horizontal product views,
design tiles, then the family-standard tail. The KR influencer review section
(product_assembly_guide) is NOT migrated - ACL; AU creator content needed.
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
    "n1": {"type": "link", "settings": {"label": "What is new", "anchor": "renewal"}},
    "n2": {"type": "link", "settings": {"label": "Work and chill", "anchor": "work-chill"}},
    "n3": {"type": "link", "settings": {"label": "Gaming tilt", "anchor": "tilt"}},
    "n4": {"type": "link", "settings": {"label": "Armrest", "anchor": "armrest"}},
    "n5": {"type": "link", "settings": {"label": "Adjustment", "anchor": "adjustment-guide"}},
    "n6": {"type": "link", "settings": {"label": "Specifications", "anchor": "specifications"}},
    "n7": {"type": "link", "settings": {"label": "FAQ", "anchor": "faq"}},
}
S["sticky_nav"]["block_order"] = ["n1", "n2", "n3", "n4", "n5", "n6", "n7"]

S["pdp_head"] = copy.deepcopy(B["pdp_head"])
S["pdp_head"]["blocks"]["i1"]["settings"]["value"] = "SIDIZ GX Ergonomic Gaming and Office Chair"
S["pdp_head"]["blocks"]["i3"]["settings"]["value"] = "Mesh, moulded foam, plastic, steel"
S["pdp_head"]["blocks"]["i4"]["settings"]["value"] = "Grey\nBlack\nChameleon Grey\nChameleon Black"
S["pdp_head"]["settings"]["subtitle"] = (
    "One ergonomic gaming chair for work and rest alike - dual-tension mesh backrest, "
    "wide headrest, gaming tilt and a 9-step armrest."
)

S["renewal_tiles"] = {
    "type": "sidiz-tile-card-list",
    "blocks": {
        "t1": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "A headrest with height adjustment added",
            "description": "<p>Where the previous GX adjusted angle only, height adjustment is added for a finer fit to your build.</p>",
            "image_url": img("gx-_1.jpg"),
            "alt": "The renewed GX headrest adjusting in height"}},
        "t2": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "Mesh engineered to hold the lower back firmer",
            "description": "<p>The lumbar zone of the mesh is woven firmer on an ergonomic basis, so differentiated support holds good posture comfortably.</p>",
            "image_url": img("gx-_33.jpg"),
            "alt": "The firmer lumbar mesh zone of the renewed GX"}},
    },
    "block_order": ["t1", "t2"],
    "settings": {"heading": "The renewed GX - what changed?"},
}

S["hero"] = {
    "type": "sidiz-pdp-hero",
    "settings": {
        "subtitle": "<em class=\"caps\">Joy Explorer</em><br>The ergonomic gaming chair for work and rest",
        "subtitle_colour": "#ffffff",
        "heading": "GX",
        "heading_colour": "#ffffff",
        "text_align": "center",
        "header_scheme": "dark",
        "video_url": vid("237dc7ea071243c397ab4f460c6c69a6", "HD-1080p-7.2Mbps", "82736419"),
        "poster_url": poster("237dc7ea071243c397ab4f460c6c69a6"),
        "video_url_mobile": vid("405eee554ab3493da98045bf4065b7f2", "HD-1080p-7.2Mbps", "82736610"),
        "poster_url_mobile": poster("405eee554ab3493da98045bf4065b7f2"),
        "alt": "SIDIZ GX ergonomic gaming chair in motion",
        "description": (
            "<p>Dual-tension support backrest. Wide headrest. Gaming tilt. 9-step armrest.</p>"
            "<p>The GX is an ergonomic gaming chair for enjoying work and rest smartly in one "
            "seat - balancing immersion and ease, work and play, for the way you live.</p>"
        ),
        "description_colour": "#000000",
        "description_align": "left",
        "product_type": "default",
    },
}

S["work_chill_banner"] = {
    "type": "sidiz-wb-scroll-banner",
    "settings": {
        "heading": "<em class=\"caps\">Work and chill</em><br>Switch freely between work and rest in one chair",
        "heading_colour": "#000000",
        "header_scheme": "dark",
        "tag": "Pro-tension mesh &amp; wide headrest",
        "tag_colour": "#000000",
        "tag_background": "#eaedf0",
        "subheading": "",
        "description": (
            "<p>Deep focus through long working hours is a given - and everyday comfort "
            "should have no limits either. Let the GX dissolve the boundary between work "
            "and rest.</p>"
        ),
        "text_colour": "#ffffff",
        "image_url": img("home_01_pc.jpg"),
        "image_url_mobile": img("home_01_mo.jpg"),
        "alt": "The GX at home, between work and rest",
    },
}

S["feature_cards"] = {
    "type": "sidiz-wb-scroll-card-list",
    "blocks": {
        "c1": {"type": "card", "settings": {
            "title": "Dual-tension support backrest",
            "title_colour": "#ffffff",
            "description": (
                "<p>Tension tuned by body zone supports every moment - work, play and rest - "
                "without slackening. The flexible Relax Zone up top wraps shoulders and back "
                "softly; the dense, firm Core Zone at the lumbar acts as a built-in lumbar "
                "support, no extra hardware needed.</p>"
            ),
            "description_colour": "#a4aab0",
            "video_url": vid("afad8111d62e419381c52160c83dc129", "HD-1080p-7.2Mbps", "72835973"),
            "poster_url": poster("afad8111d62e419381c52160c83dc129"),
            "alt": "The dual-tension mesh backrest flexing by zone"}},
        "c2": {"type": "card", "settings": {
            "title": "Wide headrest",
            "title_colour": "#ffffff",
            "description": (
                "<p>A broader headrest in the same fresh pro-tension mesh steadies the head "
                "even as posture drifts, with a hammock-like ease. Fine height and angle "
                "adjustment supports neck and head at the most comfortable angle in any "
                "position.</p>"
            ),
            "description_colour": "#a4aab0",
            "video_url": vid("22d20ad4070a4e0f949e70b370c9212f", "HD-1080p-7.2Mbps", "50402657"),
            "poster_url": poster("22d20ad4070a4e0f949e70b370c9212f"),
            "alt": "The wide GX headrest adjusting"}},
        "c3": {"type": "card", "settings": {
            "title": "Cloud Foam",
            "title_colour": "#ffffff",
            "description": (
                "<p>The chair you spend most of your day in should feel comfortable for a "
                "lifetime. A foam-forming technique that maximises compression gives support "
                "shaped to the body, and a generous thickness keeps long sittings free of "
                "pressure points.</p>"
            ),
            "description_colour": "#a4aab0",
            "video_url": vid("9aa80dcca3144d209c4becd8a30fe869", "HD-1080p-7.2Mbps", "50402702"),
            "poster_url": poster("9aa80dcca3144d209c4becd8a30fe869"),
            "alt": "The Cloud Foam seat compressing"}},
    },
    "block_order": ["c1", "c2", "c3"],
    "settings": {"header_scheme": "dark", "background": "#000000"},
}

S["professional_banner"] = {
    "type": "sidiz-wb-banner",
    "settings": {
        "heading": "<em class=\"caps\">Be the professional</em>",
        "align": "left",
        "title_colour": "#000000",
    },
}

S["tilt_view"] = {
    "type": "sidiz-product-view",
    "settings": {
        "tag": "Steady posture completes working focus",
        "heading": "A gaming tilt that holds without wobble",
        "description": (
            "<p>Lock the backrest at 90 degrees for moments of deep focus, or at 120 degrees "
            "when it is time to rest. The gaming tilt supports every moment steadily, without "
            "play. *4-step backrest lock, 4-step tilting tension.</p>"
        ),
        "video_url": vid("da745b07c0d147b1aed86a9fbe1e2a84", "HD-1080p-3.3Mbps", "54722576"),
        "poster_url": poster("da745b07c0d147b1aed86a9fbe1e2a84"),
        "alt": "The GX gaming tilt locking through its steps",
    },
    "blocks": {
        "b1": {"type": "feature", "settings": {
            "title": "Backrest angle lock",
            "description": "<p>A stable, play-free 90 degree setting, with a lock that holds whichever angle you choose.</p>",
            "image_url": img("Be_the_player.jpg"),
            "alt": "The GX backrest locked upright"}},
        "b2": {"type": "feature", "settings": {
            "title": "Tilting tension control",
            "description": "<p>Switch quickly to the tension you want, moving freely between focus mode and rest mode.</p>",
            "image_url": img("Img2_174c8a25-e805-445a-bbd8-b51b8ac873d2.jpg"),
            "alt": "The GX tilting tension control"}},
    },
    "block_order": ["b1", "b2"],
}

S["armrest_view"] = {
    "type": "sidiz-product-view",
    "settings": {
        "tag": "The difference precision makes to immersion",
        "heading": "A 9-step armrest for every setup",
        "description": (
            "<p>Where your arms rest directly affects focus and efficiency. The GX armrest "
            "adjusts precisely to your working style and environment: nine height steps ease "
            "wrists and shoulders through long typing, meetings and rest. *110 mm height, "
            "60 degree rotation, 50 mm range.</p>"
        ),
        "image_url": img("GX__AI__04.jpg"),
        "alt": "The GX 9-step armrest in a working setup",
    },
    "blocks": {
        "b1": {"type": "feature", "settings": {
            "title": "9-step height adjustment",
            "description": "<p>Set the height for monitors, tablets and every device in between.</p>",
            "image_url": img("GX_02-1.jpg"),
            "alt": "Armrest height steps"}},
        "b2": {"type": "feature", "settings": {
            "title": "7-step angle adjustment",
            "description": "<p>Fine settings to match the posture you want.</p>",
            "image_url": img("GX_02-2.jpg"),
            "alt": "Armrest angle steps"}},
        "b3": {"type": "feature", "settings": {
            "title": "Wide armrest pad",
            "description": "<p>A generous size to lean on without restricting movement.</p>",
            "image_url": img("GX_02-3.jpg"),
            "alt": "The wide GX armrest pad"}},
    },
    "block_order": ["b1", "b2", "b3"],
}

S["design_tiles"] = {
    "type": "sidiz-tile-card-list",
    "blocks": {
        "t1": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "Chameleon mesh, easy on the eyes",
            "description": "<p>Mesh that shifts colour with the viewing angle fills a space with life and a day with style.</p>",
            "image_url": img("GX__1-1__01.jpg"),
            "alt": "The chameleon mesh shifting colour"}},
        "t2": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "A lever designed to the last detail",
            "description": "<p>A diagonal lever means no over-bent fingers, and a soft silicone insert considers even the touch of the fingertip.</p>",
            "image_url": img("Img3_b8ff1387-aa42-408a-ab7e-3e28bf913155.jpg"),
            "alt": "The GX lever with its silicone insert"}},
    },
    "block_order": ["t1", "t2"],
    "settings": {"heading": "A dimensional design for all the senses"},
}

S["find_your_fit"] = {
    "type": "sidiz-find-your-fit",
    "blocks": {
        "s1": {"type": "adjustment", "settings": {
            "title": "Chair height / seat depth",
            "description": "<p>Set both to your body frame.</p>",
            "image_url": img("GX_FYF_01.jpg"),
            "alt": "Adjusting the GX chair height and seat depth"}},
        "s2": {"type": "adjustment", "settings": {
            "title": "Headrest angle",
            "description": "<p>Ease the load on your head and neck.</p>",
            "image_url": img("Find_your_fit_01.jpg"),
            "alt": "Adjusting the GX headrest"}},
        "s3": {"type": "adjustment", "settings": {
            "title": "Armrest height / fore-and-aft / angle",
            "description": "<p>Keep shoulders and arms relaxed.</p>",
            "image_url": img("GX_FYF_03.jpg"),
            "alt": "Adjusting the GX armrests"}},
        "s4": {"type": "adjustment", "settings": {
            "title": "Tilting tension / backrest lock",
            "description": "<p>Choose how the backrest moves and holds.</p>",
            "image_url": img("Find_your_fit_02.jpg"),
            "alt": "Adjusting the GX tilt"}},
    },
    "block_order": ["s1", "s2", "s3", "s4"],
    "settings": {
        "heading": "GX adjustment guide",
        "subtitle": "FIND YOUR FIT. Set it up for your body",
        "guide_label": "USER GUIDE",
        "guide_link": "/pages/user-guide",
    },
}

S["goes_with"] = {
    "type": "sidiz-related-products",
    "settings": {"heading": "Goes well with the GX", "source": "collection", "limit": 4},
}

S["easy_repair"] = copy.deepcopy(B["easy_repair"])
S["easy_repair"]["settings"]["heading"] = "GX | EASY REPAIR"
S["easy_repair"]["settings"]["subtitle"] = "Repair it, keep it longer"
S["easy_repair"]["settings"]["description"] = (
    "<p>Even after long use, buy just the part you need and swap it in to keep the chair "
    "like new.</p>"
)

S["warranty"] = copy.deepcopy(B["warranty"])
S["warranty"]["settings"]["heading"] = "GX | 5-year warranty"
S["warranty"]["settings"]["body"] = (
    "<p>So the journey with your GX continues, SIDIZ provides a 5-year warranty to "
    "customers who complete product registration. Once your chair arrives, register it "
    "before you forget, for more comfortable years ahead.</p>"
)

S["specifications"] = copy.deepcopy(B["specifications"])
S["specifications"]["settings"]["heading"] = "GX dimensions"
S["specifications"]["settings"]["figures"] = "Maximum load 115 kg / product weight approximately 17 kg."
S["specifications"]["blocks"]["d1"]["settings"].update({
    "image_url": img("GX_bef2ce3c-faec-4514-8da5-179075a4775f.png"),
    "alt": "Dimension drawing of the SIDIZ GX, front elevation"})
S["specifications"]["blocks"]["d2"]["settings"].update({
    "image_url": img("GX-1_01744ba6-1e09-47a6-a5ca-377598f694bb.png"),
    "alt": "Dimension drawing of the SIDIZ GX, side elevation"})

S["safety_info"] = copy.deepcopy(B["safety_info"])

S["faq"] = {
    "type": "sidiz-faq",
    "blocks": {
        "q1": {"type": "faq", "settings": {
            "question": "How far does the backrest recline, and can it lock?",
            "answer": "<p>The GX backrest adjusts across four steps from 100 to 120 degrees, and the angle can be locked.</p>"}},
        "q2": {"type": "faq", "settings": {
            "question": "Can the seat be replaced?",
            "answer": "<p>Yes - if you would like a replacement seat, contact our support team.</p>"}},
        "q3": {"type": "faq", "settings": {
            "question": "The tension will not adjust with the backrest locked at steps 2 to 4",
            "answer": "<p>That is by design - the tension lever is fixed while the backrest is locked reclined. Return the backrest upright to step 1 and adjust the tension without leaning on it.</p>"}},
        "q4": {"type": "faq", "settings": {
            "question": "Is the GX only for gaming?",
            "answer": "<p>No. The GX is built for work and rest alike: lock the backrest upright for focused work, recline it to 120 degrees to unwind, and the dual-tension mesh supports both.</p>"}},
    },
    "block_order": ["q1", "q2", "q3", "q4"],
    "settings": {"heading": "Frequently asked questions", "open_first": True, "background": "#f5f6f7"},
}

S["reviews"] = copy.deepcopy(B["reviews"])

S["stockists"] = {
    "type": "sidiz-store-info",
    "settings": {
        "heading": "Sit in one before you decide",
        "description": "Seat feel differs from body to body. Try a GX in person where you can; otherwise our returns policy is there to fall back on.",
        "link_label": "Find a stockist",
        "link": "/pages/contact",
        "image_url": img("shop.png"),
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
    "sticky_nav", "pdp_head", "renewal_tiles", "hero",
    "work_chill_banner", "feature_cards", "professional_banner",
    "tilt_view", "armrest_view", "design_tiles",
    "find_your_fit", "goes_with", "easy_repair", "warranty",
    "specifications", "safety_info", "faq", "reviews", "stockists",
    "recommend", "notices",
]
assert set(order) == set(S), set(order) ^ set(S)

out = ROOT / "theme/templates/product.gx-work.json"
out.write_text(json.dumps({"sections": S, "order": order}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print("written", out.name, "sections:", len(order))
