"""Compose product.trevo.json.

TREVO is the living-room growing high chair: intro H1 row, video hero, an
image-backed light scroll banner over a DARK four-card list, the switchable
easy-growing view (one KR block is text-only), care tiles (the Korean
supplier-conformity certification stated as such), and the four-model kids
chair finder (two KR two-column rows folded into one tile list). KR user
reviews are skipped (ACL).
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
    "n1": {"type": "link", "settings": {"label": "Living study", "anchor": "living"}},
    "n2": {"type": "link", "settings": {"label": "Easy growing", "anchor": "growing"}},
    "n3": {"type": "link", "settings": {"label": "Care and safety", "anchor": "care"}},
    "n4": {"type": "link", "settings": {"label": "Which chair?", "anchor": "finder"}},
    "n5": {"type": "link", "settings": {"label": "Specifications", "anchor": "specifications"}},
    "n6": {"type": "link", "settings": {"label": "FAQ", "anchor": "faq"}},
}
S["sticky_nav"]["block_order"] = ["n1", "n2", "n3", "n4", "n5", "n6"]

S["pdp_head"] = copy.deepcopy(B["pdp_head"])
S["pdp_head"]["blocks"]["i1"]["settings"]["value"] = "SIDIZ TREVO Growing High Chair"
S["pdp_head"]["blocks"]["i3"]["settings"]["value"] = "Plastic, steel"
S["pdp_head"]["blocks"]["i4"]["settings"]["value"] = "White\nDusty Pink\nDusty Green"
S["pdp_head"]["settings"]["subtitle"] = (
    "The living-room study chair that grows from age five to ten - a switchable body "
    "changes the height with one lever, no tools, and a footrest keeps posture steady."
)

S["intro"] = {
    "type": "sidiz-product-row",
    "settings": {
        "heading": "SIDIZ TREVO Kids Chair for the Living-Room Study and Dining Table",
        "body": (
            "<ul><li><strong>Switchable body</strong> - flip the body with a lever, no "
            "tools, to change the height as your child grows from five to ten.</li>"
            "<li><strong>A steady footrest</strong> - supports the legs, spreads the "
            "load, and stops dangling feet from breaking concentration.</li>"
            "<li><strong>Minimal design, easy upkeep</strong> - a clean look that suits "
            "living and dining spaces, in stain-resistant plastic made for shared "
            "rooms.</li></ul>"
            "<p>A lasting living-room study chair that flexes with your child's growth "
            "at the dining table.</p>"
        ),
        "align": "left",
        "background": "#ffffff",
        "text_colour": "#000000",
    },
}

S["hero"] = {
    "type": "sidiz-pdp-hero",
    "settings": {
        "subtitle": "<em class=\"caps\">My first learning mate</em>",
        "subtitle_colour": "#ffffff",
        "heading": "TREVO",
        "heading_colour": "#ffffff",
        "text_align": "center",
        "header_scheme": "dark",
        "video_url": vid("8920be3d055c4a668ba5a89d990056e2", "HD-1080p-7.2Mbps", "40944855"),
        "poster_url": poster("8920be3d055c4a668ba5a89d990056e2"),
        "video_url_mobile": vid("e75324e3450e4a07a852731e7670ca66", "HD-1080p-7.2Mbps", "40945177"),
        "poster_url_mobile": poster("e75324e3450e4a07a852731e7670ca66"),
        "alt": "A child learning at the table in the SIDIZ TREVO",
        "description": (
            "<p>Where living-and-dining learning with your child begins: the TREVO is a "
            "growth-fitted living-room study chair, made new again each day as your "
            "child grows.</p><p>A first step into good study habits and posture - a "
            "chair that adjusts with growth and lasts, the perfect learning mate for "
            "every moment of discovery.</p>"
        ),
        "description_colour": "#000000",
        "description_align": "left",
        "product_type": "default",
    },
}

S["living_banner"] = {
    "type": "sidiz-wb-scroll-banner",
    "settings": {
        "heading": "",
        "header_scheme": "light",
        "tag": "",
        "subheading": "The habit of focus begins in the living room -<br>a living study, face to face with you",
        "description": (
            "<p>At the age when curious questions turn into learning, a child's first "
            "study space should not be a closed room but the living table, sharing eye "
            "contact with a parent. The TREVO turns the living room into the best "
            "learning-mate space your child could have.</p>"
        ),
        "text_colour": "#000000",
        "image_url": img("Img_284dcf6a-68b6-468d-8119-c895202bffa1.jpg"),
        "image_url_mobile": img("Head_M_aa34ff21-191b-4f91-9b1b-f5906e52d77b.jpg"),
        "alt": "A parent and child learning together at the living table",
    },
}

S["living_cards"] = {
    "type": "sidiz-wb-scroll-card-list",
    "blocks": {
        "c1": {"type": "card", "settings": {
            "title": "Designed to living-table height",
            "title_colour": "#ffffff",
            "description": "<p>SIDIZ's ergonomic fit, built from a precise study of the body balance of children aged five to ten as they read and learn at dining and living tables.</p>",
            "description_colour": "#a4aab0",
            "image_url": img("Img_4_3_3e565934-0068-4a2c-9987-f3cdd5f4e3fc.jpg"),
            "alt": "The TREVO matched to living-table height"}},
        "c2": {"type": "card", "settings": {
            "title": "A slim silhouette that never blocks the view",
            "title_colour": "#ffffff",
            "description": "<p>Dining chair and study chair in one, in a minimal, refined design that soaks into the space without disturbing the interior.</p>",
            "description_colour": "#a4aab0",
            "image_url": img("Img_4_3_2_e7de3b2a-cae2-4f12-be29-c67c2973bde0.jpg"),
            "alt": "The TREVO's slim silhouette at the table"}},
        "c3": {"type": "card", "settings": {
            "title": "A backrest handle hole that adds convenience",
            "title_colour": "#ffffff",
            "description": "<p>A handle hole in the backrest makes the TREVO easy to carry between the spaces it serves.</p>",
            "description_colour": "#a4aab0",
            "video_url": vid("dfcf89ec1ff742cf990dc94311d34a56", "HD-720p-4.5Mbps", "40610319"),
            "poster_url": poster("dfcf89ec1ff742cf990dc94311d34a56"),
            "alt": "Carrying the TREVO by its handle hole"}},
        "c4": {"type": "card", "settings": {
            "title": "A cushioned seat cover, comfortable and easy to keep",
            "title_colour": "#ffffff",
            "description": "<p>Comfortable through long sittings, in neutral colours that warm the room, wrapping the seat as if part of the chair. *Sold separately.</p>",
            "description_colour": "#a4aab0",
            "video_url": vid("beaa882c3dba421b9bf3c99663dcd067", "HD-1080p-7.2Mbps", "65182666"),
            "poster_url": poster("beaa882c3dba421b9bf3c99663dcd067"),
            "alt": "Fitting the TREVO seat cushion cover"}},
    },
    "block_order": ["c1", "c2", "c3", "c4"],
    "settings": {"header_scheme": "dark", "background": "#000000"},
}

S["growing_view"] = {
    "type": "sidiz-product-view-vertical",
    "settings": {
        "heading": "Easy growing, no tools needed",
        "description": (
            "<p>Matched to how fast children grow between five and ten, the TREVO "
            "switches between two modes with a lever alone - no tools - so the fit "
            "stays right and the study posture stays optimal as your child changes. "
            "*HIGH SITTING MODE: ages 5-7, chair and footrest at the higher setting. "
            "*LOW SITTING MODE: ages 8-10, chair and footrest at the lower setting.</p>"
        ),
        "video_url": vid("1a08fa76a636451bb60c8f6c5cdcb63d", "HD-1080p-4.8Mbps", "40945889"),
        "poster_url": poster("1a08fa76a636451bb60c8f6c5cdcb63d"),
        "alt": "The TREVO switching between its two sitting modes",
    },
    "blocks": {
        "b1": {"type": "feature", "settings": {
            "title": "A switchable body that flips front to back",
            "description": "<p>Switch the body forward or back and the height changes - growing made simple.</p>",
            "video_url": vid("fc1d25c9ae6d4284961f0e48904c18e3", "SD-480p-1.5Mbps", "40610430"),
            "poster_url": poster("fc1d25c9ae6d4284961f0e48904c18e3"),
            "alt": "Flipping the TREVO's switchable body"}},
        "b2": {"type": "feature", "settings": {
            "title": "A footrest matched to each mode",
            "description": "<p>The footrest follows the chair's height so a child holds a stable, upright posture in either mode.</p>"}},
        "b3": {"type": "feature", "settings": {
            "title": "HIGH SITTING MODE: ages 5-7",
            "description": "<p>Chair and footrest sit higher for smaller children still growing into the table.</p>",
            "image_url": img("Img123.jpg"),
            "alt": "The TREVO in high sitting mode"}},
        "b4": {"type": "feature", "settings": {
            "title": "LOW SITTING MODE: ages 8-10",
            "description": "<p>Chair and footrest sit lower for school-age children who have grown.</p>",
            "image_url": img("Img234.jpg"),
            "alt": "The TREVO in low sitting mode"}},
    },
    "block_order": ["b1", "b2", "b3", "b4"],
}

S["care_tiles"] = {
    "type": "sidiz-tile-card-list",
    "blocks": {
        "t1": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "A material that shrugs off stains and scratches",
            "description": "<p>Liquids do not soak in and the scratch-resistant plastic holds its finish through the busiest play, keeping upkeep simple.</p>",
            "video_url": vid("e2df630f5f7f40d0be6665b095fd7742", "HD-1080p-7.2Mbps", "40610488"),
            "poster_url": poster("e2df630f5f7f40d0be6665b095fd7742"),
            "alt": "Wiping the TREVO clean"}},
        "t2": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "A removable cover that washes separately",
            "description": "<p>The optional cushion separates into sponge and cover, so the cover washes easily. *Sold separately.</p>",
            "image_url": img("Img124.jpg"),
            "alt": "Removing the TREVO cushion cover"}},
        "t3": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "Soft, rounded curves that prevent knocks",
            "description": "<p>Every element, footrest included, is rounded so curious children stay safe whatever they get up to.</p>",
            "image_url": img("TREVO_03-3.jpg"),
            "alt": "The TREVO's rounded edges"}},
        "t4": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "Certified as a children's product",
            "description": "<p>The TREVO holds Korea's supplier-conformity certification for children's products, issued by an accredited body.</p>",
            "image_url": img("TREVO_03-4.jpg"),
            "alt": "The TREVO's children's product certification"}},
    },
    "block_order": ["t1", "t2", "t3", "t4"],
    "settings": {"heading": "Everyday care made simpler, safety made surer"},
}

S["finder_tiles"] = {
    "type": "sidiz-tile-card-list",
    "blocks": {
        "t1": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "ATTI",
            "description": "<p>For toddlers spending their first hours at a desk, forming posture habits. Recommended: 18 months to age 5.</p>",
            "image_url": img("b2b3269a8d070feac4c2016984845fd9.png"),
            "alt": "The SIDIZ ATTI toddler chair"}},
        "t2": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "TREVO",
            "description": "<p>For children studying with a parent at the living table. Recommended: ages 5-10, height 110-140 cm.</p>",
            "image_url": img("2_1b836bc7-f129-40e4-bdd6-bc2fa64715b1.png"),
            "alt": "The SIDIZ TREVO growing high chair"}},
        "t3": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "RINGO",
            "description": "<p>For primary students beginning self-directed study in their own room. Recommended: age 7 to primary school, height 110-160 cm.</p>",
            "image_url": img("5_9a36585e-be44-4c38-b9c7-03a270f0c9e0.png"),
            "alt": "The SIDIZ RINGO kids chair"}},
        "t4": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "IBLE",
            "description": "<p>For secondary students who need unshakeable focus at the desk. Recommended: secondary school and up, height 160 cm and above.</p>",
            "image_url": img("4_74ebe688-caeb-4f9d-99dc-ecbb22824764.png"),
            "alt": "The SIDIZ IBLE study chair"}},
    },
    "block_order": ["t1", "t2", "t3", "t4"],
    "settings": {"heading": "Find the SIDIZ chair for your child"},
}

S["goes_with"] = {
    "type": "sidiz-related-products",
    "settings": {"heading": "Goes well with the TREVO", "source": "collection", "limit": 4},
}

S["warranty"] = copy.deepcopy(B["warranty"])
S["warranty"]["settings"]["heading"] = "TREVO | 5-year warranty"
S["warranty"]["settings"]["body"] = (
    "<p>So the journey with your TREVO continues, SIDIZ provides a 5-year warranty to "
    "customers who complete product registration. Once your chair arrives, register it "
    "before you forget, for more comfortable years ahead.</p>"
)

S["specifications"] = copy.deepcopy(B["specifications"])
S["specifications"]["settings"]["heading"] = "TREVO dimensions"
S["specifications"]["settings"]["figures"] = "Maximum load 80 kg / product weight approximately 7 kg."
S["specifications"]["blocks"]["d1"]["settings"].update({
    "image_url": img("TREVO_01_59eee42a-2dab-4ba7-bb95-8f8c3a72ad17.jpg"),
    "alt": "Dimension drawing of the SIDIZ TREVO, front elevation"})
S["specifications"]["blocks"]["d2"]["settings"].update({
    "image_url": img("TREVO_02_8727acd4-f384-44eb-9e55-09de526cc96f.jpg"),
    "alt": "Dimension drawing of the SIDIZ TREVO, side elevation"})

S["safety_info"] = {
    "type": "sidiz-safety-info",
    "blocks": {
        "n1": {"type": "note", "settings": {
            "title": "Washing the cushion cover",
            "body": "<p>Wash gently at 40 degrees. No oxygen bleach. Iron between 80 and 120 degrees if needed. No dry cleaning. Dry flat, in the shade.</p>",
            "image_url": img("TREVO_NOTIC.jpg"),
            "alt": "Cushion cover washing guidance"}},
        "n2": {"type": "note", "settings": {
            "title": "Removing stains from the frame",
            "body": "<p>If the frame gets marked during assembly or use, a melamine sponge lifts stains easily. *Rubbing hard can damage the surface.</p>",
            "image_url": img("BLOCK-EGA-NOTICE.jpg"),
            "alt": "Cleaning the TREVO frame"}},
    },
    "block_order": ["n1", "n2"],
    "settings": {"heading": "Care and cautions"},
}

S["faq"] = {
    "type": "sidiz-faq",
    "blocks": {
        "q1": {"type": "faq", "settings": {
            "question": "Up to what age can the TREVO be used?",
            "answer": "<p>The recommended height range is 100 to 140 cm - designed around standard child growth data to suit roughly ages 5 to 10, though every child grows at their own pace.</p>"}},
        "q2": {"type": "faq", "settings": {
            "question": "Can an adult sit in it?",
            "answer": "<p>The TREVO's maximum load is 80 kg - please keep weight in mind when it is used.</p>"}},
        "q3": {"type": "faq", "settings": {
            "question": "Does changing modes need any tools?",
            "answer": "<p>No - the body switches front to back with the lever alone, and the footrest follows the chair's height in each mode.</p>"}},
    },
    "block_order": ["q1", "q2", "q3"],
    "settings": {"heading": "Frequently asked questions", "open_first": True, "background": "#f5f6f7"},
}

S["reviews"] = copy.deepcopy(B["reviews"])

S["stockists"] = {
    "type": "sidiz-store-info",
    "settings": {
        "heading": "Sit in one before you decide",
        "description": "Seat feel differs from child to child. Try a TREVO in person where you can; otherwise our returns policy is there to fall back on.",
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
    "living_banner", "living_cards", "growing_view", "care_tiles",
    "finder_tiles", "goes_with", "warranty", "specifications",
    "safety_info", "faq", "reviews", "stockists", "recommend", "notices",
]
assert set(order) == set(S), set(order) ^ set(S)

out = ROOT / "theme/templates/product.trevo.json"
out.write_text(json.dumps({"sections": S, "order": order}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print("written", out.name, "sections:", len(order))
