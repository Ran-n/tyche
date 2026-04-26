# Tyche

Random number selector desktop app built with [Flet](https://flet.dev).

Pick **N** numbers from **1…M**, with or without replacement. Results are displayed as styled chips with color-coded order indicators. The UI is available in English, Spanish, and Galician.

## Usage

```
uv run main.py
```

## Options

| Field | Default | Description |
|---|---|---|
| N | 6 | How many numbers to draw |
| M | 10 | Upper bound of the range (1…M) |
| Replacement | off | Allow the same number to appear more than once |

## Requirements

- Python ≥ 3.12
- [uv](https://github.com/astral-sh/uv)

Dependencies are declared in `pyproject.toml` and resolved automatically by uv.

## License

[PayBack License (PBL)](LICENSE)
