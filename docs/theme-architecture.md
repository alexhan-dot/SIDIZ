# sidiz.au — Theme Architecture

**Target:** a new **draft (unpublished)** Shopify OS 2.0 theme rebuilding the kr.sidiz.com
structure for the Australian store. The live `2-Symmetry` theme is not touched.

**Base:** Shopify Dawn (OS 2.0, free, actively maintained) — used for the plumbing
(cart, search, predictive search, accessibility, image/media snippets), with the SIDIZ
architecture built on top.

**Source of truth:** kr.sidiz.com rendered output, mapped 2026-08-25.
See [section-blueprint.md](../data/kr-theme/section-blueprint.md).

---

## Why not copy the KR theme directly

The KR theme is fully custom. Without kr.sidiz.com admin access its Liquid source cannot be
exported. What *is* publicly available — and has been harvested into
`data/kr-theme/assets/` — is the compiled output:

- **78 stylesheets** including `theme.css` (70 KB) and per-section CSS
- **51 scripts**
- **8 webfonts** — CentraNo2 (Thin/Light/Book/Medium), Pretendard (Thin/Light/Regular/Medium)

That is enough to rebuild the structure and match the visual design precisely. The Liquid is
re-authored; the design system is carried over exactly.

> ⚠️ **CentraNo2 is a commercial typeface** (Sharp Type). Confirm the SIDIZ web licence covers
> the `sidiz.au` domain and the AU pageview tier before launch. Pretendard is SIL OFL — no issue.

---

## Design tokens

Extracted verbatim from KR `theme.css` into [`theme/assets/sidiz-tokens.css`](../theme/assets/sidiz-tokens.css).

| Group | Tokens |
|---|---|
| Brand | `--sidiz-blue #003EFF` · `--light-blue #357FFF` · `--background-blue #E3EDFF` · `--red-error #FF3A4A` |
| Greyscale | `--gray-000 #FFFFFF` … `--gray-900 #000000` (10 steps) |
| Warm neutrals | `--warm-white #FDFAF6` · `--text-dark #2A1F1A` · `--text-mid #6B5C52` · `--text-light #9E8E84` |
| Spacing | `--gutter-small/regular/large/xlarge/container`, `--sidebar-width`, `--header-vertical-space` |
| Breakpoints | 1365 · 1280 · 833 · 767 · 474 · 374 |

The AU build drops the CJK font fallback chain (`Noto Sans CJK KR`, `맑은 고딕`, `굴림`) and runs
Latin-first stacks.

---

## Section consolidation

kr.sidiz.com renders **61 unique sections across 17 templates**, but many are the same component
with different widths or content. Rebuilding all 61 one-for-one would be unmaintainable, so they
consolidate into **~22 parameterised OS 2.0 sections** driven by settings and blocks. This is what
"templatise everything" means in practice: merchandisers compose pages in the theme editor instead
of asking for a new section each time.

