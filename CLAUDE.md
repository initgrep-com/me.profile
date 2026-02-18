# CLAUDE.md

Static personal resume for Irshad Sheikh, deployed at [me.initgrep.com](https://me.initgrep.com) via GitHub Pages. Single-page, no build step, no npm.

## Files

| File | Purpose |
|------|---------|
| `index.html` | Single source — **edit this directly** |
| `irshad-sheikh_cv.pdf` | Downloadable CV |
| `fav.svg` | Favicon |

**Workflow**: Edit `index.html` directly. No separate draft/production split.

## Tech Stack (all CDN, no local deps)

- **DaisyUI v5** — components (`card`, `badge`, `btn`, `link`)
- **Tailwind CSS v4** — utilities
- **Lucide Icons** — `<i data-lucide="icon-name" aria-hidden="true">`, init via `lucide.createIcons()`
- **Vanilla JS** — theme toggle + icon init only

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

## Deployment

Push to `main` → GitHub Pages serves directly from branch root. No build step, no Actions workflow.

**GitHub Pages setting**: Repo Settings → Pages → Source → "Deploy from branch" → main → /(root).
