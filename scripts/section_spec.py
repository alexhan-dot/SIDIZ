"""Build a definitive per-section spec from the extracted KR HTML.

For every section on the KR T90 page this records, mechanically:
  - the wrapper class (which stylesheet governs it)
  - every colour declared in its inline <style data-shopify> blocks
  - its headings and text, in order
  - how many media items it holds

The point is to stop inferring what a section looks like and read what it
actually declares, so the AU template can be checked against it line by line.

Usage: python scripts/section_spec.py t90
"""

import html as html_mod
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]

STYLE = re.compile(r"<style data-shopify>(.*?)</style>", re.S)
RULE = re.compile(r"([^{}]+)\{([^{}]*)\}")
TAGTEXT = re.compile(
    r"<(h1|h2|h3|h4|div|span)[^>]*class=\"([^\"]*\b(?:title|tag|description|subtitle)\b[^\"]*)\"[^>]*>(.*?)</\1>",
    re.S | re.I,
)
DROP = re.compile(r"<[^>]+>")


def text_of(fragment):
    t = DROP.sub(" ", fragment)
    t = html_mod.unescape(t)
    return re.sub(r"\s+", " ", t).strip()


def main():
    handle = sys.argv[1] if len(sys.argv) > 1 else "t90"
    src = ROOT / "data" / "products" / handle / "sections"
    order = json.loads(
        (ROOT / "data" / "products" / handle / "section-media.json").read_text(encoding="utf-8")
    )
    seq = [s["section"] for s in order]

    spec = {}
    for name in seq:
        f = src / f"{name}.html"
        if not f.exists():
            continue
        doc = f.read_text(encoding="utf-8")

        wrapper = re.search(r'<section[^>]*class="([^"]+)"', doc)
        wrapper = wrapper.group(1) if wrapper else ""

        colours = {}
        for block in STYLE.findall(doc):
            for sel, body in RULE.findall(block):
                sel = re.sub(r"\s+", " ", sel).strip()
                for prop, val in re.findall(r"(background-color|color)\s*:\s*([^;]+)", body):
                    val = val.strip()
                    if not val:
                        continue
                    key = re.sub(r"^.*?(\.[a-z0-9_-]+(?:\s+\.[a-z0-9_-]+)*)$", r"\1", sel)
                    colours.setdefault(f"{key} :: {prop}", val)

        texts = []
        for _tag, cls, body in TAGTEXT.findall(doc):
            t = text_of(body)
            if t and len(t) < 400:
                kind = "title" if "title" in cls else ("tag" if "tag" in cls else "description")
                texts.append({"kind": kind, "text": t})

        spec[name] = {
            "wrapper": wrapper,
            "colours": colours,
            "media": len(re.findall(r"<(?:video|img)\b", doc)),
            "texts": texts[:14],
        }

    dest = ROOT / "data" / "products" / handle / "section-spec.json"
    dest.write_text(json.dumps(spec, ensure_ascii=False, indent=1), encoding="utf-8")

    for name in seq:
        s = spec.get(name)
        if not s:
            continue
        cls = s["wrapper"].replace("shopify-section ", "")
        print(f"\n### {name}   [{cls}]   media={s['media']}")
        for k, v in s["colours"].items():
            print(f"    {k:52} {v}")
        for t in s["texts"][:4]:
            print(f"    · {t['kind']:11} {t['text'][:78]}")

    print(f"\n-> {dest.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
