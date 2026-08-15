import json
import os
import sys

sys.path.insert(0, os.environ.get("JOBFEED_PATH", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "jobfeed")))
from jobfeed import storage  # noqa: E402

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "jobs.json")

rows = storage.search([], 2000)
jobs = []
for r in rows:
    jobs.append({
        "title": r[1],
        "company": r[2],
        "url": r[3],
        "location": r[4],
        "summary": r[5],
        "tags": (r[6].split(",") if r[6] else []),
        "published": r[7],
    })

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(jobs, f, ensure_ascii=False, indent=1)

print(f"exported {len(jobs)} jobs -> {OUT}")
