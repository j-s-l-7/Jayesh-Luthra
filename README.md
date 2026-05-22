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

This repo deploys to **GitHub Pages** via `.github/workflows/pages.yml`. Every
push to `main` triggers the workflow, which uploads the repo root as a static
site artifact and publishes it to Pages. The `CNAME` file points the site at
`jayeshluthra.com`. No build step.

`deploy.py` is kept around as a fallback for one-off manual deploys via the
Vercel REST API.

## Required setup (one-time)

1. **Enable Pages** in repo Settings → Pages → Build and deployment → Source:
   "GitHub Actions". Custom domain auto-detects from the `CNAME` file in the
   repo root; tick "Enforce HTTPS" once the cert provisions (~10 min).
2. **DNS** at your registrar — point `jayeshluthra.com` at GitHub Pages:
   - Apex `A` records: `185.199.108.153`, `185.199.109.153`, `185.199.110.153`,
     `185.199.111.153`.
   - Optional `AAAA` (IPv6): `2606:50c0:8000::153`, `2606:50c0:8001::153`,
     `2606:50c0:8002::153`, `2606:50c0:8003::153`.
   - `www` CNAME → `j-s-l-7.github.io`.
3. **Create a GitHub PAT** with `contents: write` scope on this repo
   (fine-grained, limited to this single repo).
4. **Add the PAT as `JAYESH_LUTHRA_PAT`** to both agent repos' Actions secrets:
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
