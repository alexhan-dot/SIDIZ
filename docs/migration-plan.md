# SIDIZ AU — Migration Plan

**Source:** kr.sidiz.com (Shopify, Korean) — public access only, no admin credentials
**Target:** sidiz.au (Shopify, Australian English, AUD)
**Content rights:** All video and image content cleared for use (confirmed by owner, 2026-08-25)

---

## 0. Prerequisites

| Item | Status | Notes |
|---|---|---|
| Shopify MCP connected to SIDIZ AU store | ⏳ **Blocked** | Previous connection was `sihoo.com.au`; revoked. Needs re-auth via claude.ai connector settings. |
| GitHub repo `alexhan-dot/SIDIZ` | ✅ | Public, empty → being scaffolded |
| kr.sidiz.com admin access | ❌ Not available | Working from public site only |
| Shopify CLI installed | ⏳ | Required for `theme pull` / `theme push` |

---

## 1. Source inventory (complete)

Fetched from `kr.sidiz.com/sitemap.xml` on 2026-08-25. Raw files in `data/source-sitemaps/`,
parsed CSVs in `data/inventory/`.

| Type | Count | File |
|---|---|---|
| Products | 87 | `data/inventory/products.csv` |
| Collections | 45 | `data/inventory/collections.csv` |
| Pages | 77 | `data/inventory/pages.csv` |
| Blog articles | 353 | `data/inventory/blogs.csv` |
| Metaobject pages | 127 | `data/inventory/metaobjects.csv` |

### Product breakdown

The 87 products are **not** 87 chairs. They split roughly as:

| Group | Approx. count | AU launch relevance |
|---|---|---|
| Task / office chairs (T-series: T90, T80, T60, T60 AIR, T60 LDA, T50, T50 AIR, T50 2nd gen, T50 AIR 2nd gen, T50 HF, T20) | 11 | **Core** |
| Light work (MUUVE, LINIE, EGA, BUTTON) | 4 | **Core** |
| Living & dining (PLIT, MANE, OUI) | 3 | Core |
| Gaming (GC PRO, GX) | 2 | Core |
| Study (IBLE, RINGO gen2, TREVO) | 3 | Core |
| Growing / kids (ATTI chair, ATTI desk, MOLTI) | 3 | Core |
| Seat booster (STEPO, PILLO, FUNGUS, OLLY) | 4 | Core |
| The P Goods (The P Bag, Multi Spray) | 2 | Optional |
| Tottenham Hotspur collab (T20, OLLY, FUNGUS, T20 armpad) | 4 | ⚠️ **Licensing check required** — KR-market licence may not extend to AU |
| Easy Repair spare parts (headrests, seats, armpads, casters, glides, covers, levers…) | ~43 | Phase 2 — depends on AU parts logistics |
| Re:LIFE refurbished (T80, T90, T50 HLDA, T50 HF, T60, T60 AIR, GC PRO, IBLE, GX) | 9 | ⚠️ Likely **KR-only** — refurb programme is market-specific |

### Decisions needed before catalogue build

1. **Tottenham Hotspur line** — is the collaboration licence valid for Australian sale?
2. **Re:LIFE** — is a refurbished programme planned for AU? If not, exclude the 9 SKUs.
3. **Easy Repair** — will spare parts be stocked in AU at launch, or phase 2?
4. **New AU-only products** — which products are launching that don't exist on kr.sidiz.com? Need names, specs, imagery, pricing.
5. **Pricing** — AUD price list per SKU (not derivable from the KR site).

---

## 2. Content localisation — Korean → Australian English

**Style rules for all copy:**

- Australian spelling: `colour`, `centre`, `customise`, `organise`, `metre`, `fibre`, `armour`
- **Not** US spelling (`color`, `center`, `customize`) — this is the single most common slip
- Dates: `25 August 2026` or `25/08/2026` (day-first)
- Currency: `$1,299` / `AUD $1,299` — GST-inclusive pricing is the Australian norm
- Units: metric — cm, kg. Never inches or lbs.
- Warranty language must comply with **Australian Consumer Law** — the ACL guarantees cannot be
  excluded and must not be contradicted by manufacturer warranty text
- Tone: direct and plain. Korean marketing copy tends to be more formal and superlative-heavy;
  Australian retail copy is flatter and more concrete. Translate the *intent*, don't transliterate.

**Do not machine-translate and ship.** Every product page and brand page gets a human-readable
rewrite pass. Korean source copy is preserved alongside the English in `data/content/` so the
translation is auditable.

### Pages requiring full rewrite (not just translation)

These contain KR-specific legal, logistics or account content that must be **replaced**, not translated:

| KR page | Action |
|---|---|
| `pages/privacy-policy` | Rewrite for Australian Privacy Act 1988 / APPs |
| `pages/terms-of-service` | Rewrite for ACL |
| `pages/warranty-policy` | Rewrite for ACL consumer guarantees |
| `pages/sustainability-policy` | Adapt |
| `pages/안전보건-경영방침` (safety & health policy) | Adapt or drop |
| `pages/naver-login`, `pages/kakao-login` | **Drop** — no AU relevance |
| `pages/danal-callback` | **Drop** — KR payment gateway |
| `pages/invoice` | Rewrite — KR tax invoice (세금계산서) has no AU equivalent |
| `pages/customers-convert-user`, `customers-find-user_email`, `customers-pw-init` etc. | **Drop** — legacy KR account migration flows |
| `pages/shop-search`, `pages/shop-detail` | Rewrite — AU stockist/showroom locations |
| `pages/as-apply`, `pages/as-main` | Rewrite — AU service & repair process |
| `pages/business`, `pages/business-consulting` | Rewrite — AU B2B / commercial fit-out |
| `pages/register-product`, `pages/product-registration` | Rewrite — AU warranty registration |

