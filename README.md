# jayeshluthra.com

[![Deploy](https://github.com/j-s-l-7/Jayesh-Luthra/actions/workflows/pages.yml/badge.svg)](https://github.com/j-s-l-7/Jayesh-Luthra/actions/workflows/pages.yml)
[![Live](https://img.shields.io/badge/live-jayeshluthra.com-1d1d1f)](https://jayeshluthra.com)

The personal site of Jayesh Luthra. It currently shows a minimal greeting page and **opens on February 6, 2027**.

It is a single static HTML file with no build step and no framework, hosted for free on GitHub Pages.

---

## Design

- **Minimal by intent.** White page, near-black type, soft grey supporting text, and lots of empty space.
- **System typography.** Apple's San Francisco font on Apple devices, with [Inter](https://rsms.me/inter/) as a near-identical fallback everywhere else.
- **Fluid on every screen.** Type and spacing scale with both viewport width and height (`clamp()` + `min(vw, vh)`), so it reads well on small phones, landscape phones, tablets and desktops. Content stays clear of the iPhone notch and home bar.
- **Accessible motion.** A gentle fade-in that is switched off for visitors whose device is set to reduce motion.

## Repository layout

```
.
├── index.html               # The whole page: markup + inline CSS
├── reports/                 # Agent reports, published as-is (see below)
│   ├── manifest.json        # Index of report dates per agent
│   ├── leading-indicators/  # YYYY-MM-DD.html
│   └── research-agent/      # YYYY-MM-DD.html
├── CNAME                    # Custom domain for GitHub Pages
├── .nojekyll                # Serve files as-is (skip Jekyll)
└── .github/workflows/
    └── pages.yml            # Deploy to GitHub Pages on every push to main
```

## Deployment

Every push to `main` runs [`pages.yml`](.github/workflows/pages.yml), which:

1. Copies **only** the public files (`index.html`, `reports/`, `CNAME`, `.nojekyll`) into `_site/`.
2. Publishes `_site/` to GitHub Pages.

Nothing else in the repo (README, workflows) is ever served. A deploy takes about 30 seconds, and the latest run is shown in the badge above.

### Hosting setup (already done)

| Setting | Value |
| --- | --- |
| Pages source | GitHub Actions |
| Custom domain | `jayeshluthra.com` (HTTPS enforced) |
| DNS (GoDaddy) apex `A` | `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153` |
| DNS (GoDaddy) `www` `CNAME` | `j-s-l-7.github.io` |

## Agent reports

Two automated agents publish daily reports into this repo:

| Agent | Repo | Published at |
| --- | --- | --- |
| Leading Indicators | `j-s-l-7/Leading-Indicators` | `jayeshluthra.com/reports/leading-indicators/YYYY-MM-DD.html` |
| Research Agent | `j-s-l-7/Distribution-Research---Analyez` | `jayeshluthra.com/reports/research-agent/YYYY-MM-DD.html` |

After each run, the agent's workflow uses the `JAYESH_LUTHRA_PAT` secret to commit its report to `reports/<agent>/`, update `reports/manifest.json`, and push to `main`. That push triggers a deploy. Reports are self-contained HTML and keep their own styling.

The homepage does not link to the reports until launch. They are still reachable by direct URL.

## Editing the page

Everything lives in [`index.html`](index.html). To preview locally:

```bash
python3 -m http.server 8000   # then open http://localhost:8000
```

Commit and push to `main` to go live.
