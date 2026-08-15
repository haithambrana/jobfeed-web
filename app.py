import json
import os
import sys

from flask import Flask, jsonify, render_template, request

sys.path.insert(0, os.environ.get("JOBFEED_PATH", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "jobfeed")))
from jobfeed import storage  # noqa: E402

app = Flask(__name__)
DATA_JSON = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "jobs.json")


def _rows_to_dicts(rows):
    out = []
    for r in rows:
        out.append({
            "source_id": r[0],
            "title": r[1],
            "company": r[2],
            "url": r[3],
            "location": r[4],
            "summary": r[5],
            "tags": (r[6].split(",") if r[6] else []),
            "published": r[7],
        })
    return out


def _snapshot_dicts():
    if not os.path.exists(DATA_JSON):
        return []
    with open(DATA_JSON, encoding="utf-8") as f:
        return json.load(f)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/jobs")
def api_jobs():
    q = request.args.get("q", "").strip()
    limit = request.args.get("limit", 50, type=int)
    try:
        rows = storage.search(q.split() if q else [], limit)
        jobs = _rows_to_dicts(rows)
        source = "live"
    except Exception:
        jobs = _snapshot_dicts()
        if q:
            jobs = [j for j in jobs if q.lower() in (j.get("title", "") + " " + j.get("summary", "") + " " + " ".join(j.get("tags", []))).lower()]
        source = "snapshot"
    return jsonify({"source": source, "total": len(jobs), "jobs": jobs})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001, debug=False)
