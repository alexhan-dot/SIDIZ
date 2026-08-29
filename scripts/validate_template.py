"""Check a product template against the schemas of the sections it uses.

Shopify accepts a template whose settings do not exist in the section schema —
the values are simply never rendered. That is how the T60 hero and gallery
shipped without images (skill gotcha 15). This makes the mismatch loud.

Checks, per section in the template:
  - the section liquid file exists
  - every settings key exists in the schema (colour/media/text alike)
  - every block type exists, and every block setting key exists on that type
  - the section count is within Shopify's 25-section template cap

Usage: python scripts/validate_template.py t50-2
"""

import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]


def schema_of(section_type):
    f = ROOT / "theme" / "sections" / f"{section_type}.liquid"
    if not f.exists():
        return None
    doc = f.read_text(encoding="utf-8")
    m = re.search(r"{%\s*schema\s*%}(.*?){%\s*endschema\s*%}", doc, re.S)
    return json.loads(m.group(1)) if m else {}


def main():
    handle = sys.argv[1]
    tpl_path = ROOT / "theme" / "templates" / f"product.{handle}.json"
    tpl = json.loads(tpl_path.read_text(encoding="utf-8"))

    problems = []
    order = tpl.get("order", [])
    if len(order) > 25:
        problems.append(f"template has {len(order)} sections; Shopify caps at 25")

    for key, sec in tpl["sections"].items():
        stype = sec["type"]
        if stype.startswith("apps"):
            continue
        sch = schema_of(stype)
        if sch is None:
            problems.append(f"{key}: section file {stype}.liquid does not exist")
            continue

        valid = {s["id"] for s in sch.get("settings", []) if s.get("id")}
        for sid in sec.get("settings", {}):
            if sid not in valid:
                problems.append(f"{key}: setting '{sid}' not in {stype} schema")

        btypes = {b["type"]: {s["id"] for s in b.get("settings", []) if s.get("id")}
                  for b in sch.get("blocks", [])}
        for bkey, block in sec.get("blocks", {}).items():
            if block["type"] == "@app":
                continue
            if block["type"] not in btypes:
                problems.append(f"{key}.{bkey}: block type '{block['type']}' not in {stype} schema")
                continue
            for sid in block.get("settings", {}):
                if sid not in btypes[block["type"]]:
                    problems.append(f"{key}.{bkey}: block setting '{sid}' not in {stype}/{block['type']}")

    if problems:
        print(f"{tpl_path.name}: {len(problems)} problem(s)")
        for p in problems:
            print("  -", p)
        raise SystemExit(1)
    print(f"{tpl_path.name}: OK ({len(order)} sections, all settings declared)")


if __name__ == "__main__":
    main()
