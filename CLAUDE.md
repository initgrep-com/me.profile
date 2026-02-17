# CLAUDE.md

## Project Overview

This is a **static personal resume/portfolio website** for Irshad Sheikh, deployed to [me.initgrep.com](https://me.initgrep.com) via GitHub Pages. It is a single-page site with no build step, no package manager, and no backend. The design mirrors the theme system used on [initgrep.com](https://www.initgrep.com).

## Repository Structure

```
me.profile/
├── .github/
│   └── workflows/
│       └── static.yml       # GitHub Actions: deploys to GitHub Pages on push to main
├── CNAME                     # Custom domain config: me.initgrep.com
├── index.html                # Production page (minified version of draft.html)
├── draft.html                # Source/working page (formatted, readable HTML)
├── fav.svg                   # Favicon (radiation icon, SVG)
└── irshad-sheikh_cv.pdf      # Downloadable CV document
```

## Technology Stack

- **HTML5** with semantic elements (`header`, `nav`, `section`, `footer`, `article`, `time`)
- **DaisyUI v5** via CDN (`https://cdn.jsdelivr.net/npm/daisyui@5`) — component library
- **Tailwind CSS v4** via CDN (`https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4`) — utility CSS
- **Lucide Icons** via CDN (`https://unpkg.com/lucide@latest`) — initialized with `lucide.createIcons()`
- **No JavaScript framework** — vanilla JS for theme toggling and icon initialization
- **No package.json / npm** — all dependencies are CDN-loaded

## Theme System

The site uses DaisyUI's theming with two themes and system detection:

- **Light theme**: `lofi` (DaisyUI built-in)
- **Dark theme**: `halloween` (DaisyUI built-in)
- **System**: Follows OS `prefers-color-scheme` preference

### Theme Toggle

- Cycle order: **system** → **lofi** (light) → **halloween** (dark) → back to system
- Icons per state: `monitor` (system), `sun` (lofi/light), `moon` (halloween/dark)
- Persisted in `localStorage` under the key `theme`
- Flash prevention: inline IIFE in `<head>` sets `data-theme` before paint
- System preference listener: auto-updates when OS theme changes (if set to system)

### Theme Colors (DaisyUI semantic)

- Use `bg-base-100`, `bg-base-200`, `text-base-content` instead of hardcoded colors
- Section heading icons use colored circles: `bg-primary/10`, `bg-secondary/10`, `bg-accent/10`, `bg-info/10`, `bg-success/10`
- Links use `link link-primary` classes
- Badges use `badge badge-ghost`

## Development Workflow

### Editing Content

1. **Edit `draft.html`** — this is the readable, properly formatted source file
2. **Minify into `index.html`** — the production file is a minified version of `draft.html`
3. Both files must stay in sync; `draft.html` is the source of truth

### Key Conventions

- **Section cards**: `card bg-base-200 shadow-sm` with `card-body`
- **Section headings**: `card-title` with a colored icon circle (`w-10 h-10 rounded-full bg-{color}/10`)
- **Skill badges**: `badge badge-ghost` (DaisyUI)
- **Experience metadata**: `badge badge-ghost gap-1` with inline Lucide icons
- **List items**: `flex items-start gap-2` with `chevron-right` icon bullets
- **Icons**: Use `<i data-lucide="icon-name" aria-hidden="true">` for accessibility
- **External links**: Use `link link-primary` class and `target="_blank"`
- **Sticky navbar**: `sticky top-0 z-50 bg-base-100 border-b border-base-200`

### Icons Used (Lucide)

`terminal`, `download`, `sun`, `moon`, `monitor`, `map-pin`, `mail`, `linkedin`, `github`, `speech`, `lightbulb`, `code`, `layers`, `cloud`, `database`, `test-tubes`, `git-branch`, `puzzle`, `layout-list`, `building-2`, `hourglass`, `chevron-right`, `external-link`, `graduation-cap`, `university`

## Deployment

- **Platform**: GitHub Pages
- **Trigger**: Push to `main` branch (automatic via `.github/workflows/static.yml`)
- **Custom domain**: `me.initgrep.com` (configured via `CNAME` file)
- **Process**: The entire repository is uploaded as a static artifact and deployed — no build step

## Accessibility Standards

The site follows accessibility best practices:
- `aria-label` on navigation and experience sections
- `aria-hidden="true"` on decorative icons
- Semantic `<time datetime="...">` elements for dates
- Proper heading hierarchy (`h1` > `h2` > `h3`)
- Theme toggle has `aria-label="Toggle theme"`

## SEO

- `<meta name="description">` tag present
- JSON-LD structured data (`schema.org/Person`) in `<head>`
- `<meta name="theme-color">` dynamically updated per theme
- Semantic HTML throughout

## Important Notes

- There is **no build process, test suite, or linter** — this is a pure static HTML project
- The entire site loads from CDNs; there are no local dependencies to install
- When modifying content, always update `draft.html` first, then produce the minified `index.html`
- The `irshad-sheikh_cv.pdf` is linked from the "Resume" button in the navbar
- Copyright notice in the footer should be kept current
- Smooth theme transitions are applied via CSS `transition` on key elements
