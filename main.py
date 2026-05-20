#!/usr/bin/env python3
"""
Authors: Ran# <ran.hash@proton.me>
Created: 2026/04/26 19:07:46.747401
Revised: 2026/05/20 08:33:02.374446
"""

import logging
import random
import shutil
from pathlib import Path

import flet as ft

STRINGS = {
    "en": {
        "subtitle": "random number selector",
        "pick_n": "quantity",
        "from_m": "total",
        "replacement": "replacement",
        "draw": "Draw",
        "clear": "Clear",
        "hint": "press Draw to pick numbers",
        "err_int": "N and M must be whole numbers.",
        "err_zero": "N and M must be greater than zero.",
        "err_range": "Can't pick {n} unique numbers from 1…{m}.",
        "tip_n": "Quantity — how many numbers to draw",
        "tip_m": "Total — size of the pool",
    },
    "es": {
        "subtitle": "selector de números aleatorios",
        "pick_n": "cantidad",
        "from_m": "total",
        "replacement": "repetición",
        "draw": "Sortear",
        "clear": "Limpiar",
        "hint": "pulsa Sortear para elegir números",
        "err_int": "N y M deben ser números enteros.",
        "err_zero": "N y M deben ser mayores que cero.",
        "err_range": "No se pueden elegir {n} números únicos del 1…{m}.",
        "tip_n": "Cantidad — cuántos números sortear",
        "tip_m": "Total — tamaño del grupo",
    },
    "gl": {
        "subtitle": "selector de números aleatorios",
        "pick_n": "cantidade",
        "from_m": "total",
        "replacement": "repetición",
        "draw": "Sortear",
        "clear": "Limpar",
        "hint": "preme Sortear para escoller números",
        "err_int": "N e M deben ser números enteiros.",
        "err_zero": "N e M deben ser maiores que cero.",
        "err_range": "Non se poden escoller {n} números únicos do 1…{m}.",
        "tip_n": "Cantidade — cantos números sortear",
        "tip_m": "Total — tamaño do grupo",
    },
    "eo": {
        "subtitle": "hazarda nombro-elektilo",
        "pick_n": "kvanto",
        "from_m": "totalo",
        "replacement": "ripeto",
        "draw": "Tiri",
        "clear": "Forigi",
        "hint": "premu Tiri por elekti nombrojn",
        "err_int": "N kaj M devas esti entjeroj.",
        "err_zero": "N kaj M devas esti pli grandaj ol nulo.",
        "err_range": "Ne eblas elekti {n} unikajn nombrojn el 1…{m}.",
        "tip_n": "Kvanto — kiom da nombroj tiri",
        "tip_m": "Totalo — grando de la grupo",
    },
}

LANGS = [
    ("en", "flag_en.svg"),
    ("gl", "flag_gl.svg"),
    ("es", "flag_es.svg"),
    ("eo", "flag_eo.svg"),
]


