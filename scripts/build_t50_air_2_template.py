"""Derive product.t50-air-2.json from product.t50-2.json.

The two KR pages share their skeleton; the AIR deltas are the full-mesh
horizontal view, mesh-headrest wording, a single ergonomics block, two detail
tiles, and AIR-specific hero/intro/compare/spec content.
"""

import copy
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
KR = "https://kr.sidiz.com/cdn/shop"


def vid(id_, n, variant="HD-1080p-7.2Mbps"):
    return f"{KR}/videos/c/vp/{id_}/{id_}.{variant}-{n}.mp4"


def poster(id_):
    return f"{KR}/files/preview_images/{id_}.thumbnail.0000000000_small.jpg"


base = json.loads((ROOT / "theme/templates/product.t50-2.json").read_text(encoding="utf-8"))
t = copy.deepcopy(base)
S = t["sections"]

S["pdp_head"]["blocks"]["i1"]["settings"]["value"] = "SIDIZ T50 AIR 2nd Generation Ergonomic Full-Mesh Office Chair"
S["pdp_head"]["blocks"]["i3"]["settings"]["value"] = "Airflex mesh, plastic, steel"
S["pdp_head"]["settings"]["subtitle"] = (
    "The precision fitting of the new T50 with high-resilience Airflex mesh "
    "across the seat and backrest - firm support and fresh coolness through the longest days."
)

S["hero"]["settings"].update({
    "subtitle": "<em class=\"caps\">The Airy Standard</em><br>Rewriting what a mesh chair should be",
    "heading": "T50 AIR 2nd Generation",
    "alt": "SIDIZ T50 AIR 2nd Generation full-mesh office chair in motion",
    "description": (
        "<p>The T50 AIR analyses the real usage data and reviews of three million sitters, "
        "adding an overwhelming coolness to precise personal fitting. High-stiffness Airflex "
        "mesh runs across the whole chair, seat included, circulating body heat and sweat in "
        "real time.</p><p>Through long hours of focus, it holds firm support and crisp "
        "freshness at once - comfortable in every season.</p>"
    ),
})

S["intro"]["settings"]["heading"] = "SIDIZ T50 AIR 2nd Generation Ergonomic Office Computer Mesh Chair"
S["intro"]["settings"]["body"] = (
    "<p><strong>Custom Mechanism Airy Full Mesh Chair</strong> - built on the real usage data "
    "of three million sitters, with the subtle discomforts and play of the old design "
    "engineered out, and high-stiffness Airflex mesh from backrest to seat for all-day "
    "coolness with a firm, tailored fit: SIDIZ's premium full-mesh office chair.</p>"
    "<ul><li><strong>Wide Mesh Headrest &amp; 2D Lumbar Support</strong> - a 310 mm wide mesh "
    "headrest that cradles the nape through frequent posture changes, and a lumbar support "
    "with the pressure-point feel and slip-down fully resolved, meeting the lumbar curve with "
    "precise 50 mm height and 10 mm depth adjustment.</li>"
    "<li><strong>Airflex Full Mesh Seat &amp; 4D Waterfall Armrest</strong> - a "
    "high-resilience mesh seat that circulates body heat and sweat in real time, "
    "interchangeable with the fabric seat and self-replaceable through Easy Repair, plus "
    "waterfall armrests raised 25 mm at base height with 4D fine adjustment to ease shoulder "
    "fatigue.</li>"
    "<li><strong>Synchronised &amp; 5-Step Limited Tilting</strong> - sync tilt that keeps "
    "the back in contact as you recline, with a 105-130 degree five-step range and fine "
    "tension control that protects the lumbar.</li></ul>"
    "<p>Optimised for offices, home offices and studies - everywhere long sitting cycles "
    "between focus and rest, and a plain chair's limits show on a hot day.</p>"
)

S["full_mesh"] = {
    "type": "sidiz-product-view",
    "settings": {
        "heading": "Full mesh, from backrest to seat",
        "description": (
            "<p>Mesh across the whole chair cools trapped sweat and heat fast and keeps you "
            "fresh. A structure that maximises airflow keeps sitting cool and comfortable all "
            "day, all year round.</p>"
        ),
        "video_url": vid("24a0efbf1d8843bcb907653feef49d32", "76611715"),
        "poster_url": poster("24a0efbf1d8843bcb907653feef49d32"),
        "alt": "Airflex mesh flexing across the T50 AIR seat and backrest",
    },
    "blocks": {
        "b1": {"type": "feature", "settings": {
            "title": "Airflex Mesh",
            "description": (
                "<p>A special mesh weave with outstanding stiffness and resilient recovery "
                "holds its shape through years of use, supporting the hips and the whole back "
                "firmly yet flexibly for balanced ergonomic support.</p>"
            ),
            "image_url": f"{KR}/files/Img2_f746652c-719b-4616-9a41-6d5f36fc68e0.jpg",
            "alt": "Close view of the Airflex mesh weave"}},
        "b2": {"type": "feature", "settings": {
            "title": "Durable Design",
            "description": (
                "<p>Passing the strict BIFMA test standards, it supports loads up to 125 kg "
                "with outstanding durability. If a part wears, buy just the seat and swap it "
                "yourself for years of worry-free use.</p>"
            ),
            "image_url": f"{KR}/files/Img3_311d07fd-09dc-411a-b8e0-e628f395da27.jpg",
            "alt": "T50 AIR seat structure built for durability"}},
    },
    "block_order": ["b1", "b2"],
}

