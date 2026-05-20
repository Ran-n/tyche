[//]: # ( ---------------------------------------------------------------------- )
[//]: # (+ Authors: 	Ran# <ran.hash@proton.me> )
[//]: # (+ Created: 	2026/04/26 20:50:05.000000 )
[//]: # (+ Revised: 	2026/05/19 23:34:30.416907 )
[//]: # ( ---------------------------------------------------------------------- )

# [Tyche](https://github.com/Ran-n/tyche)

Tyche (Τύχη) was the Greek goddess of fortune, luck, and chance — the force that governed the unpredictable outcomes of human affairs. In art she is often depicted holding a rudder, steering fate, and a cornucopia overflowing with the bounty she might bestow or withhold. The name is a fitting one for a tool whose sole purpose is to let chance decide.

A cross-platform random number selector built with [Flet](https://flet.dev). Runs as a native desktop app or in the browser. Draws **N** numbers from a pool of **1…M** — configurable on every run. Sampling can be done with or without replacement, making it suitable for lotteries, random assignments, statistical sampling, and any other scenario where unbiased selection matters. Results are displayed as ordered, color-coded chips and can be redrawn or cleared instantly. The interface is available in Galician, English, Spanish, and Esperanto.

## Usage

**Desktop**

```
python main.py
```

**Web (dev server)**

```
flet run --web main.py
```

## Languages

The interface is available in the following languages, selectable at runtime via a flag dropdown:

| Flag | Code | Language |
|---|---|---|
| ![](assets/flag_gl.svg) | `gl` | Galician |
| ![](assets/flag_en.svg) | `en` | English |
| ![](assets/flag_es.svg) | `es` | Spanish |
| ![](assets/flag_eo.svg) | `eo` | Esperanto |

## Options

| Field | Default | Description |
|---|---|---|
| N | 6 | How many numbers to draw |
| M | 10 | Upper bound of the range (1…M) |
| Replacement | off | Allow the same number to appear more than once |

## Requirements

- Python ≥ 3.12
- [uv](https://github.com/astral-sh/uv)
- [Flet](https://flet.dev) ≥ 0.84.0

Dependencies are declared in `pyproject.toml` and resolved automatically by uv.

## License

[PayBack License (PBL)](LICENSE)
