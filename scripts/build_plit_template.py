"""Compose product.plit.json.

PLIT is the easy-care dining chair: video hero (separate mobile cut), four
AI-styled table tiles with their disclaimers, three light image-backed scroll
banners each over a light card list (easy care / hidden structure /
part-replacement), the DIY assembly view and a compact tail with the cover
washing guidance.
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
    "n1": {"type": "link", "settings": {"label": "Styling", "anchor": "styling"}},
    "n2": {"type": "link", "settings": {"label": "Easy care", "anchor": "easy-care"}},
    "n3": {"type": "link", "settings": {"label": "Structure", "anchor": "structure"}},
    "n4": {"type": "link", "settings": {"label": "Replaceable parts", "anchor": "parts"}},
    "n5": {"type": "link", "settings": {"label": "Specifications", "anchor": "specifications"}},
    "n6": {"type": "link", "settings": {"label": "FAQ", "anchor": "faq"}},
}
S["sticky_nav"]["block_order"] = ["n1", "n2", "n3", "n4", "n5", "n6"]

S["pdp_head"] = copy.deepcopy(B["pdp_head"])
S["pdp_head"]["blocks"]["i1"]["settings"]["value"] = "SIDIZ PLIT Easy-Care Dining Chair"
S["pdp_head"]["blocks"]["i3"]["settings"]["value"] = "Fabric, sponge, plastic, steel"
S["pdp_head"]["blocks"]["f3"] = {"type": "fact", "settings": {
    "label": "Assembly",
    "value": "Simple DIY assembly"}}
S["pdp_head"]["block_order"] = ["f1", "f2", "f3", "i1", "i2", "i3", "i4", "i5"]
S["pdp_head"]["settings"]["subtitle"] = (
    "Easy care, beyond comfort: a washable snap-off seat cover and part-level "
    "replaceable modules keep the dining chair like new, every day."
)

S["hero"] = {
    "type": "sidiz-pdp-hero",
    "settings": {
        "subtitle": "Easy Care, Beyond Comfort.",
        "subtitle_colour": "#ffffff",
        "heading": "PLIT",
        "heading_colour": "#ffffff",
        "text_align": "center",
        "header_scheme": "dark",
        "video_url": vid("5a7b78bfdf094ab88c8e401594d4d3be", "HD-1080p-7.2Mbps", "75199912"),
        "poster_url": poster("5a7b78bfdf094ab88c8e401594d4d3be"),
        "video_url_mobile": vid("9d3fcbb351f14de18bc5b23f7aa2cfe2", "HD-1080p-7.2Mbps", "75200032"),
        "poster_url_mobile": poster("9d3fcbb351f14de18bc5b23f7aa2cfe2"),
        "alt": "The SIDIZ PLIT dining chair and its washable cover",
        "description": (
            "<p>Past the limits of dining chairs that stain so easily: the clever choice "
            "you keep like new, every day. With a simply washed cover and part-level "
            "replaceable modules, the PLIT lifts the burden of stains and wear - "
            "sustainable everyday comfort at the table.</p>"
        ),
        "description_colour": "#000000",
        "description_align": "left",
        "product_type": "default",
    },
}

S["styling_tiles"] = {
    "type": "sidiz-tile-card-list",
    "blocks": {
        "t1": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "Beige tones, snug and warm",
            "description": f"<p>The PLIT's plain silhouette and fabric texture lift the gentle warmth of a beige interior, settling in without breaking the calm.{AI_NOTE}</p>",
            "image_url": img("AI_PLIT_15.png"),
            "alt": "The PLIT in a beige dining room"}},
        "t2": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "White tones, clean and considered",
            "description": f"<p>Its minimal, unadorned lines match the refined taste of a white room, with straight edges and planes bringing calm to a bright space.{AI_NOTE}</p>",
            "image_url": img("AI_PLIT_14.png"),
            "alt": "The PLIT in a white dining room"}},
        "t3": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "A modern dining look with fine contrast",
            "description": f"<p>The soft curve of the PLIT's backrest gently lightens a black table's weight - a modern balance with real finesse.{AI_NOTE}</p>",
            "image_url": img("AI_PLIT_05.png"),
            "alt": "The PLIT at a black table"}},
        "t4": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "Natural timber, matched to the grain",
            "description": f"<p>Timber's warm texture meets the PLIT's tidy design in an easy balance, its precise silhouette anchoring the room's natural mood.{AI_NOTE}</p>",
            "image_url": img("AI_PLIT_09.png"),
            "alt": "The PLIT at a timber table"}},
    },
    "block_order": ["t1", "t2", "t3", "t4"],
    "settings": {"heading": "At home with any taste, any table"},
}

S["care_banner"] = {
    "type": "sidiz-wb-scroll-banner",
    "settings": {
        "heading": "",
        "header_scheme": "light",
        "tag": "Easy care, beyond comfort",
        "tag_colour": "#000000",
        "tag_background": "#eaedf0",
        "subheading": "Easy-care design,<br>completed by a washable seat",
        "description": (
            "<p>Built for the dining table, where everyday stains are a given: a "
            "washable fabric seat and a simple-release structure take the chore out of "
            "keeping it clean.</p>"
        ),
        "text_colour": "#000000",
        "image_url": img("Img_01_08c42136-2b13-4c18-a109-dfce0a0fc3af.jpg"),
        "image_url_mobile": img("Img_M_2.jpg"),
        "alt": "Washing the PLIT seat cover",
    },
}

S["care_cards"] = {
    "type": "sidiz-wb-scroll-card-list",
    "blocks": {
        "c1": {"type": "card", "settings": {
            "title": "A washable fabric cover",
            "title_colour": "#000000",
            "description": "<p>Light marks wipe away; heavier stains go straight in the washing machine - juice and sauce hold no fear. *Machine or hand wash at 40 degrees or below; a laundry net is recommended.</p>",
            "description_colour": "#7c8084",
            "image_url": img("Img_02_58a8f197-3e2e-4148-8b57-c9cec2f7a6a4.jpg"),
            "alt": "The washable PLIT cover"}},
        "c2": {"type": "card", "settings": {
            "title": "A snap-fit seat that lifts free, no tools",
            "title_colour": "#000000",
            "description": "<p>No screws, no tools: lift the seat's edge and it releases at once - intuitive even if furniture care is not your thing.</p>",
            "description_colour": "#7c8084",
            "video_url": vid("8571c73dc3864cb5957eb7a80b9777ae", "HD-720p-4.5Mbps", "75200687"),
            "poster_url": poster("8571c73dc3864cb5957eb7a80b9777ae"),
            "alt": "Lifting the PLIT seat free"}},
        "c3": {"type": "card", "settings": {
            "title": "A buttoned cover, on and off in moments",
            "title_colour": "#000000",
            "description": "<p>Buttons under the seat fasten and release the cover quickly, so a spill is dealt with before it settles.</p>",
            "description_colour": "#7c8084",
            "video_url": vid("b42079ff197c4af6bff782fcd8ee4958", "HD-720p-4.5Mbps", "75201047"),
            "poster_url": poster("b42079ff197c4af6bff782fcd8ee4958"),
            "alt": "Unbuttoning the PLIT cover"}},
    },
    "block_order": ["c1", "c2", "c3"],
    "settings": {"header_scheme": "light", "background": "#ffffff"},
}

S["structure_banner"] = {
    "type": "sidiz-wb-scroll-banner",
    "settings": {
        "heading": "",
        "header_scheme": "light",
        "tag": "",
        "subheading": "Precise structure,<br>hidden inside a minimal design",
        "description": (
            "<p>Inside the clean silhouette hides SIDIZ's precise ergonomic support and "
            "tuned elasticity. In a chair the body touches every day, the unseen details "
            "set the standard of a perfect sit.</p>"
        ),
        "text_colour": "#000000",
        "image_url": img("Img_03.jpg"),
        "image_url_mobile": img("Img_M_3.jpg"),
        "alt": "The PLIT's hidden structure",
    },
}

S["structure_cards"] = {
    "type": "sidiz-wb-scroll-card-list",
    "blocks": {
        "c1": {"type": "card", "settings": {
            "title": "A natural curve and the right height",
            "title_colour": "#000000",
            "description": "<p>A backrest curve that holds the back gently, at a height tuned to living-dining life - steady support from a quick meal to a long tea.</p>",
            "description_colour": "#7c8084",
            "image_url": img("Img_04.jpg"),
            "alt": "The PLIT's backrest curve"}},
        "c2": {"type": "card", "settings": {
            "title": "Flexible spring from a slit structure",
            "title_colour": "#000000",
            "description": "<p>Slits inside the seat spread your weight naturally, easing a fixed chair's stiffness with a subtle spring that keeps long sittings light.</p>",
            "description_colour": "#7c8084",
            "image_url": img("Img_05.jpg"),
            "alt": "The slit structure inside the seat"}},
        "c3": {"type": "card", "settings": {
            "title": "Front-and-rear glides for movement and hold",
            "title_colour": "#000000",
            "description": "<p>Plastic glides up front slide the chair smoothly; silicone glides behind plant it firmly once you sit. *Fit the included felt glides for an even softer slide.</p>",
            "description_colour": "#7c8084",
            "image_url": img("Img_06.jpg"),
            "alt": "The PLIT's dual glide setup"}},
    },
    "block_order": ["c1", "c2", "c3"],
    "settings": {"header_scheme": "light", "background": "#ffffff"},
}

S["parts_banner"] = {
    "type": "sidiz-wb-scroll-banner",
    "settings": {
        "heading": "",
        "header_scheme": "light",
        "tag": "",
        "subheading": "A structure that lasts,<br>a design that takes responsibility",
        "description": (
            "<p>Only the worn or stained part is replaced, extending the product's life - "
            "SIDIZ's sustainability, easing the everyday and thinking of the planet.</p>"
        ),
        "text_colour": "#000000",
        "image_url": img("Img_07.jpg"),
        "image_url_mobile": img("Img_M_4.jpg"),
        "alt": "The PLIT's replaceable modules",
    },
}

S["parts_cards"] = {
    "type": "sidiz-wb-scroll-card-list",
    "blocks": {
        "c1": {"type": "card", "settings": {
            "title": "Smart upkeep, part by part",
            "title_colour": "#000000",
            "description": "<p>No need to buy a new chair - choose and replace only the part that needs it, a sensible way to keep the chair going.</p>",
            "description_colour": "#7c8084",
            "image_url": img("Img_08.jpg"),
            "alt": "The PLIT's separable parts"}},
        "c2": {"type": "card", "settings": {
            "title": "A fresh cover when the old one tires",
            "title_colour": "#000000",
            "description": "<p>When fabric wears thin or a stain will not lift, buy just a new cover and swap it on.</p>",
            "description_colour": "#7c8084",
            "image_url": img("Img_09.jpg"),
            "alt": "Fitting a fresh PLIT cover"}},
        "c3": {"type": "card", "settings": {
            "title": "A seat module that swaps whole",
            "title_colour": "#000000",
            "description": "<p>If the sponge settles or a stain soaks through, the whole seat module replaces on its own. *Parts available through our support team.</p>",
            "description_colour": "#7c8084",
            "image_url": img("Img_10.jpg"),
            "alt": "Swapping the PLIT seat module"}},
    },
    "block_order": ["c1", "c2", "c3"],
    "settings": {"header_scheme": "light", "background": "#ffffff"},
}

S["diy_view"] = {
    "type": "sidiz-product-view-vertical",
    "settings": {
        "heading": "A DIY product you assemble yourself",
        "description": (
            "<p>Before assembling, check every part, then follow the assembly guide on "
            "the top pad.</p>"
        ),
        "image_url": img("Img_11.jpg"),
        "alt": "The PLIT parts laid out for assembly",
    },
    "blocks": {},
    "block_order": [],
}

S["goes_with"] = {
    "type": "sidiz-related-products",
    "settings": {"heading": "Goes well with the PLIT", "source": "collection", "limit": 4},
}

S["warranty"] = copy.deepcopy(B["warranty"])
S["warranty"]["settings"]["heading"] = "PLIT | 5-year warranty"
S["warranty"]["settings"]["body"] = (
    "<p>So the journey with your PLIT continues, SIDIZ provides a 5-year warranty to "
    "customers who complete product registration. Once your chair arrives, register it "
    "before you forget, for more comfortable years ahead.</p>"
)

S["specifications"] = copy.deepcopy(B["specifications"])
S["specifications"]["settings"]["heading"] = "PLIT dimensions"
S["specifications"]["settings"]["figures"] = "Maximum load 125 kg / product weight approximately 7.5 kg."
S["specifications"]["blocks"]["d1"]["settings"].update({
    "image_url": img("PLIT_01.jpg"),
    "alt": "Dimension drawing of the SIDIZ PLIT, front elevation"})
S["specifications"]["blocks"]["d2"]["settings"].update({
    "image_url": img("PLIT_02.jpg"),
    "alt": "Dimension drawing of the SIDIZ PLIT, side elevation"})

S["safety_info"] = {
    "type": "sidiz-safety-info",
    "blocks": {
        "n1": {"type": "note", "settings": {
            "title": "Washing the cover",
            "body": "<p>Wash gently at 40 degrees. No oxygen bleach. Iron between 80 and 120 degrees if needed. No dry cleaning. Dry flat, in the shade.</p>"}},
        "n2": {"type": "note", "settings": {
            "title": "Removing stains from the frame",
            "body": "<p>If the frame gets marked during assembly or use, a melamine sponge lifts stains easily. *Rubbing hard can damage the surface.</p>"}},
    },
    "block_order": ["n1", "n2"],
    "settings": {"heading": "Care and cautions"},
}

S["faq"] = {
    "type": "sidiz-faq",
    "blocks": {
        "q1": {"type": "faq", "settings": {
            "question": "What is the PLIT's maximum load?",
            "answer": "<p>The PLIT supports up to 125 kg.</p>"}},
        "q2": {"type": "faq", "settings": {
            "question": "Can the seat be washed?",
            "answer": "<p>Yes - remove the seat, take off the cover and wash it gently in lukewarm water at 40 degrees or below. A laundry net is recommended in the machine.</p>"}},
        "q3": {"type": "faq", "settings": {
            "question": "The chair does not slide easily - is that normal?",
            "answer": "<p>Yes - the rear legs use silicone glides for a steady hold while seated. For a smoother slide, fit the felt glides included in the box.</p>"}},
    },
    "block_order": ["q1", "q2", "q3"],
    "settings": {"heading": "Frequently asked questions", "open_first": True, "background": "#f5f6f7"},
}

S["reviews"] = copy.deepcopy(B["reviews"])

S["stockists"] = {
    "type": "sidiz-store-info",
    "settings": {
        "heading": "Try one before you decide",
        "description": "Seat feel differs from body to body. Try a PLIT in person where you can; otherwise our returns policy is there to fall back on.",
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
    "sticky_nav", "pdp_head", "hero", "styling_tiles",
    "care_banner", "care_cards", "structure_banner", "structure_cards",
    "parts_banner", "parts_cards", "diy_view",
    "goes_with", "warranty", "specifications", "safety_info", "faq",
    "reviews", "stockists", "recommend", "notices",
]
assert set(order) == set(S), set(order) ^ set(S)

out = ROOT / "theme/templates/product.plit.json"
out.write_text(json.dumps({"sections": S, "order": order}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print("written", out.name, "sections:", len(order))