def main(page: ft.Page):
    page.title = "Tyche"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#080810"
    page.padding = 0
    page.window.icon = "assets/icon.ico"
    page.window.min_width = 480
    page.fonts = {"mono": "Courier New"}

    selected: list[int] = []
    lang = page.client_storage.get("lang") or "en"

    def t(key: str, **kwargs) -> str:
        s = STRINGS[lang][key]
        return s.format(**kwargs) if kwargs else s

    COLORS = [
        "#818cf8",
        "#a78bfa",
        "#e879f9",
        "#38bdf8",
        "#34d399",
        "#fb923c",
        "#f472b6",
        "#facc15",
        "#ef4444",
        "#22d3ee",
    ]

    def pill_color(idx: int) -> str:
        return COLORS[idx % len(COLORS)]

    # ── input fields ───────────────────────────────────────────────────────
    field_style = dict(
        width=120,
        text_align=ft.TextAlign.CENTER,
        keyboard_type=ft.KeyboardType.NUMBER,
        text_size=24,
        border=ft.InputBorder.UNDERLINE,
        border_color="#2a2a45",
        focused_border_color="#a78bfa",
        color="white",
        bgcolor="transparent",
        label_style=ft.TextStyle(size=13, color="#7c6af7", weight=ft.FontWeight.W_500),
    )

    n_field = ft.TextField(
        label=t("pick_n"),
        value=page.client_storage.get("n") or "6",
        tooltip=t("tip_n"),
        **field_style,
    )
    m_field = ft.TextField(
        label=t("from_m"),
        value=page.client_storage.get("m") or "10",
        tooltip=t("tip_m"),
        **field_style,
    )

    replacement_toggle = ft.Switch(
        label=t("replacement"),
        value=page.client_storage.get("replacement")
        if page.client_storage.contains_key("replacement")
        else False,
        active_color="#a78bfa",
        inactive_thumb_color="#2a2a45",
    )

    error_text = ft.Text(
        "",
        color="#f87171",
        size=12,
        visible=False,
        text_align=ft.TextAlign.CENTER,
    )

    # ── chip builder ───────────────────────────────────────────────────────
    def build_chip(number: int, idx: int) -> ft.Container:
        color = pill_color(idx)
        return ft.Column(
            [
                ft.Text(
                    f"#{idx + 1}",
                    size=10,
                    color=color + "99",
                    weight=ft.FontWeight.W_600,
                    text_align=ft.TextAlign.CENTER,
                    font_family="mono",
                ),
                ft.Container(
                    content=ft.Text(
                        str(number),
                        size=28,
                        weight=ft.FontWeight.BOLD,
                        color="white",
                        font_family="mono",
                        text_align=ft.TextAlign.CENTER,
                    ),
                    width=86,
                    height=86,
                    border_radius=20,
                    bgcolor="#0a0a18",
                    border=ft.Border.all(1.5, color + "88"),
                    shadow=ft.BoxShadow(
                        spread_radius=0,
                        blur_radius=24,
                        color=color + "33",
                        offset=ft.Offset(0, 4),
                    ),
                    alignment=ft.Alignment.CENTER,
                    animate=ft.Animation(250, ft.AnimationCurve.EASE_OUT),
                ),
            ],
            spacing=5,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

    result_wrap = ft.Row(
        wrap=True,
        spacing=16,
        run_spacing=16,
        alignment=ft.MainAxisAlignment.CENTER,
    )

    empty_hint_text = ft.Text(
        t("hint"),
        color="#2a2a45",
        size=13,
        text_align=ft.TextAlign.CENTER,
    )

    def empty_hint_column():
        return ft.Column(
            [
                ft.Icon(ft.Icons.CASINO_ROUNDED, color="#1c1c35", size=52),
                empty_hint_text,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,
            expand=True,
        )

    result_area = ft.Container(
        content=empty_hint_column(),
        expand=True,
        border_radius=20,
        bgcolor="#07070f",
        border=ft.Border.all(1, "#14142a"),
        padding=ft.Padding.symmetric(horizontal=24, vertical=24),
        margin=ft.Margin(left=0, right=0, top=0, bottom=0),
    )

    def refresh_ui():
        if selected:
            result_wrap.controls = [
                build_chip(num, i) for i, num in enumerate(selected)
            ]
            result_area.content = ft.Column(
                [result_wrap],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                scroll=ft.ScrollMode.AUTO,
                expand=True,
            )
        else:
            result_wrap.controls = []
            result_area.content = empty_hint_column()
        page.update()

    # ── handlers ───────────────────────────────────────────────────────────
    def on_draw(e):
        error_text.visible = False
        try:
            n = int(n_field.value or 0)
            m = int(m_field.value or 0)
        except ValueError:
            error_text.value = t("err_int")
            error_text.visible = True
            page.update()
            return
        if n <= 0 or m <= 0:
            error_text.value = t("err_zero")
            error_text.visible = True
            page.update()
            return
        if not replacement_toggle.value and n > m:
            error_text.value = t("err_range", n=n, m=m)
            error_text.visible = True
            page.update()
            return

        page.client_storage.set("n", str(n))
        page.client_storage.set("m", str(m))
        page.client_storage.set("replacement", replacement_toggle.value)
        nonlocal selected
        population = list(range(1, m + 1))
        selected = (
            [random.choice(population) for _ in range(n)]
            if replacement_toggle.value
            else random.sample(population, n)
        )
        refresh_ui()

    def on_clear(e):
        nonlocal selected
        selected = []
        error_text.visible = False
        refresh_ui()

    # ── buttons ────────────────────────────────────────────────────────────
    def icon_text_row(icon, label, color):
        return ft.Row(
            [
                ft.Icon(icon, color=color, size=16),
                ft.Text(label, color=color, weight=ft.FontWeight.W_600, size=14),
            ],
            spacing=8,
            tight=True,
        )

    draw_btn = ft.Button(
        content=icon_text_row(ft.Icons.CASINO_ROUNDED, t("draw"), "white"),
        bgcolor="#5b48e0",
        on_click=on_draw,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=12),
            padding=ft.Padding.symmetric(horizontal=36, vertical=16),
            overlay_color="#7c6af718",
            shadow_color="#5b48e044",
            elevation=4,
        ),
    )
    clear_btn = ft.Button(
        content=icon_text_row(ft.Icons.CLOSE_ROUNDED, t("clear"), "#555577"),
        bgcolor="#0d0d1a",
        on_click=on_clear,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=12),
            padding=ft.Padding.symmetric(horizontal=28, vertical=16),
            side=ft.BorderSide(1, "#222240"),
            overlay_color="#ffffff08",
        ),
    )

    # ── language switcher ──────────────────────────────────────────────────
    dropdown_open = False

    def lang_svg(code: str) -> str:
        return next(svg for c, svg in LANGS if c == code)

    def make_dropdown_item(code: str) -> ft.Container:
        return ft.Container(
            content=ft.Image(src=lang_svg(code), width=26, height=17),
            on_click=lambda _, c=code: select_lang(c),
            border_radius=5,
            bgcolor="transparent",
            padding=ft.Padding.symmetric(horizontal=6, vertical=4),
            animate=ft.Animation(120, ft.AnimationCurve.EASE_OUT),
            tooltip=code.upper(),
        )

    current_flag = ft.Container(
        content=ft.Image(src=lang_svg(lang), width=26, height=17),
        on_click=lambda _: toggle_dropdown(),
        border_radius=6,
        bgcolor="#0f0f1e",
        border=ft.Border.all(1, "#222240"),
        padding=ft.Padding.symmetric(horizontal=7, vertical=5),
        animate=ft.Animation(120, ft.AnimationCurve.EASE_OUT),
        tooltip=lang.upper(),
    )

    dropdown_col = ft.Column(controls=[], spacing=4, tight=True)
    dropdown_panel = ft.Container(
        content=dropdown_col,
        bgcolor="#0a0a18",
        border=ft.Border.all(1, "#222240"),
        border_radius=8,
        padding=ft.Padding.symmetric(horizontal=4, vertical=4),
        visible=False,
        animate=ft.Animation(150, ft.AnimationCurve.EASE_OUT),
    )

    lang_widget = ft.Column(
        [current_flag, dropdown_panel],
        spacing=4,
        tight=True,
        horizontal_alignment=ft.CrossAxisAlignment.END,
    )

    def toggle_dropdown():
        nonlocal dropdown_open
        dropdown_open = not dropdown_open
        if dropdown_open:
            dropdown_col.controls = [
                make_dropdown_item(c) for c, _ in LANGS if c != lang
            ]
        dropdown_panel.visible = dropdown_open
        page.update()

    def select_lang(code: str):
        nonlocal lang, dropdown_open
        lang = code
        page.client_storage.set("lang", code)
        dropdown_open = False
        dropdown_panel.visible = False
        current_flag.content = ft.Image(src=lang_svg(lang), width=26, height=17)
        current_flag.tooltip = lang.upper()
        n_field.label = t("pick_n")
        n_field.tooltip = t("tip_n")
        m_field.label = t("from_m")
        m_field.tooltip = t("tip_m")
        replacement_toggle.label = t("replacement")
        empty_hint_text.value = t("hint")
        subtitle_text.value = t("subtitle")
        draw_btn.content = icon_text_row(ft.Icons.CASINO_ROUNDED, t("draw"), "white")
        clear_btn.content = icon_text_row(ft.Icons.CLOSE_ROUNDED, t("clear"), "#555577")
        if error_text.visible:
            error_text.visible = False
        page.update()

    # ── header ─────────────────────────────────────────────────────────────
    subtitle_text = ft.Text(
        t("subtitle"),
        size=12,
        color="#383858",
        text_align=ft.TextAlign.CENTER,
        style=ft.TextStyle(letter_spacing=1),
    )

    header = ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "TYCHE",
                    size=48,
                    weight=ft.FontWeight.W_800,
                    color="#6d59f0",
                    text_align=ft.TextAlign.CENTER,
                    style=ft.TextStyle(letter_spacing=8),
                ),
                subtitle_text,
            ],
            spacing=2,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=ft.Padding(left=0, right=0, top=40, bottom=4),
    )

    # ── controls card ──────────────────────────────────────────────────────
    controls_card = ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    [n_field, m_field, replacement_toggle],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=20,
                    wrap=True,
                ),
                ft.Row(
                    [draw_btn, clear_btn],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=10,
                ),
                error_text,
            ],
            spacing=20,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=ft.Padding.symmetric(horizontal=32, vertical=24),
        border_radius=16,
        bgcolor="#09091a",
        border=ft.Border.all(1, "#14142a"),
    )

    # ── content column (max-width centred) ─────────────────────────────────
    content = ft.Column(
        [
            header,
            controls_card,
            result_area,
            ft.Container(height=28),
        ],
        spacing=16,
        horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
        expand=True,
    )

    # ── keyboard shortcuts ─────────────────────────────────────────────────
    def on_keyboard(e: ft.KeyboardEvent):
        if e.key == "Escape":
            if dropdown_open:
                toggle_dropdown()
            else:
                on_clear(None)

    page.on_keyboard_event = on_keyboard

    # ── layout ─────────────────────────────────────────────────────────────
    page.add(
        ft.Stack(
            [
                ft.Row(
                    [
                        ft.Container(
                            content=content,
                            width=780,
                            padding=ft.Padding.symmetric(horizontal=32),
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    expand=True,
                ),
                ft.Container(
                    content=lang_widget,
                    right=16,
                    top=14,
                ),
            ],
            expand=True,
        )
    )


class _DropDisconnect(logging.Filter):
    _NOISE = ("ClientDisconnected", "WebSocketDisconnect", "ConnectionClosedOK")

    def filter(self, record: logging.LogRecord) -> bool:
        msg = record.getMessage()
        return not any(kw in msg for kw in self._NOISE)


for _logger in ("uvicorn.error", "uvicorn.access"):
    logging.getLogger(_logger).addFilter(_DropDisconnect())

try:
    import flet_web

    _loading_target = (
        Path(flet_web.__file__).parent / "web" / "icons" / "loading-animation.png"
    )
    shutil.copy(Path(__file__).parent / "assets" / "icon.png", _loading_target)
except Exception:
    pass

app = ft.run(
    main, assets_dir=str(Path(__file__).parent / "assets"), export_asgi_app=True
)

if __name__ == "__main__":
    ft.run(main, assets_dir=str(Path(__file__).parent / "assets"))
