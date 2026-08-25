# SIDIZ Australia — Store Migration

Migration of [kr.sidiz.com](https://kr.sidiz.com/) (Shopify, Korean) → **sidiz.au** (Shopify, Australian English),
plus the launch of new products for the Australian market.

> ⚠️ **This repository is public.** Never commit API keys, access tokens, `.env` files,
> customer data, or unreleased product information. See [.gitignore](.gitignore).

## Repository layout

| Path | Contents |
|---|---|
| `theme/` | Shopify theme code for sidiz.au (pulled via Shopify CLI) |
| `data/source-sitemaps/` | Raw sitemaps fetched from kr.sidiz.com |
| `data/inventory/` | Extracted URL inventories (products, collections, pages, blogs, metaobjects) |
| `data/content/` | Scraped Korean source copy + Australian English translations |
| `docs/` | Migration plan, checklists, decision log |

## Source inventory (kr.sidiz.com, fetched 2026-08-25)

| Type | Count |
|---|---|
| Products | 87 |
| Collections | 45 |
| Pages | 77 |
| Blog articles (S-CULTURE) | 353 |
| Metaobject pages | 127 |
| **Total URLs** | **689** |

## Status

See [docs/migration-plan.md](docs/migration-plan.md) for the phased plan and current progress.
