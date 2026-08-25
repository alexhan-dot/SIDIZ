"""Map the section architecture of kr.sidiz.com across every page type.

Fetches a representative page per template and extracts the Shopify section
names, so the AU theme can be rebuilt with the same structure.

Writes: data/kr-theme/sections-by-template.json  +  a markdown blueprint.
"""

import json
import pathlib
import re
import time
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "kr-theme"

SAMPLES = {
    "index":            "https://kr.sidiz.com/",
    "product":          "https://kr.sidiz.com/products/t60",
    "product.parts":    "https://kr.sidiz.com/products/t80-headrest",
    "product.relife":   "https://kr.sidiz.com/products/t60-re-life",
    "collection.work":  "https://kr.sidiz.com/collections/work",
    "collection.model": "https://kr.sidiz.com/collections/t60",
    "page.brand":       "https://kr.sidiz.com/pages/brand-story-1",
    "page.history":     "https://kr.sidiz.com/pages/history",
    "page.findchair":   "https://kr.sidiz.com/pages/find-your-chair",
    "page.compare":     "https://kr.sidiz.com/pages/compare",
    "page.support":     "https://kr.sidiz.com/pages/support",
    "page.easyrepair":  "https://kr.sidiz.com/pages/easy-repair",
    "page.work":        "https://kr.sidiz.com/pages/work",
    "page.experience":  "https://kr.sidiz.com/pages/experience",
    "blog":             "https://kr.sidiz.com/blogs/s-culture",
    "cart":             "https://kr.sidiz.com/cart",
    "search":           "https://kr.sidiz.com/search?q=t60",
}

UA = "Mozilla/5.0 (compatible; SIDIZ-AU-migration/1.0)"
SECTION_RE = re.compile(r'id="shopify-section-([^"]+)"')
# section ids look like:  template--<id>__<name>  |  sections--<id>__<name>  |  <name>
STRIP_RE = re.compile(r"^(?:template|sections)--\d+__")
SUFFIX_RE = re.compile(r"_[A-Za-z0-9]{6}$")


def normalise(raw):
    name = STRIP_RE.sub("", raw)
    return SUFFIX_RE.sub("", name)


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8", errors="replace")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    result = {}

    for template, url in SAMPLES.items():
        try:
            html = fetch(url)
        except Exception as exc:  # noqa: BLE001
            result[template] = {"url": url, "error": str(exc)}
            print(f"{template:20} ERROR {exc}")
            continue

        ordered, seen = [], set()
        for raw in SECTION_RE.findall(html):
            name = normalise(raw)
            ordered.append(name)
            seen.add(name)

        result[template] = {"url": url, "sections": ordered, "unique": sorted(seen)}
        print(f"{template:20} {len(ordered):>3} sections  ({len(seen)} unique)")
        time.sleep(1)

    (OUT / "sections-by-template.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    # global sections appear on (almost) every template
    ok = {k: v for k, v in result.items() if "sections" in v}
    counts = {}
    for v in ok.values():
        for s in set(v["sections"]):
            counts[s] = counts.get(s, 0) + 1
    globals_ = {s for s, n in counts.items() if n >= len(ok) - 2}

    lines = ["# kr.sidiz.com — Theme Section Blueprint", ""]
    lines += [f"Mapped {len(ok)} page templates on 2026-08-25.", ""]
    lines += ["## Global sections (present on nearly every template)", ""]
    lines += [f"- `{s}`" for s in sorted(globals_)] + [""]

    for template, v in ok.items():
        body = [s for s in v["sections"] if s not in globals_]
        lines += [f"## `{template}`", "", f"Sample: {v['url']}", ""]
        lines += [f"{i}. `{s}`" for i, s in enumerate(body, 1)] or ["_(only global sections)_"]
        lines += [""]

    (OUT / "section-blueprint.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"\nglobal sections: {sorted(globals_)}")
    print(f"total unique sections: {len(counts)}")


if __name__ == "__main__":
    main()
