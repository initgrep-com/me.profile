# CLAUDE.md

## Project Overview

This is a **static personal resume/portfolio website** for Irshad Sheikh, deployed to [me.initgrep.com](https://me.initgrep.com) via GitHub Pages. It is a single-page site with no build step, no package manager, and no backend.

## Repository Structure

```
me.profile/
├── .github/
│   └── workflows/
│       └── static.yml       # GitHub Actions: deploys to GitHub Pages on push to main
├── CNAME                     # Custom domain config: me.initgrep.com
├── index.html                # Production page (minified, single-line HTML)
├── draft.html                # Source/working page (formatted, readable HTML)
├── fav.svg                   # Favicon (radiation icon, SVG)
└── irshad-sheikh_cv.pdf      # Downloadable CV document
```

## Technology Stack

- **HTML5** with semantic elements (`header`, `nav`, `section`, `footer`, `article`, `time`)
- **TailwindCSS** via CDN (`https://cdn.tailwindcss.com`) — no local install
- **Lucide Icons** via CDN (`https://unpkg.com/lucide@latest`) — initialized with `lucide.createIcons()`
- **No JavaScript framework** — vanilla JS only (single icon init call)
- **No package.json / npm** — all dependencies are CDN-loaded

## Development Workflow

### Editing Content

1. **Edit `draft.html`** — this is the readable, properly formatted source file (554 lines)
2. **Minify into `index.html`** — the production file is a minified version of `draft.html`
3. Both files must stay in sync; `draft.html` is the source of truth

### Key Conventions

- **Dark theme**: `bg-neutral-900` background, `text-gray-300` body text
- **Accent colors**: green (`text-green-400`) for section headings, blue (`text-blue-400`) for links, cyan (`text-cyan-400`) for metadata
- **Skill badges**: `px-3 py-1 rounded-full bg-neutral-800 text-sm`
- **Experience cards**: `bg-neutral-800 rounded-xl p-4 shadow`
- **Icons**: Use `<i data-lucide="icon-name">` with `aria-hidden="true"`, `focusable="false"`, `role="presentation"` for accessibility
- **External links**: Always use `target="_blank"` and `class="text-blue-400 hover:underline"`

### Icons Used (Lucide)

`map-pin`, `mail`, `linkedin`, `github`, `download`, `speech`, `lightbulb`, `layout-list`, `puzzle`, `graduation-cap`, `building-2`, `hourglass`, `university`

## Deployment

- **Platform**: GitHub Pages
- **Trigger**: Push to `main` branch (automatic via `.github/workflows/static.yml`)
- **Custom domain**: `me.initgrep.com` (configured via `CNAME` file)
- **Process**: The entire repository is uploaded as a static artifact and deployed — no build step

## Accessibility Standards

The site follows accessibility best practices:
- `aria-label` on navigation and experience sections
- `aria-hidden="true"` on decorative icons
- `focusable="false"` and `role="presentation"` on icon elements
- Semantic `<time datetime="...">` elements for dates
- Proper heading hierarchy (`h1` > `h2` > `h3`)

## SEO

- `<meta name="description">` tag present
- JSON-LD structured data (`schema.org/Person`) in `<head>`
- Semantic HTML throughout

## Important Notes

- There is **no build process, test suite, or linter** — this is a pure static HTML project
- The entire site loads from CDNs; there are no local dependencies to install
- When modifying content, always update `draft.html` first, then produce the minified `index.html`
- The `irshad-sheikh_cv.pdf` is linked from the "Download Resume" button in the header
- Copyright notice in the footer should be kept current
