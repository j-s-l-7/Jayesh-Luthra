# Jayesh Luthra — Personal Landing Page

A minimalist landing page for [jayeshluthra.com](https://jayeshluthra.com). The
hero shows **"making machines"** with a bouncing-dots loader. Below the hero,
two columns — **Leading Indicators** and **Research Agent** — list dated links
to the reports those two cron-driven agents produce. Each link opens that day's
full report (the agent's own design, untouched).

## File structure

```
.
├── index.html                  # hero + two-column index that reads manifest.json
├── style.css                   # tokens, hero, columns
├── deploy.py                   # legacy: direct Vercel API deploy (kept for manual pushes)
└── reports/
    ├── manifest.json           # { "leading-indicators": [...], "research-agent": [...] }
    ├── leading-indicators/     # YYYY-MM-DD.html files pushed by the LI workflow
    └── research-agent/         # YYYY-MM-DD.html files pushed by the RA workflow
```

## How content gets here

Both agent repos run on GitHub Actions cron schedules. After each successful
run, the workflow:

1. Saves the generated HTML to `out/YYYY-MM-DD.html`.
2. Clones this repo (`j-s-l-7/Jayesh-Luthra`) using the `JAYESH_LUTHRA_PAT`
   secret it has stored.
3. Drops the file at `reports/<source>/YYYY-MM-DD.html`.
4. Updates `reports/manifest.json` (sorted newest-first, deduped).
5. Commits and pushes to `main`. On push conflict (because both workflows can
   race), it rebases and retries up to 5 times.

Each agent's report HTML is fully self-contained — it embeds its own `<style>`
block, so the design of a Leading Indicators report stays Leading Indicators,
and a Research Agent report stays Research Agent. The landing page never
restyles their content.

## Deployment

This repo is connected to Vercel via the Git integration. Every push to `main`
triggers an auto-redeploy. No manual step needed.

`deploy.py` is kept around for one-off manual deploys (e.g. if you ever
disconnect Git integration); it uses the Vercel REST API with a token.

## Required setup (one-time)

1. **Connect this repo to Vercel** via the Vercel dashboard → Add New Project →
   Import `j-s-l-7/Jayesh-Luthra`. No framework, no build step.
2. **Create a GitHub PAT** with `contents: write` scope on this repo (a
   fine-grained PAT limited to this single repo is recommended).
3. **Add the PAT as `JAYESH_LUTHRA_PAT`** to both agent repos' Actions secrets:
   - `j-s-l-7/Leading-Indicators` → Settings → Secrets → Actions
   - `j-s-l-7/Distribution-Research---Analyez` → Settings → Secrets → Actions

## Local development

Open `index.html` directly in a browser (no build step). The JS will fetch
`reports/manifest.json` from the same directory — if you want to preview with a
real path layout, run any static server, e.g.:

```bash
python3 -m http.server 8000
```

then visit `http://localhost:8000/`.
