# nabla-b.engineering

Website of **nabla B Ingenieurbüro und Dienstleistungs-UG (haftungsbeschränkt)**, Bochum.
Static, hosted on GitHub Pages, custom domain `nabla-b.engineering` (see `CNAME`).

## Editing

All content (DE/EN/ZH), the reference list, the blog posts (`POSTS`) and the JSON-LD live in **`build.py`**.
Blog posts are short company-perspective summaries (< 400 words per language, enforced by an assert) of articles on maxclerkwell.tech; each links to its original via `orig` and JSON-LD `isBasedOn`.
After changing it, regenerate the HTML and commit everything:

```sh
python3 build.py     # no dependencies, Python ≥ 3.8
git add -A && git commit -m "content: …" && git push
```

Generated files: `index.html`, `*/index.html`, `en/**`, `zh/**`, `sitemap.xml`, `llms.txt`, `robots.txt`, `404.html`.
Do not edit those by hand.

## Corporate design

- Colour: `#323942` (nabla B grey) and tints 80/60/40/20 % — nothing else besides black/white.
- Font: CMU Bright Roman (body) / CMU Bright SemiBold (emphasis), self-hosted as woff2 in `assets/fonts/`.
- Logo: `assets/img/logo.svg` (word-picture mark, from `NablaB_logo.ai`). Never invert, rotate or put on coloured background.
- Manual: `assets/nablaB-corporate-design.pdf` (internal; not linked from the site).

## Structure

| DE | EN | ZH |
|---|---|---|
| `/` | `/en/` | `/zh/` |
| `/leistungen/` | `/en/services/` | `/zh/services/` |
| `/referenzen/` | `/en/references/` | `/zh/references/` |
| `/blog/`, `/blog/<slug>/` | `/en/blog/…` | `/zh/blog/…` |
| `/team/` | `/en/team/` | `/zh/team/` |
| `/kontakt/` | `/en/contact/` | `/zh/contact/` |
| `/impressum/` | `/en/imprint/` | `/zh/imprint/` |
| `/datenschutz/` | `/en/privacy/` | `/zh/privacy/` |

Entity IDs used in JSON-LD (keep stable, they are referenced from maxclerkwell.tech and edge-compute.skainet.io):
`https://nabla-b.engineering/#organization`, `https://maxclerkwell.tech/#person`, `https://edge-compute.skainet.io/team#tabea-boekelmann`.
