# sidiz.au — Store Audit

**Audited:** 2026-08-25 · **Store:** SIDIZ AUSTRALIA (`www.sidiz.au`) · **Plan:** Shopify · **Currency:** AUD · **Market:** Australia only · **Locale:** `en` only

> **This changes the shape of the project.** sidiz.au is not an empty store waiting for a migration —
> it is a **live, trading store** with existing inventory and 112 blog articles. The work is therefore
> *content expansion + data cleanup on a running shop*, not a greenfield build.
> Every change must be treated as a production change.

---

## 1. Catalogue

**30 product records — but only 8 distinct models.**

| Model | Records | On kr.sidiz.com? |
|---|---|---|
| T50 High Performance | 5 | ✅ |
| T50 AIR | 1 | ✅ |
| T80 Premium | 3 | ✅ |
| T25 Small | 8 | ❌ **AU-only** |
| T40 SE | 5 | ❌ **AU-only** |
| Ringo Kids | 4 | ✅ |
| Ringo Sanrio Cover (Cinnamoroll, Kuromi) | 2 | ❌ AU-only licence |
| GC Pro Gaming | 2 | ✅ |

### 🔴 Critical — duplicate product records

Each model exists **both** as a parent product with colour variants **and** as separate
one-colour products. Example, T50:

- `sidiz-t50-white-home-office-desk-chair` — 7 variants
- `t50-high-performance-ergonomic-office-chair-black-frame-black-seat` — 4 variants (itself inconsistent)
- `...-white-frame-beige-seat` — 1 variant
- `...-white-frame-blue-seat` — 1 variant
- `...-white-frame-gray-seat` — 1 variant

**Consequences:** duplicate content in Google Shopping and organic search; customers land on a
dead-end single-colour page with no colour picker; ad spend split across competing URLs.

### 🔴 Critical — duplicate SKUs across products

The same SKU is attached to multiple products, so inventory is double-counted:

| SKU | Appears on |
|---|---|
| `T25F0AOKA` | 4+ separate variants |
| `T50HLDA0AOKA456BK` | T50 parent **and** T50 black-frame product |
| `T50HLDA0AOKA451MWW` | T50 parent **and** T50 white/grey product |
| `SNA509AVABA444N` | Ringo parent **and** Ringo lavender product |
| `T40HA0COKA831BBK` | T40 SE parent **and** T40 SE black/grey product |

### 🔴 Critical — negative inventory

`T50 AIR` → *White Frame Grey Mesh* (`T50HLDA0AOKA2D1WW`) shows **−1**. Oversold; reconcile against
actual stock before anything else touches inventory.

### 🟡 Missing catalogue vs kr.sidiz.com

sidiz.au carries **8 of ~30** SIDIZ models. Absent:

`T90` · `T60` · `T60 AIR` · `T60 LDA` · `T20` · `T50 2nd gen` · `T50 AIR 2nd gen` · `T50 HF` ·
`MUUVE` · `LINIE` · `EGA` · `BUTTON` · `PLIT` · `MANE` · `OUI` · `GX` · `IBLE` · `TREVO` ·
`ATTI` (chair + desk) · `MOLTI` · `STEPO` · `PILLO` · `FUNGUS` · `The P Bag` · `Multi Spray` ·
Tottenham Hotspur line

This is the actual scope of the "new product launches".

---

## 2. Collections — 61 total, ~34 are zombies

**~34 expired/duplicated seasonal sale collections are still live and indexable:**

Aussie Day ×4 · Autumn ×3 · Early Autumn ×4 · Black Friday ×2 · Cyber Monday · Christmas ·
Christmas in July · Easter ×2 · EOFY ×6 · March Madness ×4 · Valentines ×4 · Halloween ·
Back To School ×2 · Flash Sale · Online Frenzy · Fathers Day

Nearly all share the **identical** smart rule `VARIANT_INVENTORY > 1`, so all 34 contain the
**same 12 products**. That is 34 near-identical indexable URLs — a textbook thin/duplicate content
problem that also dilutes crawl budget away from real product pages.

**9 empty collections:** `GIFT CARDS`, `HEADREST`, `SEAT CUSHION`, `OTHERS`, `pro-template-landing`,
`PRE-ORDER NOW FOR JUNE DELIVERY!` (stale since 2024), `Buy Ringo, Win T50`, `Fathers Day T50 Sale`,
`Online Frenzy AfterPay Sale`

