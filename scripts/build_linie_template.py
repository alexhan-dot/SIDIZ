"""Compose product.linie.json.

LINIE is the compact minimal chair: image hero, a Flex-vs-Mesh option compare
(the KR natural-leather guidance is dropped - the AU LINIE sells no leather),
a design view, space tiles, the auto-fit-tilt view, detail tiles (one KR tile
is text-only), a two-card adjustment guide and a four-drawing spec. The KR
related-article link is skipped until an AU story exists.
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
    "n1": {"type": "link", "settings": {"label": "Options", "anchor": "options"}},
    "n2": {"type": "link", "settings": {"label": "Design", "anchor": "design"}},
    "n3": {"type": "link", "settings": {"label": "Spaces", "anchor": "spaces"}},
    "n4": {"type": "link", "settings": {"label": "Auto-fit tilt", "anchor": "auto-fit"}},
    "n5": {"type": "link", "settings": {"label": "Adjustment", "anchor": "adjustment-guide"}},
    "n6": {"type": "link", "settings": {"label": "Specifications", "anchor": "specifications"}},
    "n7": {"type": "link", "settings": {"label": "FAQ", "anchor": "faq"}},
}
S["sticky_nav"]["block_order"] = ["n1", "n2", "n3", "n4", "n5", "n6", "n7"]

S["pdp_head"] = copy.deepcopy(B["pdp_head"])
S["pdp_head"]["blocks"]["i1"]["settings"]["value"] = "SIDIZ LINIE Compact Ergonomic Chair"
S["pdp_head"]["blocks"]["i3"]["settings"]["value"] = "Fabric, mesh, moulded foam, plastic, steel"
S["pdp_head"]["blocks"]["i4"]["settings"]["value"] = "Warm Grey\nSand Beige\nAsh Green\nCharcoal"
S["pdp_head"]["settings"]["subtitle"] = (
    "A minimal computer chair that melts into the room - auto-fit tilt, a compact "
    "low-back structure and a choice of mesh or flex backrest."
)

S["hero"] = {
    "type": "sidiz-pdp-hero",
    "settings": {
        "subtitle": "<em class=\"caps\">Fits anywhere, for anyone</em>",
        "subtitle_colour": "#ffffff",
        "heading": "LINIE",
        "heading_colour": "#ffffff",
        "text_align": "center",
        "header_scheme": "dark",
        "image_url": img("LINIE_Head.jpg"),
        "image_url_mobile": img("LINIE_Head_M-0.jpg"),
        "alt": "SIDIZ LINIE compact ergonomic chair in a minimal interior",
        "description": (
            "<p>Minimal design. Auto-fit tilt. Mesh or flex backrest.</p>"
            "<p>The SIDIZ LINIE steps out of the boxy office-chair mould - a minimal "
            "computer and desk chair that melts naturally into the room. With the headrest "
            "boldly omitted and the backrest lowered, its compact structure keeps even a "
            "small space feeling open and considered.</p>"
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
            "title": "Flex",
            "description": "Flex backrest",
            "images": img("LINIE_Option1.jpg") + "," + img("LINIE_Option1-1.jpg"),
            "colours": "#a39c95,#d9c9b2,#9aa694,#36393b",
            "alt": "SIDIZ LINIE with the flex backrest"}},
        "o2": {"type": "option", "settings": {
            "title": "Mesh",
            "description": "Mesh backrest",
            "images": img("LINIE_Option2.jpg") + "," + img("LINIE_Option2-1.jpg"),
            "colours": "#a39c95,#d9c9b2,#9aa694,#36393b",
            "alt": "SIDIZ LINIE with the mesh backrest"}},
    },
    "block_order": ["o1", "o2"],
    "settings": {"heading": "The LINIE option for you"},
}

S["design_view"] = {
    "type": "sidiz-product-view",
    "settings": {
        "tag": "Minimal design",
        "heading": "A minimal design that melts into the space",
        "description": (
            "<p>Clean restraint and refined curves let the LINIE settle naturally into "
            "any room.</p>"
        ),
        "video_url": vid("6b0ff48d654b4cd4bac5bc7e1f34a441", "HD-1080p-7.2Mbps", "36792243"),
        "poster_url": poster("6b0ff48d654b4cd4bac5bc7e1f34a441"),
        "alt": "The LINIE's curves in a minimal room",
    },
    "blocks": {
        "b1": {"type": "feature", "settings": {
            "title": "Refined curved design",
            "description": "<p>Out of the boxy office-chair mould - a clean design that satisfies the eye as much as the body.</p>",
            "image_url": img("LINIE_01-1.jpg"),
            "alt": "The LINIE's curved backrest"}},
        "b2": {"type": "feature", "settings": {
            "title": "A simple lower structure",
            "description": "<p>An open layout with no protruding levers, kept simple below the seat.</p>",
            "image_url": img("LINIE_01-2.jpg"),
            "alt": "The LINIE's clean base"}},
    },
    "block_order": ["b1", "b2"],
}

S["space_tiles"] = {
    "type": "sidiz-tile-card-list",
    "blocks": {
        "t1": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "Home office",
            "description": "<p>For the home office where neither productivity nor style can give way.</p>",
            "image_url": img("LINIE_1_1__01.jpg"),
            "alt": "The LINIE in a home office"}},
        "t2": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "A student's room",
            "description": "<p>For growing students who need good posture at the desk.</p>",
            "image_url": img("LINIE_1_1__02.jpg"),
            "alt": "The LINIE at a student desk"}},
        "t3": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "The living room",
            "description": "<p>For the living room where one table hosts many activities.</p>",
            "image_url": img("LINIE_1_1__03.jpg"),
            "alt": "The LINIE at a living-room table"}},
        "t4": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "Small spaces",
            "description": "<p>For snug rooms where several pieces of furniture have to work together.</p>",
            "image_url": img("LINIE_1_1__04.jpg"),
            "alt": "The LINIE in a compact room"}},
    },
    "block_order": ["t1", "t2", "t3", "t4"],
    "settings": {"heading": "Spaces completed by the LINIE"},
}

S["autofit_view"] = {
    "type": "sidiz-product-view-vertical",
    "settings": {
        "heading": "Easy for anyone, anywhere",
        "description": (
            "<p>A chair that is shared should be comfortable and simple for whoever sits "
            "in it. The LINIE pairs an auto-fit tilt anyone can use with a design layout "
            "that fits any space.</p>"
        ),
        "image_url": img("LINIE_02.jpg"),
        "alt": "The LINIE shared across a household",
    },
    "blocks": {
        "b1": {"type": "feature", "settings": {
            "title": "Auto-fit tilt that sets itself",
            "description": "<p>No hands needed - the moment you sit, the tilt finds and sets the optimal tension for your weight.</p>",
            "video_url": vid("0ce2f2fdbdbc4e5a8cdd492398cb7263", "SD-480p-0.9Mbps", "40950678"),
            "poster_url": poster("0ce2f2fdbdbc4e5a8cdd492398cb7263"),
            "alt": "The auto-fit tilt responding to a sitter"}},
        "b2": {"type": "feature", "settings": {
            "title": "A generous size for everyone",
            "description": "<p>A roomy seat and a backrest that supports the lower spine - comfortable for every build.</p>",
            "image_url": img("LINIE_02-2-0.jpg"),
            "alt": "The LINIE's generous seat"}},
        "b3": {"type": "feature", "settings": {
            "title": "A compact structure, essentials only",
            "description": "<p>Headrest omitted, backrest lowered - a compact structure that never crowds a small space.</p>",
            "image_url": img("LINIE_02-3.jpg"),
            "alt": "The LINIE's compact low-back silhouette"}},
    },
    "block_order": ["b1", "b2", "b3"],
}

S["detail_tiles"] = {
    "type": "sidiz-tile-card-list",
    "blocks": {
        "t1": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "Mesh backrest",
            "description": "<p>A firmly woven mesh backrest keeps sitting fresh and cool in every season.</p>",
            "image_url": img("LINIE_1_1__05_2bbe7b0c-aedf-400f-a502-588f3370c27d.jpg"),
            "alt": "The LINIE mesh backrest weave"}},
        "t2": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "Flex backrest",
            "description": "<p>Lines of differing thickness and length flex with your movement, supple yet firm.</p>",
            "image_url": img("LINIE_1_1__06_37f1da99-6c7d-4042-a008-df28619fd08c.jpg"),
            "alt": "The LINIE flex backrest lines"}},
        "t3": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "Simple controls, from where you sit",
            "description": "<p>No bending down: levers on both sides of the seat set the tilt lock and chair height as you sit.</p>",
            "image_url": img("LINIE_1_1__07.jpg"),
            "alt": "The LINIE's side levers"}},
        "t4": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "A stream line that spreads the weight",
            "description": "<p>A stream line in the seat's inner frame spreads pressure evenly from the hips, easing the lower back through long sittings.</p>",
            "alt": "The LINIE seat's stream-line frame"}},
    },
    "block_order": ["t1", "t2", "t3", "t4"],
    "settings": {"heading": "Fine detail inside the simplicity"},
}

S["find_your_fit"] = {
    "type": "sidiz-find-your-fit",
    "blocks": {
        "s1": {"type": "adjustment", "settings": {
            "title": "Chair height",
            "description": "<p>Set to your body frame.</p>",
            "image_url": img("LINIE_FYF_01_133478ce-b5c3-431f-b798-ef0f295614cb.jpg"),
            "alt": "Adjusting the LINIE chair height"}},
        "s2": {"type": "adjustment", "settings": {
            "title": "Tilt lock",
            "description": "<p>Lock the backrest for moments of focus.</p>",
            "image_url": img("LINIE_FYF_02.jpg"),
            "alt": "Locking the LINIE tilt"}},
    },
    "block_order": ["s1", "s2"],
    "settings": {
        "heading": "LINIE adjustment guide",
        "subtitle": "FIND YOUR FIT. Set it up for your body",
        "guide_label": "USER GUIDE",
        "guide_link": "/pages/user-guide",
    },
}

S["goes_with"] = {
    "type": "sidiz-related-products",
    "settings": {"heading": "Goes well with the LINIE", "source": "collection", "limit": 4},
}

S["easy_repair"] = copy.deepcopy(B["easy_repair"])
S["easy_repair"]["settings"]["heading"] = "LINIE | EASY REPAIR"
S["easy_repair"]["settings"]["subtitle"] = "Repair it, keep it longer"
S["easy_repair"]["settings"]["description"] = (
    "<p>Even after long use, buy just the part you need and swap it in to keep the chair "
    "like new.</p>"
)

S["warranty"] = copy.deepcopy(B["warranty"])
S["warranty"]["settings"]["heading"] = "LINIE | 5-year warranty"
S["warranty"]["settings"]["body"] = (
    "<p>So the journey with your LINIE continues, SIDIZ provides a 5-year warranty to "
    "customers who complete product registration. Once your chair arrives, register it "
    "before you forget, for more comfortable years ahead.</p>"
)

S["specifications"] = copy.deepcopy(B["specifications"])
S["specifications"]["settings"]["heading"] = "LINIE dimensions"
S["specifications"]["settings"]["figures"] = (
    "Maximum load 125 kg / product weight approximately 13.7 kg (Flex) or 13.2 kg (Mesh)."
)
S["specifications"]["blocks"] = {
    "d1": {"type": "drawing", "settings": {
        "image_url": img("TXNA250NF_01_02259039-f13c-4f89-bec8-6a75063e27f1.jpg"),
        "alt": "Dimension drawing of the SIDIZ LINIE with flex backrest, front elevation"}},
    "d2": {"type": "drawing", "settings": {
        "image_url": img("TXNA250NF_02_7da8fade-433c-4c72-8658-34cd10b766f8.jpg"),
        "alt": "Dimension drawing of the SIDIZ LINIE with flex backrest, side elevation"}},
    "d3": {"type": "drawing", "settings": {
        "image_url": img("TXNA250F_01_e548e80f-008c-4dca-85f5-6162c915f402.jpg"),
        "alt": "Dimension drawing of the SIDIZ LINIE with mesh backrest, front elevation"}},
    "d4": {"type": "drawing", "settings": {
        "image_url": img("TXNA250F_02_18b7ddea-ccf4-494e-8c9a-460d6f2fe7d3.jpg"),
        "alt": "Dimension drawing of the SIDIZ LINIE with mesh backrest, side elevation"}},
}
S["specifications"]["block_order"] = ["d1", "d2", "d3", "d4"]

S["safety_info"] = copy.deepcopy(B["safety_info"])
del S["safety_info"]["blocks"]["n1"]
S["safety_info"]["block_order"] = ["n2"]

S["faq"] = {
    "type": "sidiz-faq",
    "blocks": {
        "q1": {"type": "faq", "settings": {
            "question": "From what height can the LINIE be used?",
            "answer": "<p>The recommended height is 150 cm and above. Depending on build, sitters under about 160 cm may find their heels off the floor - a footrest such as the STEPO makes the posture stable.</p>"}},
        "q2": {"type": "faq", "settings": {
            "question": "What is the difference between the Flex and Mesh backrests?",
            "answer": "<p>The mesh backrest is a firm weave that stays fresh and airy in every season; the flex backrest supports through lines of differing thickness that move with you, supple yet firm. The rest of the chair is identical.</p>"}},
        "q3": {"type": "faq", "settings": {
            "question": "How does the auto-fit tilt work?",
            "answer": "<p>There is nothing to set: as you sit, the tilt adjusts its tension to your weight automatically, and side levers lock the tilt or set the height without bending down.</p>"}},
    },
    "block_order": ["q1", "q2", "q3"],
    "settings": {"heading": "Frequently asked questions", "open_first": True, "background": "#f5f6f7"},
}

S["reviews"] = copy.deepcopy(B["reviews"])

S["stockists"] = {
    "type": "sidiz-store-info",
    "settings": {
        "heading": "Sit in one before you decide",
        "description": "Seat feel differs from body to body. Try a LINIE in person where you can; otherwise our returns policy is there to fall back on.",
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
    "sticky_nav", "pdp_head", "hero", "options", "design_view",
    "space_tiles", "autofit_view", "detail_tiles", "find_your_fit",
    "goes_with", "easy_repair", "warranty", "specifications",
    "safety_info", "faq", "reviews", "stockists", "recommend", "notices",
]
assert set(order) == set(S), set(order) ^ set(S)

out = ROOT / "theme/templates/product.linie.json"
out.write_text(json.dumps({"sections": S, "order": order}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print("written", out.name, "sections:", len(order))
