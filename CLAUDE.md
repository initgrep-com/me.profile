# CLAUDE.md

Static personal resume for Irshad Sheikh, deployed at [me.initgrep.com](https://me.initgrep.com) via GitHub Pages. Single-page, data-driven via YAML + Jinja2 template.

## Files

| File | Purpose |
|------|---------|
| `resume.yaml` | All resume content — **edit this to change data** |
| `resume.schema.json` | JSON Schema for `resume.yaml` (validation + editor autocomplete) |
| `templates/base.html` | Jinja2 HTML template — **edit this for layout/style changes** |
| `build.py` | Reads YAML + template, writes `index.html` |
| `index.html` | Generated output (committed, served by GH Pages) — **do not edit directly** |
| `.githooks/pre-commit` | Auto-runs `build.py` on commit |
| `requirements.txt` | Python deps: pyyaml, jinja2, jsonschema |
| `irshad-sheikh_cv.pdf` | Downloadable CV |
| `fav.svg` | Favicon |

## Workflow

1. Edit `resume.yaml` for content changes (new experience, updated skills, etc.)
2. Edit `templates/base.html` for layout/style changes
3. `git commit` — pre-commit hook runs `build.py` automatically, regenerates and stages `index.html`
4. Push to `main` — GitHub Pages serves the static `index.html`

**Manual build:** `python build.py` (requires venv: `source .venv/bin/activate`)

**Setup:** `python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt && git config core.hooksPath .githooks`

## Tech Stack (all CDN, no local deps)

- **DaisyUI v5** — components (`card`, `badge`, `btn`, `link`)
- **Tailwind CSS v4** — utilities
- **Lucide Icons** — `<i data-lucide="icon-name" aria-hidden="true">`, init via `lucide.createIcons()`
- **Vanilla JS** — theme toggle + icon init only
- **Python + Jinja2** — local build only (not deployed)

## Theme System

- Light: `lofi` | Dark: `halloween` | System: OS `prefers-color-scheme`
- Toggle cycles: system → lofi → halloween → system
- Persisted in `localStorage` key `theme`; IIFE in `<head>` prevents flash

## CSS Conventions

- Section cards: `card bg-base-200 shadow-sm` + `card-body`
- Section headings: `card-title` with `w-10 h-10 rounded-full bg-{color}/10` icon circle
- Skill/meta badges: `badge badge-ghost`
- List bullets: `flex items-start gap-2` with `chevron-right` Lucide icon
- Links: `link link-primary` + `target="_blank"`
- Colors: use semantic (`bg-base-100`, `text-base-content`) — no hardcoded colors

## Experience Weight System

Each experience entry in `resume.yaml` has a `weight` field controlling web view appearance:
- `prominent`: large timeline dot (w-3.5), ring-2, primary-colored chevrons (recent/current roles)
- `standard`: medium dot (w-3 or w-2.5), ring-2 or ring-1, muted chevrons (mid-career)
- `compact`: small dot (w-2), condensed inline layout, muted text (early career)

ATS print view renders all entries identically regardless of weight.

## Deployment

Push to `main` → GitHub Pages serves directly from branch root. No CI/CD build — the build runs locally via pre-commit hook.

**GitHub Pages setting**: Repo Settings → Pages → Source → "Deploy from branch" → main → /(root).