### Pages that are test / junk — exclude

`pages/test`, `pages/test-sidiz`, `pages/jsontoexel`, `pages/xptmxmdlqpsxm`,
`pages/신청-팝업-테스트`, `pages/f44b5b166b1fb643dc4356e96b8505cc`,
`pages/21bf5abd3e04702663d901f97cebf87f`, `pages/copy-of-find-your-chair`,
plus superseded `find-your-chair-ver-3/4` (keep only the current version).

Also `collections/non-exposure-1`, `collections/non-exposure-2` — hidden collections, exclude.

### Blog content (353 articles)

The 353 "blog" URLs are mostly **not** editorial content — Shopify blogs are used on kr.sidiz.com
to hold FAQs, IR material and legal documents. Actual breakdown:

| Blog | Count | Decision |
|---|---|---|
| `product-faq` | 67 | ✅ **Migrate** — high value, directly reduces AU support load |
| `service-faq-new` | 50 | ✅ **Migrate & adapt** — AU service process differs |
| `s-culture` | 76 | 🔶 **Triage** — evergreen ergonomics/brand content migrates, KR-campaign posts don't |
| `news` | 66 | ❌ Skip — Korean press releases and corporate news |
| `IR자료` (investor relations) | 33 | ❌ **Skip** — KR-listed-company IR material, no AU relevance |
| `special-offers` | 21 | ❌ Skip — expired KR promotions |
| `개인정보 수집 및 이용 동의` (privacy consent) | 16 | 🔁 **Replace** — rewrite for Australian Privacy Act / APPs |
| `시디즈 쇼핑몰 이용약관` (store T&C) | 6 | 🔁 **Replace** — rewrite for ACL |
| `storage`, `contents` | 7 | 🔶 Triage |
| `품질보증정책` (warranty policy) | 2 | 🔁 **Replace** — rewrite for ACL consumer guarantees |
| `마케팅 수신 동의` (marketing consent) | 2 | 🔁 **Replace** — rewrite for Spam Act 2003 |
| `임직원 할인` (employee discount) | 2 | ❌ Skip — internal KR programme |
| `제품가이드 상세` (product guide detail) | 2 | 🔶 Triage — likely fold into product pages |
| `test`, `s-culture-test`, `service-faq` | 3 | ❌ Skip — test artefacts |

**Net:** ~117 articles to translate (`product-faq` + `service-faq-new`), ~83 to triage,
~26 legal documents to **rewrite from scratch** for Australian law, ~124 to drop.

This materially changes the effort estimate: the FAQ content is the bulk of the work and it is
also the highest-value content to get right, because it directly determines AU support volume.

---

## 3. Media

All imagery and video is cleared for use. Approach:

- Reference Shopify CDN URLs are captured in the inventory CSVs where the sitemap exposed them
- Download originals at full resolution, re-upload to the AU store's Files
- **Any image with burned-in Korean text must be recreated** with English text — this is the largest
  hidden cost in the migration and needs an early audit
- Video: check whether KR videos have Korean voiceover or on-screen text; subtitle or re-cut as needed

---

## 4. Theme

kr.sidiz.com runs on Shopify, so the theme is portable in principle.

1. Connect Shopify CLI to the AU store
2. `shopify theme pull` the current AU theme into `theme/` as the baseline
3. Rebuild KR sections/templates that don't exist in AU, adapting for English text lengths
   (English strings typically run 20–40% longer than Korean — check every fixed-width component)
4. Remove KR-only integrations: Naver, Kakao, Danal, KakaoTalk channel, KR review apps
5. Add AU essentials: AUD currency formatting, GST display, Australia Post / courier shipping,
   AU payment methods (Afterpay/Zip are near-mandatory for AU furniture retail)

---

## 5. SEO & redirects

- `hreflang` between `kr.sidiz.com` (ko-KR) and `sidiz.au` (en-AU)
- Handles should be English and stable — several KR handles are URL-encoded Korean
  (e.g. `collections/atti-책상`, `products/gc-pro-게이밍-의자-re-life`). These **must not** be carried over.
- Build a handle mapping table in `data/content/handle-map.csv` as pages are created
- Australian keyword research — "office chair", "ergonomic chair", "desk chair Australia"

---

## 6. Phases

| Phase | Scope | Blocked on |
|---|---|---|
| **0. Setup** | Repo, inventory, plan | ✅ Done |
| **1. Connect** | Shopify MCP → SIDIZ AU; Shopify CLI; theme baseline | Shopify re-auth |
| **2. Decide** | Answer the 5 catalogue decisions in §1; blog triage | Owner input |
| **3. Content** | Scrape KR copy → translate to en-AU → review | Phase 2 |
| **4. Catalogue** | Create products, variants, collections, metafields in AU store | Phases 1–3 + AUD pricing |
| **5. Theme** | Build/adapt templates and sections | Phase 1 |
| **6. Media** | Download, audit Korean-text imagery, recreate, upload | Phase 2 |
| **7. Legal** | ACL-compliant policies, warranty, privacy | Legal review |
| **8. Launch** | Redirects, hreflang, QA, go-live checklist | All |

---

## Decision log

| Date | Decision |
|---|---|
| 2026-08-25 | Source access: public site crawl only (no KR admin credentials) |
| 2026-08-25 | Repo stays public → strict `.gitignore`, no secrets or unreleased product data committed |
| 2026-08-25 | Repo holds theme code + migration data + working docs |
