# SIDIZ KR→AU migration

Before any work, read `HANDOVER.md` — it holds the full project state, the
connection checklist (store/theme IDs), what is done, and what comes next.

Ground rules (details in HANDOVER.md and the `kr-product-migration` skill):

- Product migrations run through the `kr-product-migration` skill, one model
  per run. Never improvise the pipeline.
- Theme #192452231490 on desker-9264.myshopify.com is the LIVE theme. Pushing
  is a live change — confirm with the owner before the first push of a session.
- Products are created DRAFT; only the owner publishes anything.
- Australian English (colour/grey), metric, GST-inclusive prices from
  `data/pricing/price-list.csv`. No KR reviews or influencer content (ACL).