S["headrest"]["blocks"]["b1"]["settings"].update({
    "title": "Mesh headrest",
    "description": (
        "<p>Mesh on the headrest too releases heat easily over long sittings, staying fresh "
        "and cool, while a generously sized surface supports the neck and head steadily "
        "through any posture or movement.</p>"
    ),
})

S["ergonomics"]["settings"]["description"] = (
    "<p>The essence of a good chair is holding any build straight, without a hint of "
    "strangeness. For long hours of work and focus, the design follows the body's curves "
    "precisely - wrapping spine and pelvis softly from the moment you sit and keeping "
    "pressure minimal through every change of posture.</p>"
)
del S["ergonomics"]["blocks"]["b2"]
S["ergonomics"]["block_order"] = ["b1"]

S["tilt"]["blocks"]["b2"]["settings"].update({
    "video_url": vid("2fc6ac7be44d4a78bf9feaaf4b7d224f", "88202556"),
    "poster_url": poster("2fc6ac7be44d4a78bf9feaaf4b7d224f"),
})

del S["detail_tiles"]["blocks"]["t1"]
S["detail_tiles"]["block_order"] = ["t2", "t3"]

S["compare_banner"]["settings"]["heading"] = "T50 AIR 2nd Generation &amp; 1st Generation at a glance"
S["compare_tables"]["blocks"]["m1"]["settings"].update({
    "image_url": f"{KR}/files/T501_T502_Air_web-1_8cb862be-33f6-4d22-95fe-b2d096dbfc34.png",
    "alt": "Comparison table of the T50 AIR 2nd and 1st Generation, part one"})
S["compare_tables"]["blocks"]["m2"]["settings"].update({
    "image_url": f"{KR}/files/T502_T501_Air_web-2_7f730434-1777-4ffb-96a5-e9c69b46fbe2.png",
    "alt": "Comparison table of the T50 AIR 2nd and 1st Generation, part two"})

S["find_your_fit"]["settings"]["heading"] = "T50 AIR 2nd Generation adjustment guide"
S["easy_repair"]["settings"]["heading"] = "T50 AIR 2nd Generation | EASY REPAIR"
S["warranty"]["settings"]["heading"] = "T50 AIR 2nd Generation | 5-year warranty"
S["warranty"]["settings"]["body"] = (
    "<p>So the journey with your T50 AIR continues, SIDIZ provides a 5-year warranty to "
    "customers who complete product registration. Once your chair arrives, register it "
    "before you forget, for more comfortable years ahead.</p>"
)
S["specifications"]["settings"]["heading"] = "T50 AIR 2nd Generation dimensions"
S["specifications"]["blocks"]["d1"]["settings"].update({
    "image_url": f"{KR}/files/T53HLDA0KK_01.jpg",
    "alt": "Dimension drawing of the SIDIZ T50 AIR 2nd Generation, front elevation"})
S["specifications"]["blocks"]["d2"]["settings"].update({
    "image_url": f"{KR}/files/T53HLDA0KK_02.jpg",
    "alt": "Dimension drawing of the SIDIZ T50 AIR 2nd Generation, side elevation"})

S["faq"]["blocks"]["q1"]["settings"]["question"] = "What changed in the fully redesigned T50 AIR 2nd Generation?"
S["faq"]["blocks"]["q1"]["settings"]["answer"] = (
    "<p>The 2nd Generation carries the S-line identity of the three-million-selling T50 "
    "family while resolving the frustrations real users reported: a wide lumbar support with "
    "the play and pressure-point feel engineered out, a 310 mm wide mesh headrest, and 4D "
    "armrests raised 25 mm. On the AIR, high-stiffness Airflex mesh runs across the whole "
    "chair, seat included, and the seat interchanges with the fabric T50 seat - each sold "
    "separately for self-service Easy Repair.</p>"
)

S["sticky_nav"]["blocks"]["n1"]["settings"] = {"label": "Full mesh", "anchor": "full-mesh"}

order = t["order"]
order.insert(order.index("comfort_banner"), "full_mesh")
assert order.index("full_mesh") == order.index("journey_cards") + 1

out = ROOT / "theme/templates/product.t50-air-2.json"
out.write_text(json.dumps(t, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print("written", out.name, "sections:", len(order))
