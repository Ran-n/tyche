# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Build

- `pyproject.toml`: add PEP 621 metadata — readme, license, authors, keywords, classifiers, project URLs, ruff config (2026-05-20)
- GitHub Pages: fix workflow trigger branch `master` → `main` (2026-05-20)
- GitLab Pages: fix pipeline rule branch `master` → `main` (2026-05-20)
- GitHub Pages: simplified workflow to upload pre-built `web/` dir, removing Flutter/Python build steps (2026-05-20)
- GitLab Pages: switched to `alpine:3.21` image, serving pre-built `web/index.html` without flet/uv (2026-05-20)
- Added pre-built `web/index.html` to repository (2026-05-20)
- GitLab Pages deployment via `flet publish` (2026-05-19)

### Documentation

- README title linked to GitHub repository (2026-05-20)
- `pyproject.toml` description filled in (2026-05-20)

### Added

- Persist language selection across sessions via `localStorage` (web) and `page.client_storage` (desktop) (2026-05-20)
- Persist quantity, total, and replacement toggle across sessions (2026-05-20)
- `[project.scripts]` entry `tyche = "main:run"` for pip-installed invocation (2026-05-20)
- Migrate persistence layer from `client_storage` to `shared_preferences` async API (2026-05-20)
- `run()` wrapper function; `__main__` block delegates to it (2026-05-20)

### Build

- Switch build backend from virtual to hatchling; add `[build-system]` and `[tool.hatch.build.targets.wheel]` (2026-05-20)
- Drop Pillow dependency (2026-05-20)
- Set `[tool.uv] package = true` (2026-05-20)
- Bump `line-length` from 88 to 120 (2026-05-20)

### Fixed

- Relax Pillow constraint for Pyodide compatibility (2026-05-19)
- Exclude Pillow from web build (2026-05-19)
- Drop `--flutter-path` flag, unsupported in flet 0.84.0 (2026-05-19)

### Changed

- Restyle web UI with the Gruvbox palette and a breren-style light/dark toggle (2026-08-05)
- Rework language picker to breren's trigger + listbox pattern, with browser-language auto-detection (2026-08-05)
- Light mode uses a neutral white/grey page instead of Gruvbox's cream `bg0`, keeping accents (orange, chip colors) authentically Gruvbox (2026-08-05)

## [0.1.0] — 2026-04-27

### Added

- Initial random number draw application (2026-04-26)
- GitHub Pages deployment via `flet build web` (2026-04-27)
- Esperanto language support (2026-04-27)
- Languages section in README with keyboard shortcut docs (2026-04-27)

### Changed

- Fixed-width container alignment in layout (2026-04-26)
- Desktop launch via `python main.py` (2026-04-27)
- Languages table with flags, Galician listed first (2026-04-27)

### Documentation

- README: name, description, run commands (2026-04-27)
