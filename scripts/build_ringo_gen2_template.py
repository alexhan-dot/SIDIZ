"""Compose product.ringo-gen2.json.

RINGO Gen2 is the growing kids chair: intro H1 row, video hero, two light
scroll banners (one image-backed, one video) each followed by a card list -
KR ships several cards and one tile TEXT-ONLY, which is replicated. The 2WAY
growing patent stays attributed as a Korean patent, and the KC children's
safety certification is stated as the Korean certification it is. KR user
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
    "n1": {"type": "link", "settings": {"label": "Growing", "anchor": "growing"}},
    "n2": {"type": "link", "settings": {"label": "Posture", "anchor": "posture"}},
    "n3": {"type": "link", "settings": {"label": "Safety", "anchor": "safety"}},
    "n4": {"type": "link", "settings": {"label": "Easy Repair", "anchor": "easy-repair"}},
    "n5": {"type": "link", "settings": {"label": "Gen 1 vs Gen 2", "anchor": "compare"}},
    "n6": {"type": "link", "settings": {"label": "Specifications", "anchor": "specifications"}},
    "n7": {"type": "link", "settings": {"label": "FAQ", "anchor": "faq"}},
}
S["sticky_nav"]["block_order"] = ["n1", "n2", "n3", "n4", "n5", "n6", "n7"]

S["pdp_head"] = copy.deepcopy(B["pdp_head"])
S["pdp_head"]["blocks"]["i1"]["settings"]["value"] = "SIDIZ RINGO gen2 Growing Kids Chair"
S["pdp_head"]["blocks"]["i3"]["settings"]["value"] = "Synthetic leather, fabric, moulded foam, plastic, steel"
S["pdp_head"]["blocks"]["i4"]["settings"]["value"] = "Greyish Beige\nGreyish Green\nGreyish Pink"
S["pdp_head"]["settings"]["subtitle"] = (
    "The growing chair for primary schoolers: backrest and seat adjust together in "
    "four stages as your child grows, with a dedicated footrest for steady posture."
)

S["intro"] = {
    "type": "sidiz-product-row",
    "settings": {
        "heading": "SIDIZ RINGO Growing Chair for Primary Schoolers",
        "body": (
            "<ul><li><strong>Hidden-button growing adjustment</strong> - children adjust "
            "the backrest height and seat depth themselves, across four stages.</li>"
            "<li><strong>A dedicated footrest for the lower body</strong> - supports the "
            "legs steadily and guides upright posture.</li>"
            "<li><strong>Rounded form design</strong> - a softly curved frame throughout "
            "removes the hazards of hard corners.</li></ul>"
            "<p>An ergonomic growing solution: a mechanism matched to each stage of "
            "childhood builds straight posture and settled focus for learning.</p>"
        ),
        "align": "left",
        "background": "#ffffff",
        "text_colour": "#000000",
    },
}

S["hero"] = {
    "type": "sidiz-pdp-hero",
    "settings": {
        "subtitle": "<em class=\"caps\">Dream to grow</em>",
        "subtitle_colour": "#ffffff",
        "heading": "RINGO",
        "heading_colour": "#ffffff",
        "text_align": "center",
        "header_scheme": "dark",
        "video_url": vid("18bc780b16ae4e9982b3a4e02f9807cb", "HD-1080p-4.8Mbps", "40951610"),
        "poster_url": poster("18bc780b16ae4e9982b3a4e02f9807cb"),
        "video_url_mobile": vid("b67a41864418473bb90f6f7c2ad987ee", "HD-1080p-4.8Mbps", "40951608"),
        "poster_url_mobile": poster("b67a41864418473bb90f6f7c2ad987ee"),
        "alt": "A child growing with the SIDIZ RINGO chair",
        "description": (
            "<p>A child's growth is more than physical change - it is a journey toward "
            "limitless possibility. The SIDIZ RINGO supports both the changing body and "
            "the expanding mind, staying alongside every moment of finding their own "
            "path.</p><p>A growing mechanism optimises the backrest and seat together at "
            "each stage of childhood, bringing straight posture, settled comfort and the "
            "best environment for learning to take hold.</p>"
        ),
        "description_colour": "#000000",
        "description_align": "left",
        "product_type": "default",
    },
}

S["growing_banner"] = {
    "type": "sidiz-wb-scroll-banner",
    "settings": {
        "heading": "",
        "header_scheme": "light",
        "tag": "",
        "subheading": "From the first day of primary school to the last,<br>posture held true as they grow",
        "description": (
            "<p>Designed from close observation of how children grow, the RINGO keeps a "
            "child comfortably immersed through every moment the body and mind expand.</p>"
        ),
        "text_colour": "#000000",
        "image_url": img("Group_1000006327_fc6d763c-f916-43c2-99d3-5a3a79f571af.jpg"),
        "image_url_mobile": img("RINGO2_M_64bf61f1-215c-43af-ad7e-8d16d3b69356.jpg"),
        "alt": "The RINGO adjusting through the primary years",
    },
}

S["growing_cards"] = {
    "type": "sidiz-wb-card-list",
    "blocks": {
        "c1": {"type": "card", "settings": {
            "title": "2WAY growing: backrest and seat together",
            "title_colour": "#000000",
            "description": "<p>Backrest height and seat depth extend together along a 25 degree diagonal, supporting a growing child naturally - SIDIZ's own 2way growing. *Korean Patent No. 10-2014-0094938.</p>",
            "description_colour": "#7c8084",
            "video_url": vid("cffe9eb0747642d7a0ffdedaaec421ed", "SD-480p-1.5Mbps", "40611002"),
            "poster_url": poster("cffe9eb0747642d7a0ffdedaaec421ed"),
            "alt": "The 2WAY growing mechanism extending"}},
        "c2": {"type": "card", "settings": {
            "title": "Four growing stages, junior years to senior",
            "title_colour": "#000000",
            "description": "<p>Adjusts with each stage of growth for a closer, more comfortable fit. Stage 1: 110-125 cm. Stage 2: 125-135 cm. Stage 3: 135-150 cm. Stage 4: 150-160 cm.</p>",
            "description_colour": "#7c8084"}},
        "c3": {"type": "card", "settings": {
            "title": "A one-touch hidden growing button children use safely",
            "title_colour": "#000000",
            "description": "<p>Tucked inside the handle, the growing button lets a child find the fit that suits them - and keeps the diagonal growing motion at its most natural.</p>",
            "description_colour": "#7c8084"}},
    },
    "block_order": ["c1", "c2", "c3"],
    "settings": {"heading": ""},
}

S["posture_banner"] = {
    "type": "sidiz-wb-scroll-banner",
    "settings": {
        "heading": "",
        "header_scheme": "light",
        "tag": "",
        "subheading": "Straight posture from precise support -<br>the solid basics behind every achievement",
        "description": (
            "<p>Every kind of growth starts from the basics, and straight posture is the "
            "steady starting point for creativity and imagination. Backrest and footrest "
            "support with height adjustment lay the foundation - the possibilities go on "
            "from there.</p>"
        ),
        "text_colour": "#000000",
        "video_url": vid("0675e0dc7ab44898ab4e3209b0e2b5ed", "HD-1080p-4.8Mbps", "40951798"),
        "poster_url": poster("0675e0dc7ab44898ab4e3209b0e2b5ed"),
        "video_url_mobile": vid("5ba22d5763294d14be24adfc1feeb4f8", "HD-1080p-4.8Mbps", "40951797"),
        "poster_url_mobile": poster("5ba22d5763294d14be24adfc1feeb4f8"),
        "alt": "A child sitting upright in the RINGO",
    },
}

S["posture_cards"] = {
    "type": "sidiz-wb-card-list",
    "blocks": {
        "c1": {"type": "card", "settings": {
            "title": "Precise height adjustment for each growth stage",
            "title_colour": "#000000",
            "description": "<p>Comfortable posture depends on where the elbows and shoulders sit; the button sets the right height against the desk.</p>",
            "description_colour": "#7c8084"}},
        "c2": {"type": "card", "settings": {
            "title": "A dedicated footrest for steady legs and a settled mind",
            "title_colour": "#000000",
            "description": "<p>When the chair is raised to the desk and small feet cannot reach the floor, the footrest carries the legs so posture stays stable and upright.</p>",
            "description_colour": "#7c8084",
            "image_url": img("dsc7203.png"),
            "alt": "A child's feet resting on the RINGO footrest"}},
        "c3": {"type": "card", "settings": {
            "title": "A rounded backrest that hugs without fidgeting",
            "title_colour": "#000000",
            "description": "<p>Firm and generously padded, the backrest supports the lower back naturally so long stretches of focus stay comfortable.</p>",
            "description_colour": "#7c8084",
            "image_url": img("DSC7130.png"),
            "alt": "The rounded RINGO backrest"}},
    },
    "block_order": ["c1", "c2", "c3"],
    "settings": {"heading": ""},
}

S["safety_tiles"] = {
    "type": "sidiz-tile-card-list",
    "blocks": {
        "t1": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "Materials certified safe for children",
            "description": "<p>The RINGO is certified under Korea's Children's Product Safety Special Act (KC), which tests for hazardous substances and safe form.</p>",
            "image_url": img("RINGO2__1_1__01_493b1080-30cf-4fe2-b611-97f7014d0cf3.jpg"),
            "alt": "The RINGO's certified-safe materials"}},
        "t2": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "A rounded frame with nothing protruding",
            "description": "<p>Protruding levers are removed and every corner rounded, so an active child uses the chair safely.</p>",
            "image_url": img("DSC7269_d61ebf65-4fec-4a1f-b95d-d178236bdb96.png"),
            "alt": "The rounded, lever-free frame"}},
        "t3": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "A fixed column that curbs restlessness",
            "description": "<p>The column does not swivel, helping a child settle into focus naturally.</p>",
            "image_url": img("RINGO2_03-3.jpg"),
            "alt": "The fixed, non-swivel column"}},
        "t4": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "Durable synthetic leather that wipes clean",
            "description": "<p>Spills and food marks wipe away easily, keeping everyday mess hygienic to manage.</p>",
            "alt": "The wipe-clean synthetic leather"}},
        "t5": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "Sit-brake castors, sold separately",
            "description": "<p>Castors that resist rolling under a seated child's weight can be purchased separately and swapped in to match study habits.</p>",
            "image_url": img("RINGO2__1_1__05.jpg"),
            "alt": "Sit-brake castors on the RINGO"}},
        "t6": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "A removable fabric cover, always like new",
            "description": "<p>A washable cover protects the chair from stains and clips on and off easily.</p>",
            "image_url": img("RINGO2_03-6_01ee5875-5fc2-4c6d-a025-2c55f790b969.jpg"),
            "alt": "Removing the RINGO fabric cover"}},
    },
    "block_order": ["t1", "t2", "t3", "t4", "t5", "t6"],
    "settings": {"heading": "The details behind a children's chair"},
}

S["repair_view"] = {
    "type": "sidiz-product-view-vertical",
    "settings": {
        "heading": "Easy Repair: like new, for years",
        "description": (
            "<p>The RINGO is designed so that only the parts that naturally wear are "
            "replaced - economical long use, with the chair feeling new again each "
            "time.</p>"
        ),
        "image_url": img("RINGO2.jpg"),
        "alt": "The RINGO's replaceable parts",
    },
    "blocks": {
        "b1": {"type": "feature", "settings": {
            "title": "An easy-care seat that swaps without tools",
            "description": "<p>The seat fastens with a snap fit, so it detaches and replaces the moment it stains - no tools needed.</p>",
            "video_url": vid("83fd851c93704cf19addf88e1de510fc", "SD-480p-0.9Mbps", "40953278"),
            "poster_url": poster("83fd851c93704cf19addf88e1de510fc"),
            "alt": "Snapping the RINGO seat off"}},
        "b2": {"type": "feature", "settings": {
            "title": "A backrest that swaps with a single bolt",
            "description": "<p>One bolt releases and refits the backrest, keeping it in like-new condition.</p>"}},
        "b3": {"type": "feature", "settings": {
            "title": "A footrest that detaches as they grow",
            "description": "<p>When your child outgrows the footrest, remove the bolts and take it off. *Chairs ship with either of two fastening designs; assembly differs slightly but performance and quality are identical.</p>"}},
        "b4": {"type": "feature", "settings": {
            "title": "Castors that swap with the supplied spanner",
            "description": "<p>Castors bought separately come with a dedicated spanner for easy removal and refitting.</p>"}},
    },
    "block_order": ["b1", "b2", "b3", "b4"],
}

S["compare_tiles"] = {
    "type": "sidiz-tile-card-list",
    "blocks": {
        "t1": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "Reinforced back and seat layers that hold posture",
            "description": "<p>Where generation 1 was slim and sleek, generation 2 adds 25 mm to the backrest and 20 mm to the seat for a gentler, steadier sit.</p>",
            "image_url": img("RINGO2_05-1.jpg"),
            "alt": "Generation 1 and 2 backrests compared"}},
        "t2": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "Premium tone-on-tone colours for the room",
            "description": "<p>From generation 1's bright, imagination-sparking colours to generation 2's neutral palette that completes a considered kids' room.</p>",
            "alt": "The generation 2 tone-on-tone palette"}},
        "t3": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "Generation 1: the intuitive lever",
            "description": "<p>An easy-to-grip, protruding lever made adjustment obvious.</p>",
            "image_url": img("RINGO2_05-2.jpg"),
            "alt": "The generation 1 adjustment lever"}},
        "t4": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "Generation 2: the hidden growing button",
            "description": "<p>Recessing the control removes the protrusion - preventing knocks and completing a clean, simple exterior.</p>",
            "image_url": img("RINGO2_05-3.jpg"),
            "alt": "The recessed generation 2 growing button"}},
        "t5": {"type": "tile", "settings": {
            "ratio": "4/5",
            "title": "Easy self-care, tools not required",
            "description": "<p>The seat snaps off and the backrest releases with one bolt, so worn parts swap easily and the chair keeps its first-day condition.</p>",
            "video_url": vid("b6b32917b3e54142853dcf8c21ea101c", "HD-720p-1.6Mbps", "40945621"),
            "poster_url": poster("b6b32917b3e54142853dcf8c21ea101c"),
            "alt": "Swapping RINGO parts by hand"}},
    },
    "block_order": ["t1", "t2", "t3", "t4", "t5"],
    "settings": {"heading": "Adjustment to upkeep: the leap past generation 1"},
}

S["goes_with"] = {
    "type": "sidiz-related-products",
    "settings": {"heading": "Goes well with the RINGO", "source": "collection", "limit": 4},
}

S["easy_repair"] = copy.deepcopy(B["easy_repair"])
S["easy_repair"]["settings"]["heading"] = "RINGO | EASY REPAIR"
S["easy_repair"]["settings"]["subtitle"] = "Repair it, keep it longer"
S["easy_repair"]["settings"]["description"] = (
    "<p>Even after long use, buy just the part you need and swap it in to keep the chair "
    "like new.</p>"
)

S["warranty"] = copy.deepcopy(B["warranty"])
S["warranty"]["settings"]["heading"] = "RINGO | 5-year warranty"
S["warranty"]["settings"]["body"] = (
    "<p>So the journey with your RINGO continues, SIDIZ provides a 5-year warranty to "
    "customers who complete product registration. Once your chair arrives, register it "
    "before you forget, for more comfortable years ahead.</p>"
)

S["specifications"] = copy.deepcopy(B["specifications"])
S["specifications"]["settings"]["heading"] = "RINGO dimensions"
S["specifications"]["settings"]["figures"] = "Maximum load 100 kg / product weight approximately 11 kg."
S["specifications"]["blocks"]["d1"]["settings"].update({
    "image_url": img("ringo_2__01_73d328a2-2024-436e-a1a7-c8e15c91bf03.jpg"),
    "alt": "Dimension drawing of the SIDIZ RINGO gen2, front elevation"})
S["specifications"]["blocks"]["d2"]["settings"].update({
    "image_url": img("ringo_2__02_632cc804-385a-43ed-83d2-173910e99fca.jpg"),
    "alt": "Dimension drawing of the SIDIZ RINGO gen2, side elevation"})

S["safety_info"] = {
    "type": "sidiz-safety-info",
    "blocks": {
        "n1": {"type": "note", "settings": {
            "title": "Check the footrest direction before assembly",
            "body": "<p>Assemble with the front of the chair body facing the footrest. Rotating the body after the fixed column is assembled can cause damage.</p>",
            "image_url": img("RINGO-2-NOTICE.jpg"),
            "alt": "The correct footrest assembly direction"}},
        "n2": {"type": "note", "settings": {
            "title": "Washing the fabric cover",
            "body": "<p>Wash gently at 40 degrees. No oxygen bleach. Iron between 80 and 120 degrees if needed. No dry cleaning. Dry flat, in the shade.</p>",
            "image_url": img("TREVO_NOTIC.jpg"),
            "alt": "Fabric cover washing guidance"}},
        "n3": {"type": "note", "settings": {
            "title": "Removing stains from the frame",
            "body": "<p>If the frame gets marked, a melamine sponge lifts stains easily. *Rubbing hard can damage the surface.</p>",
            "image_url": img("BLOCK-RING-NOTICE.jpg"),
            "alt": "Cleaning the RINGO frame"}},
    },
    "block_order": ["n1", "n2", "n3"],
    "settings": {"heading": "Care and cautions"},
}

S["faq"] = {
    "type": "sidiz-faq",
    "blocks": {
        "q1": {"type": "faq", "settings": {
            "question": "Up to what age can the RINGO gen2 be used?",
            "answer": "<p>The recommended height range is 110 to 160 cm - designed around standard child growth data to suit roughly ages 6 to 13, though every child grows at their own pace.</p>"}},
        "q2": {"type": "faq", "settings": {
            "question": "At what height is the footrest recommended?",
            "answer": "<p>From 110 to 140 cm. Standing on the footrest can roll or tip the chair - please supervise so it is used safely.</p>"}},
        "q3": {"type": "faq", "settings": {
            "question": "Is there a castor that both rolls and holds?",
            "answer": "<p>Yes - sit-brake castors resist rolling once a sitter over 25 kg is seated, and are sold separately on sidiz.au.</p>"}},
        "q4": {"type": "faq", "settings": {
            "question": "Any tips for keeping it like new?",
            "answer": "<p>The synthetic leather wipes clean easily; with persistent staining, the backrest and seat can be replaced. A washable fabric cover is also sold separately.</p>"}},
        "q5": {"type": "faq", "settings": {
            "question": "The column rotates - is that a fault?",
            "answer": "<p>First, sit in the chair and load it fully so the column and body seat together; after assembly, avoid forcing the chair to rotate. A chair forced around once will turn more easily afterwards.</p>"}},
    },
    "block_order": ["q1", "q2", "q3", "q4", "q5"],
    "settings": {"heading": "Frequently asked questions", "open_first": True, "background": "#f5f6f7"},
}

S["reviews"] = copy.deepcopy(B["reviews"])

S["stockists"] = {
    "type": "sidiz-store-info",
    "settings": {
        "heading": "Sit in one before you decide",
        "description": "Seat feel differs from child to child. Try a RINGO in person where you can; otherwise our returns policy is there to fall back on.",
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
    "growing_banner", "growing_cards", "posture_banner", "posture_cards",
    "safety_tiles", "repair_view", "compare_tiles",
    "goes_with", "easy_repair", "warranty", "specifications",
    "safety_info", "faq", "reviews", "stockists", "recommend", "notices",
]
assert set(order) == set(S), set(order) ^ set(S)

out = ROOT / "theme/templates/product.ringo-gen2.json"
out.write_text(json.dumps({"sections": S, "order": order}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print("written", out.name, "sections:", len(order))
