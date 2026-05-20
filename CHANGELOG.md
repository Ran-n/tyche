# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Build

- GitHub Pages: simplified workflow to upload pre-built `web/` dir, removing Flutter/Python build steps (2026-05-20)
- GitLab Pages: switched to `alpine:3.21` image, serving pre-built `web/index.html` without flet/uv (2026-05-20)
- Added pre-built `web/index.html` to repository (2026-05-20)
- GitLab Pages deployment via `flet publish` (2026-05-19)

### Documentation

- README title linked to GitHub repository (2026-05-20)
- `pyproject.toml` description filled in (2026-05-20)

### Fixed

- Relax Pillow constraint for Pyodide compatibility (2026-05-19)
- Exclude Pillow from web build (2026-05-19)
- Drop `--flutter-path` flag, unsupported in flet 0.84.0 (2026-05-19)

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