**Overlapping real collections** — two parallel naming schemes duplicating each other:
`OFFICE` / `Home Office Chairs` / `Professional Office Chairs`, `GAMING` / `Gaming Chairs`,
`FOR KIDS` / `Kids & Study Chairs`, `HOME` (handle `ergonomic-desk-chairs`)

---

## 3. Theme

**11 themes installed.** Live theme: **`2-Symmetry`** (Symmetry, theme store ID 568), updated 2026-08-19.

Unpublished clutter to archive: `Dawn`, `Copy of Dawn`, `Updated copy of Dawn`, `Spotlight`,
`sidiz-america-shopify-theme`, `Copy of sidiz-america-shopify-theme`, `Symmetry`, `Copy of Symmetry`,
`Do not Edit - Symmetry(Original)`, `Backup | Symmetry`

> kr.sidiz.com runs a **custom** theme. sidiz.au runs stock **Symmetry**. The KR theme sections
> (Find Your Chair, Compare, product configurators, S-CULTURE layouts) do **not** exist here and
> need rebuilding for Symmetry rather than copying across.

---

## 4. Pages — 22 total, 11 unpublished

**Published (11):** Contact · Privacy Policy · Delivery & Lead Time · Terms of Use ·
Become a distributor · Return Policy · Warranty · COMPARE MODELS · FAQ · Customer Reviews · USER GUIDE

**Unpublished (11):** 🔴 **About Us** · FAQ's - Frequently Asked (superseded) · SHOP · SALE ·
Office Chairs · Kids Chairs · Study Chairs · Executive Chairs · Gaming Chairs · `atamy` (Untitled) · T20-2

**About Us being unpublished is a live problem** — a brand selling $500–1,600 chairs with no
accessible brand story loses trust-stage conversions. The KR `brand-story` / `history` /
`technology` content is the natural fill.

---

## 5. Blogs

| Blog | Articles | Note |
|---|---|---|
| `BLOG` (`guide`) | 112 | The active blog |
| `Brand Story` | 3 | Thin |
| `All About Fursys Australia Blog` | 0 | 🔴 **Stale legacy brand name** — delete |
| `About our products` | 0 | Empty — delete |
| `WORKERS HIGH CLUB` | 0 | Empty — delete |

KR has 117 FAQ articles (`product-faq` 67 + `service-faq-new` 50) that would slot straight into AU
support content — the highest-value content transfer available.

---

## 6. Localisation defects already in the store

Existing AU copy is **US English, not Australian English**:

| Issue | Example |
|---|---|
| 🔴 US spelling | `Gray Seat` / `Gray` variant, handles `...-gray-seat` — should be **Grey** |
| 🔴 Inconsistent | Titles say "Grey" while handles and variants say "Gray" — both spellings live at once |
| 🔴 Typo | `Lavendar Blue` → **Lavender** |
| 🔴 Imperial units | T25 copy uses feet and inches for user height — must be metric (cm) for AU |
| 🟡 Legacy brand | Handle `fursys-t50-air-home-office-desk-chair` and blog "All About **Fursys** Australia" |

---

## 7. Platform constraints

- **Plan is `Shopify`** (not Plus/Advanced) — no Markets Pro, limited checkout extensibility
- **Single locale `en`** — no translation layer configured
- **Single market `Australia`** — fine now; NZ expansion would need a second market
- `hreflang` to kr.sidiz.com is not configured

---

## 8. Recommended order of work

Cleanup before expansion — adding 22 models on top of this data would multiply the existing problems.

| # | Action | Risk |
|---|---|---|
| 1 | Reconcile the −1 inventory on T50 AIR | Low |
| 2 | Resolve duplicate SKUs (one SKU = one variant) | ⚠️ Touches inventory |
| 3 | Consolidate duplicate products → parent + variants; 301 the retired handles | ⚠️ Destructive, needs redirects |
| 4 | Archive ~34 zombie sale collections; keep one reusable "Sale" collection | ⚠️ Check live ad campaigns first |
| 5 | Delete 9 empty collections + 3 empty blogs | Low |
| 6 | Fix Gray→Grey, Lavendar→Lavender, imperial→metric | Low |
| 7 | Publish About Us using KR brand content | Low |
| 8 | Archive 10 unused themes | Low |
| 9 | **Then** begin new model launches | — |

> ⚠️ Steps 3 and 4 are irreversible and affect a trading store. **Do not execute without explicit
> sign-off**, a confirmed export backup, and a check against running Google/Meta campaigns — several
> sale collections carry `-gads`, `-meta`, `-seo`, `-email` handle suffixes, which strongly suggests
> they are (or were) live ad landing pages.
