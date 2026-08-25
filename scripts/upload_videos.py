"""Upload the T90 videos to the staged targets returned by stagedUploadsCreate.

Each staged policy is signed for one exact byte length, so the target is matched
to a local file by that length rather than by list order — a mismatch would
otherwise upload the wrong footage under the right name and be very hard to spot.

Reads a TSV of: external_video_id, key, policy, signature
Writes: data/products/t90/video-upload-results.json
"""

import base64
import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
MEDIA = ROOT / "data" / "products" / "t90" / "media"
PLAN = ROOT / "data" / "products" / "t90" / "video-upload-plan.json"
OUT = ROOT / "data" / "products" / "t90" / "video-upload-results.json"

BUCKET = "https://shopify-video-production-core-originals.storage.googleapis.com"
ACCESS_ID = "video-production@video-production-225115.iam.gserviceaccount.com"


def signed_length(policy_b64):
    """The content-length-range the policy is signed for."""
    pad = "=" * (-len(policy_b64) % 4)
    doc = json.loads(base64.b64decode(policy_b64 + pad))
    for cond in doc["conditions"]:
        if isinstance(cond, list) and cond[0] == "content-length-range":
            return int(cond[1])
    raise ValueError("no content-length-range in policy")


def main():
    tsv = pathlib.Path(sys.argv[1])
    plan = json.loads(PLAN.read_text(encoding="utf-8"))
    by_size = {}
    for p in plan:
        by_size.setdefault(p["bytes"], []).append(p)

    results = []
    rows = [l for l in tsv.read_text(encoding="utf-8").splitlines() if l.strip()]
    print(f"{len(rows)} staged targets\n")

    for i, line in enumerate(rows, 1):
        ext_id, key, policy, signature = line.split("\t")
        size = signed_length(policy)

        candidates = by_size.get(size)
        if not candidates:
            print(f"  [{i:2}/{len(rows)}] no local file of {size:,} bytes — skipped")
            continue
        entry = candidates.pop(0)
        path = MEDIA / entry["local"]

        proc = subprocess.run(
            [
                "curl", "-sS", "-o", "/dev/null", "-w", "%{http_code}",
                "-X", "POST", BUCKET,
                "-F", f"GoogleAccessId={ACCESS_ID}",
                "-F", f"key={key}",
                "-F", f"policy={policy}",
                "-F", f"signature={signature}",
                "-F", f"file=@{path}",
            ],
            capture_output=True, text=True,
        )
        code = proc.stdout.strip()
        ok = code == "204"
        print(f"  [{i:2}/{len(rows)}] {code}  {entry['filename']:52} {size/1048576:6.2f} MB"
              f"{'' if ok else '   FAILED: ' + proc.stderr[:120]}")

        results.append({
            "external_video_id": ext_id,
            "resourceUrl": f"{BUCKET}?external_video_id={ext_id}",
            "filename": entry["filename"],
            "alt": entry["alt"],
            "local": entry["local"],
            "hash": entry["hash"],
            "bytes": size,
            "uploaded": ok,
        })

    OUT.write_text(json.dumps(results, indent=1, ensure_ascii=False), encoding="utf-8")
    good = sum(1 for r in results if r["uploaded"])
    print(f"\nuploaded {good}/{len(results)}  -> {OUT.relative_to(ROOT)}")
    leftover = [p["local"] for group in by_size.values() for p in group]
    if leftover:
        print(f"unmatched local files ({len(leftover)}): {', '.join(leftover)}")


if __name__ == "__main__":
    main()
