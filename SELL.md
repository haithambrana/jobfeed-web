# JobFeed — Self-Hosted Remote Job Board (product)

> Turn any niche into a searchable job board in minutes. Aggregates remote jobs from 5 public
> feeds, deduplicates them into SQLite, and serves a fast searchable web UI. No SaaS fees, no
> per-job costs — you own the whole thing.

## Live demo
https://haithambrana.github.io/jobfeed-web/ (static snapshot) — the same frontend, live.

## What you get
- Full Python source (the `jobfeed` aggregator engine + `jobfeed-web` Flask app)
- Docker + docker-compose — deploy on any VPS with one command
- SQLite storage, deduplication, keyword search, CSV export
- Daily refresh scheduling (cron example included)
- Telegram bot digest (optional, needs a BotFather token)
- MIT-style license, no platform lock-in

## Sources (public APIs/feeds)
RemoteOK · We Work Remotely · Remotive · Jobicy · Mostaql (Arabic)
Easily extended in `jobfeed/sources.py`.

## Stack
Python 3, Flask, SQLite, requests, feedparser, vanilla JS. No build step.

## Quick start
```bash
docker compose up --build        # http://localhost:8001
# or without Docker:
pip install -r jobfeed/requirements.txt -r jobfeed-web/requirements.txt
python -m jobfeed.cli fetch && python app.py
```

## Ideas to customize
- Change the sources (drop Mostaql, add a niche board)
- Rebrand the UI (`templates/index.html`)
- Add email alerts, filters, or an RSS output
- Use it as a landing page + search for a community niche

## Pricing on the sales listing
Suggested: $29 USD (single license). Free updates.