| New section | Replaces KR sections | Key settings |
|---|---|---|
| `sidiz-content-row` | `product_row_1_wide`, `product_row_1_narrow`, `product_row_1` | width (wide/narrow/contained), media side, text align, background |
| `sidiz-banner` | `banner`, `product_wb_banner`, `list_guide_banner` | full-bleed/contained, overlay, CTA, video or image |
| `sidiz-scroll-banner` | `product_wb_scroll_banner` | pinned scroll, frame sequence |
| `sidiz-card-list` | `product_wb_scroll_card_list`, `product_wb_card_list`, `product_tile_card_list` | layout (scroll/grid/tile), columns per breakpoint |
| `sidiz-pdp-head` | `product_pdp_head` | gallery, variant picker, price, sticky ATC |
| `sidiz-configurator` | `configurator` | option-driven product configurator |
| `sidiz-view-vertical` | `product_view_vertical` | vertical scroll gallery |
| `sidiz-spec` | `product_spec` | spec table via metafields |
| `sidiz-warranty` | `product_warranty` | ⚠️ AU: must state ACL consumer guarantees |
| `sidiz-faq` | `product_faq` | FAQ accordion from metaobjects |
| `sidiz-review` | `product_review` | review app embed |
| `sidiz-store-info` | `product_store_info` | ⚠️ AU stockists, not KR showrooms |
| `sidiz-easy-repair` | `product_easy_repair`, `self_repair_search`, `product_compatible` | parts finder by model |
| `sidiz-assembly-guide` | `product_assembly_guide` | assembly steps/video |
| `sidiz-find-your-fit` | `product_find_your_fit`, `fit_for_me` | fit quiz entry |
| `sidiz-product-carousel` | `product_related`, `product_related_product`, `product_recommend`, `recommend`, `cart-recommendations` | source (related/manual/collection) |
| `sidiz-brand-block` | `whoweare_section_1`–`4`, `main-about` | brand story blocks |
| `sidiz-journey` | `journey_title`, `journey_main`, `journey_sub` | history timeline |
| `sidiz-editorial-list` | `s-culture`, `story`, `news`, `available` | blog/article listing |
| `sidiz-sticky-nav` | `product_sticky`, `sticky`, `sidebar-complementary` | in-page anchor nav |
| `sidiz-notice` | `product-notice`, `announcement` | notice bar / disclaimers |
| `sidiz-popup` | `popups`, `main_popup_swiper`, `tilt-popup` | modal / popup manager |

**Carried from Dawn, restyled:** `header`, `footer`, `site-menu-sidebar` (Dawn drawer),
`product-grid` (Dawn collection grid), `main` (cart/search/page/blog mains).

**Not rebuilt — KR-only, no AU equivalent:**
`partner_exec` (KR corporate), `muuve_event` (KR campaign), `brand-menu` (KR site map),
`store` (KR showroom locator), `article_link`/`article_header` (fold into editorial list).

---

## Templates

| Template | Composition |
|---|---|
| `index` | banner · find-your-fit · product-carousel · banner(special) · editorial-list · brand-block · content-row |
| `product` | pdp-head · content-row ×n · banner · scroll-banner · card-list · view-vertical · find-your-fit · product-carousel · easy-repair · warranty · spec · faq · review · store-info · notice |
| `product.parts` | pdp-head · content-row · easy-repair(compatible) · assembly-guide · product-carousel · review · notice |
| `product.relife` | banner · content-row · faq · journey · warranty · card-list · spec · easy-repair · review · store-info · notice |
| `collection` | banner · product-grid |
| `page.brand` | brand-block ×4 |
| `page.history` | journey |
| `page.find-your-chair` | sticky-nav · content-row ×n · product-carousel |
| `page.compare` | compare table · popup |
| `page.easy-repair` | easy-repair (parts finder) |
| `blog` / `article` | editorial-list · banner · sticky-nav |
| `cart`, `search`, `404` | Dawn defaults, restyled |

---

## Australian adaptations baked into the build

These are not translations — they are structural differences the AU theme must have:

1. **`sidiz-warranty`** must present Australian Consumer Law consumer guarantees; the KR
   warranty wording cannot be carried over.
2. **`sidiz-store-info`** lists AU stockists/delivery, not KR flagship showrooms.
3. **No KR integrations** — Naver, Kakao (`#kakaoChatPC` is in the KR CSS), Danal payments,
   KR tax invoice (세금계산서) flows are all dropped.
4. **AU payment badges** — Afterpay and Zip are close to mandatory for AU furniture retail.
5. **GST-inclusive pricing** display.
6. **English text runs 20–40% longer than Korean** — every fixed-width component from the KR
   design needs a length check. This is the most common visual break when porting KR layouts.

---

## Build status

| Stage | State |
|---|---|
| Dawn scaffold | ✅ `theme/` (48 base sections, 13 templates) |
| Brand fonts installed | ✅ 8 woff2 files |
| Design tokens | ✅ `theme/assets/sidiz-tokens.css` |
| Section build | 🔄 In progress |
| Templates | ⏳ |
| Push as draft to sidiz.au | ⏳ |
