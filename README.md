# JobFeed Web — remote job search demo

A searchable web frontend over the [jobfeed](../jobfeed) aggregator database. Live demo of
"data extraction → clean UI" — exactly the kind of deliverable clients pay for.

Two modes:
1. **Flask app (live DB)**: `python app.py` → serves a search UI + `/api/jobs?q=...` backed by the
   SQLite store.
2. **Static (GitHub Pages)**: `python export_json.py` produces `data/jobs.json`; the same frontend
   auto-falls back to it when the API is unavailable.

## Run locally
```bash
pip install -r requirements.txt
cd ../jobfeed && ../venv/bin/python -m jobfeed.cli fetch   # optional: refresh data
python export_json.py      # snapshot for static mode
python app.py              # http://localhost:8001
```

## Stack
Python, Flask, SQLite (via the jobfeed package), vanilla JS (no build step).
