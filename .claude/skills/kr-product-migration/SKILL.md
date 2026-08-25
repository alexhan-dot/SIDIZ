---
name: kr-product-migration
description: Migrate one kr.sidiz.com product to the sidiz.au store — pull the KR data and media, translate copy to Australian English, convert pricing to AUD, build the product page from the SIDIZ sections, self-host the media, and run the SEO checks. Use for every remaining SIDIZ product after the T90 pilot. Trigger with "migrate <model>", "port <model> to AU", or "add <model> product page".
---

# KR → AU product migration

This is the pipeline proven on T90 (`products/product.t90.json`). Follow every
phase in order. The **Gotchas** section at the end lists the traps that cost
time on T90 — read it before starting, not after.

Store: `desker-9264.myshopify.com` (www.sidiz.au). Draft theme:
`SIDIZ AU - T90 draft` #192452231490. Products are created **DRAFT** and never
published without sign-off. Prices come from `data/pricing/price-list.csv`
(KRW → AUD, x99 at $100+, x9 below); the six pre-existing live models keep their
current AU price unless told otherwise.

All scripts take the KR product handle as their argument, e.g. `t60`, `muuve`.

---

## Phase 0 — Scope check (before touching anything)

1. Confirm the model is in scope. Excluded pending owner sign-off: Tottenham
   Hotspur collab (AU licence), Re:LIFE (KR-only programme). Confirm before
   building these.
2. Confirm whether the model already exists on sidiz.au (`search_products`).
   If it does, this is an **update**, not a create — do not make a duplicate.
3. Note the KR handle and the intended AU handle. AU handles are descriptive
   English (`t60-ergonomic-office-chair`), never the bare model code, and never
   URL-encoded Korean.

## Phase 1 — Pull the KR source

```
python scripts/harvest_product_media.py <handle> <baseline>   # media, minus shared chrome
python scripts/map_section_media.py <handle>                   # section → media, in DOM order
python scripts/extract_page_text.py <handle>                  # Korean copy, for translation
python scripts/section_spec.py <handle>                       # per-section wrapper/colours/text/media
```

Then extract the HTML of every section the page renders (get the list from
`section_spec.py`):

```
python scripts/extract_section_html.py <handle> <section>     # once per section
python scripts/skeleton.py <handle> <section> [<section>...]  # condensed DOM to read
```

Do not skip the HTML extraction. Building a section from its stylesheet alone
is guesswork and was wrong every time on T90.

## Phase 2 — Translate to Australian English

Write `data/products/<handle>/en-content.md`, section by section, from the
extracted Korean copy. Rules:

- Australian spelling: colour, grey, optimised, moulded, aluminium, centre.
  Never US spelling. **Grey, never Gray.**
- Metric only. Convert any imperial figure.
- Korean patents stay attributed as Korean (`Korean Patent No. 10-…`). Never
  imply AU patent protection.
- **Do not migrate KR reviews or KR influencer endorsements** — misleading
  conduct under the ACL, and one T90 review was a legal complaint. Featured
  reviews must be genuine AU-customer reviews.
- Warranty copy gets the mandatory ACL consumer-guarantees statement
  (`sidiz-warranty` renders it as fixed markup — leave `show_acl` on).
- Drop KR-market modules: Naver/Kakao, Danal, KR tax invoice, showroom-visit
  wording (→ AU stockists), card interest-free instalment (→ Afterpay/Zip),
  KC certification row.

## Phase 3 — Pricing

Look up every SKU in `data/pricing/price-list.csv`. If the model is not there,
re-run `scripts/build_price_list.py` after refreshing `data/kr-catalogue`. AUD
prices are GST-inclusive; the buy box shows the GST note.

## Phase 4 — Create the product (DRAFT)

`productSet` mutation, synchronous, with:

- `status: DRAFT`, descriptive `handle`, `templateSuffix: "<handle>"`
- `seo.title` and `seo.description` (en-AU, keyword-bearing)
- `productOptions` — **Material** and **Colour** in Australian English
- one `variant` per KR variant, with SKU and AUD `price`

Then, in order:

1. `productCreateMedia` — gallery images, each with **written English alt text**
   (map KR filenames → variants via the SKU colour codes; see
   `build_media_seo.py`).
2. `productVariantAppendMedia` — pin each variant to its colour image.
3. `publishablePublish` to the Online Store publication (stays DRAFT; this only
   makes the draft themeable in preview).

## Phase 5 — Self-host the media

Videos and images must not ship pointing at the KR CDN. Run:

```
python scripts/plan_video_upload.py <handle>       # english names + alt, matched to files
# stagedUploadsCreate (batch) → POST each file → fileCreate (no filename)
python scripts/upload_videos.py <targets.tsv>      # matches target to file by SIGNED BYTE LENGTH
# poll fileStatus READY, read back sources, then:
python scripts/repoint_videos_to_au.py <handle>    # KR CDN URLs → AU store URLs in the template
```

Do the same for still images. Posters use the full-resolution AU preview frame,
not KR's `_small`.

## Phase 6 — Build the template

Compose `theme/templates/product.<handle>.json` from the SIDIZ sections. **The
KR section order is the contract** — read it off `section_spec.py` and match it
one for one. The T90 order, for reference:

1. `sticky_nav` — sidiz-sticky-nav
2. `pdp_head` — sidiz-pdp-head (the buy box + gallery; holds the single H1)
3. `intro` — sidiz-product-row (centred H1 + bullet list)  ← this H1 is the page H1
4. `hero` — sidiz-pdp-hero (wordmark over video + positioning paragraph)
5. `materials` — sidiz-option-compare (material panels with swatch dots)
6. `ergonomics_banner` — sidiz-wb-scroll-banner (pinned, dark)
7. `ergonomics_cards` — sidiz-wb-scroll-card-list (dark, must follow the banner)
8. `armrests` — sidiz-product-view (light; sticky media + feature row)
9. `tilt_banner` — sidiz-wb-banner
10. `tilt_cards` — sidiz-wb-card-list
11. `comfort_cards` — sidiz-tile-card-list (square tiles + overlay caption)
12. `material_tiles` — sidiz-tile-card-list (materials showcase)
13. `find_your_fit` — sidiz-find-your-fit (adjustment grid + USER GUIDE)
14. `goes_with` — sidiz-related-products
15. `easy_repair` — sidiz-related-products
16. `warranty` — sidiz-warranty (ACL statement on)
17. `specifications` — sidiz-spec (dimension drawings + figures)
18. `faq` — sidiz-faq
19. `reviews` — sidiz-review (@app slot + AU featured reviews only)
20. `stockists` — sidiz-store-info
21. `recommend` — sidiz-related-products
22. `notices` — sidiz-contact-notice (contact + after-sales, AU details)

Per-section colours (title/description/tag/background) live in **inline
`<style data-shopify>` blocks scoped to `section-{{ section.id }}`**, driven by
section settings. This is how KR does it and how the AU sections do it — set the
colours per section, do not assume a default.

Dark sections (hero, both wb-scroll, wb-banner) set
`data-header-scheme="dark"` so the floating header turns its text white over
them.

## Phase 7 — Validate, push, verify by eye

```
cd theme && shopify theme check          # zero errors on sidiz-* files
shopify theme push --store desker-9264.myshopify.com --theme 192452231490
```

Then **open the preview and look**, section by section, against the KR page:

```
https://admin.shopify.com/store/fursysau/themes/192452231490/editor?previewPath=/products/<handle>
```

Do not report a section done from the code alone. On T90, several sections
passed theme check and still rendered wrong. If access is blocked, ask the user
to check; screen recordings can be turned into frames with ffmpeg for exact
comparison.

## Phase 8 — SEO checks

Run the heading/schema/alt audit (the inline audit block in `section_spec` era,
or by hand):

- Exactly **one H1** on the page (the descriptive product title in `intro`).
  The buy-box title is an H2.
- Meta title + description set on the product.
- Every image has written alt text (never keyword-stuffed).
- `sidiz-product-schema` emits Product + AggregateOffer (per variant) +
  BreadcrumbList; `sidiz-faq` emits FAQPage. Facts in schema must match the
  visible page (ACL: price/availability especially).
- Descriptive handle; add a 301 from any old handle if one existed.

---

## Gotchas — read before starting

These each cost real time on T90.

1. **KR injects 51 CSS variables into the document head** (`--color-text-header`,
   `--container-vertical-space-base`, `--grid-gap-original-base`, type scale…).
   They are in no stylesheet. Without them var() resolves to nothing: invisible
   header text, wrong spacing, wrong type. They ship in
   `assets/sidiz-root-variables.css`, loaded first in the layout head. Already
   global — just do not remove it.

2. **Per-section colours are inline `<style data-shopify>`**, not in the shared
   CSS. A section rebuilt from its stylesheet alone renders with the wrong
   colours (the black-panel-white-text scroll section was the tell).

3. **Section name ≠ content.** KR `product_assembly_guide` is the customer
   reviews carousel; `product_information` is the safety-notes block;
   `product-notice` is the contact/after-sales footer, not "before you buy".
   Read the extracted HTML, not the name.

4. **Option values are drops, not strings.** `{{ value | handleize }}` returns
   empty. Capture to text first (`{% capture %}{{ value }}{% endcapture %}`).
   This silently broke the colour swatches.

5. **Colour swatches are drawn as inline SVG** (`snippets/sidiz-swatch.liquid`),
   not a coloured div — KR sizes the inner dot through a four-level descendant
   chain that collapses to zero height wherever it does not match.

6. **Chip design keys off `data-option`** on `.product-variant`
   (`option`/`option-2` = bordered pill, `color` = round swatch). Remove the
   attribute and the chips lose their borders.

7. **Gallery grid is on `.product-media--wrapper`, not `.product-gallery`**, and
   below 1023px `.web` is hidden and `.mobile` (a swiper) takes over — build
   both.

8. **The header floats and only its text recolours** (white/black) via
   `data-header-scheme`, with a backdrop blur. Not mix-blend-mode (tints text
   against colour) and not a stacked bar that pushes the page down.

9. **Staged uploads: match target to file by the signed byte length**, never by
   list order — a wrong pairing uploads the right name over the wrong footage.

10. **fileCreate takes no `filename`** when the source is a staged upload URL
    (the URL has no extension; passing one fails validation).

11. **Shopify does not upscale.** A 480p KR source stays 480p. The eight
    genuinely-SD T90 clips can only be improved with masters from SIDIZ.

12. **Mixed-case headings**: KR pairs a Korean line with an all-caps English
    line at the same visual size. Translated, sentence case + caps look
    mismatched. Wrap the caps line in `<em class="caps">` (0.9em, +0.04em
    tracking) — see `sidiz-au-overrides.css`.

13. **Theme-editor CSS caches hard.** After a CSS-only change, hard-reload
    (ctrl+shift+r) before judging; prefer inline styles for anything that must
    render regardless.
