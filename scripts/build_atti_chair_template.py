"""Compose product.atti-chair.json.

ATTI is the toddler chair: image hero, a three-colour view, the grow banner,
the two-step height/footrest view, the matching-desk view (desk noted as sold
separately), four safety tiles, and a compact tail. No videos on the KR page.
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
    "n1": {"type": "link", "settings": {"label": "Colours", "anchor": "colours"}},
    "n2": {"type": "link", "settings": {"label": "Posture", "anchor": "posture"}},
    "n3": {"type": "link", "settings": {"label": "ATTI desk", "anchor": "desk"}},
    "n4": {"type": "link", "settings": {"label": "Safety", "anchor": "safety"}},
    "n5": {"type": "link", "settings": {"label": "Specifications", "anchor": "specifications"}},
    "n6": {"type": "link", "settings": {"label": "FAQ", "anchor": "faq"}},
}
S["sticky_nav"]["block_order"] = ["n1", "n2", "n3", "n4", "n5", "n6"]

S["pdp_head"] = copy.deepcopy(B["pdp_head"])
S["pdp_head"]["blocks"]["i1"]["settings"]["value"] = "SIDIZ ATTI Toddler Chair"
S["pdp_head"]["blocks"]["i3"]["settings"]["value"] = "Synthetic leather, moulded foam, plastic"
S["pdp_head"]["blocks"]["i4"]["settings"]["value"] = "Soy Milk\nMellow Peach\nSage Mint"
S["pdp_head"]["blocks"]["f3"] = {"type": "fact", "settings": {
    "label": "Assembly",
    "value": "Simple DIY assembly"}}
S["pdp_head"]["block_order"] = ["f1", "f2", "f3", "i1", "i2", "i3", "i4", "i5"]
S["pdp_head"]["settings"]["subtitle"] = (
    "The first chair for toddlers at their first desk - two-step growing height, side "
    "guards, a footrest and rounded, wipe-clean materials for safe, upright sitting."
)

S["intro"] = {
    "type": "sidiz-product-row",
    "settings": {
        "heading": "SIDIZ ATTI Toddler Chair",
        "body": (
            "<ul><li><strong>Two-step growing height</strong> - a simple re-assembly "
            "changes the height as your child grows, holding a correct sitting posture "
            "throughout.</li>"
            "<li><strong>Side guards and footrest</strong> - guards prevent falls while "
            "little bodies are still finding their balance, and a steady footrest brings "
            "upright posture and a settled feeling at once.</li>"
            "<li><strong>Toddler-safe materials</strong> - rounded corners and easy-wipe "
            "synthetic leather stay safe and hygienic through any kind of play.</li>"
            "<li><strong>Neutral-tone colours</strong> - calm shades that suit the kids' "
            "room and the living room alike.</li></ul>"
            "<p>A chair designed so that good posture habits form naturally from the very "
            "first time your child sits down.</p>"
        ),
        "align": "left",
        "background": "#ffffff",
        "text_colour": "#000000",
    },
}

S["hero"] = {
    "type": "sidiz-pdp-hero",
    "settings": {
        "subtitle": "The first step to sitting well",
        "subtitle_colour": "#ffffff",
        "heading": "ATTI",
        "heading_colour": "#ffffff",
        "text_align": "center",
        "header_scheme": "dark",
        "image_url": img("ATTI_Head_chair.jpg"),
        "image_url_mobile": img("ATTI_Head_chair_M_b4955b76-21ee-475e-9d7d-02bb72a64a69.jpg"),
        "alt": "A toddler sitting upright in the SIDIZ ATTI",
        "description": (
            "<p>The SIDIZ ATTI is a toddler chair designed so that a child sitting at a "
            "desk for the first time learns good posture naturally.</p><p>Two-step height "
            "adjustment follows their growth, a footrest steadies small feet, and rounded "
            "corners, side guards and high-resilience cushioning complete a design built "
            "around toddler safety - so the right posture forms from the first sit.</p>"
        ),
        "description_colour": "#000000",
        "description_align": "left",
        "product_type": "default",
    },
}

S["colours_view"] = {
    "type": "sidiz-product-view",
    "settings": {
        "heading": "Soft, calm neutral colours",
        "description": (
            "<p>Renewed in soft, calm shades that add warmth and settle naturally into "
            "any corner of a child's room.</p>"
        ),
        "image_url": img("ATTI_01_-1_6a5bab8c-acc6-412d-bc27-0c8a9240cd40.jpg"),
        "alt": "The ATTI in its three neutral colours",
    },
    "blocks": {
        "b1": {"type": "feature", "settings": {
            "title": "Soy Milk",
            "image_url": img("ATTI_01-1_e4523865-b612-48b0-8816-cfdaddff6936.jpg"),
            "alt": "The ATTI in Soy Milk"}},
        "b2": {"type": "feature", "settings": {
            "title": "Mellow Peach",
            "image_url": img("ATTI_01-2_61adcc06-efb2-442e-b937-1191c50bce0c.jpg"),
            "alt": "The ATTI in Mellow Peach"}},
        "b3": {"type": "feature", "settings": {
            "title": "Sage Mint",
            "image_url": img("ATTI_01-3_35dd0a16-bb0d-4b93-adf5-f87f9cc373fc.jpg"),
            "alt": "The ATTI in Sage Mint"}},
    },
    "block_order": ["b1", "b2", "b3"],
}

S["grow_banner"] = {
    "type": "sidiz-wb-banner",
    "settings": {
        "heading": "Grow up straight -<br>the child, and the posture",
        "align": "left",
        "title_colour": "#000000",
    },
}

S["posture_view"] = {
    "type": "sidiz-product-view-vertical",
    "settings": {
        "heading": "Height and posture, matched to their growth",
        "description": (
            "<p>With height adjustment that follows your child's growth, the ATTI keeps "
            "sitting steady and posture true.</p>"
        ),
        "image_url": img("ATTI_02-0.jpg"),
        "alt": "The ATTI adjusting with a growing toddler",
    },
    "blocks": {
        "b1": {"type": "feature", "settings": {
            "title": "Two-step height adjustment",
            "description": "<p>A simple re-assembly changes the height with your child's growth, so one chair stays with them for years.</p>",
            "image_url": img("ATTI_02-1-0.jpg"),
            "alt": "The ATTI's two height settings"}},
        "b2": {"type": "feature", "settings": {
            "title": "A footrest that builds good posture",
            "description": "<p>A steady place to rest small feet brings upright posture and a sense of security together.</p>",
            "image_url": img("ATTI_02-2_430e7d59-ddcc-4e90-bb43-904af1ea4507.jpg"),
            "alt": "A toddler's feet on the ATTI footrest"}},
    },
    "block_order": ["b1", "b2"],
}

S["desk_view"] = {
    "type": "sidiz-product-view",
    "settings": {
        "tag": "Sold separately",
        "heading": "The ATTI desk, designed alongside from the start",
        "description": (
            "<p>Made to match the ATTI chair, the ATTI desk completes the set - and its "
            "own two-step height adjustment keeps it useful as your child grows. Chair "
            "and desk both rise 40 mm between steps. *Desk sold separately.</p>"
        ),
        "image_url": img("ATTI_03-0.jpg"),
        "alt": "The ATTI chair and desk together",
    },
    "blocks": {
        "b1": {"type": "feature", "settings": {
            "title": "Step 1: from 18 months",
            "image_url": img("ATTI_03-1_565bcdf8-c06e-456a-9272-9daf0f83e048.jpg"),
            "alt": "The ATTI set at step one"}},
        "b2": {"type": "feature", "settings": {
            "title": "Step 2: from 40 months",
            "description": "<p>Chair and desk both rise 40 mm.</p>",
            "image_url": img("ATTI_03-2_7866facf-6c5d-4a3b-9211-55e128ac996b.jpg"),
            "alt": "The ATTI set at step two"}},
    },
    "block_order": ["b1", "b2"],
}

S["safety_tiles"] = {
    "type": "sidiz-tile-card-list",
    "blocks": {
        "t1": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "Plush back and seat cushions",
            "description": "<p>Thick, high-resilience sponge holds safety and comfort in the same seat.</p>",
            "image_url": img("ATTI_1_1__01_736565b3-2f5d-472e-8fd9-e4e1da3be442.jpg"),
            "alt": "The ATTI's cushioned back and seat"}},
        "t2": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "Rounded, cornerless design",
            "description": "<p>With no hard corners anywhere, a bump never has to mean an injury.</p>",
            "image_url": img("ATTI_1_1__02_b7d2f317-ed98-47bc-994b-2f62b5e56ef8.jpg"),
            "alt": "The ATTI's rounded edges"}},
        "t3": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "Side guards for little ones",
            "description": "<p>Guards on both sides support children who are still finding their balance.</p>",
            "image_url": img("ATTI_1_1__03_4efc68cc-882d-4268-844d-d038092b09ed.jpg"),
            "alt": "The ATTI's side guards"}},
        "t4": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "Stain-resistant synthetic leather",
            "description": "<p>Food and spills wipe straight off the synthetic leather surface.</p>",
            "image_url": img("ATTI_1_1__04_fc2fe51c-76cc-487e-90e8-5d86168e594d.jpg"),
            "alt": "Wiping the ATTI clean"}},
    },
    "block_order": ["t1", "t2", "t3", "t4"],
    "settings": {"heading": "Safety designed first, whatever the play"},
}

S["goes_with"] = {
    "type": "sidiz-related-products",
    "settings": {"heading": "Goes well with the ATTI", "source": "collection", "limit": 4},
}

S["easy_repair"] = copy.deepcopy(B["easy_repair"])
S["easy_repair"]["settings"]["heading"] = "ATTI | EASY REPAIR"
S["easy_repair"]["settings"]["subtitle"] = "Repair it, keep it longer"
S["easy_repair"]["settings"]["description"] = (
    "<p>Buy just the part you need - like the ATTI height-extension block - and keep "
    "the chair growing with your child.</p>"
)

S["warranty"] = copy.deepcopy(B["warranty"])
S["warranty"]["settings"]["heading"] = "ATTI | 5-year warranty"
S["warranty"]["settings"]["body"] = (
    "<p>So the journey with your ATTI continues, SIDIZ provides a 5-year warranty to "
    "customers who complete product registration. Once your chair arrives, register it "
    "before you forget, for more comfortable years ahead.</p>"
)

S["specifications"] = copy.deepcopy(B["specifications"])
S["specifications"]["settings"]["heading"] = "ATTI dimensions"
S["specifications"]["settings"]["figures"] = "Product weight approximately 2.9 kg."
S["specifications"]["settings"]["caveats"] = (
    "*Measurements may vary by plus or minus 20 mm and 1 kg depending on where and how "
    "they are taken; this is not a fault.<br>*Dimensions are measured with nobody seated."
)
S["specifications"]["blocks"]["d1"]["settings"].update({
    "image_url": img("K301F_01_b43c9431-a7f2-4f8d-b3dc-53112c6ff56c.jpg"),
    "alt": "Dimension drawing of the SIDIZ ATTI, front elevation"})
S["specifications"]["blocks"]["d2"]["settings"].update({
    "image_url": img("K301F_02_830f7c8c-60c3-448e-8314-472177b2be41.jpg"),
    "alt": "Dimension drawing of the SIDIZ ATTI, side elevation"})

S["faq"] = {
    "type": "sidiz-faq",
    "blocks": {
        "q1": {"type": "faq", "settings": {
            "question": "Up to what age can the ATTI be used?",
            "answer": "<p>The recommended range is 18 months to age 5, though every child grows at their own pace.</p>"}},
        "q2": {"type": "faq", "settings": {
            "question": "Does it need assembly?",
            "answer": "<p>Yes - the ATTI chair and desk are simple DIY products you assemble yourself.</p>"}},
    },
    "block_order": ["q1", "q2"],
    "settings": {"heading": "Frequently asked questions", "open_first": True, "background": "#f5f6f7"},
}

S["reviews"] = copy.deepcopy(B["reviews"])

S["stockists"] = {
    "type": "sidiz-store-info",
    "settings": {
        "heading": "Sit in one before you decide",
        "description": "Seat feel differs from child to child. Try an ATTI in person where you can; otherwise our returns policy is there to fall back on.",
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
    "sticky_nav", "pdp_head", "intro", "hero",
    "colours_view", "grow_banner", "posture_view", "desk_view",
    "safety_tiles", "goes_with", "easy_repair", "warranty",
    "specifications", "faq", "reviews", "stockists", "recommend", "notices",
]
assert set(order) == set(S), set(order) ^ set(S)

out = ROOT / "theme/templates/product.atti-chair.json"
out.write_text(json.dumps({"sections": S, "order": order}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print("written", out.name, "sections:", len(order))
