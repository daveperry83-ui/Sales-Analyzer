"""Robertet LATAM — Sales Analytics · build de un solo archivo.

Generado por build_single_file.py — no editar a mano; edita el paquete y
vuelve a generar.

Despliegue: sube SOLO este archivo y requirements.txt. No hay carpetas que
puedan faltar, así que el ModuleNotFoundError de arranque no puede ocurrir.
El logo va embebido en base64.
"""

from __future__ import annotations

import sys
import types

import streamlit as st

# --------------------------------------------------------------------------- #
# Dependency preflight: a missing package here would otherwise surface as a
# redacted ModuleNotFoundError pointing at a line inside a bundled module.
# --------------------------------------------------------------------------- #
_REQUIRED = {
    "pandas": "pandas>=2.2",
    "numpy": "numpy>=1.26",
    "plotly": "plotly>=5.24",
    "openpyxl": "openpyxl>=3.1",
}

_missing = []
for _mod, _spec in _REQUIRED.items():
    try:
        __import__(_mod)
    except ImportError:
        _missing.append((_mod, _spec))

if _missing:
    _names = ", ".join(f"`{m}`" for m, _ in _missing)
    _lines = "\n".join(spec for _, spec in _missing)
    st.error(
        f"**Faltan dependencias: {_names}.**\n\n"
        "El repositorio necesita un archivo `requirements.txt` junto a este "
        "archivo .py, con este contenido:\n\n"
        "```\nstreamlit>=1.60\npandas>=2.2\nnumpy>=1.26\nplotly>=5.24\n"
        "openpyxl>=3.1\n```\n\n"
        "Súbelo al repositorio y en Streamlit Cloud usa **Manage app → Reboot** "
        "para que reinstale.",
        icon="📦",
    )
    st.stop()

_MODULES: dict[str, str] = {}

_MODULES["core.theme"] = r'''"""Robertet visual identity: navy #002856, plus a data palette built around it."""

from __future__ import annotations

import base64
from pathlib import Path

import plotly.graph_objects as go
import plotly.io as pio

NAVY = "#002856"
NAVY_DARK = "#001A38"
NAVY_MID = "#14507E"
AZURE = "#2E7EB3"
SKY = "#6BA8D0"
MIST = "#A9CBE3"
PAPER = "#FFFFFF"
CANVAS = "#F5F7FA"
INK = "#1B2530"
MUTED = "#6B7A88"
RULE = "#DDE3EA"

POSITIVE = "#1F7A5A"
NEGATIVE = "#B03A2E"
WARNING = "#C08A2E"
NEUTRAL = "#8896A4"

# Categorical series palette — navy-anchored, distinguishable in greyscale.
CATEGORICAL = [
    NAVY, "#2E7EB3", "#0F7C7B", "#C08A2E", "#A8452F",
    "#6E8B5A", "#6B4A6E", "#5B6B7C", "#6BA8D0", "#8C6B3F",
]

SEQUENTIAL = [[0.0, "#EAF1F7"], [0.25, MIST], [0.5, SKY], [0.75, AZURE], [1.0, NAVY]]
DIVERGING = [[0.0, NEGATIVE], [0.35, "#E5B4AC"], [0.5, "#F2F4F6"],
             [0.65, "#A8CFBE"], [1.0, POSITIVE]]

FONT = "Inter, Segoe UI, Helvetica Neue, Arial, sans-serif"


def register_template() -> None:
    tpl = go.layout.Template()
    tpl.layout = go.Layout(
        font=dict(family=FONT, size=13, color=INK),
        paper_bgcolor=PAPER,
        plot_bgcolor=PAPER,
        colorway=CATEGORICAL,
        title=dict(font=dict(size=17, color=NAVY), x=0, xanchor="left", pad=dict(b=12)),
        margin=dict(l=8, r=8, t=56, b=8),
        xaxis=dict(gridcolor=RULE, zerolinecolor=RULE, linecolor=RULE,
                   ticks="outside", tickcolor=RULE, automargin=True),
        yaxis=dict(gridcolor=RULE, zerolinecolor="#C3CCD6", linecolor=RULE,
                   ticks="outside", tickcolor=RULE, automargin=True),
        legend=dict(orientation="h", yanchor="bottom", y=1.0, xanchor="left", x=0,
                    bgcolor="rgba(0,0,0,0)", font=dict(size=12)),
        hoverlabel=dict(bgcolor=PAPER, bordercolor=RULE,
                        font=dict(family=FONT, size=12, color=INK)),
        colorscale=dict(sequential=SEQUENTIAL, diverging=DIVERGING),
    )
    pio.templates["robertet"] = tpl
    pio.templates.default = "robertet"


_LOGO_B64 = "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"


def logo_data_uri() -> str | None:
    return ("data:image/png;base64," + _LOGO_B64) if _LOGO_B64 else None


CSS = f"""
<style>
  .stApp {{ background: {CANVAS}; }}
  section[data-testid="stSidebar"] {{ background: {PAPER}; border-right: 1px solid {RULE}; }}
  h1, h2, h3 {{ color: {NAVY}; font-family: {FONT}; letter-spacing: -0.01em; }}
  .rb-header {{
      display: flex; align-items: center; gap: 1.25rem;
      padding: 0.5rem 0 1rem 0; border-bottom: 2px solid {NAVY}; margin-bottom: 1rem;
  }}
  .rb-header img {{ height: 34px; }}
  .rb-header .rb-title {{ font-family: {FONT}; color: {NAVY};
      font-size: 1.05rem; font-weight: 600; letter-spacing: 0.02em; }}
  .rb-header .rb-sub {{ color: {MUTED}; font-size: 0.8rem; }}
  .rb-privacy {{
      background: #EAF1F7; border-left: 3px solid {NAVY}; color: {NAVY};
      padding: 0.55rem 0.9rem; border-radius: 4px; font-size: 0.82rem; margin-bottom: 1rem;
  }}
  .rb-card {{
      background: {PAPER}; border: 1px solid {RULE}; border-radius: 8px;
      padding: 0.9rem 1rem; height: 100%;
  }}
  .rb-card .rb-label {{ color: {MUTED}; font-size: 0.74rem; text-transform: uppercase;
      letter-spacing: 0.06em; margin-bottom: 0.2rem; }}
  .rb-card .rb-value {{ color: {NAVY}; font-size: 1.55rem; font-weight: 650; line-height: 1.1; }}
  .rb-card .rb-delta {{ font-size: 0.8rem; margin-top: 0.35rem; }}
  .rb-up {{ color: {POSITIVE}; }} .rb-down {{ color: {NEGATIVE}; }} .rb-flat {{ color: {MUTED}; }}
  .rb-note {{ color: {MUTED}; font-size: 0.82rem; margin: -0.4rem 0 0.9rem 0; }}
  .rb-chip {{ display:inline-block; padding: 0.12rem 0.5rem; border-radius: 999px;
      font-size: 0.7rem; font-weight: 600; letter-spacing: 0.03em; }}
  .rb-chip-ok {{ background:#E4F1EB; color:{POSITIVE}; }}
  .rb-chip-warn {{ background:#FAF0DC; color:{WARNING}; }}
  .rb-chip-bad {{ background:#F7E4E1; color:{NEGATIVE}; }}
  div[data-testid="stMetricValue"] {{ color: {NAVY}; }}
  .stTabs [data-baseweb="tab-list"] {{ gap: 0.35rem; border-bottom: 1px solid {RULE}; }}
  .stTabs [data-baseweb="tab"] {{ font-family: {FONT}; font-size: 0.9rem; }}
  .stTabs [aria-selected="true"] {{ color: {NAVY} !important; font-weight: 600; }}
</style>
"""


# --- formatters -------------------------------------------------------------
def money(v, decimals: int = 0) -> str:
    if v is None or (isinstance(v, float) and v != v):
        return "—"
    return f"${v:,.{decimals}f}"


def money_compact(v) -> str:
    if v is None or (isinstance(v, float) and v != v):
        return "—"
    a = abs(v)
    if a >= 1_000_000:
        return f"${v/1_000_000:,.2f} MM"
    if a >= 1_000:
        return f"${v/1_000:,.0f} K"
    return f"${v:,.0f}"


def pct(v, decimals: int = 1) -> str:
    if v is None or (isinstance(v, float) and v != v):
        return "—"
    return f"{v*100:,.{decimals}f}%"


def pp(v, decimals: int = 1) -> str:
    if v is None or (isinstance(v, float) and v != v):
        return "—"
    return f"{v:+,.{decimals}f} pp"


def qty(v, unit: str = "kg") -> str:
    if v is None or (isinstance(v, float) and v != v):
        return "—"
    return f"{v:,.0f} {unit}"


def unit_value(v) -> str:
    if v is None or (isinstance(v, float) and v != v):
        return "—"
    return f"${v:,.2f}"


def signed(v, formatter=money_compact) -> str:
    if v is None or (isinstance(v, float) and v != v):
        return "—"
    return ("+" if v >= 0 else "−") + formatter(abs(v))


FORMATTERS = {
    "money": money_compact,
    "pct": pct,
    "qty": qty,
    "unit": unit_value,
    "int": lambda v: "—" if v is None or v != v else f"{v:,.0f}",
}
'''

_MODULES["core.i18n"] = r'''"""Bilingual strings for the whole app — labels, chart titles and prose.

`t("key", value=…)` returns the string for the active language and applies
`str.format` with whatever keyword arguments are passed, so sentences that embed
numbers stay translatable instead of being concatenated in code.
"""

from __future__ import annotations

import streamlit as st

STRINGS: dict[str, dict[str, str]] = {
    # ---------------------------------------------------------------- shell --
    "app_title":       {"es": "Análisis de Ventas LATAM", "en": "LATAM Sales Analytics"},
    "app_sub":         {"es": "Ventas · Margen · Budget — sesión efímera",
                        "en": "Sales · Margin · Budget — ephemeral session"},
    "privacy_banner":  {"es": "🔒 Datos en memoria. Nada se guarda en disco y todo se elimina al cerrar la sesión.",
                        "en": "🔒 Data in memory. Nothing is written to disk; everything is erased when the session closes."},
    "language":        {"es": "Idioma", "en": "Language"},
    "cancel":          {"es": "Cancelar", "en": "Cancel"},
    "none":            {"es": "(ninguna)", "en": "(none)"},
    "empty_all":       {"es": "Vacío = todos", "en": "Empty = all"},

    # --------------------------------------------------------------- upload --
    "upload_title":    {"es": "Cargar archivos", "en": "Load files"},
    "upload_ytd":      {"es": "Archivo YTD (año actual vs año anterior)",
                        "en": "YTD file (current vs prior year)"},
    "upload_fy":       {"es": "Archivo histórico / Full Year (multi-año)",
                        "en": "Historical / Full Year file (multi-year)"},
    "upload_help":     {"es": "Export del BI en Excel. La app reconoce el formato aunque cambien nombres de columna, el idioma o el orden.",
                        "en": "BI export in Excel. The app recognises the layout even if column names, language or order change."},
    "upload_error":    {"es": "No se pudo leer {name}: {error}",
                        "en": "Could not read {name}: {error}"},
    "processing":      {"es": "Procesando {name}…", "en": "Processing {name}…"},
    "file_loaded":     {"es": "{label}: {rows} filas · {y0}–{y1}",
                        "en": "{label}: {rows} rows · {y0}–{y1}"},
    "no_files":        {"es": "Carga al menos un archivo para comenzar.",
                        "en": "Load at least one file to begin."},
    "file_ytd":        {"es": "Archivo YTD", "en": "YTD file"},
    "file_fy":         {"es": "Archivo histórico / Full Year",
                        "en": "Historical / Full Year file"},

    # -------------------------------------------------------------- session --
    "session":         {"es": "Sesión", "en": "Session"},
    "clear_all":       {"es": "🗑️ Borrar todo", "en": "🗑️ Clear everything"},
    "clear_confirm":   {"es": "Confirmar borrado", "en": "Confirm deletion"},
    "clear_warning":   {"es": "Se eliminarán los archivos y todo el análisis de esta sesión.",
                        "en": "This removes the files and every analysis in this session."},
    "cleared":         {"es": "Sesión borrada. No queda ningún dato en memoria.",
                        "en": "Session cleared. No data remains in memory."},
    "idle_left":       {"es": "Auto-borrado en", "en": "Auto-wipe in"},
    "idle_timeout":    {"es": "Minutos de inactividad antes del borrado",
                        "en": "Idle minutes before wipe"},
    "auto_wiped":      {"es": "La sesión se borró automáticamente por inactividad.",
                        "en": "Session was wiped automatically after inactivity."},

    # -------------------------------------------------------------- welcome --
    "how_title":       {"es": "Cómo funciona", "en": "How it works"},
    "how_1":           {"es": "**1 · Carga**\n\nDos exports del BI: el YTD del año en curso contra el año anterior, y el histórico multi-año / Full Year. Puedes trabajar con uno solo, con funcionalidad reducida.",
                        "en": "**1 · Load**\n\nTwo BI exports: the current year to date against the prior year, and the multi-year / Full Year history. One file alone works too, with reduced functionality."},
    "how_2":           {"es": "**2 · Filtra**\n\nEnciende y apaga métricas, cambia la agrupación, acota clientes y familias. Todo el tablero reacciona, como una tabla dinámica.",
                        "en": "**2 · Filter**\n\nSwitch metrics on and off, change the grouping, narrow customers and families. The whole board reacts, like a pivot table."},
    "how_3":           {"es": "**3 · Decide**\n\nPuentes de precio, volumen y costo; desviaciones ordenadas por dólares; y bullets de estrategia calculados sobre tu filtro.",
                        "en": "**3 · Decide**\n\nPrice, volume and cost bridges; deviations ranked by dollars; and strategy bullets computed on your filter."},
    "privacy_long":    {"es": "**Privacidad.** Los archivos se procesan en memoria. No se escribe nada en disco, no hay base de datos y no queda historial. Al cerrar la pestaña, al cumplirse el tiempo de inactividad o al pulsar «Borrar todo», no queda rastro.",
                        "en": "**Privacy.** Files are processed in memory. Nothing is written to disk, there is no database and no history is kept. Closing the tab, hitting the idle timeout or pressing “Clear everything” leaves no trace."},

    # -------------------------------------------------------------- filters --
    "comparison":      {"es": "Base de comparación", "en": "Comparison basis"},
    "data_source":     {"es": "Fuente de datos", "en": "Data source"},
    "current_year":    {"es": "Año actual", "en": "Current year"},
    "base_year":       {"es": "Año base", "en": "Base year"},
    "dimensions":      {"es": "Dimensiones", "en": "Dimensions"},
    "group_by":        {"es": "Agrupar por", "en": "Group by"},
    "second_dim":      {"es": "Dimensión secundaria", "en": "Secondary dimension"},
    "filter_customer": {"es": "Filtrar cliente (grupo)", "en": "Filter customer (group)"},
    "filter_customer_help": {"es": "Vacío = todos. Filtra por grupo para conservar el budget, que se carga a ese nivel.",
                             "en": "Empty = all. Filter by group to keep the budget, which is loaded at that level."},
    "filter_account":  {"es": "…o cuentas dentro del grupo", "en": "…or accounts within the group"},
    "filter_account_help": {"es": "Vacío = todas las cuentas del grupo. El budget del grupo se conserva.",
                            "en": "Empty = every account in the group. The group budget is preserved."},
    "filter_active":   {"es": "🔎 Filtro activo · {n} filas", "en": "🔎 Filter active · {n} rows"},
    "filter_family":   {"es": "Filtrar familias", "en": "Filter families"},
    "top_n":           {"es": "Top N en gráficos", "en": "Top N in charts"},
    "metrics":         {"es": "Métricas (encender / apagar)", "en": "Metrics (on / off)"},
    "metrics_help":    {"es": "Apaga lo que no quieras ver; desaparece de KPIs, gráficos y tablas.",
                        "en": "Switch off what you don't want; it disappears from KPIs, charts and tables."},
    "basis":           {"es": "Base de cálculo", "en": "Calculation basis"},
    "include_open":    {"es": "Incluir cartera abierta (Sold & Open)",
                        "en": "Include open orders (Sold & Open)"},
    "include_open_help": {"es": "Suma los pedidos ya tomados y aún no facturados a ventas, profit y volumen.",
                          "en": "Adds orders already booked but not yet invoiced to sales, profit and volume."},
    "materiality":     {"es": "Umbral de materialidad (USD)", "en": "Materiality threshold (USD)"},
    "materiality_help": {"es": "Oculta líneas por debajo de este monto en ambos períodos.",
                         "en": "Hides lines below this amount in both periods."},
    "unit":            {"es": "Unidad de volumen", "en": "Volume unit"},
    "budget_level_note": {"es": "ℹ️ El budget viene cargado a nivel grupo, no por cuenta individual: en esta agrupación las comparaciones vs budget quedan desactivadas.",
                          "en": "ℹ️ Budget is loaded at group level, not per individual account: budget comparisons are disabled in this grouping."},

    # ----------------------------------------------------------------- tabs --
    "tab_overview":    {"es": "Resumen", "en": "Overview"},
    "tab_backlog":     {"es": "Cartera", "en": "Backlog"},
    "tab_fy":          {"es": "YTD vs Full Year", "en": "YTD vs Full Year"},
    "tab_customers":   {"es": "Clientes", "en": "Customers"},
    "tab_products":    {"es": "Productos", "en": "Products"},
    "tab_deviations":  {"es": "Desviaciones", "en": "Deviations"},
    "tab_strategy":    {"es": "Estrategia", "en": "Strategy"},
    "tab_data":        {"es": "Datos y calidad", "en": "Data & quality"},

    # ------------------------------------------------------------- grouping --
    "level_enterprise":     {"es": "Cliente (grupo)", "en": "Customer (group)"},
    "level_customer":       {"es": "Cliente (cuenta)", "en": "Customer (account)"},
    "level_product_family": {"es": "Familia de producto", "en": "Product family"},
    "level_product":        {"es": "Producto", "en": "Product"},
    "level_item_code":      {"es": "Código de ítem", "en": "Item code"},

    # ------------------------------------------------------------- measures --
    "sales":           {"es": "Ventas", "en": "Sales"},
    "profit":          {"es": "Profit", "en": "Profit"},
    "margin":          {"es": "Margen", "en": "Margin"},
    "volume":          {"es": "Volumen", "en": "Volume"},
    "price":           {"es": "Precio", "en": "Price"},
    "budget":          {"es": "Budget", "en": "Budget"},
    "invoiced":        {"es": "Facturado", "en": "Invoiced"},
    "open_orders":     {"es": "Cartera abierta", "en": "Open orders"},
    "sold_open":       {"es": "Facturado + cartera", "en": "Invoiced + backlog"},
    "landing":         {"es": "Aterrizaje proyectado", "en": "Projected landing"},
    "achieved":        {"es": "Logrado", "en": "Achieved"},
    "missing":         {"es": "Falta", "en": "Remaining"},
    "rest":            {"es": "Resto", "en": "Rest"},
    "start":           {"es": "Inicio", "en": "Start"},
    "end":             {"es": "Final", "en": "End"},
    "real":            {"es": "Real", "en": "Actual"},

    # -------------------------------------------------------------- effects --
    "eff_volume":      {"es": "Efecto volumen", "en": "Volume effect"},
    "eff_price":       {"es": "Efecto precio", "en": "Price effect"},
    "eff_cost":        {"es": "Efecto costo", "en": "Cost effect"},
    "eff_new":         {"es": "Altas cliente-ítem", "en": "New customer-item"},
    "eff_lost":        {"es": "Bajas cliente-ítem", "en": "Lost customer-item"},
    "eff_other":       {"es": "Otros", "en": "Other"},

    # ------------------------------------------------------------- overview --
    "ov_title":        {"es": "Resumen {cur} vs {base}", "en": "Overview {cur} vs {base}"},
    "ov_note":         {"es": "Base: {basis} · Agrupación: {level} · {n} clientes en el filtro.",
                        "en": "Basis: {basis} · Grouping: {level} · {n} customers in the filter."},
    "basis_invoiced":  {"es": "facturado", "en": "invoiced"},
    "basis_sold_open": {"es": "facturado + cartera abierta", "en": "invoiced + open orders"},
    "ov_sales_bar":    {"es": "Ventas vs budget anual", "en": "Sales vs annual budget"},
    "ov_profit_bar":   {"es": "Profit vs budget anual", "en": "Profit vs annual budget"},
    "ov_qty_bar":      {"es": "Volumen vs budget anual", "en": "Volume vs annual budget"},
    "ov_pace_sub":     {"es": "marcador = ritmo esperado a esta altura",
                        "en": "marker = expected pace at this point"},
    "ov_sales_bridge": {"es": "Puente de ventas {base} → {cur}",
                        "en": "Sales bridge {base} → {cur}"},
    "ov_margin_bridge": {"es": "Puente de margen {base} → {cur}",
                         "en": "Margin bridge {base} → {cur}"},
    "ov_bridge_note":  {"es": "Las ventas {dir} {amount} ({pct}), con el {driver} como componente dominante ({value}).",
                        "en": "Sales {dir} {amount} ({pct}), with {driver} as the dominant component ({value})."},
    "dir_up":          {"es": "suben", "en": "rise"},
    "dir_down":        {"es": "caen", "en": "fall"},
    "ov_margin_note":  {"es": "Efecto precio {price} · efecto costo {cost}. El margen se mueve principalmente por {cause}.",
                        "en": "Price effect {price} · cost effect {cost}. Margin moves mainly on {cause}."},
    "cause_price":     {"es": "precio", "en": "price"},
    "cause_cost":      {"es": "costo unitario", "en": "unit cost"},
    "ov_budget_gap":   {"es": "Brecha vs budget por {level}", "en": "Budget gap by {level}"},
    "ov_backlog_card": {"es": "Cartera abierta vs brecha de budget",
                        "en": "Open orders vs budget gap"},
    "ov_backlog_delta": {"es": "cubre {pct} de la brecha de {gap}",
                         "en": "covers {pct} of the {gap} gap"},

    # -------------------------------------------------------------- backlog --
    "bl_title":        {"es": "Cartera abierta — pedidos tomados y aún no facturados",
                        "en": "Open orders — booked and not yet invoiced"},
    "bl_note":         {"es": "Es negocio ya ganado: el impacto que tendrá al facturarse, contra el budget y contra el año base.",
                        "en": "Business already won: the impact it will have once invoiced, against budget and against the base year."},
    "bl_none":         {"es": "El archivo activo no trae cartera abierta (columna Open Orders vacía o ausente).",
                        "en": "The active file carries no open orders (Open Orders column empty or absent)."},
    "bl_total":        {"es": "Cartera abierta total", "en": "Total open orders"},
    "bl_share":        {"es": "Cartera sobre facturado", "en": "Backlog over invoiced"},
    "bl_groups":       {"es": "{n} de {total} con cartera", "en": "{n} of {total} with backlog"},
    "bl_coverage":     {"es": "Cobertura de la brecha", "en": "Gap coverage"},
    "bl_coverage_sub": {"es": "brecha de budget {gap}", "en": "budget gap {gap}"},
    "bl_profit":       {"es": "Profit en cartera", "en": "Profit in backlog"},
    "bl_margin_sub":   {"es": "margen de cartera {pct}", "en": "backlog margin {pct}"},
    "bl_bridge":       {"es": "De lo facturado al budget: cuánto cierra la cartera",
                        "en": "From invoiced to budget: how much the backlog closes"},
    "bl_bridge_note":  {"es": "Facturado {inv} + cartera {open} = {so}, contra un budget de {bdg}. La cartera cubre {cov} de la brecha y deja {left} por conseguir.",
                        "en": "Invoiced {inv} + backlog {open} = {so}, against a budget of {bdg}. The backlog covers {cov} of the gap and leaves {left} still to win."},
    "bl_stack":        {"es": "Facturado y cartera por {level}", "en": "Invoiced and backlog by {level}"},
    "bl_rank":         {"es": "Mayor cartera abierta por {level}", "en": "Largest open orders by {level}"},
    "bl_effect":       {"es": "Efecto de la cartera sobre la variación vs {base}",
                        "en": "Backlog effect on the change vs {base}"},
    "bl_effect_note":  {"es": "Sin cartera la variación es {without}; con cartera pasa a {with_}. La cartera revierte el signo en {n} {level}.",
                        "en": "Without backlog the change is {without}; with backlog it becomes {with_}. Backlog flips the sign for {n} {level}."},
    "bl_table":        {"es": "Detalle de cartera", "en": "Backlog detail"},
    "bl_col_open":     {"es": "Cartera", "en": "Backlog"},
    "bl_col_share":    {"es": "% sobre facturado", "en": "% of invoiced"},
    "bl_col_so":       {"es": "Facturado + cartera", "en": "Invoiced + backlog"},
    "bl_col_cover":    {"es": "Avance con cartera", "en": "Attainment with backlog"},

    # ------------------------------------------------------------ full year --
    "fy_trend":        {"es": "Tendencia multi-año", "en": "Multi-year trend"},
    "fy_trend_note":   {"es": "Del archivo histórico, internamente consistente: años {y0}–{y1}. Bandas ocultas por vacías o parciales: {hidden}.",
                        "en": "From the historical file, internally consistent: years {y0}–{y1}. Bands hidden as empty or partial: {hidden}."},
    "fy_sales_year":   {"es": "Ventas por año", "en": "Sales by year"},
    "fy_sales_margin": {"es": "Ventas y margen por año", "en": "Sales and margin by year"},
    "fy_cagr":         {"es": "CAGR de ventas {y0}–{y1}: {cagr} · margen {m0} → {m1} ({pp}).",
                        "en": "Sales CAGR {y0}–{y1}: {cagr} · margin {m0} → {m1} ({pp})."},
    "fy_need_ytd":     {"es": "Carga también el archivo YTD para habilitar el forecast de aterrizaje.",
                        "en": "Load the YTD file as well to enable the landing forecast."},
    "fy_basis_warn":   {"es": "**Advertencia de base de fecha.** Los dos archivos no cuadran en {year}: {bad} grupos muestran un YTD mayor que su año completo, lo cual es imposible sobre una misma base. Se proyectan individualmente {ok} de {total} grupos; el resto usa el índice de cartera y queda marcado como indicativo. {match} coinciden exactamente entre archivos.",
                        "en": "**Date-basis warning.** The two files do not reconcile in {year}: {bad} groups show a YTD larger than their full year, which is impossible on a single basis. {ok} of {total} groups are projected individually; the rest use the portfolio index and are flagged as indicative. {match} match exactly across files."},
    "fy_share_done":   {"es": "% del FY {year} ya logrado", "en": "% of FY {year} achieved"},
    "fy_share_sub":    {"es": "ritmo del año pasado a esta altura: {pace}",
                        "en": "last year's pace at this point: {pace}"},
    "fy_attain":       {"es": "Avance de budget", "en": "Budget attainment"},
    "fy_pace_sub":     {"es": "pace esperado {pace}", "en": "expected pace {pace}"},
    "fy_landing_sub":  {"es": "{delta} vs budget", "en": "{delta} vs budget"},
    "fy_projectable":  {"es": "Grupos proyectables", "en": "Projectable groups"},
    "fy_inconsistent": {"es": "{n} con base inconsistente", "en": "{n} with inconsistent basis"},
    "fy_bullet":       {"es": "Aterrizaje {cur} vs budget y vs FY {prior}",
                        "en": "Landing {cur} vs budget and vs FY {prior}"},
    "fy_landing_by":   {"es": "Aterrizaje por {level}", "en": "Landing by {level}"},
    "fy_level_note":   {"es": "El budget está cargado a nivel grupo, así que el aterrizaje se calcula por Cliente (grupo) aunque estés agrupando por cuenta.",
                        "en": "Budget is loaded at group level, so the landing is computed by customer group even if you are grouping by account."},
    "fy_progress":     {"es": "Logrado vs objetivo (mayor entre budget y FY {prior})",
                        "en": "Achieved vs target (greater of budget and FY {prior})"},
    "fy_gap_chart":    {"es": "Brecha proyectada al cierre vs budget",
                        "en": "Projected year-end gap vs budget"},
    "fy_gap_note":     {"es": "{n} {level} proyectan cerrar por debajo del budget, por un total de {total}.",
                        "en": "{n} {level} are projected to close below budget, totalling {total}."},
    "fy_diag_title":   {"es": "Diagnóstico de base entre archivos (por qué algunos no se proyectan)",
                        "en": "Cross-file basis diagnosis (why some are not projected)"},
    "fy_diag_caption": {"es": "«Coincide» = misma cifra en ambos archivos. «Base inconsistente» = el YTD supera al año completo, señal de que los archivos usan campos de fecha distintos. Para eliminarlo por completo, exporta el Full Year del año anterior con el mismo reporte que genera el archivo YTD.",
                        "en": "“Matches” = same figure in both files. “Inconsistent basis” = YTD exceeds the full year, a sign the files use different date fields. To remove it entirely, export the prior Full Year from the same report that produces the YTD file."},

    # ----------------------------------------------------------- client tab --
    "tab_client":      {"es": "Ficha de cliente", "en": "Client sheet"},
    "cl_title":        {"es": "Ficha de cliente", "en": "Client sheet"},
    "cl_pick":         {"es": "Cliente (grupo)", "en": "Customer (group)"},
    "cl_note":         {"es": "Puesto {rank} de {total} por ventas · {share} de la facturación total · {accounts} cuenta(s): {names}",
                        "en": "Rank {rank} of {total} by sales · {share} of total billings · {accounts} account(s): {names}"},
    "cl_no_activity":  {"es": "{client} no tiene actividad en los años seleccionados.",
                        "en": "{client} has no activity in the selected years."},
    "cl_no_budget":    {"es": "sin budget cargado para este cliente",
                        "en": "no budget loaded for this customer"},
    "cl_budget_note":  {"es": "Faltan {gap} para el budget. Tiene {open} en cartera abierta, que cubre {cover} de esa brecha.",
                        "en": "{gap} short of budget. {open} sits in open orders, covering {cover} of that gap."},
    "cl_landing_note": {"es": "Aterrizaje {landing}, calculado con {source} ({index} del año se logra a esta altura). Brecha vs budget: {gap}.",
                        "en": "Landing {landing}, computed with {source} ({index} of the year is booked by this point). Gap vs budget: {gap}."},
    "cl_own_index":    {"es": "su propio índice de estacionalidad",
                        "en": "its own seasonality index"},
    "cl_portfolio_index": {"es": "el índice de la cartera (este cliente no es proyectable por sí solo)",
                           "en": "the portfolio index (this client is not projectable on its own)"},
    "cl_history":      {"es": "Historia del cliente por año", "en": "Client history by year"},
    "cl_why":          {"es": "Por qué se movió {delta}", "en": "Why it moved {delta}"},
    "cl_bridge_note":  {"es": "Volumen {volume} · precio {price}. El movimiento es sobre todo de {cause}.",
                        "en": "Volume {volume} · price {price}. The move is mostly {cause}."},
    "cl_products":     {"es": "Qué compra", "en": "What it buys"},
    "cl_alerts":       {"es": "Alertas de esta cuenta", "en": "Alerts for this account"},
    "cl_alert_lost":   {"es": "**{n} ítems dejaron de comprarse** ({total} el año base): {names}.",
                        "en": "**{n} items stopped being bought** ({total} in the base year): {names}."},
    "cl_alert_new":    {"es": "**{n} ítems nuevos** aportan {total} este período.",
                        "en": "**{n} new items** contribute {total} this period."},
    "cl_alert_margin": {"es": "**Margen {cur}** contra {base} del año base ({pp}).",
                        "en": "**Margin {cur}** against {base} in the base year ({pp})."},
    "cl_alert_price":  {"es": "**Caída de precio**: {name} baja {pct} sobre {sales} de ventas.",
                        "en": "**Price drop**: {name} down {pct} on {sales} of sales."},
    "cl_alert_backlog": {"es": "**{total} en cartera abierta** ya ganados, pendientes de embarque.",
                         "en": "**{total} in open orders** already won, awaiting shipment."},
    "cl_alert_gap":    {"es": "**Proyecta cerrar {total} por debajo de su budget.**",
                        "en": "**Projected to close {total} below its budget.**"},

    # ------------------------------------------------------------ dimension --
    "dim_title":       {"es": "{level} · {cur} vs {base}", "en": "{level} · {cur} vs {base}"},
    "dim_note":        {"es": "{n} registros en el filtro · {new} nuevos · {lost} perdidos · umbral de materialidad {mat}.",
                        "en": "{n} records in the filter · {new} new · {lost} lost · materiality threshold {mat}."},
    "no_threshold":    {"es": "sin umbral", "en": "none"},
    "dim_top_var":     {"es": "Mayores variaciones de ventas", "en": "Largest sales changes"},
    "dim_contrib":     {"es": "Contribución al delta por {level}", "en": "Contribution to the delta by {level}"},
    "dim_quadrant":    {"es": "Crecimiento vs margen por {level}", "en": "Growth vs margin by {level}"},
    "dim_quadrant_note": {"es": "Tamaño de burbuja = ventas del período actual. Cuadrante inferior derecho: crecen pero con margen bajo — candidatos a revisión de precio.",
                          "en": "Bubble size = current-period sales. Lower-right quadrant: growing but low margin — candidates for a price review."},
    "dim_treemap":     {"es": "Familias por ventas, coloreadas por variación de margen",
                        "en": "Families by sales, coloured by margin change"},
    "dim_scatter":     {"es": "Precio vs volumen — dónde subiste precio y perdiste kilos",
                        "en": "Price vs volume — where price went up and volume went down"},
    "dim_prod_bridge": {"es": "Puente de margen a nivel producto", "en": "Margin bridge at product level"},
    "dim_churn":       {"es": "⚠️ {n} {level} sin actividad en {year} — {amount} en juego",
                        "en": "⚠️ {n} {level} with no activity in {year} — {amount} at stake"},
    "dim_cross":       {"es": "Cruce {a} × {b}", "en": "Cross {a} × {b}"},
    "dim_cross_chart": {"es": "Variación % de ventas", "en": "Sales change %"},
    "dim_detail":      {"es": "Detalle", "en": "Detail"},
    "quad_stars":      {"es": "Estrellas", "en": "Stars"},
    "quad_defend":     {"es": "Defender margen", "en": "Defend margin"},
    "quad_price":      {"es": "Revisar precio", "en": "Review pricing"},
    "quad_rescue":     {"es": "Rescatar", "en": "Rescue"},
    "axis_growth":     {"es": "Crecimiento vs año base", "en": "Growth vs base year"},
    "axis_margin":     {"es": "Margen %", "en": "Margin %"},
    "axis_dprice":     {"es": "Δ precio unitario", "en": "Δ unit price"},
    "axis_dvolume":    {"es": "Δ volumen", "en": "Δ volume"},

    # ----------------------------------------------------------- deviations --
    "dev_title":       {"es": "Radar de desviaciones", "en": "Deviation radar"},
    "dev_note":        {"es": "Ordenado por impacto en dólares, no por porcentaje: una caída del 300% sobre una cuenta de 400 USD no debería encabezar ninguna lista.",
                        "en": "Ranked by dollar impact, not percentage: a 300% drop on a 400 USD account should not top any list."},
    "dev_type":        {"es": "Tipo de desviación", "en": "Deviation type"},
    "dev_direction":   {"es": "Dirección", "en": "Direction"},
    "dev_against":     {"es": "Medir contra", "en": "Measure against"},
    "dev_all":         {"es": "Todas", "en": "All"},
    "dev_negative":    {"es": "Negativas", "en": "Negative"},
    "dev_positive":    {"es": "Positivas", "en": "Positive"},
    "dev_base_year":   {"es": "Año base", "en": "Base year"},
    "dev_no_budget":   {"es": "El archivo activo no trae budget; se mide contra el año base.",
                        "en": "The active file has no budget; measuring against the base year."},
    "dev_neg_total":   {"es": "Desviación negativa total", "en": "Total negative deviation"},
    "dev_pos_total":   {"es": "Desviación positiva total", "en": "Total positive deviation"},
    "dev_net":         {"es": "Neto", "en": "Net"},
    "dev_records":     {"es": "{n} registros", "en": "{n} records"},
    "dev_against_sub": {"es": "contra {what}", "en": "against {what}"},
    "dev_top5":        {"es": "Concentración top 5", "en": "Top-5 concentration"},
    "dev_top5_sub":    {"es": "del movimiento absoluto", "en": "of absolute movement"},
    "dev_chart":       {"es": "Mayores desviaciones vs {what}", "en": "Largest deviations vs {what}"},
    "dev_compose":     {"es": "Composición de la desviación por tipo",
                        "en": "Deviation composition by type"},
    "dev_none":        {"es": "Ningún registro cumple estos criterios.",
                        "en": "No records match these criteria."},
    "type_churn":      {"es": "Pérdida de cliente", "en": "Customer loss"},
    "type_new":        {"es": "Cliente nuevo", "en": "New customer"},
    "type_volume":     {"es": "Volumen", "en": "Volume"},
    "type_price":      {"es": "Precio", "en": "Price"},
    "type_cost":       {"es": "Costo", "en": "Cost"},

    # ------------------------------------------------------------- strategy --
    "st_title":        {"es": "Estrategia y próximos pasos", "en": "Strategy and next steps"},
    "st_note":         {"es": "Generado sobre el filtro activo: {cur} vs {base}, agrupado por {level}. Cambia los filtros y los bullets se recalculan.",
                        "en": "Generated on the active filter: {cur} vs {base}, grouped by {level}. Change the filters and the bullets recompute."},
    "st_diagnosis":    {"es": "🔍 Diagnóstico", "en": "🔍 Diagnosis"},
    "st_diagnosis_c":  {"es": "Qué pasó, cuantificado.", "en": "What happened, quantified."},
    "st_risks":        {"es": "⚠️ Riesgos", "en": "⚠️ Risks"},
    "st_risks_c":      {"es": "Lo que puede empeorar si nadie actúa.",
                        "en": "What gets worse if nobody acts."},
    "st_opps":         {"es": "🌱 Oportunidades", "en": "🌱 Opportunities"},
    "st_opps_c":       {"es": "Dónde está el upside disponible.", "en": "Where the available upside is."},
    "st_actions":      {"es": "🎯 Acciones sugeridas", "en": "🎯 Suggested actions"},
    "st_actions_c":    {"es": "Priorizadas por dólares en juego.", "en": "Prioritised by dollars at stake."},
    "st_edit":         {"es": "Editar antes de exportar", "en": "Edit before exporting"},
    "st_dl_md":        {"es": "Descargar resumen (Markdown)", "en": "Download summary (Markdown)"},
    "st_dl_xlsx":      {"es": "Descargar bullets (Excel)", "en": "Download bullets (Excel)"},
    "st_report_title": {"es": "Análisis de ventas {cur} vs {base}", "en": "Sales analysis {cur} vs {base}"},
    "st_report_meta":  {"es": "_Generado {stamp} · agrupación por {level}_",
                        "en": "_Generated {stamp} · grouped by {level}_"},

    # ----------------------------------------------------------------- data --
    "dq_title":        {"es": "Datos y calidad", "en": "Data & quality"},
    "dq_note":         {"es": "El export del BI es una tabla dinámica con subtotales embebidos. Todo lo que ves se calcula sobre las filas hoja; los subtotales se recalculan, nunca se suman.",
                        "en": "The BI export is a pivot with embedded subtotals. Everything you see is computed on leaf rows; subtotals are recomputed, never summed."},
    "dq_not_loaded":   {"es": "{title}: no cargado.", "en": "{title}: not loaded."},
    "dq_rows":         {"es": "Filas en el archivo", "en": "Rows in the file"},
    "dq_leaves":       {"es": "Filas hoja analizadas", "en": "Leaf rows analysed"},
    "dq_pruned":       {"es": "Subtotales podados", "en": "Subtotals pruned"},
    "dq_bands":        {"es": "Bandas de año", "en": "Year bands"},
    "dq_recognised":   {"es": "Qué reconoció el parser", "en": "What the parser recognised"},
    "dq_sheet":        {"es": "Hoja", "en": "Sheet"},
    "dq_header_row":   {"es": "Fila de encabezado", "en": "Header row"},
    "dq_year_source":  {"es": "Origen del año", "en": "Year source"},
    "dq_dims":         {"es": "Dimensiones detectadas", "en": "Detected dimensions"},
    "dq_metrics":      {"es": "Métricas detectadas", "en": "Detected metrics"},
    "dq_ignored":      {"es": "Columnas ignoradas ({n})", "en": "Ignored columns ({n})"},
    "dq_notes":        {"es": "Notas de interpretación", "en": "Interpretation notes"},
    "dq_recon":        {"es": "Conciliación entre archivos · {year}",
                        "en": "Cross-file reconciliation · {year}"},
    "dq_match":        {"es": "Coinciden", "en": "Match"},
    "dq_coherent":     {"es": "Coherentes (YTD < FY)", "en": "Coherent (YTD < FY)"},
    "dq_inconsistent": {"es": "Base inconsistente", "en": "Inconsistent basis"},
    "dq_recon_error":  {"es": "El total {year} del archivo YTD ({ytd}) supera al del archivo Full Year ({fy}). Sobre una misma base de fecha esto es imposible, así que los dos exports usan campos distintos. El forecast lo maneja marcando cada grupo, pero la solución de fondo es exportar el Full Year del año anterior con el mismo reporte que genera el archivo YTD.",
                        "en": "The {year} total in the YTD file ({ytd}) exceeds the Full Year file ({fy}). On a single date basis that is impossible, so the two exports use different fields. The forecast handles it by flagging each group, but the real fix is to export the prior Full Year from the same report that produces the YTD file."},

    # ------------------------------------------------------------- insights --
    "ins_nodata":      {"es": "Sin datos suficientes para diagnosticar con los filtros actuales.",
                        "en": "Not enough data to diagnose with the current filters."},
    "ins_headline":    {"es": "**Ventas {cur}** contra {base} del año base: {delta} ({pct}).",
                        "en": "**Sales {cur}** against {base} in the base year: {delta} ({pct})."},
    "ins_driver":      {"es": "El movimiento lo explica sobre todo **{driver}** ({value}). Volumen {volume}, precio {price}.",
                        "en": "The move is driven mainly by **{driver}** ({value}). Volume {volume}, price {price}."},
    "ins_margin":      {"es": "**Margen {cur}** vs {base} ({pp}). El componente dominante es el **{cause}** (precio {price}, costo {cost} en profit).",
                        "en": "**Margin {cur}** vs {base} ({pp}). The dominant component is **{cause}** (price {price}, cost {cost} on profit)."},
    "ins_concentration": {"es": "**3 cuentas concentran el {pct} del movimiento total**: {names}.",
                          "en": "**3 accounts concentrate {pct} of the total movement**: {names}."},
    "ins_pace":        {"es": "**Avance de budget {att}** contra un pace esperado de {pace} a esta altura: {verdict} del ritmo. Aterrizaje proyectado {landing} vs budget {budget}.",
                        "en": "**Budget attainment {att}** against an expected pace of {pace} at this point: {verdict} pace. Projected landing {landing} vs budget {budget}."},
    "ins_above":       {"es": "por encima", "en": "above"},
    "ins_below":       {"es": "por debajo", "en": "below"},
    "ins_attain":      {"es": "**Avance de budget {att}** sobre el budget anual de {budget}.",
                        "en": "**Budget attainment {att}** on an annual budget of {budget}."},
    "ins_top_product": {"es": "A nivel producto, **{name}** es el mayor movimiento individual ({value}).",
                        "en": "At product level, **{name}** is the single largest move ({value})."},
    "ins_churn":       {"es": "**Churn: {n} cuentas sin facturación este período** que valían {total}. La mayor: {name} ({value}).",
                        "en": "**Churn: {n} accounts with no billing this period**, worth {total}. Largest: {name} ({value})."},
    "ins_margin_erosion": {"es": "**Erosión de margen en {n} cuentas materiales** (caída > 3 pp). La más severa: {name} con {pp} sobre {sales} de ventas.",
                           "en": "**Margin erosion in {n} material accounts** (drop > 3 pp). Worst: {name} at {pp} on {sales} of sales."},
    "ins_concentration_risk": {"es": "**Concentración {level}** (Herfindahl {hhi}). El mayor cliente pesa {pct} de la facturación del período.",
                               "en": "**{level} concentration** (Herfindahl {hhi}). The largest customer is {pct} of period billings."},
    "ins_conc_high":   {"es": "alta", "en": "High"},
    "ins_conc_mid":    {"es": "moderada", "en": "Moderate"},
    "ins_conc_low":    {"es": "baja", "en": "Low"},
    "ins_budget_short": {"es": "**{n} grupos proyectan cerrar por debajo de su budget**, por un total de {total}. La mayor brecha: {name} ({value}).",
                         "en": "**{n} groups are projected to close below budget**, totalling {total}. Largest gap: {name} ({value})."},
    "ins_unprojectable": {"es": "⚠️ **{n} de {total} grupos no son proyectables** por diferencia de base entre los dos archivos; usan el índice de cartera y su aterrizaje es indicativo, no auditable.",
                          "en": "⚠️ **{n} of {total} groups are not projectable** due to the date-basis difference between the two files; they use the portfolio index and their landing is indicative, not auditable."},
    "ins_product_drop": {"es": "**Producto en retroceso material**: {name} cae {value} ({pct}).",
                         "en": "**Product in material decline**: {name} falls {value} ({pct})."},
    "ins_growing":     {"es": "**{n} cuentas en crecimiento** aportan +{total}. Las tres mayores: {detail}.",
                        "en": "**{n} growing accounts** contribute +{total}. Top three: {detail}."},
    "ins_rich_products": {"es": "**Productos de margen alto y baja penetración** — candidatos a empujar: {detail}.",
                          "en": "**High-margin, low-penetration products** — candidates to push: {detail}."},
    "ins_new_accounts": {"es": "**{n} cuentas nuevas** suman {total}. Consolidar el segundo pedido es la conversión que define si quedan en cartera.",
                         "en": "**{n} new accounts** add {total}. Landing the second order is the conversion that decides whether they stay."},
    "ins_backlog":     {"es": "**{total} en cartera abierta** repartidos en {n} cuentas: negocio ya ganado que sólo espera embarque.",
                        "en": "**{total} in open orders** across {n} accounts: business already won, waiting only on shipment."},
    "ins_recover":     {"es": "**Recuperar run-rate en {n} cuentas rentables** (margen > 40%) devolvería hasta {total} de facturación sin sacrificar margen.",
                        "en": "**Recovering run-rate in {n} profitable accounts** (margin > 40%) would return up to {total} of billings without sacrificing margin."},
    "act_churn":       {"es": "**30 días · Recuperación de churn** — contactar {names}. En juego {total}. Dueño: comercial de cuenta.",
                        "en": "**30 days · Churn recovery** — contact {names}. {total} at stake. Owner: account sales."},
    "act_cost":        {"es": "**30 días · Revisión de costos** — el efecto costo drena {value} de profit. Revisar contratos de compra y trasladar a lista de precios donde el contrato lo permita.",
                        "en": "**30 days · Cost review** — the cost effect drains {value} of profit. Review purchase contracts and pass through to price lists where contracts allow."},
    "act_price":       {"es": "**60 días · Repricing selectivo** — el efecto precio resta {value}. Priorizar ítems con volumen estable y elasticidad baja antes de tocar cuentas en riesgo.",
                        "en": "**60 days · Selective repricing** — the price effect costs {value}. Prioritise items with stable volume and low elasticity before touching at-risk accounts."},
    "act_volume":      {"es": "**60 días · Plan de volumen** — se perdieron {value} por kilos. Definir objetivo de reposición por cuenta y producto.",
                        "en": "**60 days · Volume plan** — {value} lost on kilos. Set a recovery target by account and product."},
    "act_backlog":     {"es": "**Continuo · Conversión de cartera** — {total} en pedidos abiertos. Asegurar fecha de embarque para que caigan dentro del ejercicio.",
                        "en": "**Ongoing · Backlog conversion** — {total} in open orders. Lock shipping dates so they land inside the financial year."},
    "act_budget":      {"es": "**90 días · Cierre de brecha de budget** — plan cuenta por cuenta para las 5 mayores brechas proyectadas ({total}). Revisión quincenal con seguimiento de cartera abierta.",
                        "en": "**90 days · Budget gap closure** — account-by-account plan for the 5 largest projected gaps ({total}). Fortnightly review tracking open orders."},

    # --------------------------------------------------------------- common --
    "download_excel":  {"es": "Descargar Excel", "en": "Download Excel"},
    "download_table":  {"es": "Descargar tabla (Excel)", "en": "Download table (Excel)"},
    "no_data":         {"es": "Sin datos para los filtros actuales.",
                        "en": "No data for the current filters."},
    "no_metrics":      {"es": "Enciende al menos una métrica en el panel lateral.",
                        "en": "Switch on at least one metric in the sidebar."},
    "needs_fy":        {"es": "Esta vista necesita el archivo histórico / Full Year.",
                        "en": "This view needs the historical / Full Year file."},
    "needs_ytd":       {"es": "Esta vista necesita el archivo YTD.",
                        "en": "This view needs the YTD file."},
    "col_current":     {"es": "actual", "en": "current"},
    "col_base":        {"es": "base", "en": "base"},
    "status":          {"es": "Estado", "en": "Status"},
    "status_new":      {"es": "nuevo", "en": "new"},
    "status_lost":     {"es": "perdido", "en": "lost"},
    "status_kept":     {"es": "continuo", "en": "ongoing"},
    "vs_budget":       {"es": "vs budget", "en": "vs budget"},
    "vs_base_year":    {"es": "vs {year}", "en": "vs {year}"},
}


def language() -> str:
    return st.session_state.get("lang", "es")


def t(key: str, **kwargs) -> str:
    entry = STRINGS.get(key)
    if entry is None:
        return key
    text = entry.get(language(), entry.get("es", key))
    if kwargs:
        try:
            return text.format(**kwargs)
        except (KeyError, IndexError):
            return text
    return text


def level_label(level: str) -> str:
    return t(f"level_{level}")


def metric_label(key: str) -> str:
    from core.schema import TOGGLEABLE_METRICS
    meta = TOGGLEABLE_METRICS.get(key)
    return meta[language()] if meta else key


def set_language(lang: str) -> None:
    st.session_state["lang"] = lang
'''

_MODULES["core.schema"] = r'''"""Canonical mapping of the BI export into the app's internal vocabulary.

The real files vary: column captions get renamed, translated, reordered, or
shipped with a single header row instead of two. Everything here is therefore
matched on a *normalised* caption (lowercase, accent-free, punctuation-free)
against a list of synonyms, never on an exact string or a fixed position.

Only *base* metrics are kept. Every delta, percentage, ratio and variance the
BI file ships is deliberately discarded and recomputed downstream, because the
exported ratios (Margin, Price) cannot be aggregated safely.
"""

from __future__ import annotations

import re
import unicodedata

# --------------------------------------------------------------------------- #
# Normalisation
# --------------------------------------------------------------------------- #
_PUNCT = re.compile(r"[^a-z0-9]+")


def normalise(text: object) -> str:
    """'Sales - Prior Year' / 'Ventas Año Anterior' -> 'sales prior year' style key."""
    if text is None:
        return ""
    raw = str(text).strip().lower()
    raw = unicodedata.normalize("NFKD", raw)
    raw = "".join(ch for ch in raw if not unicodedata.combining(ch))
    return _PUNCT.sub(" ", raw).strip()


# --------------------------------------------------------------------------- #
# Dimensions
# --------------------------------------------------------------------------- #
# Enterprise Code and the concatenated "Enterprise & Product" are intentionally
# dropped. Order matters: the first synonym list that matches a column wins, and
# a column is only claimed once.
DIMENSION_SYNONYMS: dict[str, list[str]] = {
    "enterprise": [
        "enterprise", "enterprise group", "group", "grupo", "cliente grupo",
        "customer group", "parent customer", "corporate group", "holding",
    ],
    "customer": [
        "customer", "cliente", "sold to", "sold to customer", "customer name",
        "account", "cuenta", "ship to", "razon social",
    ],
    "product_family": [
        "product family", "familia", "familia de producto", "family",
        "product group", "grupo de producto", "categoria", "category",
    ],
    "product": [
        "product", "producto", "product name", "descripcion", "description",
        "item description", "item name", "articulo",
    ],
    "item_code": [
        "item code", "codigo", "codigo de item", "item", "sku", "material",
        "product code", "codigo producto", "item no", "part number",
    ],
}

# Captions we never want as a dimension even if they look like one.
DIMENSION_BLOCKLIST = {
    "enterprise code", "enterprise w code", "enterprise with code",
    "enterprise product", "enterprise and product", "codigo enterprise",
}

DIMENSIONS = list(DIMENSION_SYNONYMS)

# Grouping levels offered in the UI, in hierarchy order.
GROUP_LEVELS = {
    "enterprise": "Cliente (grupo)",
    "customer": "Cliente (cuenta)",
    "product_family": "Familia de producto",
    "product": "Producto",
    "item_code": "Código de ítem",
}

# --------------------------------------------------------------------------- #
# Metrics
# --------------------------------------------------------------------------- #
# IMPORTANT: in this export "Cost" and "Price" are PER-UNIT values, not totals.
# Total cost is derived as sales - profit.
#
# Each canonical metric lists the normalised captions that map onto it. Matching
# is exact-on-normalised-caption, so "Sales - YOY%" never collides with "Sales".
METRIC_SYNONYMS: dict[str, list[str]] = {
    "sales":        ["sales", "ventas", "revenue", "net sales", "turnover",
                     "facturacion", "importe", "amount"],
    "profit":       ["profit", "gross profit", "margen bruto", "utilidad",
                     "beneficio", "gp"],
    "quantity":     ["quantity", "qty", "volumen", "volume", "cantidad", "kg",
                     "kilos", "units"],
    "unit_cost":    ["cost", "costo", "coste", "unit cost", "costo unitario",
                     "cogs unit"],
    "unit_price":   ["price", "precio", "unit price", "precio unitario", "asp"],
    "sales_bdg":    ["sales budget", "budget", "presupuesto", "ventas budget",
                     "ventas presupuesto", "budget sales", "sales bud"],
    "profit_bdg":   ["profit budget", "budget profit", "presupuesto profit",
                     "profit bud"],
    "qty_bdg":      ["quantity budget", "budget quantity", "presupuesto volumen",
                     "volumen budget", "qty budget"],
    "sales_open":   ["sales open orders", "open orders", "cartera", "pedidos abiertos",
                     "backlog", "sales backlog", "ordenes abiertas",
                     "cartera abierta", "open order value"],
    "profit_open":  ["profit open orders", "open orders profit", "cartera profit",
                     "backlog profit"],
    "qty_open":     ["quantity open orders", "open orders quantity",
                     "cartera volumen", "backlog quantity"],
    "sales_so":     ["sales sold open", "sales sold and open", "sold open",
                     "vendido mas cartera"],
    "profit_so":    ["profit sold open", "profit sold and open"],
    "qty_so":       ["quantity sold open", "quantity sold and open"],
    "sales_py_col": ["sales prior year", "ventas ano anterior", "sales py",
                     "prior year sales", "sales last year"],
    "profit_py_col": ["profit prior year", "profit py", "prior year profit"],
    "qty_py_col":   ["quantity prior year", "quantity py", "volumen ano anterior"],
    "lines":        ["transaction count lines", "lines", "lineas", "order lines",
                     "transaction lines", "num lineas"],
}

SUM_COLUMNS = [
    "sales", "profit", "quantity",
    "sales_bdg", "profit_bdg", "qty_bdg",
    "sales_open", "profit_open", "qty_open",
    "lines",
]

# Metrics the user can switch on/off, pivot-table style.
TOGGLEABLE_METRICS = {
    "sales":      {"es": "Ventas",          "en": "Sales",       "fmt": "money", "default": True},
    "profit":     {"es": "Profit",          "en": "Profit",      "fmt": "money", "default": True},
    "margin_pct": {"es": "Margen %",        "en": "Margin %",    "fmt": "pct",   "default": True},
    "quantity":   {"es": "Volumen",         "en": "Volume",      "fmt": "qty",   "default": True},
    "price":      {"es": "Precio unitario", "en": "Unit price",  "fmt": "unit",  "default": True},
    "unit_cost":  {"es": "Costo unitario",  "en": "Unit cost",   "fmt": "unit",  "default": False},
    "lines":      {"es": "Líneas",          "en": "Order lines", "fmt": "int",   "default": False},
    "sales_open": {"es": "Cartera abierta", "en": "Open orders", "fmt": "money", "default": True},
}

# Captions that must never be treated as a base metric: they are derived values
# the app recomputes, or placeholders the BI ships empty.
DERIVED_CAPTION_MARKERS = (
    "yoy", "vs budget", "vs forecast", "not ready", "revenue budget",
    "sold open vs", "variance", "variacion", "delta", "growth", "crecimiento",
)

# Budget is loaded against a placeholder customer ("<GROUP> []"), so it can only
# be attributed at these levels. Grouping by the individual customer account
# yields no budget at all — the app says so rather than inventing a gap.
BUDGET_LEVELS = {"enterprise", "product_family", "product", "item_code"}

# Row labels that mark an aggregate row inside the pivot export.
SUBTOTAL_TOKENS = {
    "total", "totals", "grand total", "subtotal", "sub total",
    "total general", "suma", "all", "todos",
}


def match_dimension(caption: object, taken: set[str]) -> str | None:
    """Return the canonical dimension a column caption belongs to, if any."""
    key = normalise(caption)
    if not key or key in DIMENSION_BLOCKLIST:
        return None
    for canon, synonyms in DIMENSION_SYNONYMS.items():
        if canon in taken:
            continue
        if key in synonyms:
            return canon
    # Second pass: allow a caption that *contains* a synonym, so
    # "Customer Name (Sold To)" still resolves.
    for canon, synonyms in DIMENSION_SYNONYMS.items():
        if canon in taken:
            continue
        for syn in synonyms:
            if re.search(rf"\b{re.escape(syn)}\b", key):
                return canon
    return None


def match_metric(caption: object) -> str | None:
    """Return the canonical base metric for a column caption, if any."""
    key = normalise(caption)
    if not key:
        return None
    if any(marker in key for marker in DERIVED_CAPTION_MARKERS):
        return None
    for canon, synonyms in METRIC_SYNONYMS.items():
        if key in synonyms:
            return canon
    return None


def is_subtotal(value: object) -> bool:
    return normalise(value) in SUBTOTAL_TOKENS
'''

_MODULES["core.metrics"] = r'''"""Safe aggregation. The single rule: ratios are never averaged."""

from __future__ import annotations

import numpy as np
import pandas as pd

from core.schema import SUM_COLUMNS


def _safe_div(num: pd.Series | float, den: pd.Series | float):
    num = pd.Series(num) if not isinstance(num, pd.Series) else num
    den = pd.Series(den) if not isinstance(den, pd.Series) else den
    out = pd.Series(np.nan, index=num.index, dtype="float64")
    ok = den.notna() & (den != 0)
    out[ok] = num[ok] / den[ok]
    return out


def add_ratios(df: pd.DataFrame) -> pd.DataFrame:
    """Recompute every ratio from its components. Call after any groupby."""
    out = df.copy()
    out["margin_pct"] = _safe_div(out.get("profit"), out.get("sales"))
    out["price"] = _safe_div(out.get("sales"), out.get("quantity"))
    if "cost_total" not in out.columns:
        out["cost_total"] = out.get("sales", 0) - out.get("profit", 0)
    out["unit_cost"] = _safe_div(out["cost_total"], out.get("quantity"))
    out["margin_bdg_pct"] = _safe_div(out.get("profit_bdg"), out.get("sales_bdg"))
    out["price_bdg"] = _safe_div(out.get("sales_bdg"), out.get("qty_bdg"))
    out["sales_sold_open"] = out.get("sales", 0).fillna(0) + out.get("sales_open", 0).fillna(0)
    return out


def aggregate(tidy: pd.DataFrame, by: list[str] | str) -> pd.DataFrame:
    """Group and re-derive ratios. Never sums a ratio column."""
    by = [by] if isinstance(by, str) else list(by)
    cols = [c for c in SUM_COLUMNS + ["cost_total"] if c in tidy.columns]
    grouped = tidy.groupby(by, dropna=False)[cols].sum(min_count=1).reset_index()
    return add_ratios(grouped)


def totals(tidy: pd.DataFrame) -> pd.Series:
    """Scalar totals for a slice, with ratios re-derived."""
    cols = [c for c in SUM_COLUMNS + ["cost_total"] if c in tidy.columns]
    s = tidy[cols].sum(min_count=1)
    frame = add_ratios(s.to_frame().T)
    return frame.iloc[0]


def compare(
    tidy: pd.DataFrame,
    by: list[str] | str,
    current_year: int,
    base_year: int,
    include_open: bool = False,
) -> pd.DataFrame:
    """Side-by-side of two year bands at a chosen grouping level.

    Returns one row per group with `_cur` / `_base` suffixed measures plus
    absolute and relative deltas. Groups absent from either side are kept
    (filled with 0) so churn and new business stay visible.
    """
    by = [by] if isinstance(by, str) else list(by)
    cur = aggregate(tidy[tidy["year"] == current_year], by)
    base = aggregate(tidy[tidy["year"] == base_year], by)

    if include_open:
        cur = cur.copy()
        cur["sales"] = cur["sales"].fillna(0) + cur["sales_open"].fillna(0)
        cur["profit"] = cur["profit"].fillna(0) + cur["profit_open"].fillna(0)
        cur["quantity"] = cur["quantity"].fillna(0) + cur["qty_open"].fillna(0)
        cur = add_ratios(cur)

    measures = ["sales", "profit", "quantity", "margin_pct", "price",
                "unit_cost", "lines", "sales_open", "sales_bdg", "profit_bdg", "qty_bdg"]
    measures = [m for m in measures if m in cur.columns or m in base.columns]

    merged = cur.merge(base, on=by, how="outer", suffixes=("_cur", "_base"))

    additive = {"sales", "profit", "quantity", "lines", "sales_open",
                "sales_bdg", "profit_bdg", "qty_bdg"}
    for m in measures:
        for side in ("_cur", "_base"):
            col = f"{m}{side}"
            if col in merged.columns and m in additive:
                merged[col] = merged[col].fillna(0.0)

    for m in measures:
        c, b = f"{m}_cur", f"{m}_base"
        if c in merged.columns and b in merged.columns:
            merged[f"{m}_delta"] = merged[c] - merged[b]
            if m == "margin_pct":
                merged[f"{m}_delta_pp"] = merged[f"{m}_delta"] * 100
            else:
                merged[f"{m}_delta_pct"] = _safe_div(merged[f"{m}_delta"], merged[b].abs())

    # Budget lives only on the current band.
    if "sales_bdg_cur" in merged.columns:
        merged["sales_vs_bdg"] = merged["sales_cur"] - merged["sales_bdg_cur"]
        merged["sales_bdg_attain"] = _safe_div(merged["sales_cur"], merged["sales_bdg_cur"])
    if "profit_bdg_cur" in merged.columns:
        merged["profit_vs_bdg"] = merged["profit_cur"] - merged["profit_bdg_cur"]

    merged["status"] = np.select(
        [
            (merged.get("sales_base", 0) > 0) & (merged.get("sales_cur", 0) <= 0),
            (merged.get("sales_base", 0) <= 0) & (merged.get("sales_cur", 0) > 0),
        ],
        ["perdido", "nuevo"],
        default="continuo",
    )
    return merged


def apply_materiality(df: pd.DataFrame, threshold: float, column: str = "sales_cur") -> pd.DataFrame:
    """Hide long-tail rows below an absolute USD threshold on either side."""
    if threshold <= 0:
        return df
    base_col = column.replace("_cur", "_base")
    cur = df[column].abs() if column in df.columns else 0
    base = df[base_col].abs() if base_col in df.columns else 0
    return df[(cur >= threshold) | (base >= threshold)]


def herfindahl(values: pd.Series) -> float:
    """Concentration index on a revenue distribution (0 = atomised, 1 = single)."""
    v = values.clip(lower=0).fillna(0)
    total = v.sum()
    if total <= 0:
        return float("nan")
    shares = v / total
    return float((shares**2).sum())
'''

_MODULES["core.parser"] = r'''"""Parse a BI sales export into a tidy, leaf-level dataframe — tolerantly.

The reference file is a hierarchical pivot with a two-row header (year band on
top, metric caption below), eight dimension columns and embedded subtotal rows.
But exports drift: captions get renamed or translated, the year band disappears
into the caption itself ("2025 Sales"), a sheet gets renamed, columns move, a
dimension is dropped. So nothing here is positional and nothing is matched on an
exact string:

  * the sheet is chosen by name if recognisable, otherwise by content;
  * the header row is *found* by looking for recognisable captions, not assumed;
  * years come from a band row, from the captions, or from a single-year
    fallback;
  * dimensions and metrics resolve through synonym lists (ES/EN);
  * subtotal rows are detected by label in either language;
  * numbers survive currency symbols, thousands separators and (1.234) negatives.

Whatever it could not interpret is reported in `profile`, so the Data & quality
tab can show the user exactly what was recognised and what was ignored.

Nothing here touches disk: input is bytes, output is an in-memory dataframe.
"""

from __future__ import annotations

import io
import re
from dataclasses import dataclass, field

import pandas as pd

from core.schema import (
    DIMENSIONS,
    METRIC_SYNONYMS,
    is_subtotal,
    match_dimension,
    match_metric,
    normalise,
)

YEAR_RE = re.compile(r"(?:^|\D)((?:19|20)\d{2})(?:\D|$)")
PURE_YEAR_RE = re.compile(r"^(?:19|20)\d{2}(?:\.\d+)?$")
HEADER_SCAN_ROWS = 12
SHEET_HINTS = ("export", "data", "datos", "sheet1", "hoja1", "report", "reporte")


# --------------------------------------------------------------------------- #
# Result container
# --------------------------------------------------------------------------- #
@dataclass
class ParsedExport:
    """Everything one uploaded workbook yields. Lives in memory only."""

    tidy: pd.DataFrame                      # one row per (leaf, year)
    years: list[int] = field(default_factory=list)
    n_leaf_rows: int = 0
    n_raw_rows: int = 0
    filename: str = ""
    warnings: list[str] = field(default_factory=list)
    year_totals: pd.DataFrame | None = None
    profile: dict = field(default_factory=dict)   # what the parser recognised

    @property
    def substantive_years(self) -> list[int]:
        """Years carrying real sales, excluding empty and clearly partial bands."""
        if self.year_totals is None or self.year_totals.empty:
            return self.years
        t = self.year_totals
        live = t[t["sales"] > 0]
        if live.empty:
            return self.years
        years = sorted(live.index.tolist())
        # Drop a trailing band that holds only a sliver of business (forward
        # orders leaking into the next calendar year, e.g. 2027).
        while len(years) > 1:
            last, prev = years[-1], years[-2]
            if t.loc[last, "sales"] < 0.25 * t.loc[prev, "sales"]:
                years.pop()
            else:
                break
        return years

    @property
    def partial_years(self) -> list[int]:
        return [y for y in self.years if y not in self.substantive_years]

    @property
    def has_budget(self) -> bool:
        return "sales_bdg" in self.tidy and self.tidy["sales_bdg"].fillna(0).abs().sum() > 0

    @property
    def has_open_orders(self) -> bool:
        return "sales_open" in self.tidy and self.tidy["sales_open"].fillna(0).abs().sum() > 0


# --------------------------------------------------------------------------- #
# Workbook / sheet selection
# --------------------------------------------------------------------------- #
def _pick_sheet(book: pd.ExcelFile) -> str:
    names = book.sheet_names
    if len(names) == 1:
        return names[0]
    for name in names:
        if normalise(name) in SHEET_HINTS:
            return name
    # Otherwise take the sheet with the most non-empty cells.
    best, best_score = names[0], -1
    for name in names:
        probe = book.parse(name, header=None, nrows=60, dtype=object)
        score = int(probe.notna().sum().sum())
        if score > best_score:
            best, best_score = name, score
    return best


# --------------------------------------------------------------------------- #
# Header discovery
# --------------------------------------------------------------------------- #
def _score_header_row(row: pd.Series) -> int:
    """How many cells in this row look like captions we understand."""
    taken: set[str] = set()
    score = 0
    for value in row:
        dim = match_dimension(value, taken)
        if dim:
            taken.add(dim)
            score += 2
            continue
        if match_metric(value):
            score += 1
    return score


def _find_header_row(raw: pd.DataFrame) -> int:
    best_idx, best_score = 0, -1
    for idx in range(min(HEADER_SCAN_ROWS, len(raw))):
        score = _score_header_row(raw.iloc[idx])
        if score > best_score:
            best_idx, best_score = idx, score
    if best_score <= 0:
        raise ValueError(
            "No se reconoció ninguna fila de encabezado. Se esperan columnas de "
            "dimensión (Cliente, Producto, Código) y de métrica (Ventas, Profit, "
            "Volumen) en alguna de las primeras filas."
        )
    return best_idx


def _year_from(value: object) -> int | None:
    text = str(value).strip()
    if not text or text.lower() == "nan":
        return None
    if PURE_YEAR_RE.match(text):
        return int(float(text)) if "." in text else int(text)
    match = YEAR_RE.search(text)
    return int(match.group(1)) if match else None


def _band_row_years(raw: pd.DataFrame, header_idx: int) -> dict[int, int] | None:
    """Year for each column taken from the row above the caption row."""
    if header_idx == 0:
        return None
    band = raw.iloc[header_idx - 1]
    years = {idx: y for idx, value in band.items() if (y := _year_from(value))}
    return years if len(years) >= 2 else None


def _caption_years(captions: pd.Series) -> dict[int, int]:
    """Year embedded in the caption itself, e.g. '2025 Sales' / 'Sales FY2025'."""
    return {idx: y for idx, value in captions.items() if (y := _year_from(value))}


def _strip_year(caption: object) -> str:
    return YEAR_RE.sub(" ", str(caption)).strip()


# --------------------------------------------------------------------------- #
# Value coercion
# --------------------------------------------------------------------------- #
_NUM_CLEAN = re.compile(r"[^\d,.\-()]+")


def _to_number(series: pd.Series) -> pd.Series:
    """Tolerate '$ 1,234.50', '(1.234,50)', '1 234', '—', '' and real numbers."""
    numeric = pd.to_numeric(series, errors="coerce")
    if numeric.notna().sum() >= series.notna().sum():
        return numeric

    text = series.astype("string").str.strip()
    text = text.str.replace(_NUM_CLEAN, "", regex=True)
    negative = text.str.startswith("(", na=False) & text.str.endswith(")", na=False)
    text = text.str.strip("()")

    # Decide the decimal separator per column: if commas are followed by exactly
    # two digits at the end, they are decimals (es-ES style).
    comma_decimal = text.str.contains(r",\d{1,2}$", na=False).sum() > \
        text.str.contains(r"\.\d{1,2}$", na=False).sum()
    if comma_decimal:
        text = text.str.replace(".", "", regex=False).str.replace(",", ".", regex=False)
    else:
        text = text.str.replace(",", "", regex=False)

    out = pd.to_numeric(text, errors="coerce")
    return out.mask(negative, -out.abs())


def _clean_dimension(series: pd.Series) -> pd.Series:
    out = series.astype("string").str.strip()
    return out.replace({"nan": pd.NA, "": pd.NA, "None": pd.NA})


def _strip_code(series: pd.Series) -> pd.Series:
    """'ADITMAQ [4018]' -> 'ADITMAQ'."""
    return series.str.replace(r"\s*\[[^\]]*\]\s*$", "", regex=True).str.strip()


# --------------------------------------------------------------------------- #
# Main entry point
# --------------------------------------------------------------------------- #
def parse_export(data: bytes, filename: str = "") -> ParsedExport:
    warnings: list[str] = []
    profile: dict = {"filename": filename}

    book = pd.ExcelFile(io.BytesIO(data))
    sheet = _pick_sheet(book)
    profile["sheet"] = sheet
    if len(book.sheet_names) > 1:
        warnings.append(
            f"El libro tiene {len(book.sheet_names)} hojas; se analizó «{sheet}»."
        )

    raw = book.parse(sheet, header=None, dtype=object)
    if raw.empty:
        raise ValueError("La hoja seleccionada está vacía.")

    header_idx = _find_header_row(raw)
    captions = raw.iloc[header_idx]
    profile["header_row"] = int(header_idx) + 1

    # --- dimensions ---------------------------------------------------------
    dim_cols: dict[str, int] = {}
    for idx, caption in captions.items():
        canon = match_dimension(caption, set(dim_cols))
        if canon and canon not in dim_cols:
            dim_cols[canon] = idx
    profile["dimensions"] = {k: str(captions[v]) for k, v in dim_cols.items()}

    if not dim_cols:
        raise ValueError(
            "No se reconoció ninguna columna de dimensión. Se esperan al menos "
            "Cliente o Producto/Código de ítem."
        )
    missing = [d for d in DIMENSIONS if d not in dim_cols]
    if missing:
        warnings.append(
            "Dimensiones ausentes en el archivo (se rellenan como «N/D»): "
            + ", ".join(missing)
        )

    # --- year bands ---------------------------------------------------------
    band_years = _band_row_years(raw, header_idx)
    caption_years: dict[int, int] = {}
    if band_years:
        year_source = "banda superior del encabezado"
        column_year = band_years
    else:
        caption_years = _caption_years(captions)
        if len(caption_years) >= 2:
            year_source = "año embebido en el nombre de columna"
            column_year = caption_years
        else:
            year_source = "archivo de un solo período"
            column_year = {}
    profile["year_source"] = year_source

    # --- metrics ------------------------------------------------------------
    # blocks[year][canonical metric] = column index
    blocks: dict[int, dict[str, int]] = {}
    unmatched: list[str] = []
    for idx, caption in captions.items():
        if idx in dim_cols.values():
            continue
        text = str(caption).strip()
        if not text or text.lower() == "nan":
            continue
        canon = match_metric(_strip_year(caption) if caption_years else caption)
        if canon is None:
            canon = match_metric(caption)
        if canon is None:
            unmatched.append(text)
            continue
        year = column_year.get(idx)
        if year is None:
            year = _year_from(caption) or 0
        blocks.setdefault(year, {}).setdefault(canon, idx)

    if not blocks:
        raise ValueError(
            "No se reconoció ninguna métrica. Se esperan columnas tipo Ventas / "
            "Sales, Profit, Volumen / Quantity."
        )

    # Single-period file: label the band with the year in the filename, else 0.
    if list(blocks) == [0]:
        guessed = _year_from(filename) or 0
        blocks = {guessed: blocks.pop(0)}
        if guessed:
            warnings.append(
                f"Archivo de un solo período; el año ({guessed}) se dedujo del "
                f"nombre del archivo."
            )
        else:
            warnings.append(
                "Archivo de un solo período y sin año identificable: las "
                "comparaciones año contra año quedan desactivadas."
            )

    profile["metrics"] = sorted({m for cols in blocks.values() for m in cols})
    profile["ignored_columns"] = unmatched[:40]
    profile["n_ignored_columns"] = len(unmatched)

    # --- body ---------------------------------------------------------------
    body = raw.iloc[header_idx + 1:].reset_index(drop=True)
    body = body.dropna(how="all").reset_index(drop=True)
    n_raw = len(body)
    if n_raw == 0:
        raise ValueError("No hay filas de datos debajo del encabezado.")

    # --- prune subtotal rows ------------------------------------------------
    # The deepest dimension present identifies a leaf. Rows whose deepest label
    # is a subtotal token (in any language) are aggregates the export computed.
    depth_order = [d for d in ("item_code", "product", "product_family",
                               "customer", "enterprise") if d in dim_cols]
    leaf_dim = depth_order[0]
    leaf_values = _clean_dimension(body[dim_cols[leaf_dim]])
    subtotal_mask = leaf_values.map(is_subtotal).fillna(False)
    leaf_mask = leaf_values.notna() & ~subtotal_mask

    # Any row carrying a subtotal token in *any* dimension is an aggregate too.
    for canon, col in dim_cols.items():
        marks = _clean_dimension(body[col]).map(is_subtotal).fillna(False)
        leaf_mask &= ~marks

    if not leaf_mask.any():
        warnings.append(
            "No se detectaron filas hoja por etiqueta; se analizan todas las "
            "filas con datos."
        )
        leaf_mask = leaf_values.notna()
    leaves = body[leaf_mask].reset_index(drop=True)
    if leaves.empty:
        raise ValueError("Tras podar los subtotales no quedaron filas de datos.")
    profile["leaf_dimension"] = leaf_dim

    # --- dimension frame ----------------------------------------------------
    dims = pd.DataFrame(index=leaves.index)
    for name in DIMENSIONS:
        if name in dim_cols:
            dims[name] = _clean_dimension(leaves[dim_cols[name]]).fillna("N/D")
        else:
            dims[name] = "N/D"
    # Forward-fill the outer levels: pivot exports often print a group name once
    # and leave the repeats blank.
    for name in ("enterprise", "customer", "product_family"):
        if name in dim_cols:
            filled = _clean_dimension(leaves[dim_cols[name]]).ffill()
            dims[name] = filled.fillna("N/D")

    # Budget is loaded against a placeholder customer named "<GROUP> []" rather
    # than the real account, so budget rows and sales rows never share a
    # customer key. Flag them; downstream code attributes budget at enterprise
    # level and refuses to fake a customer-level budget.
    dims["is_group_row"] = dims["customer"].str.endswith("[]").fillna(False)
    dims["customer_name"] = _strip_code(dims["customer"])
    dims["enterprise_name"] = _strip_code(dims["enterprise"])
    dims["product_name"] = _strip_code(dims["product"])

    # --- one tidy block per year -------------------------------------------
    frames = []
    for year in sorted(blocks):
        block = dims.copy()
        block["year"] = year
        for canon, idx in blocks[year].items():
            block[canon] = _to_number(leaves[idx])
        frames.append(block)

    tidy = pd.concat(frames, ignore_index=True)
    for canon in METRIC_SYNONYMS:
        if canon not in tidy.columns:
            tidy[canon] = pd.NA
        tidy[canon] = pd.to_numeric(tidy[canon], errors="coerce")

    # Derived totals. 'Cost' in this export is per-unit, so total cost has to
    # come from sales - profit or it will be off by orders of magnitude.
    tidy["cost_total"] = tidy["sales"] - tidy["profit"]

    # Drop (leaf, year) rows with no activity at all in any tracked measure.
    activity = tidy[["sales", "profit", "quantity", "sales_bdg", "sales_open"]].fillna(0)
    tidy = tidy[activity.abs().sum(axis=1) > 0].reset_index(drop=True)
    if tidy.empty:
        raise ValueError("Ninguna fila tiene valores en ventas, profit, volumen, "
                         "budget ni cartera.")

    year_totals = (
        tidy.groupby("year")[["sales", "profit", "quantity", "sales_bdg", "sales_open"]]
        .sum(min_count=1).fillna(0.0)
    )

    parsed = ParsedExport(
        tidy=tidy,
        years=sorted(blocks),
        n_leaf_rows=int(leaf_mask.sum()),
        n_raw_rows=n_raw,
        filename=filename,
        warnings=warnings,
        year_totals=year_totals,
        profile=profile,
    )

    pruned = n_raw - parsed.n_leaf_rows
    if pruned > 0:
        warnings.append(
            f"Se podaron {pruned:,} filas de subtotal de {n_raw:,} "
            f"({pruned / n_raw:.0%}); se analizan {parsed.n_leaf_rows:,} filas hoja."
        )
    if unmatched:
        warnings.append(
            f"{len(unmatched)} columnas no se reconocieron como métrica base y se "
            f"ignoraron (son variaciones y porcentajes que la app recalcula)."
        )
    n_group_rows = int(tidy["is_group_row"].sum())
    if n_group_rows:
        warnings.append(
            f"{n_group_rows:,} filas cargan budget contra un cliente marcador "
            f"«GRUPO []». El budget se atribuye a nivel Cliente (grupo) y por "
            f"producto; a nivel cuenta individual no es atribuible."
        )
    if parsed.partial_years:
        warnings.append(
            "Bandas de año ocultas por vacías o parciales: "
            + ", ".join(str(y) for y in parsed.partial_years)
        )
    return parsed
'''

_MODULES["core.bridges"] = r'''"""Exact price / volume / mix and margin decompositions.

At item level the sales bridge is algebraically exact:

    Δ sales = Σ (q1 - q0)·p0   [volume]
            + Σ (p1 - p0)·q1   [price]
            + new business - lost business

because (q1-q0)p0 + (p1-p0)q1 = p1q1 - p0q0. No residual, nothing hand-waved.

Mix is not a fudge factor here: it only appears when you aggregate to a coarser
level than the item, and we compute it explicitly as the gap between the
coarse-level decomposition and the exact item-level one.

The margin bridge uses profit = q·(p - c):

    Δ profit = q1·(p1 - p0)      [price]
             - q1·(c1 - c0)      [unit cost]
             + (q1 - q0)·(p0-c0) [volume]
"""

from __future__ import annotations

import pandas as pd

from core.i18n import t

ITEM_KEY = ["customer", "item_code"]


def _sales_labels() -> dict[str, str]:
    return {
        "volume": t("eff_volume"), "price": t("eff_price"),
        "new": t("eff_new"), "lost": t("eff_lost"), "other": t("eff_other"),
    }


def _margin_labels() -> dict[str, str]:
    return {
        "price": t("eff_price"), "cost": t("eff_cost"), "volume": t("eff_volume"),
        "new": t("eff_new"), "lost": t("eff_lost"), "other": t("eff_other"),
    }


def _prep(tidy: pd.DataFrame, year: int, keys: list[str]) -> pd.DataFrame:
    block = tidy[tidy["year"] == year]
    agg = block.groupby(keys, dropna=False)[["sales", "profit", "quantity"]].sum(min_count=1)
    return agg.fillna(0.0)


def sales_bridge(
    tidy: pd.DataFrame,
    current_year: int,
    base_year: int,
    keys: list[str] | None = None,
) -> dict:
    """Volume / price / new / lost decomposition of the sales delta."""
    keys = keys or ITEM_KEY
    cur = _prep(tidy, current_year, keys)
    base = _prep(tidy, base_year, keys)
    both = cur.join(base, how="outer", lsuffix="_1", rsuffix="_0").fillna(0.0)

    common = both[(both["quantity_1"] > 0) & (both["quantity_0"] > 0)]
    new = both[(both["sales_0"] == 0) & (both["sales_1"] != 0)]
    lost = both[(both["sales_1"] == 0) & (both["sales_0"] != 0)]
    # Rows that traded on both sides but without usable volume (e.g. service
    # lines with no kg) are settled as a straight value delta.
    odd = both.drop(index=common.index.union(new.index).union(lost.index))

    p0 = common["sales_0"] / common["quantity_0"]
    p1 = common["sales_1"] / common["quantity_1"]
    volume = float(((common["quantity_1"] - common["quantity_0"]) * p0).sum())
    price = float(((p1 - p0) * common["quantity_1"]).sum())

    steps = {
        "volume": volume,
        "price": price,
        "new": float(new["sales_1"].sum()),
        "lost": float(-lost["sales_0"].sum()),
        "other": float((odd["sales_1"] - odd["sales_0"]).sum()),
    }
    start = float(both["sales_0"].sum())
    end = float(both["sales_1"].sum())
    residual = end - start - sum(steps.values())
    if abs(residual) > max(1.0, abs(end) * 1e-9):
        steps["other"] += residual

    return {
        "start": start,
        "end": end,
        "steps": steps,
        "detail": both,
        "labels": _sales_labels(),
    }


def margin_bridge(
    tidy: pd.DataFrame,
    current_year: int,
    base_year: int,
    keys: list[str] | None = None,
) -> dict:
    """Price / unit-cost / volume decomposition of the profit delta."""
    keys = keys or ITEM_KEY
    cur = _prep(tidy, current_year, keys)
    base = _prep(tidy, base_year, keys)
    both = cur.join(base, how="outer", lsuffix="_1", rsuffix="_0").fillna(0.0)

    common = both[(both["quantity_1"] > 0) & (both["quantity_0"] > 0)]
    new = both[(both["sales_0"] == 0) & (both["sales_1"] != 0)]
    lost = both[(both["sales_1"] == 0) & (both["sales_0"] != 0)]
    odd = both.drop(index=common.index.union(new.index).union(lost.index))

    p0 = common["sales_0"] / common["quantity_0"]
    p1 = common["sales_1"] / common["quantity_1"]
    c0 = (common["sales_0"] - common["profit_0"]) / common["quantity_0"]
    c1 = (common["sales_1"] - common["profit_1"]) / common["quantity_1"]

    steps = {
        "price": float((common["quantity_1"] * (p1 - p0)).sum()),
        "cost": float((-common["quantity_1"] * (c1 - c0)).sum()),
        "volume": float(((common["quantity_1"] - common["quantity_0"]) * (p0 - c0)).sum()),
        "new": float(new["profit_1"].sum()),
        "lost": float(-lost["profit_0"].sum()),
        "other": float((odd["profit_1"] - odd["profit_0"]).sum()),
    }
    start = float(both["profit_0"].sum())
    end = float(both["profit_1"].sum())
    residual = end - start - sum(steps.values())
    if abs(residual) > max(1.0, abs(end) * 1e-9):
        steps["other"] += residual

    return {
        "start": start,
        "end": end,
        "steps": steps,
        "detail": both,
        "labels": _margin_labels(),
    }


def mix_effect(tidy: pd.DataFrame, current_year: int, base_year: int, level: str) -> float:
    """Portfolio-composition effect visible only above item level."""
    fine = sales_bridge(tidy, current_year, base_year, ITEM_KEY)["steps"]
    coarse = sales_bridge(tidy, current_year, base_year, [level])["steps"]
    return (coarse["volume"] + coarse["price"]) - (fine["volume"] + fine["price"])


def contribution_by_group(
    tidy: pd.DataFrame, current_year: int, base_year: int, level: str, top_n: int = 10
) -> pd.DataFrame:
    """Which groups build and which destroy the total delta, ranked by USD."""
    cur = _prep(tidy, current_year, [level])["sales"]
    base = _prep(tidy, base_year, [level])["sales"]
    delta = cur.subtract(base, fill_value=0.0).sort_values()
    frame = delta.rename("delta").reset_index()
    frame["direction"] = frame["delta"].apply(lambda v: "positivo" if v >= 0 else "negativo")
    top = pd.concat([frame.head(top_n), frame.tail(top_n)]).drop_duplicates()
    rest = frame.drop(index=top.index)
    if not rest.empty:
        top = pd.concat(
            [top, pd.DataFrame([{level: t("rest"), "delta": rest["delta"].sum(),
                                 "direction": "rest"}])],
            ignore_index=True,
        )
    return top.sort_values("delta")
'''

_MODULES["core.forecast"] = r'''"""Seasonality, landing forecast, and the cross-file basis guard.

The two exports are NOT on the same date basis. Evidence found in the real
files: the budget reconciles to the cent per customer, but 39 of 142 customers
disagree on sales, and the "YTD" prior year comes out *larger* than the "full
year" prior for the portfolio as a whole — impossible on a single basis.

So the seasonality index is computed per group and each group is graded. Groups
whose two sides are mutually impossible are never projected; they are surfaced
as an explicit warning instead of quietly producing a wrong forecast.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

MIN_BASE = 5_000.0        # USD below which a group is too small to project
MIN_INDEX = 0.15          # an index under this implies an implausible ramp
MATCH_TOL = 0.005         # 0.5% — treated as the same figure

# Budget is loaded against a placeholder customer, so it only attributes at
# these levels (see schema.BUDGET_LEVELS).
BUDGET_LEVELS = {"enterprise", "product_family", "product", "item_code"}


def _year_sales(parsed_tidy: pd.DataFrame, year: int, level: str) -> pd.Series:
    block = parsed_tidy[parsed_tidy["year"] == year]
    return block.groupby(level, dropna=False)["sales"].sum(min_count=1).fillna(0.0)


def cross_file_diagnosis(
    ytd_tidy: pd.DataFrame,
    fy_tidy: pd.DataFrame,
    prior_year: int,
    level: str = "enterprise",
) -> pd.DataFrame:
    """Compare the same prior-year band across both files, group by group."""
    a = _year_sales(ytd_tidy, prior_year, level).rename("ytd_file")
    b = _year_sales(fy_tidy, prior_year, level).rename("fy_file")
    frame = pd.concat([a, b], axis=1).fillna(0.0)
    frame["diff"] = frame["ytd_file"] - frame["fy_file"]
    denom = frame[["ytd_file", "fy_file"]].abs().max(axis=1).replace(0, np.nan)
    frame["diff_pct"] = frame["diff"] / denom

    frame["verdict"] = np.select(
        [
            frame["diff"].abs() <= (denom.fillna(0) * MATCH_TOL),
            frame["ytd_file"] > frame["fy_file"],
        ],
        ["coincide", "base inconsistente"],
        default="coherente (YTD < FY)",
    )
    return frame.sort_values("diff", key=abs, ascending=False)


def seasonality_index(
    ytd_tidy: pd.DataFrame,
    fy_tidy: pd.DataFrame,
    prior_year: int,
    level: str = "enterprise",
) -> pd.DataFrame:
    """index = prior YTD / prior full year — the share of the year normally
    booked by this point. Graded for reliability."""
    ytd = _year_sales(ytd_tidy, prior_year, level).rename("prior_ytd")
    fy = _year_sales(fy_tidy, prior_year, level).rename("prior_fy")
    frame = pd.concat([ytd, fy], axis=1).fillna(0.0)

    with np.errstate(divide="ignore", invalid="ignore"):
        frame["index"] = np.where(frame["prior_fy"] > 0,
                                  frame["prior_ytd"] / frame["prior_fy"], np.nan)

    frame["reliability"] = np.select(
        [
            (frame["prior_fy"] < MIN_BASE) | (frame["prior_ytd"] < MIN_BASE),
            frame["index"] > 1.0 + MATCH_TOL,
            frame["index"] < MIN_INDEX,
            frame["index"].isna(),
        ],
        ["inmaterial", "base inconsistente", "índice atípico", "sin historia"],
        default="proyectable",
    )
    frame["projectable"] = frame["reliability"] == "proyectable"
    return frame


def landing_forecast(
    ytd_tidy: pd.DataFrame,
    fy_tidy: pd.DataFrame,
    current_year: int,
    prior_year: int,
    level: str = "enterprise",
    fallback_index: float | None = None,
) -> pd.DataFrame:
    """Project full-year landing per group, and flag what could not be projected.

    Groups that are not individually projectable fall back to the portfolio
    index (computed only from the projectable subset) and are labelled as such,
    so the number is never presented as if it were solid.
    """
    idx = seasonality_index(ytd_tidy, fy_tidy, prior_year, level)
    current = _year_sales(ytd_tidy, current_year, level).rename("ytd_current")
    if level in BUDGET_LEVELS:
        budget = (
            ytd_tidy[ytd_tidy["year"] == current_year]
            .groupby(level, dropna=False)["sales_bdg"].sum(min_count=1)
            .rename("budget").fillna(0.0)
        )
    else:
        # No honest way to split a group-level budget across the accounts
        # inside the group, so it is left empty rather than guessed.
        budget = pd.Series(dtype="float64", name="budget")
    frame = idx.join(current, how="outer").join(budget, how="outer").fillna(
        {"ytd_current": 0.0, "budget": 0.0, "prior_ytd": 0.0, "prior_fy": 0.0}
    )
    # Groups that exist only on the current side arrive from the join with no
    # grade at all; they are not projectable.
    frame["projectable"] = frame["projectable"].fillna(False).astype(bool)
    frame["reliability"] = frame["reliability"].fillna("sin historia")

    good = frame[frame["projectable"]]
    if fallback_index is None:
        fallback_index = (
            good["prior_ytd"].sum() / good["prior_fy"].sum()
            if good["prior_fy"].sum() > 0 else np.nan
        )
    frame["index_used"] = np.where(frame["projectable"], frame["index"], fallback_index)
    frame["index_source"] = np.where(frame["projectable"], "propio", "cartera")

    with np.errstate(divide="ignore", invalid="ignore"):
        frame["landing"] = np.where(
            (frame["index_used"] > 0) & frame["index_used"].notna(),
            frame["ytd_current"] / frame["index_used"], np.nan,
        )
    # A landing below what is already booked is nonsense.
    frame["landing"] = frame[["landing", "ytd_current"]].max(axis=1)
    frame["gap_vs_budget"] = frame["landing"] - frame["budget"]
    frame["gap_vs_prior_fy"] = frame["landing"] - frame["prior_fy"]
    frame["budget_attainment"] = np.where(
        frame["budget"] > 0, frame["ytd_current"] / frame["budget"], np.nan
    )
    return frame.sort_values("gap_vs_budget")


def portfolio_pace(
    ytd_tidy: pd.DataFrame,
    fy_tidy: pd.DataFrame,
    current_year: int,
    prior_year: int,
) -> dict:
    """Headline numbers for the executive progress bars."""
    idx = seasonality_index(ytd_tidy, fy_tidy, prior_year, "enterprise")
    good = idx[idx["projectable"]]
    pace = (good["prior_ytd"].sum() / good["prior_fy"].sum()
            if good["prior_fy"].sum() > 0 else np.nan)

    cur = float(_year_sales(ytd_tidy, current_year, "enterprise").sum())
    budget = float(
        ytd_tidy[ytd_tidy["year"] == current_year]["sales_bdg"].fillna(0).sum()
    )
    prior_fy_total = float(_year_sales(fy_tidy, prior_year, "enterprise").sum())

    return {
        "pace_index": pace,
        "expected_share": pace,
        "current_ytd": cur,
        "budget": budget,
        "budget_attainment": cur / budget if budget else np.nan,
        "pace_gap": (cur / budget - pace) if budget and not np.isnan(pace) else np.nan,
        "prior_fy": prior_fy_total,
        "landing": cur / pace if pace and not np.isnan(pace) else np.nan,
        "n_projectable": int(idx["projectable"].sum()),
        "n_total": int(len(idx)),
        "n_inconsistent": int((idx["reliability"] == "base inconsistente").sum()),
    }


def multi_year_trend(fy_tidy: pd.DataFrame, years: list[int], level: str | None = None) -> pd.DataFrame:
    """Year-over-year series from the multi-year file (internally consistent)."""
    block = fy_tidy[fy_tidy["year"].isin(years)]
    keys = ["year"] + ([level] if level else [])
    agg = block.groupby(keys, dropna=False)[["sales", "profit", "quantity"]].sum(min_count=1)
    agg = agg.fillna(0.0).reset_index()
    agg["margin_pct"] = np.where(agg["sales"] != 0, agg["profit"] / agg["sales"], np.nan)
    agg["price"] = np.where(agg["quantity"] != 0, agg["sales"] / agg["quantity"], np.nan)
    return agg
'''

_MODULES["core.charts"] = r'''"""Reusable Plotly builders. One visual language across every tab."""

from __future__ import annotations

import numpy as np
import pandas as pd
import plotly.graph_objects as go

from core import theme as T
from core.i18n import t


def _trunc(values, width: int = 26):
    """Long account names blow up chart margins; keep the tail readable."""
    out = []
    for v in values:
        text = str(v)
        out.append(text if len(text) <= width else text[: width - 1] + "…")
    return out


def _empty(msg: str | None = None) -> go.Figure:
    fig = go.Figure()
    fig.add_annotation(text=msg or t("no_data"), showarrow=False, font=dict(color=T.MUTED, size=13))
    fig.update_layout(xaxis=dict(visible=False), yaxis=dict(visible=False), height=220)
    return fig


def waterfall(bridge: dict, title: str, unit: str = "$",
              horizontal: bool = False) -> go.Figure:
    """Bridge chart from a bridges.py result.

    Use horizontal=True when the steps are named entities (customers, products)
    rather than effects — long names are unreadable rotated onto an x axis.
    """
    steps = {k: v for k, v in bridge["steps"].items() if abs(v) > 0.5}
    if not steps:
        return _empty()
    labels = bridge.get("labels", {})

    names = [t("start")] + [labels.get(k, k) for k in steps] + [t("end")]
    measure = ["absolute"] + ["relative"] * len(steps) + ["total"]
    values = [bridge["start"]] + list(steps.values()) + [bridge["end"]]
    text = [T.signed(v) if m == "relative" else T.money_compact(v)
            for v, m in zip(values, measure)]

    style = dict(
        connector=dict(line=dict(color=T.RULE, width=1)),
        increasing=dict(marker=dict(color=T.POSITIVE)),
        decreasing=dict(marker=dict(color=T.NEGATIVE)),
        totals=dict(marker=dict(color=T.NAVY)),
        textposition="outside",
        cliponaxis=False,
    )

    if horizontal:
        fig = go.Figure(go.Waterfall(
            orientation="h", y=_trunc(names, 30)[::-1], x=values[::-1],
            measure=measure[::-1], text=text[::-1],
            hovertemplate="%{y}<br>%{x:$,.0f}<extra></extra>", **style,
        ))
        span = max(abs(min(values)), abs(max(values))) or 1.0
        fig.update_layout(
            title=title, height=max(360, 30 * len(names) + 130), showlegend=False,
            xaxis=dict(tickprefix=unit, tickformat=",.2s",
                       range=[min(0.0, min(values)) - span * 0.30,
                              max(values) + span * 0.30]),
            yaxis=dict(automargin=True),
        )
        return fig

    fig = go.Figure(go.Waterfall(
        orientation="v", x=_trunc(names, 22), y=values, measure=measure, text=text,
        hovertemplate="%{x}<br>%{y:$,.0f}<extra></extra>", **style,
    ))
    top = max(values) if values else 1.0
    fig.update_layout(title=title, height=440, showlegend=False,
                      xaxis=dict(tickangle=-25, automargin=True),
                      yaxis=dict(tickprefix=unit, tickformat=",.2s",
                                 range=[0, top * 1.2]))
    return fig


def progress_bar(
    value: float,
    target: float,
    pace: float | None = None,
    title: str = "",
    subtitle: str = "",
    formatter=None,
) -> go.Figure:
    """Horizontal attainment bar with an expected-pace marker."""
    if not target or target <= 0 or value is None:
        return _empty(t("budget"))
    share = value / target
    colour = T.POSITIVE if (pace is None or share >= pace) else (
        T.WARNING if share >= (pace or 0) * 0.9 else T.NEGATIVE
    )

    fig = go.Figure()
    # Track first, fill on top — overlay, not stack, or the fill would start
    # where the track ends.
    fig.add_trace(go.Bar(x=[1.0], y=[""], orientation="h", marker=dict(color="#EDF1F5"),
                         hoverinfo="skip", showlegend=False, width=0.5))
    fig.add_trace(go.Bar(x=[share], y=[""], orientation="h",
                         marker=dict(color=colour), showlegend=False, width=0.5,
                         hovertemplate=f"{share:.1%}<extra></extra>"))
    if pace is not None and not np.isnan(pace):
        fig.add_shape(type="line", x0=pace, x1=pace, y0=-0.4, y1=0.4,
                      line=dict(color=T.NAVY, width=2, dash="dot"))
        fig.add_annotation(x=pace, y=0.45, text=f"{pace:.0%}", showarrow=False,
                           font=dict(size=11, color=T.NAVY), yanchor="bottom")

    fmt = formatter or T.money_compact
    label = f"{share:.0%} · {fmt(value)} / {fmt(target)}"
    fig.update_layout(
        barmode="overlay", height=132, title=dict(text=title, font=dict(size=14)),
        xaxis=dict(range=[0, max(1.15, share * 1.1)], tickformat=".0%",
                   showgrid=False, zeroline=False),
        yaxis=dict(showticklabels=False, showgrid=False),
        margin=dict(l=4, r=4, t=44, b=28), showlegend=False,
    )
    fig.add_annotation(x=0, y=-0.62, text=f"{label}   {subtitle}", showarrow=False,
                       xanchor="left", font=dict(size=11, color=T.MUTED))
    return fig


def bullet(value: float, target: float, reference: float, title: str) -> go.Figure:
    """Landing forecast against budget and prior full year."""
    if value is None or (isinstance(value, float) and np.isnan(value)):
        return _empty(t("landing"))
    top = max(v for v in [value, target, reference] if v and not np.isnan(v)) * 1.15
    fig = go.Figure(go.Indicator(
        mode="number+gauge+delta",
        value=value,
        delta={"reference": target, "valueformat": ",.0f",
               "increasing": {"color": T.POSITIVE}, "decreasing": {"color": T.NEGATIVE}},
        number={"prefix": "$", "valueformat": ",.0f", "font": {"size": 26}},
        gauge={
            "shape": "bullet",
            "axis": {"range": [0, top], "tickprefix": "$", "tickformat": ",.2s"},
            "bar": {"color": T.NAVY, "thickness": 0.55},
            "bgcolor": "#EDF1F5",
            "bordercolor": T.RULE,
            "steps": [
                {"range": [0, reference or 0], "color": "#DCE6EF"},
            ],
            "threshold": {"line": {"color": T.NEGATIVE, "width": 3},
                          "thickness": 0.85, "value": target or 0},
        },
        title={"text": title, "font": {"size": 13, "color": T.MUTED}},
    ))
    fig.update_layout(height=150, margin=dict(l=140, r=20, t=30, b=20))
    return fig


def diverging_bars(
    df: pd.DataFrame, label_col: str, value_col: str, title: str, top_n: int = 15
) -> go.Figure:
    """Winners and losers on one axis, ranked by USD impact."""
    if df.empty:
        return _empty()
    d = df.reindex(df[value_col].abs().sort_values(ascending=False).index).head(top_n)
    d = d.sort_values(value_col)
    colours = [T.NEGATIVE if v < 0 else T.POSITIVE for v in d[value_col]]
    span = float(d[value_col].abs().max()) or 1.0
    fig = go.Figure(go.Bar(
        x=d[value_col], y=_trunc(d[label_col], 32), orientation="h",
        marker=dict(color=colours), cliponaxis=False,
        text=[T.signed(v) for v in d[value_col]], textposition="outside",
        customdata=d[label_col].astype(str),
        hovertemplate="%{customdata}<br>%{x:$,.0f}<extra></extra>",
    ))
    fig.update_layout(title=title, height=max(300, 27 * len(d) + 120),
                      xaxis=dict(tickprefix="$", tickformat=",.2s",
                                 range=[min(0, float(d[value_col].min())) - span * 0.28,
                                        max(0, float(d[value_col].max())) + span * 0.28]),
                      yaxis=dict(automargin=True), showlegend=False)
    return fig


def grouped_bars(
    df: pd.DataFrame, label_col: str, series: dict[str, str], title: str, top_n: int = 12
) -> go.Figure:
    """series maps column -> legend label."""
    if df.empty:
        return _empty()
    first = list(series)[0]
    d = df.sort_values(first, ascending=False).head(top_n)
    fig = go.Figure()
    for i, (col, name) in enumerate(series.items()):
        if col not in d.columns:
            continue
        fig.add_trace(go.Bar(
            name=name, x=d[label_col].astype(str), y=d[col],
            marker=dict(color=T.CATEGORICAL[i % len(T.CATEGORICAL)]),
            hovertemplate="%{x}<br>" + name + ": %{y:$,.0f}<extra></extra>",
        ))
    fig.update_layout(title=title, barmode="group", height=400,
                      yaxis=dict(tickprefix="$", tickformat=",.2s"),
                      xaxis=dict(tickangle=-30))
    return fig


def trend_lines(
    df: pd.DataFrame, x: str, y: str, title: str, y_fmt: str = "$",
    budget_col: str | None = None,
) -> go.Figure:
    if df.empty:
        return _empty()
    d = df.sort_values(x)
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=d[x], y=d[y], mode="lines+markers+text", name=t("real"),
        line=dict(color=T.NAVY, width=3), marker=dict(size=9),
        text=[T.money_compact(v) for v in d[y]], textposition="top center",
        textfont=dict(size=11, color=T.MUTED),
        hovertemplate="%{x}<br>%{y:$,.0f}<extra></extra>",
    ))
    if budget_col and budget_col in d.columns and d[budget_col].notna().any():
        fig.add_trace(go.Scatter(
            x=d[x], y=d[budget_col], mode="lines+markers", name=t("budget"),
            line=dict(color=T.WARNING, width=2, dash="dash"), marker=dict(size=7),
        ))
    fig.update_layout(title=title, height=380,
                      yaxis=dict(tickprefix=y_fmt if y_fmt == "$" else "",
                                 tickformat=",.2s"),
                      xaxis=dict(type="category"))
    return fig


def dual_axis_trend(df: pd.DataFrame, x: str, bar: str, line: str, title: str) -> go.Figure:
    if df.empty:
        return _empty()
    d = df.sort_values(x)
    fig = go.Figure()
    fig.add_trace(go.Bar(x=d[x], y=d[bar], name=t("sales"),
                         marker=dict(color=T.AZURE),
                         hovertemplate="%{x}<br>%{y:$,.0f}<extra></extra>"))
    fig.add_trace(go.Scatter(x=d[x], y=d[line], name=t("axis_margin"), yaxis="y2",
                             mode="lines+markers", line=dict(color=T.NAVY, width=3),
                             marker=dict(size=8),
                             hovertemplate="%{x}<br>%{y:.1%}<extra></extra>"))
    fig.update_layout(
        title=title, height=380, xaxis=dict(type="category"),
        yaxis=dict(tickprefix="$", tickformat=",.2s"),
        yaxis2=dict(overlaying="y", side="right", tickformat=".0%",
                    showgrid=False, range=[0, max(0.7, float(d[line].max() or 0) * 1.25)]),
    )
    return fig


def quadrant(
    df: pd.DataFrame, x: str, y: str, size: str, label: str, title: str,
    x_ref: float = 0.0, y_ref: float | None = None, top_n: int = 40,
) -> go.Figure:
    """Growth vs margin bubble map with named quadrants."""
    d = df.dropna(subset=[x, y]).copy()
    if d.empty:
        return _empty()
    d = d.reindex(d[size].abs().sort_values(ascending=False).index).head(top_n)
    if y_ref is None:
        y_ref = float(d[y].median())

    colours = [
        T.POSITIVE if (gx >= x_ref and gy >= y_ref) else
        T.AZURE if (gx < x_ref and gy >= y_ref) else
        T.WARNING if (gx >= x_ref and gy < y_ref) else T.NEGATIVE
        for gx, gy in zip(d[x], d[y])
    ]
    sizes = d[size].abs()
    scale = float(sizes.max()) or 1.0

    fig = go.Figure(go.Scatter(
        x=d[x], y=d[y], mode="markers",
        marker=dict(size=8 + 42 * (sizes / scale), color=colours,
                    line=dict(width=1, color="white"), opacity=0.85),
        text=d[label].astype(str),
        customdata=np.stack([d[size]], axis=-1),
        hovertemplate="<b>%{text}</b><br>%{x:.1%}<br>%{y:.1%}"
                      "<br>%{customdata[0]:$,.0f}<extra></extra>",
    ))
    fig.add_vline(x=x_ref, line=dict(color=T.RULE, width=1, dash="dash"))
    fig.add_hline(y=y_ref, line=dict(color=T.RULE, width=1, dash="dash"))
    notes = [
        (0.99, 0.99, t("quad_stars"), "right", "top"),
        (0.01, 0.99, t("quad_defend"), "left", "top"),
        (0.99, 0.01, t("quad_price"), "right", "bottom"),
        (0.01, 0.01, t("quad_rescue"), "left", "bottom"),
    ]
    for px, py, txt, xa, ya in notes:
        fig.add_annotation(xref="paper", yref="paper", x=px, y=py, text=txt,
                           showarrow=False, xanchor=xa, yanchor=ya,
                           font=dict(size=11, color=T.MUTED))
    fig.update_layout(title=title, height=480,
                      xaxis=dict(title=t("axis_growth"), tickformat=".0%"),
                      yaxis=dict(title=t("axis_margin"), tickformat=".0%"))
    return fig


def treemap(df: pd.DataFrame, path_cols: list[str], value: str, colour: str,
            title: str) -> go.Figure:
    d = df.copy()
    d = d[d[value] > 0]
    if d.empty:
        return _empty()
    labels, parents, values, colours = [], [], [], []
    root = "Total"
    labels.append(root); parents.append(""); values.append(float(d[value].sum()))
    colours.append(0.0)

    level1 = d.groupby(path_cols[0], dropna=False).agg(
        v=(value, "sum"), c=(colour, "mean")).reset_index()
    for _, r in level1.iterrows():
        labels.append(str(r[path_cols[0]])); parents.append(root)
        values.append(float(r["v"])); colours.append(float(r["c"]) if pd.notna(r["c"]) else 0.0)

    if len(path_cols) > 1:
        for _, r in d.iterrows():
            labels.append(f"{r[path_cols[1]]}")
            parents.append(str(r[path_cols[0]]))
            values.append(float(r[value]))
            colours.append(float(r[colour]) if pd.notna(r[colour]) else 0.0)

    lim = max(abs(np.nanpercentile(colours, 5)), abs(np.nanpercentile(colours, 95)), 0.01)
    fig = go.Figure(go.Treemap(
        labels=labels, parents=parents, values=values, branchvalues="total",
        marker=dict(colors=colours, colorscale=T.DIVERGING, cmid=0, cmin=-lim, cmax=lim,
                    line=dict(width=1, color="white"),
                    colorbar=dict(title="Δ pp", tickformat=".0f")),
        hovertemplate="<b>%{label}</b><br>%{value:$,.0f}<extra></extra>",
        tiling=dict(pad=2),
    ))
    fig.update_layout(title=title, height=520, margin=dict(t=56, l=4, r=4, b=4))
    return fig


def scatter_price_volume(df: pd.DataFrame, title: str) -> go.Figure:
    d = df.dropna(subset=["price_delta_pct", "quantity_delta_pct"]).copy()
    d = d[(d["sales_base"] > 0) & (d["quantity_base"] > 0)]
    if d.empty:
        return _empty()
    sizes = d["sales_cur"].abs()
    scale = float(sizes.max()) or 1.0
    fig = go.Figure(go.Scatter(
        x=d["price_delta_pct"].clip(-1, 2), y=d["quantity_delta_pct"].clip(-1, 3),
        mode="markers",
        marker=dict(size=8 + 34 * (sizes / scale), color=d["margin_pct_cur"],
                    colorscale=T.SEQUENTIAL, showscale=True,
                    colorbar=dict(title=t("margin"), tickformat=".0%"),
                    line=dict(width=1, color="white"), opacity=0.85),
        text=d.iloc[:, 0].astype(str),
        hovertemplate="<b>%{text}</b><br>%{x:.1%}<br>%{y:.1%}<extra></extra>",
    ))
    fig.add_vline(x=0, line=dict(color=T.RULE, width=1))
    fig.add_hline(y=0, line=dict(color=T.RULE, width=1))
    fig.update_layout(title=title, height=460,
                      xaxis=dict(title=t("axis_dprice"), tickformat=".0%"),
                      yaxis=dict(title=t("axis_dvolume"), tickformat=".0%"))
    return fig


def stacked_progress(df: pd.DataFrame, label: str, done: str, missing: str,
                     title: str, top_n: int = 15) -> go.Figure:
    if df.empty:
        return _empty()
    d = df.sort_values(done, ascending=False).head(top_n).sort_values(done)
    gap = (d[missing] - d[done]).clip(lower=0)
    fig = go.Figure()
    fig.add_trace(go.Bar(y=_trunc(d[label], 32), x=d[done], orientation="h",
                         name=t("achieved"), marker=dict(color=T.NAVY),
                         hovertemplate="%{y}<br>%{x:$,.0f}<extra></extra>"))
    fig.add_trace(go.Bar(y=_trunc(d[label], 32), x=gap, orientation="h",
                         name=t("missing"), marker=dict(color="#DCE6EF"),
                         hovertemplate="%{y}<br>%{x:$,.0f}<extra></extra>"))
    fig.update_layout(title=title, barmode="stack",
                      height=max(320, 26 * len(d) + 110),
                      xaxis=dict(tickprefix="$", tickformat=",.2s"),
                      yaxis=dict(automargin=True))
    return fig


def heatmap(pivot: pd.DataFrame, title: str, fmt: str = ".0%") -> go.Figure:
    if pivot.empty:
        return _empty()
    lim = float(np.nanmax(np.abs(pivot.values))) or 0.01
    fig = go.Figure(go.Heatmap(
        z=pivot.values, x=[str(c) for c in pivot.columns],
        y=_trunc(pivot.index, 30),
        colorscale=T.DIVERGING, zmid=0, zmin=-lim, zmax=lim,
        hovertemplate="%{y} · %{x}<br>%{z:" + fmt + "}<extra></extra>",
        colorbar=dict(tickformat=fmt),
    ))
    fig.update_layout(title=title, height=max(320, 22 * len(pivot) + 130),
                      xaxis=dict(type="category"), yaxis=dict(automargin=True))
    return fig
'''

_MODULES["core.ui"] = r'''"""Small shared UI pieces: KPI cards, table styling, in-memory Excel export."""

from __future__ import annotations

import io

import numpy as np
import pandas as pd
import streamlit as st

from core import theme as T
from core.schema import TOGGLEABLE_METRICS

_FMT = {
    "money": T.money_compact,
    "pct": T.pct,
    "qty": lambda v: T.qty(v, st.session_state.get("flt_unit", "kg")),
    "unit": T.unit_value,
    "int": lambda v: "—" if v is None or v != v else f"{v:,.0f}",
}


def kpi_card(label: str, value: str, deltas: list[tuple[str, float, bool]] | None = None) -> str:
    rows = ""
    for text, direction, higher_is_better in deltas or []:
        if direction is None or (isinstance(direction, float) and np.isnan(direction)):
            cls = "rb-flat"
        elif direction == 0:
            cls = "rb-flat"
        else:
            good = (direction > 0) == higher_is_better
            cls = "rb-up" if good else "rb-down"
        rows += f'<div class="rb-delta {cls}">{html_escape(str(text))}</div>'
    return (
        f'<div class="rb-card"><div class="rb-label">{label}</div>'
        f'<div class="rb-value">{html_escape(str(value))}</div>{rows}</div>'
    )


def kpi_row(cards: list[str]) -> None:
    if not cards:
        return
    cols = st.columns(len(cards))
    for col, html in zip(cols, cards):
        col.markdown(html, unsafe_allow_html=True)


def metric_cards(cur: pd.Series, base: pd.Series, active: list[str],
                 base_label: str, budget: pd.Series | None = None) -> list[str]:
    """Build KPI cards for whichever metrics are switched on."""
    lang = st.session_state.get("lang", "es")
    cards = []
    higher_better = {"unit_cost": False}
    for key in active:
        meta = TOGGLEABLE_METRICS.get(key)
        if meta is None:
            continue
        src_key = {"margin_pct": "margin_pct", "price": "price"}.get(key, key)
        v = cur.get(src_key, np.nan)
        b = base.get(src_key, np.nan)
        fmt = _FMT[meta["fmt"]]
        deltas = []
        if b is not None and not (isinstance(b, float) and np.isnan(b)):
            if key == "margin_pct":
                d = (v - b) * 100
                deltas.append((f"{d:+.1f} pp {base_label}", d, True))
            else:
                d = v - b
                rel = d / abs(b) if b else np.nan
                txt = f"{T.signed(d, fmt)} ({rel*100:+.1f}%) {base_label}" \
                    if not np.isnan(rel) else f"{T.signed(d, fmt)} {base_label}"
                deltas.append((txt, d, higher_better.get(key, True)))
        if budget is not None and key in ("sales", "profit", "quantity"):
            bkey = {"sales": "sales_bdg", "profit": "profit_bdg", "quantity": "qty_bdg"}[key]
            bv = budget.get(bkey, np.nan)
            if bv and not np.isnan(bv):
                d = v - bv
                deltas.append((f"{T.signed(d, fmt)} vs budget", d, True))
        cards.append(kpi_card(meta[lang], fmt(v), deltas))
    return cards


def _diverging_css(value, scale: float) -> str:
    """Red↔green cell shading in the Robertet palette.

    Written by hand on purpose: pandas' background_gradient needs matplotlib,
    which is a heavy dependency that is absent on a clean Streamlit Cloud image
    and fails there with an opaque ImportError.
    """
    try:
        v = float(value)
    except (TypeError, ValueError):
        return ""
    if v != v or scale <= 0:
        return ""
    ratio = max(-1.0, min(1.0, v / scale))
    if abs(ratio) < 0.02:
        return ""
    # Blend white toward the semantic colour; cap opacity so text stays readable.
    end = (31, 122, 90) if ratio > 0 else (176, 58, 46)
    weight = 0.12 + 0.55 * abs(ratio)
    r = round(255 + (end[0] - 255) * weight)
    g = round(255 + (end[1] - 255) * weight)
    b = round(255 + (end[2] - 255) * weight)
    text = "#FFFFFF" if weight > 0.5 else T.INK
    return f"background-color: rgb({r},{g},{b}); color: {text};"


def style_table(df: pd.DataFrame, money_cols: list[str], pct_cols: list[str],
                pp_cols: list[str] | None = None, qty_cols: list[str] | None = None,
                highlight: list[str] | None = None):
    fmt = {}
    for c in money_cols:
        if c in df.columns:
            fmt[c] = lambda v: T.money(v, 0)
    for c in pct_cols:
        if c in df.columns:
            fmt[c] = lambda v: T.pct(v, 1)
    for c in pp_cols or []:
        if c in df.columns:
            fmt[c] = lambda v: T.pp(v, 1)
    for c in qty_cols or []:
        if c in df.columns:
            fmt[c] = lambda v: f"{v:,.0f}" if pd.notna(v) else "—"

    styler = df.style.format(fmt, na_rep="—")
    for c in highlight or []:
        if c in df.columns and df[c].notna().any():
            scale = float(pd.to_numeric(df[c], errors="coerce").abs().max() or 1.0)
            styler = styler.map(lambda v, s=scale: _diverging_css(v, s), subset=[c])
    return styler


def to_excel_bytes(sheets: dict[str, pd.DataFrame]) -> bytes:
    """Build a workbook entirely in memory — never touches the filesystem."""
    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
        for name, frame in sheets.items():
            frame.to_excel(writer, sheet_name=name[:31], index=False)
    return buffer.getvalue()


def download_button(label: str, sheets: dict[str, pd.DataFrame], filename: str, key: str) -> None:
    st.download_button(
        label, data=to_excel_bytes(sheets), file_name=filename, key=key,
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )


def md_escape(text: str) -> str:
    """Streamlit renders $...$ as LaTeX, which mangles any sentence carrying two
    dollar amounts. Escape them before handing text to plain st.markdown."""
    return text.replace("$", r"\$")


def html_escape(text: str) -> str:
    """Same problem, HTML context: a backslash would render literally there, so
    the dollar sign goes in as an entity instead."""
    return text.replace("$", "&#36;")


def note(text: str) -> None:
    st.markdown(f'<div class="rb-note">{html_escape(text)}</div>',
                unsafe_allow_html=True)


def chip(text: str, kind: str = "ok") -> str:
    return f'<span class="rb-chip rb-chip-{kind}">{text}</span>'
'''

_MODULES["core.insights"] = r'''"""Rule engine: turns the filtered numbers into quantified, actionable bullets.

Every bullet carries a USD figure. Nothing generic, nothing that could have been
written before seeing the data. Sentences live in `core.i18n` as templates so
the whole tab switches language with everything else.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from core import theme as T
from core.i18n import t
from core.metrics import herfindahl

M = T.money_compact


def _pctf(v, d=1):
    return "—" if v is None or (isinstance(v, float) and np.isnan(v)) else f"{v*100:,.{d}f}%"


def _names(frame: pd.DataFrame, col: str, n: int = 3) -> str:
    return ", ".join(str(x) for x in frame[col].head(n))


# --------------------------------------------------------------------------- #
def diagnose(cmp_cust: pd.DataFrame, cmp_prod: pd.DataFrame, sales_br: dict,
             margin_br: dict, pace: dict | None, label_col: str = "customer") -> list[str]:
    out: list[str] = []
    if cmp_cust.empty:
        return [t("ins_nodata")]

    cur = cmp_cust["sales_cur"].sum()
    base = cmp_cust["sales_base"].sum()
    delta = cur - base
    out.append(t("ins_headline", cur=M(cur), base=M(base),
                 delta=T.signed(delta), pct=_pctf(delta / base if base else np.nan)))

    steps = sales_br["steps"]
    driver_key, driver_value = max(steps.items(), key=lambda kv: abs(kv[1]))
    out.append(t("ins_driver",
                 driver=sales_br["labels"].get(driver_key, driver_key).lower(),
                 value=T.signed(driver_value),
                 volume=T.signed(steps.get("volume", 0)),
                 price=T.signed(steps.get("price", 0))))

    mc = cmp_cust["profit_cur"].sum() / cur if cur else np.nan
    mb = cmp_cust["profit_base"].sum() / base if base else np.nan
    if not np.isnan(mc) and not np.isnan(mb):
        msteps = margin_br["steps"]
        price_e, cost_e = msteps.get("price", 0.0), msteps.get("cost", 0.0)
        out.append(t("ins_margin", cur=_pctf(mc), base=_pctf(mb),
                     pp=f"{(mc - mb) * 100:+.1f} pp",
                     cause=t("cause_price") if abs(price_e) >= abs(cost_e)
                     else t("cause_cost"),
                     price=T.signed(price_e), cost=T.signed(cost_e)))

    movers = cmp_cust.reindex(cmp_cust["sales_delta"].abs().sort_values(ascending=False).index)
    total_move = movers["sales_delta"].abs().sum()
    if total_move:
        top3 = movers.head(3)
        out.append(t("ins_concentration",
                     pct=_pctf(top3["sales_delta"].abs().sum() / total_move, 0),
                     names=_names(top3, label_col)))

    if pace and not np.isnan(pace.get("budget_attainment", np.nan)):
        att = pace["budget_attainment"]
        exp = pace.get("expected_share", np.nan)
        if not np.isnan(exp):
            out.append(t("ins_pace", att=_pctf(att, 0), pace=_pctf(exp, 0),
                         verdict=t("ins_above") if att >= exp else t("ins_below"),
                         landing=M(pace.get("landing")), budget=M(pace.get("budget"))))
        else:
            out.append(t("ins_attain", att=_pctf(att, 0), budget=M(pace.get("budget"))))

    if not cmp_prod.empty:
        pm = cmp_prod.reindex(cmp_prod["sales_delta"].abs().sort_values(ascending=False).index)
        top = pm.iloc[0]
        out.append(t("ins_top_product", name=top[pm.columns[0]],
                     value=T.signed(top["sales_delta"])))
    return out


def risks(cmp_cust: pd.DataFrame, cmp_prod: pd.DataFrame, forecast: pd.DataFrame | None,
          label_col: str = "customer") -> list[str]:
    out: list[str] = []
    if cmp_cust.empty:
        return out

    lost = cmp_cust[cmp_cust["status"] == "perdido"].sort_values("sales_base", ascending=False)
    if not lost.empty:
        out.append(t("ins_churn", n=len(lost), total=M(lost["sales_base"].sum()),
                     name=lost.iloc[0][label_col], value=M(lost.iloc[0]["sales_base"])))

    if "margin_pct_delta_pp" in cmp_cust.columns:
        eroding = cmp_cust[(cmp_cust["margin_pct_delta_pp"] < -3)
                           & (cmp_cust["sales_cur"] > 20_000)]
        if not eroding.empty:
            worst = eroding.sort_values("margin_pct_delta_pp").iloc[0]
            out.append(t("ins_margin_erosion", n=len(eroding), name=worst[label_col],
                         pp=f"{worst['margin_pct_delta_pp']:+.1f} pp",
                         sales=M(worst["sales_cur"])))

    hhi = herfindahl(cmp_cust["sales_cur"])
    if not np.isnan(hhi):
        total = cmp_cust["sales_cur"].sum()
        top_share = cmp_cust["sales_cur"].max() / total if total else np.nan
        level = t("ins_conc_high") if hhi > 0.18 else (
            t("ins_conc_mid") if hhi > 0.10 else t("ins_conc_low"))
        out.append(t("ins_concentration_risk", level=level, hhi=f"{hhi:.3f}",
                     pct=_pctf(top_share, 0)))

    if forecast is not None and not forecast.empty:
        short = forecast[(forecast["gap_vs_budget"] < 0) & (forecast["budget"] > 0)]
        if not short.empty:
            out.append(t("ins_budget_short", n=len(short),
                         total=M(abs(short["gap_vs_budget"].sum())),
                         name=short.index[0],
                         value=M(abs(short.iloc[0]["gap_vs_budget"]))))
        unreliable = forecast[~forecast["projectable"]]
        if len(unreliable) > 0:
            out.append(t("ins_unprojectable", n=len(unreliable), total=len(forecast)))

    if not cmp_prod.empty:
        col = cmp_prod.columns[0]
        drop = cmp_prod[(cmp_prod["sales_delta"] < 0) & (cmp_prod["sales_base"] > 30_000)]
        if not drop.empty:
            w = drop.sort_values("sales_delta").iloc[0]
            out.append(t("ins_product_drop", name=w[col],
                         value=M(abs(w["sales_delta"])),
                         pct=_pctf(w.get("sales_delta_pct"))))
    return out


def opportunities(cmp_cust: pd.DataFrame, cmp_prod: pd.DataFrame,
                  label_col: str = "customer") -> list[str]:
    out: list[str] = []
    if cmp_cust.empty:
        return out

    grow = cmp_cust[(cmp_cust["sales_delta"] > 0) & (cmp_cust["sales_cur"] > 0)]
    if not grow.empty:
        top = grow.sort_values("sales_delta", ascending=False).head(3)
        detail = ", ".join(f"{r[label_col]} (+{M(r['sales_delta'])})"
                           for _, r in top.iterrows())
        out.append(t("ins_growing", n=len(grow),
                     total=M(grow["sales_delta"].sum()), detail=detail))

    if not cmp_prod.empty and "margin_pct_cur" in cmp_prod.columns:
        col = cmp_prod.columns[0]
        rich = cmp_prod[(cmp_prod["margin_pct_cur"] > cmp_prod["margin_pct_cur"].median())
                        & (cmp_prod["sales_cur"] > 0)]
        if not rich.empty:
            small = rich.sort_values("sales_cur").head(3)
            detail = ", ".join(
                f"{r[col]} ({_pctf(r['margin_pct_cur'], 0)}, {M(r['sales_cur'])})"
                for _, r in small.iterrows())
            out.append(t("ins_rich_products", detail=detail))

    new = cmp_cust[cmp_cust["status"] == "nuevo"]
    if not new.empty:
        out.append(t("ins_new_accounts", n=len(new), total=M(new["sales_cur"].sum())))

    if "sales_open_cur" in cmp_cust.columns:
        backlog = float(cmp_cust["sales_open_cur"].fillna(0).sum())
        if backlog > 0:
            carriers = int((cmp_cust["sales_open_cur"].fillna(0) > 0).sum())
            out.append(t("ins_backlog", total=M(backlog), n=carriers))

    if "margin_pct_cur" in cmp_cust.columns:
        recover = cmp_cust[(cmp_cust["sales_delta"] < 0) & (cmp_cust["sales_cur"] > 0)
                           & (cmp_cust["margin_pct_cur"] > 0.4)]
        if not recover.empty:
            out.append(t("ins_recover", n=len(recover),
                         total=M(abs(recover["sales_delta"].sum()))))
    return out


def actions(cmp_cust: pd.DataFrame, forecast: pd.DataFrame | None,
            sales_br: dict, margin_br: dict, label_col: str = "customer") -> list[str]:
    out: list[str] = []
    if cmp_cust.empty:
        return out

    lost = cmp_cust[cmp_cust["status"] == "perdido"].sort_values("sales_base", ascending=False)
    if not lost.empty:
        out.append(t("act_churn", names=_names(lost, label_col),
                     total=M(lost["sales_base"].head(3).sum())))

    steps = margin_br["steps"]
    if steps.get("cost", 0) < -20_000:
        out.append(t("act_cost", value=M(abs(steps["cost"]))))
    if steps.get("price", 0) < -20_000:
        out.append(t("act_price", value=M(abs(steps["price"]))))
    if sales_br["steps"].get("volume", 0) < -50_000:
        out.append(t("act_volume", value=M(abs(sales_br["steps"]["volume"]))))

    if "sales_open_cur" in cmp_cust.columns:
        backlog = float(cmp_cust["sales_open_cur"].fillna(0).sum())
        if backlog > 0:
            out.append(t("act_backlog", total=M(backlog)))

    if forecast is not None and not forecast.empty:
        short = forecast[(forecast["gap_vs_budget"] < 0)
                         & (forecast["budget"] > 0)].head(5)
        if not short.empty:
            out.append(t("act_budget", total=M(abs(short["gap_vs_budget"].sum()))))
    return out


def build_all(cmp_cust: pd.DataFrame, cmp_prod: pd.DataFrame, sales_br: dict,
              margin_br: dict, pace: dict | None, forecast: pd.DataFrame | None,
              cust_label: str = "customer") -> dict[str, list[str]]:
    return {
        "diagnostico": diagnose(cmp_cust, cmp_prod, sales_br, margin_br, pace, cust_label),
        "riesgos": risks(cmp_cust, cmp_prod, forecast, cust_label),
        "oportunidades": opportunities(cmp_cust, cmp_prod, cust_label),
        "acciones": actions(cmp_cust, forecast, sales_br, margin_br, cust_label),
    }
'''

_MODULES["core.session"] = r'''"""Ephemeral session state.

Design rule, non-negotiable: nothing this module holds ever reaches disk.
Uploads are consumed as bytes from memory, parsed into dataframes held only in
`st.session_state`, and dropped when the browser tab closes, when the idle
timer expires, or when the user hits "Clear everything".
"""

from __future__ import annotations

import gc
import time

import streamlit as st

DATA_KEYS = ("ytd", "fy", "ytd_name", "fy_name", "diagnosis", "uploader_epoch")
DEFAULT_IDLE_MINUTES = 30


def init() -> None:
    st.session_state.setdefault("lang", "es")
    st.session_state.setdefault("ytd", None)
    st.session_state.setdefault("fy", None)
    st.session_state.setdefault("ytd_name", None)
    st.session_state.setdefault("fy_name", None)
    st.session_state.setdefault("presets", {})
    st.session_state.setdefault("idle_minutes", DEFAULT_IDLE_MINUTES)
    st.session_state.setdefault("last_touch", time.time())
    st.session_state.setdefault("uploader_epoch", 0)
    st.session_state.setdefault("confirm_clear", False)
    st.session_state.setdefault("auto_wiped", False)


def touch() -> None:
    st.session_state["last_touch"] = time.time()


def seconds_left() -> float:
    limit = st.session_state.get("idle_minutes", DEFAULT_IDLE_MINUTES) * 60
    return max(0.0, limit - (time.time() - st.session_state.get("last_touch", time.time())))


def enforce_idle_timeout() -> bool:
    """Wipe data if the session has gone quiet. Returns True if it wiped."""
    if seconds_left() <= 0 and has_data():
        clear_all(keep_preferences=True)
        st.session_state["auto_wiped"] = True
        return True
    return False


def has_data() -> bool:
    return st.session_state.get("ytd") is not None or st.session_state.get("fy") is not None


def store(slot: str, parsed, filename: str) -> None:
    st.session_state[slot] = parsed
    st.session_state[f"{slot}_name"] = filename
    touch()


def clear_all(keep_preferences: bool = False) -> None:
    """Drop every trace of the loaded data from memory."""
    for key in DATA_KEYS:
        if key in st.session_state:
            st.session_state[key] = None

    # Any cached derivative of the data goes too.
    for key in [k for k in list(st.session_state.keys())
                if k.startswith(("cache_", "sel_", "flt_"))]:
        del st.session_state[key]

    if not keep_preferences:
        st.session_state["presets"] = {}
    # "lang" is bound to a widget; assigning it here would raise once the widget
    # exists, so the language always survives a wipe.

    # Force the file_uploader widgets to remount empty, so the browser-side
    # buffer is released too rather than lingering in the widget.
    st.session_state["uploader_epoch"] = st.session_state.get("uploader_epoch", 0) + 1
    st.session_state["confirm_clear"] = False

    try:
        st.cache_data.clear()
    except Exception:
        pass
    gc.collect()
    touch()
'''

_MODULES["core.context"] = r'''"""Sidebar state + the filtered slice every view reads from."""

from __future__ import annotations

from dataclasses import dataclass, field

import pandas as pd
import streamlit as st

from core import metrics as MX
from core.i18n import level_label, metric_label, t
from core.schema import BUDGET_LEVELS, GROUP_LEVELS, TOGGLEABLE_METRICS


@dataclass
class Context:
    tidy: pd.DataFrame                 # filtered, from the active file
    ytd: object | None = None          # ParsedExport
    fy: object | None = None           # ParsedExport
    source: str = "ytd"
    current_year: int = 0
    base_year: int = 0
    group_level: str = "customer"
    second_level: str | None = None
    top_n: int = 15
    include_open: bool = False
    materiality: float = 0.0
    unit: str = "kg"
    active_metrics: list[str] = field(default_factory=list)
    lang: str = "es"
    selected_groups: list[str] = field(default_factory=list)
    selected_accounts: list[str] = field(default_factory=list)

    @property
    def has_both(self) -> bool:
        return self.ytd is not None and self.fy is not None

    def budget_supported(self, level: str | None = None) -> bool:
        """Budget is loaded against a placeholder customer, so it only lands
        on the enterprise and the product hierarchy."""
        return (level or self.group_level) in BUDGET_LEVELS

    def compare(self, level: str | None = None) -> pd.DataFrame:
        level = level or self.group_level
        source = self.tidy
        if not self.budget_supported(level) and "is_group_row" in source.columns:
            # Placeholder budget rows would appear as ghost accounts with a
            # budget and no sales. Drop them and the budget columns with them.
            source = source[~source["is_group_row"]]
        df = MX.compare(source, level, self.current_year, self.base_year,
                        include_open=self.include_open)
        if not self.budget_supported(level):
            df = df.drop(columns=[c for c in df.columns
                                  if "bdg" in c or c == "sales_vs_bdg"], errors="ignore")
        return MX.apply_materiality(df, self.materiality)

    def unfiltered(self):
        """The active file's full tidy frame, ignoring the sidebar filters.

        The client sheet needs the whole portfolio to rank a client inside it.
        """
        parsed = self.ytd if self.source == "ytd" else self.fy
        return parsed.tidy if parsed is not None else self.tidy

    def slice_year(self, year: int) -> pd.DataFrame:
        return self.tidy[self.tidy["year"] == year]

    def label_for(self, level: str) -> str:
        return level_label(level)


def _pretty_level(level: str) -> str:
    return level_label(level)


def build_sidebar(ytd, fy) -> Context:
    """Render the pivot-style sidebar and return the resulting Context."""
    active_file = st.session_state.get("flt_source")
    options = []
    if ytd is not None:
        options.append("ytd")
    if fy is not None:
        options.append("fy")
    if not options:
        raise RuntimeError("No hay archivos cargados.")

    labels = {"ytd": t("file_ytd"), "fy": t("file_fy")}
    st.sidebar.markdown(f"### {t('comparison')}")
    source = st.sidebar.radio(
        t("data_source"), options, key="flt_source",
        format_func=lambda k: labels[k], horizontal=len(options) > 1,
        index=options.index(active_file) if active_file in options else 0,
    )
    parsed = ytd if source == "ytd" else fy
    tidy_all = parsed.tidy
    years = parsed.substantive_years or parsed.years

    c1, c2 = st.sidebar.columns(2)
    default_cur = years[-1]
    default_base = years[-2] if len(years) > 1 else years[-1]
    current_year = c1.selectbox(t("current_year"), years, index=years.index(default_cur),
                                key="flt_cur_year")
    base_opts = [y for y in years if y != current_year] or years
    base_year = c2.selectbox(
        t("base_year"), base_opts,
        index=base_opts.index(default_base) if default_base in base_opts else 0,
        key="flt_base_year",
    )

    # --- dimensions ---------------------------------------------------------
    st.sidebar.markdown(f"### {t('dimensions')}")
    level_keys = list(GROUP_LEVELS)
    group_level = st.sidebar.selectbox(
        t("group_by"), level_keys, index=level_keys.index("enterprise"),
        format_func=_pretty_level, key="flt_group",
    )
    if group_level not in BUDGET_LEVELS:
        st.sidebar.caption(t("budget_level_note"))
    second_opts = ["__none__"] + [k for k in level_keys if k != group_level]
    second = st.sidebar.selectbox(
        t("second_dim"), second_opts, key="flt_group2",
        format_func=lambda k: t("none") if k == "__none__" else _pretty_level(k),
    )
    second_level = None if second == "__none__" else second

    # Filter on the client GROUP, not the individual account. Filtering by
    # account silently dropped the budget (loaded against a "<GROUP> []"
    # placeholder) and split a client that trades under two codes.
    all_groups = sorted(tidy_all["enterprise"].dropna().unique().tolist())
    sel_groups = st.sidebar.multiselect(
        t("filter_customer"), all_groups, key="flt_groups", help=t("filter_customer_help"),
    )

    # Optional drill-down to specific accounts inside the chosen groups.
    account_pool = tidy_all
    if sel_groups:
        account_pool = account_pool[account_pool["enterprise"].isin(sel_groups)]
    all_accounts = sorted(
        account_pool.loc[~account_pool["is_group_row"], "customer"].dropna().unique().tolist()
    )
    sel_accounts = st.sidebar.multiselect(
        t("filter_account"), all_accounts, key="flt_accounts",
        help=t("filter_account_help"),
    )

    all_families = sorted(tidy_all["product_family"].dropna().unique().tolist())
    sel_families = st.sidebar.multiselect(
        t("filter_family"), all_families, key="flt_families", help=t("empty_all"),
    )
    top_n = st.sidebar.select_slider(t("top_n"), options=[5, 10, 15, 20, 30, 50],
                                     value=15, key="flt_topn")

    # --- metric toggles -----------------------------------------------------
    st.sidebar.markdown(f"### {t('metrics')}")
    st.sidebar.caption(t("metrics_help"))
    active: list[str] = []
    cols = st.sidebar.columns(2)
    for i, (key, meta) in enumerate(TOGGLEABLE_METRICS.items()):
        on = cols[i % 2].checkbox(metric_label(key), value=meta["default"],
                                  key=f"flt_m_{key}")
        if on:
            active.append(key)

    # --- calculation basis --------------------------------------------------
    st.sidebar.markdown(f"### {t('basis')}")
    include_open = st.sidebar.toggle(t("include_open"), value=False, key="flt_open",
                                    help=t("include_open_help"))
    materiality = st.sidebar.number_input(
        t("materiality"), min_value=0, max_value=250_000, value=0, step=1_000,
        key="flt_mat", help=t("materiality_help"),
    )
    unit = st.sidebar.text_input(t("unit"), value="kg", key="flt_unit")

    # --- apply filters ------------------------------------------------------
    tidy = tidy_all
    if sel_groups:
        tidy = tidy[tidy["enterprise"].isin(sel_groups)]
    if sel_accounts:
        # Keep the group's placeholder rows so the budget survives the filter.
        keep = tidy["customer"].isin(sel_accounts) | tidy["is_group_row"]
        tidy = tidy[keep]
    if sel_families:
        tidy = tidy[tidy["product_family"].isin(sel_families)]
    tidy = tidy[tidy["year"].isin(years)]

    if sel_groups or sel_accounts or sel_families:
        st.sidebar.caption(t("filter_active", n=f"{len(tidy):,}"))

    return Context(
        tidy=tidy, ytd=ytd, fy=fy, source=source,
        current_year=int(current_year), base_year=int(base_year),
        group_level=group_level, second_level=second_level, top_n=int(top_n),
        include_open=include_open, materiality=float(materiality), unit=unit or "kg",
        active_metrics=active, lang=st.session_state.get("lang", "es"),
        selected_groups=sel_groups, selected_accounts=sel_accounts,
    )
'''

_MODULES["views.overview"] = r'''"""Tab 1 — Executive overview: KPIs, budget progress, bridges, landing."""

from __future__ import annotations

import numpy as np
import streamlit as st

from core import bridges, charts, metrics as MX, theme as T, ui
from core.forecast import portfolio_pace
from core.i18n import t


def render(ctx) -> None:
    cur_slice = ctx.slice_year(ctx.current_year)
    base_slice = ctx.slice_year(ctx.base_year)
    if cur_slice.empty and base_slice.empty:
        st.info(t("no_data"))
        return

    cur = MX.totals(cur_slice)
    base = MX.totals(base_slice)
    invoiced = float(cur.get("sales") or 0)
    if ctx.include_open:
        cur["sales"] = invoiced + (cur.get("sales_open") or 0)
        cur["profit"] = (cur.get("profit") or 0) + (cur.get("profit_open") or 0)
        cur["quantity"] = (cur.get("quantity") or 0) + (cur.get("qty_open") or 0)
        cur["margin_pct"] = cur["profit"] / cur["sales"] if cur["sales"] else np.nan
        cur["price"] = cur["sales"] / cur["quantity"] if cur["quantity"] else np.nan

    st.markdown(f"### {t('ov_title', cur=ctx.current_year, base=ctx.base_year)}")
    ui.note(t(
        "ov_note",
        basis=t("basis_sold_open") if ctx.include_open else t("basis_invoiced"),
        level=ctx.label_for(ctx.group_level),
        n=f"{len(ctx.tidy['customer'].unique()):,}",
    ))

    cards = ui.metric_cards(cur, base, ctx.active_metrics,
                            t("vs_base_year", year=ctx.base_year), budget=cur)
    ui.kpi_row(cards[:5])
    if len(cards) > 5:
        ui.kpi_row(cards[5:])

    st.divider()

    # --- budget progress ----------------------------------------------------
    pace = None
    if ctx.has_both:
        try:
            pace = portfolio_pace(ctx.ytd.tidy, ctx.fy.tidy,
                                  ctx.current_year, ctx.current_year - 1)
        except Exception:
            pace = None
    pace_share = pace.get("expected_share") if pace else None

    budget = float(cur.get("sales_bdg") or 0)
    left, right = st.columns(2)
    with left:
        st.plotly_chart(
            charts.progress_bar(
                float(cur.get("sales") or 0), budget, pace=pace_share,
                title=t("ov_sales_bar"),
                subtitle=t("ov_pace_sub") if pace else "",
            ),
            width="stretch", key="overview_1")
        st.plotly_chart(
            charts.progress_bar(float(cur.get("profit") or 0),
                                float(cur.get("profit_bdg") or 0),
                                pace=pace_share, title=t("ov_profit_bar")),
            width="stretch", key="overview_2")
    with right:
        st.plotly_chart(
            charts.progress_bar(float(cur.get("quantity") or 0),
                                float(cur.get("qty_bdg") or 0),
                                pace=pace_share, title=t("ov_qty_bar"),
                                formatter=lambda v: T.qty(v, ctx.unit)),
            width="stretch", key="overview_3")
        open_orders = float(cur.get("sales_open") or 0)
        gap = budget - invoiced
        cover = open_orders / gap if gap > 0 else np.nan
        st.markdown(
            ui.kpi_card(
                t("ov_backlog_card"), T.money_compact(open_orders),
                [(t("ov_backlog_delta", pct=T.pct(cover, 0),
                    gap=T.money_compact(max(gap, 0))),
                  cover if cover == cover else None, True)],
            ),
            unsafe_allow_html=True,
        )
        if pace and not np.isnan(pace.get("landing", np.nan)):
            st.plotly_chart(
                charts.bullet(pace["landing"], pace["budget"], pace["prior_fy"],
                              t("landing")),
                width="stretch", key="overview_4")

    st.divider()

    # --- bridges ------------------------------------------------------------
    sb = bridges.sales_bridge(ctx.tidy, ctx.current_year, ctx.base_year)
    mb = bridges.margin_bridge(ctx.tidy, ctx.current_year, ctx.base_year)

    st.plotly_chart(
        charts.waterfall(sb, t("ov_sales_bridge", base=ctx.base_year, cur=ctx.current_year)),
        width="stretch", key="overview_5")
    delta = sb["end"] - sb["start"]
    driver_key, driver_value = max(sb["steps"].items(), key=lambda kv: abs(kv[1]))
    ui.note(t(
        "ov_bridge_note",
        dir=t("dir_up") if delta >= 0 else t("dir_down"),
        amount=T.money_compact(abs(delta)),
        pct=f"{abs(delta)/sb['start']*100 if sb['start'] else 0:.1f}%",
        driver=sb["labels"].get(driver_key, driver_key).lower(),
        value=T.signed(driver_value),
    ))

    st.plotly_chart(
        charts.waterfall(mb, t("ov_margin_bridge", base=ctx.base_year, cur=ctx.current_year)),
        width="stretch", key="overview_6")
    price_e, cost_e = mb["steps"].get("price", 0), mb["steps"].get("cost", 0)
    ui.note(t(
        "ov_margin_note",
        price=T.signed(price_e), cost=T.signed(cost_e),
        cause=t("cause_price") if abs(price_e) >= abs(cost_e) else t("cause_cost"),
    ))

    # --- budget gap by group ------------------------------------------------
    cmp_df = ctx.compare()
    if "sales_vs_bdg" in cmp_df.columns and cmp_df["sales_bdg_cur"].abs().sum() > 0:
        st.plotly_chart(
            charts.diverging_bars(
                cmp_df, ctx.group_level, "sales_vs_bdg",
                t("ov_budget_gap", level=ctx.label_for(ctx.group_level).lower()),
                top_n=ctx.top_n,
            ),
            width="stretch", key="overview_7")
'''

_MODULES["views.customer"] = r'''"""Tab — Client sheet: one customer group, everything about it on one screen.

Picks a single client group (the level the budget is loaded at, and the level
that keeps a client trading under two account codes together) and answers, in
order: how big, how is it doing, why did it move, what does it buy, what is
already booked, and where will it land.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
import streamlit as st

from core import bridges, charts, metrics as MX, theme as T, ui
from core.forecast import landing_forecast, multi_year_trend
from core.i18n import t

LEVEL = "enterprise"


def _client_options(ctx) -> pd.DataFrame:
    """Every client group with its current-year sales, biggest first."""
    full = ctx.unfiltered()
    cur = (full[full["year"] == ctx.current_year]
           .groupby(LEVEL, dropna=False)["sales"].sum(min_count=1).fillna(0.0))
    base = (full[full["year"] == ctx.base_year]
            .groupby(LEVEL, dropna=False)["sales"].sum(min_count=1).fillna(0.0))
    frame = pd.concat([cur.rename("cur"), base.rename("base")], axis=1).fillna(0.0)
    return frame.sort_values("cur", ascending=False)


def _pick_client(ctx, options: pd.DataFrame) -> str | None:
    names = options.index.tolist()
    if not names:
        return None
    # A sidebar filter already narrowing to one client preselects it.
    default = 0
    if ctx.selected_groups:
        for i, n in enumerate(names):
            if n in ctx.selected_groups:
                default = i
                break

    def label(name: str) -> str:
        row = options.loc[name]
        return f"{name} — {T.money_compact(row['cur'])}"

    return st.selectbox(t("cl_pick"), names, index=default,
                        format_func=label, key="cl_pick")


def _rank_of(options: pd.DataFrame, client: str) -> tuple[int, int, float]:
    ordered = options[options["cur"] > 0]
    names = ordered.index.tolist()
    rank = names.index(client) + 1 if client in names else len(names)
    total = float(options["cur"].sum())
    share = float(options.loc[client, "cur"]) / total if total else np.nan
    return rank, len(names), share


def render(ctx) -> None:
    st.markdown(f"### {t('cl_title')}")

    options = _client_options(ctx)
    if options.empty:
        st.info(t("no_data"))
        return

    client = _pick_client(ctx, options)
    if client is None:
        st.info(t("no_data"))
        return

    full = ctx.unfiltered()
    data = full[full[LEVEL] == client]
    cur_block = data[data["year"] == ctx.current_year]
    base_block = data[data["year"] == ctx.base_year]
    if cur_block.empty and base_block.empty:
        st.info(t("cl_no_activity", client=client))
        return

    cur = MX.totals(cur_block)
    base = MX.totals(base_block)
    rank, n_clients, share = _rank_of(options, client)

    accounts = sorted(data.loc[~data["is_group_row"], "customer"].dropna().unique())
    ui.note(t("cl_note", rank=rank, total=n_clients, share=T.pct(share, 1),
              accounts=len(accounts), names=" · ".join(accounts) or "—"))

    # --- KPI row ------------------------------------------------------------
    cards = ui.metric_cards(cur, base, ctx.active_metrics,
                            t("vs_base_year", year=ctx.base_year), budget=cur)
    ui.kpi_row(cards[:5])
    if len(cards) > 5:
        ui.kpi_row(cards[5:])

    st.divider()

    # --- budget, backlog, landing -------------------------------------------
    budget = float(cur.get("sales_bdg") or 0)
    invoiced = float(cur.get("sales") or 0)
    open_sales = float(cur.get("sales_open") or 0)

    left, right = st.columns(2)
    with left:
        if budget > 0:
            st.plotly_chart(
                charts.progress_bar(invoiced, budget, title=t("ov_sales_bar")),
                width="stretch", key="cl_budget_bar",
            )
            gap = budget - invoiced
            cover = open_sales / gap if gap > 0 else np.nan
            ui.note(t("cl_budget_note", gap=T.money_compact(max(gap, 0)),
                      open=T.money_compact(open_sales), cover=T.pct(cover, 0)))
        else:
            st.markdown(ui.kpi_card(t("budget"), "—", [(t("cl_no_budget"), None, True)]),
                        unsafe_allow_html=True)

    with right:
        landing = None
        if ctx.has_both:
            try:
                fc = landing_forecast(ctx.ytd.tidy, ctx.fy.tidy, ctx.current_year,
                                      ctx.current_year - 1, LEVEL)
                if client in fc.index:
                    landing = fc.loc[client]
            except Exception:
                landing = None
        if landing is not None and not np.isnan(landing.get("landing", np.nan)):
            st.plotly_chart(
                charts.bullet(float(landing["landing"]), float(landing["budget"]),
                              float(landing["prior_fy"]), t("landing")),
                width="stretch", key="cl_bullet",
            )
            ui.note(t("cl_landing_note",
                      landing=T.money_compact(landing["landing"]),
                      source=t("cl_own_index") if landing["index_source"] == "propio"
                      else t("cl_portfolio_index"),
                      index=T.pct(landing["index_used"], 0),
                      gap=T.signed(landing["gap_vs_budget"])))
        elif open_sales > 0:
            st.markdown(ui.kpi_card(
                t("open_orders"), T.money_compact(open_sales),
                [(t("bl_margin_sub",
                    pct=T.pct(float(cur.get("profit_open") or 0) / open_sales
                              if open_sales else np.nan, 0)), None, True)]),
                unsafe_allow_html=True)

    # --- multi-year history -------------------------------------------------
    if ctx.fy is not None:
        hist = multi_year_trend(
            ctx.fy.tidy[ctx.fy.tidy[LEVEL] == client], ctx.fy.substantive_years)
        if not hist.empty and hist["sales"].abs().sum() > 0:
            st.plotly_chart(
                charts.dual_axis_trend(hist, "year", "sales", "margin_pct",
                                       t("cl_history")),
                width="stretch", key="cl_history",
            )

    st.divider()

    # --- why it moved -------------------------------------------------------
    delta = float(cur.get("sales") or 0) - float(base.get("sales") or 0)
    st.markdown(f"#### {t('cl_why', delta=T.signed(delta))}")

    sb = bridges.sales_bridge(data, ctx.current_year, ctx.base_year,
                              ["customer", "item_code"])
    mb = bridges.margin_bridge(data, ctx.current_year, ctx.base_year,
                               ["customer", "item_code"])
    c1, c2 = st.columns(2)
    with c1:
        st.plotly_chart(charts.waterfall(sb, t("ov_sales_bridge",
                                              base=ctx.base_year, cur=ctx.current_year)),
                        width="stretch", key="cl_sales_bridge")
    with c2:
        st.plotly_chart(charts.waterfall(mb, t("ov_margin_bridge",
                                              base=ctx.base_year, cur=ctx.current_year)),
                        width="stretch", key="cl_margin_bridge")

    price_e = sb["steps"].get("price", 0.0)
    vol_e = sb["steps"].get("volume", 0.0)
    ui.note(t("cl_bridge_note", volume=T.signed(vol_e), price=T.signed(price_e),
              cause=t("cause_price") if abs(price_e) > abs(vol_e) else t("type_volume").lower()))

    # --- what it buys -------------------------------------------------------
    st.markdown(f"#### {t('cl_products')}")
    prod = MX.compare(data, "product_family", ctx.current_year, ctx.base_year,
                      include_open=ctx.include_open)
    prod = MX.apply_materiality(prod, ctx.materiality)

    p1, p2 = st.columns(2)
    with p1:
        st.plotly_chart(
            charts.diverging_bars(prod, "product_family", "sales_delta",
                                  t("dim_top_var"), top_n=ctx.top_n),
            width="stretch", key="cl_prod_bars",
        )
    with p2:
        plot = prod.copy()
        plot["margin_delta_pp"] = plot.get("margin_pct_delta_pp", 0)
        st.plotly_chart(
            charts.treemap(plot, ["product_family"], "sales_cur", "margin_delta_pp",
                           t("dim_treemap")),
            width="stretch", key="cl_treemap",
        )

    item = MX.compare(data, "item_code", ctx.current_year, ctx.base_year,
                      include_open=ctx.include_open)
    item = MX.apply_materiality(item, ctx.materiality)
    cols = {"item_code": t("level_item_code"),
            "sales_cur": f'{t("sales")} {ctx.current_year}',
            "sales_base": f'{t("sales")} {ctx.base_year}',
            "sales_delta": f'Δ {t("sales")}',
            "quantity_cur": f'{t("volume")} {ctx.current_year}',
            "price_cur": f'{t("price")} {ctx.current_year}',
            "price_base": f'{t("price")} {ctx.base_year}',
            "margin_pct_cur": t("margin"),
            "sales_open_cur": t("open_orders"),
            "status": t("status")}
    present = [c for c in cols if c in item.columns]
    table = item[present].sort_values("sales_cur", ascending=False).rename(
        columns={k: cols[k] for k in present})
    st.dataframe(
        ui.style_table(
            table,
            money_cols=[cols[c] for c in present
                        if c.startswith("sales") and "pct" not in c]
            + [cols[c] for c in present if c.startswith("price")],
            pct_cols=[cols[c] for c in present if c == "margin_pct_cur"],
            qty_cols=[cols[c] for c in present if c.startswith("quantity")],
            highlight=[cols["sales_delta"]] if "sales_delta" in present else [],
        ),
        width="stretch", height=420,
    )
    ui.download_button(t("download_table"),
                       {"Client": table, "Families": prod},
                       f"cliente_{ctx.current_year}.xlsx", key="dl_client")

    # --- alerts -------------------------------------------------------------
    alerts = _alerts(ctx, item, prod, cur, base, landing, open_sales)
    if alerts:
        st.markdown(f"#### {t('cl_alerts')}")
        for a in alerts:
            st.markdown(f"- {ui.md_escape(a)}")


def _alerts(ctx, item: pd.DataFrame, prod: pd.DataFrame, cur, base,
            landing, open_sales: float) -> list[str]:
    out: list[str] = []
    M = T.money_compact

    lost = item[item["status"] == "perdido"] if "status" in item else pd.DataFrame()
    if not lost.empty:
        out.append(t("cl_alert_lost", n=len(lost), total=M(lost["sales_base"].sum()),
                     names=", ".join(str(x) for x in lost["item_code"].head(4))))

    new = item[item["status"] == "nuevo"] if "status" in item else pd.DataFrame()
    if not new.empty:
        out.append(t("cl_alert_new", n=len(new), total=M(new["sales_cur"].sum())))

    mc = float(cur.get("margin_pct") or np.nan)
    mb = float(base.get("margin_pct") or np.nan)
    if not np.isnan(mc) and not np.isnan(mb) and abs(mc - mb) > 0.02:
        out.append(t("cl_alert_margin", cur=T.pct(mc), base=T.pct(mb),
                     pp=f"{(mc - mb) * 100:+.1f} pp"))

    if "price_delta_pct" in item.columns:
        drops = item[(item["price_delta_pct"] < -0.05) & (item["sales_cur"] > 0)]
        if not drops.empty:
            worst = drops.sort_values("price_delta_pct").iloc[0]
            out.append(t("cl_alert_price", name=worst["item_code"],
                         pct=T.pct(worst["price_delta_pct"]),
                         sales=M(worst["sales_cur"])))

    if open_sales > 0:
        out.append(t("cl_alert_backlog", total=M(open_sales)))

    if landing is not None and not np.isnan(landing.get("gap_vs_budget", np.nan)):
        if landing["gap_vs_budget"] < 0:
            out.append(t("cl_alert_gap", total=M(abs(landing["gap_vs_budget"]))))
    return out
'''

_MODULES["views.backlog"] = r'''"""Tab 2 — Open orders: business already booked but not yet invoiced.

The point of this tab is the *impact* of the backlog, not its size: how much of
the budget gap it closes, which accounts it belongs to, and where it flips a
negative year-on-year variance into a positive one once it ships.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
import streamlit as st

from core import charts, metrics as MX, theme as T, ui
from core.i18n import t


def _has_backlog(ctx) -> bool:
    block = ctx.slice_year(ctx.current_year)
    return "sales_open" in block and float(block["sales_open"].fillna(0).abs().sum()) > 0


def render(ctx) -> None:
    st.markdown(f"### {t('bl_title')}")
    ui.note(t("bl_note"))

    if not _has_backlog(ctx):
        st.info(t("bl_none"))
        return

    level = ctx.group_level
    cur = MX.totals(ctx.slice_year(ctx.current_year))
    invoiced = float(cur.get("sales") or 0)
    open_sales = float(cur.get("sales_open") or 0)
    open_profit = float(cur.get("profit_open") or 0)
    budget = float(cur.get("sales_bdg") or 0)
    sold_open = invoiced + open_sales
    gap = budget - invoiced
    coverage = open_sales / gap if gap > 0 else np.nan
    remaining = max(budget - sold_open, 0.0)

    # --- headline -----------------------------------------------------------
    grouped = MX.aggregate(ctx.slice_year(ctx.current_year), level)
    with_backlog = int((grouped["sales_open"].fillna(0) > 0).sum())

    k1, k2, k3, k4 = st.columns(4)
    k1.markdown(ui.kpi_card(
        t("bl_total"), T.money_compact(open_sales),
        [(t("bl_groups", n=with_backlog, total=len(grouped)), None, True)]),
        unsafe_allow_html=True)
    k2.markdown(ui.kpi_card(
        t("bl_share"), T.pct(open_sales / invoiced if invoiced else np.nan, 0),
        [(t("sold_open") + f": {T.money_compact(sold_open)}", None, True)]),
        unsafe_allow_html=True)
    k3.markdown(ui.kpi_card(
        t("bl_coverage"), T.pct(coverage, 0),
        [(t("bl_coverage_sub", gap=T.money_compact(max(gap, 0))),
          coverage if coverage == coverage else None, True)]),
        unsafe_allow_html=True)
    k4.markdown(ui.kpi_card(
        t("bl_profit"), T.money_compact(open_profit),
        [(t("bl_margin_sub",
            pct=T.pct(open_profit / open_sales if open_sales else np.nan, 0)),
          None, True)]),
        unsafe_allow_html=True)

    # --- invoiced -> backlog -> budget bridge --------------------------------
    bridge = {
        "start": invoiced,
        "end": budget if budget > 0 else sold_open,
        "steps": {"open": open_sales},
        "labels": {"open": t("open_orders")},
    }
    if budget > 0:
        bridge["steps"]["left"] = remaining
        bridge["labels"]["left"] = t("missing")
    st.plotly_chart(charts.waterfall(bridge, t("bl_bridge")), width="stretch", key="backlog_1")
    if budget > 0:
        ui.note(t(
            "bl_bridge_note",
            inv=T.money_compact(invoiced), open=T.money_compact(open_sales),
            so=T.money_compact(sold_open), bdg=T.money_compact(budget),
            cov=T.pct(coverage, 0), left=T.money_compact(remaining),
        ))

    st.divider()

    # --- where the backlog sits ---------------------------------------------
    label = ctx.label_for(level)
    left, right = st.columns(2)
    with left:
        st.plotly_chart(
            charts.diverging_bars(grouped, level, "sales_open",
                                  t("bl_rank", level=label.lower()), top_n=ctx.top_n),
            width="stretch", key="backlog_2")
    with right:
        prog = grouped.copy()
        prog["target"] = prog["sales"].fillna(0) + prog["sales_open"].fillna(0)
        st.plotly_chart(
            charts.stacked_progress(prog, level, "sales", "target",
                                    t("bl_stack", level=label.lower()),
                                    top_n=ctx.top_n),
            width="stretch", key="backlog_3")

    # --- what the backlog changes about the year -----------------------------
    without = MX.compare(ctx.tidy, level, ctx.current_year, ctx.base_year,
                         include_open=False)
    withb = MX.compare(ctx.tidy, level, ctx.current_year, ctx.base_year,
                       include_open=True)
    merged = without[[level, "sales_delta"]].merge(
        withb[[level, "sales_delta"]], on=level, how="outer",
        suffixes=("_wo", "_w")).fillna(0.0)
    merged["effect"] = merged["sales_delta_w"] - merged["sales_delta_wo"]
    flipped = merged[(merged["sales_delta_wo"] < 0) & (merged["sales_delta_w"] >= 0)]

    st.plotly_chart(
        charts.diverging_bars(merged[merged["effect"] != 0], level, "effect",
                              t("bl_effect", base=ctx.base_year), top_n=ctx.top_n),
        width="stretch", key="backlog_4")
    ui.note(t(
        "bl_effect_note",
        without=T.signed(float(merged["sales_delta_wo"].sum())),
        with_=T.signed(float(merged["sales_delta_w"].sum())),
        n=len(flipped), level=label.lower(),
    ))

    # --- detail table --------------------------------------------------------
    st.markdown(f"#### {t('bl_table')}")
    table = grouped[[level, "sales", "sales_open", "profit_open"]].copy()
    table["sold_open"] = table["sales"].fillna(0) + table["sales_open"].fillna(0)
    table["share"] = np.where(table["sales"] > 0,
                              table["sales_open"] / table["sales"], np.nan)
    if ctx.budget_supported(level) and "sales_bdg" in grouped.columns:
        table["bdg"] = grouped["sales_bdg"]
        table["cover"] = np.where(grouped["sales_bdg"].fillna(0) > 0,
                                  table["sold_open"] / grouped["sales_bdg"], np.nan)
    table = table[table["sales_open"].fillna(0) != 0].sort_values(
        "sales_open", ascending=False)

    names = {level: label, "sales": t("invoiced"), "sales_open": t("bl_col_open"),
             "profit_open": t("bl_profit"), "sold_open": t("bl_col_so"),
             "share": t("bl_col_share"), "bdg": t("budget"),
             "cover": t("bl_col_cover")}
    table = table.rename(columns=names)
    money = [names[c] for c in ("sales", "sales_open", "profit_open", "sold_open", "bdg")
             if names[c] in table.columns]
    pcts = [names[c] for c in ("share", "cover") if names[c] in table.columns]

    st.dataframe(
        ui.style_table(table, money_cols=money, pct_cols=pcts,
                       highlight=[names["sales_open"]]),
        width="stretch", height=420,
    )
    ui.download_button(t("download_table"), {"Backlog": table},
                       f"cartera_{ctx.current_year}.xlsx", key="dl_backlog")
'''

_MODULES["views.fullyear"] = r'''"""Tab 2 — YTD vs Full Year: seasonality, landing forecast, multi-year trend.

This is the tab that needs both files, and the one where the basis mismatch
between them has to be stated out loud rather than buried.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
import streamlit as st

from core import charts, theme as T, ui
from core.i18n import t
from core.forecast import (
    cross_file_diagnosis,
    landing_forecast,
    multi_year_trend,
    portfolio_pace,
    seasonality_index,
)


def render(ctx) -> None:
    if ctx.fy is None:
        st.info(t("needs_fy"))
        return

    fy_years = ctx.fy.substantive_years
    st.markdown(f"### {t('fy_trend')}")
    ui.note(t("fy_trend_note", y0=fy_years[0], y1=fy_years[-1],
              hidden=", ".join(str(y) for y in ctx.fy.partial_years) or "—"))

    trend = multi_year_trend(ctx.fy.tidy, fy_years)
    left, right = st.columns(2)
    with left:
        st.plotly_chart(charts.trend_lines(trend, "year", "sales", t("fy_sales_year")),
                        width="stretch", key="fullyear_1")
    with right:
        st.plotly_chart(charts.dual_axis_trend(trend, "year", "sales", "margin_pct",
                                               t("fy_sales_margin")),
                        width="stretch", key="fullyear_2")

    if len(trend) >= 2:
        first, last = trend.iloc[0], trend.iloc[-1]
        years_span = int(last["year"]) - int(first["year"])
        cagr = ((last["sales"] / first["sales"]) ** (1 / years_span) - 1) \
            if years_span > 0 and first["sales"] > 0 else np.nan
        ui.note(t("fy_cagr", y0=int(first["year"]), y1=int(last["year"]),
                  cagr=T.pct(cagr), m0=T.pct(first["margin_pct"]),
                  m1=T.pct(last["margin_pct"]),
                  pp=f"{(last['margin_pct']-first['margin_pct'])*100:+.1f} pp"))

    if ctx.ytd is None:
        st.warning(t("fy_need_ytd"))
        return

    st.divider()
    prior = ctx.current_year - 1

    # --- basis guard --------------------------------------------------------
    diag = cross_file_diagnosis(ctx.ytd.tidy, ctx.fy.tidy, prior, "enterprise")
    n_bad = int((diag["verdict"] == "base inconsistente").sum())
    n_match = int((diag["verdict"] == "coincide").sum())
    idx = seasonality_index(ctx.ytd.tidy, ctx.fy.tidy, prior, "enterprise")
    n_ok = int(idx["projectable"].sum())

    if n_bad:
        st.warning(t("fy_basis_warn", year=prior, bad=n_bad, ok=n_ok,
                     total=len(idx), match=n_match), icon="⚠️")

    pace = portfolio_pace(ctx.ytd.tidy, ctx.fy.tidy, ctx.current_year, prior)

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(ui.kpi_card(
            t("fy_share_done", year=prior),
            T.pct(pace["current_ytd"] / pace["prior_fy"]) if pace["prior_fy"] else "—",
            [(t("fy_share_sub", pace=T.pct(pace["expected_share"], 0)),
              None, True)]), unsafe_allow_html=True)
    with c2:
        st.markdown(ui.kpi_card(
            t("fy_attain"), T.pct(pace["budget_attainment"], 0),
            [(t("fy_pace_sub", pace=T.pct(pace["expected_share"], 0)),
              pace["pace_gap"], True)]),
            unsafe_allow_html=True)
    with c3:
        st.markdown(ui.kpi_card(
            t("landing"), T.money_compact(pace["landing"]),
            [(t("fy_landing_sub", delta=T.signed(pace["landing"] - pace["budget"])),
              pace["landing"] - pace["budget"], True)]), unsafe_allow_html=True)
    with c4:
        st.markdown(ui.kpi_card(
            t("fy_projectable"), f"{pace['n_projectable']} / {pace['n_total']}",
            [(t("fy_inconsistent", n=pace["n_inconsistent"]),
              -pace["n_inconsistent"], True)]), unsafe_allow_html=True)

    st.plotly_chart(
        charts.bullet(pace["landing"], pace["budget"], pace["prior_fy"],
                      t("fy_bullet", cur=ctx.current_year, prior=prior)),
        width="stretch", key="fullyear_3")

    st.divider()
    level = ctx.group_level if ctx.budget_supported() else "enterprise"
    if level != ctx.group_level:
        ui.note(t("fy_level_note"))
    fc = landing_forecast(ctx.ytd.tidy, ctx.fy.tidy, ctx.current_year, prior, level)
    fc = fc[(fc["ytd_current"] > 0) | (fc["budget"] > 0) | (fc["prior_fy"] > 0)]
    if ctx.materiality > 0:
        fc = fc[(fc["ytd_current"].abs() >= ctx.materiality)
                | (fc["prior_fy"].abs() >= ctx.materiality)]

    st.markdown(f"### {t('fy_landing_by', level=ctx.label_for(level).lower())}")

    prog = fc.reset_index().rename(columns={fc.index.name or "index": level})
    prog["target"] = prog[["budget", "prior_fy"]].max(axis=1)
    st.plotly_chart(
        charts.stacked_progress(prog, level, "ytd_current", "target",
                                t("fy_progress", prior=prior),
                                top_n=ctx.top_n),
        width="stretch", key="fullyear_4")

    risk = prog[prog["gap_vs_budget"] < 0].sort_values("gap_vs_budget")
    st.plotly_chart(
        charts.diverging_bars(prog, level, "gap_vs_budget",
                              t("fy_gap_chart"), top_n=ctx.top_n),
        width="stretch", key="fullyear_5")
    if not risk.empty:
        ui.note(t("fy_gap_note", n=len(risk), level=ctx.label_for(level).lower(),
                  total=T.money_compact(abs(risk["gap_vs_budget"].sum()))))

    table = prog[[level, "ytd_current", "prior_ytd", "prior_fy", "index_used",
                  "index_source", "landing", "budget", "gap_vs_budget",
                  "gap_vs_prior_fy", "reliability"]].copy()
    table = table.sort_values("gap_vs_budget")
    table.columns = [ctx.label_for(level), f"YTD {ctx.current_year}", f"YTD {prior}",
                     f"FY {prior}", "Índice", "Origen", t("landing"),
                     t("budget"), f'{t("budget")} Δ', f"FY {prior} Δ", "Confiab."]
    st.dataframe(
        ui.style_table(
            table,
            money_cols=[f"YTD {ctx.current_year}", f"YTD {prior}", f"FY {prior}",
                        t("landing"), t("budget"), f'{t("budget")} Δ', f"FY {prior} Δ"],
            pct_cols=["Índice"], highlight=[f'{t("budget")} Δ'],
        ),
        width="stretch", height=460,
    )
    ui.download_button(t("download_table"), {"Landing": table},
                       f"aterrizaje_{ctx.current_year}.xlsx", key="dl_landing")

    with st.expander(t("fy_diag_title")):
        d = diag.reset_index()
        d.columns = [ctx.label_for("enterprise"), f"YTD · {prior}", f"FY · {prior}",
                     "Δ", "Δ %", "—"]
        st.dataframe(
            ui.style_table(d, money_cols=[f"YTD · {prior}", f"FY · {prior}", "Δ"],
                           pct_cols=["Δ %"], highlight=["Δ"]),
            width="stretch", height=360,
        )
        st.caption(t("fy_diag_caption"))
'''

_MODULES["views.dimension"] = r'''"""Tabs 3 & 4 — Customer and Product analysis. One engine, two entry points."""

from __future__ import annotations

import numpy as np
import pandas as pd
import streamlit as st

from core import bridges, charts, metrics as MX, theme as T, ui
from core.i18n import t

def _column_labels() -> dict[str, str]:
    """Built per render so a language switch re-labels every column."""
    cur, base = t("col_current"), t("col_base")
    return {
        "sales_cur": f'{t("sales")} {cur}', "sales_base": f'{t("sales")} {base}',
        "sales_delta": f'Δ {t("sales")}', "sales_delta_pct": f'Δ {t("sales")} %',
        "profit_cur": f'{t("profit")} {cur}', "profit_base": f'{t("profit")} {base}',
        "profit_delta": f'Δ {t("profit")}',
        "margin_pct_cur": f'{t("margin")} {cur}', "margin_pct_base": f'{t("margin")} {base}',
        "margin_pct_delta_pp": f'Δ {t("margin")} pp',
        "quantity_cur": f'{t("volume")} {cur}', "quantity_base": f'{t("volume")} {base}',
        "quantity_delta": f'Δ {t("volume")}', "quantity_delta_pct": f'Δ {t("volume")} %',
        "price_cur": f'{t("price")} {cur}', "price_base": f'{t("price")} {base}',
        "price_delta_pct": f'Δ {t("price")} %',
        "unit_cost_cur": f'Costo {cur}', "unit_cost_base": f'Costo {base}',
        "lines_cur": "Líneas", "sales_open_cur": t("open_orders"),
        "sales_bdg_cur": t("budget"), "sales_vs_bdg": f'Δ {t("budget")}',
        "sales_bdg_attain": f'% {t("budget")}', "status": t("status"),
    }

_METRIC_COLUMNS = {
    "sales": ["sales_cur", "sales_base", "sales_delta", "sales_delta_pct"],
    "profit": ["profit_cur", "profit_base", "profit_delta"],
    "margin_pct": ["margin_pct_cur", "margin_pct_base", "margin_pct_delta_pp"],
    "quantity": ["quantity_cur", "quantity_base", "quantity_delta", "quantity_delta_pct"],
    "price": ["price_cur", "price_base", "price_delta_pct"],
    "unit_cost": ["unit_cost_cur", "unit_cost_base"],
    "lines": ["lines_cur"],
    "sales_open": ["sales_open_cur"],
}


def _visible_columns(ctx, df: pd.DataFrame) -> list[str]:
    cols = []
    for metric in ctx.active_metrics:
        cols += [c for c in _METRIC_COLUMNS.get(metric, []) if c in df.columns]
    for extra in ("sales_bdg_cur", "sales_vs_bdg", "sales_bdg_attain", "status"):
        if extra in df.columns and df[extra].notna().any():
            cols.append(extra)
    return cols


def _render_table(ctx, df: pd.DataFrame, level: str, key: str) -> None:
    labels = _column_labels()
    cols = _visible_columns(ctx, df)
    if not cols:
        st.info(t("no_metrics"))
        return
    # Sort on the underlying frame so the order survives even when the sales
    # metric itself is switched off.
    order_col = "sales_cur" if "sales_cur" in df.columns else cols[0]
    table = df.sort_values(order_col, ascending=False)[[level] + cols].copy()
    table.columns = [ctx.label_for(level)] + [labels.get(c, c) for c in cols]

    money = [labels[c] for c in cols
             if c.startswith(("sales", "profit")) and "pct" not in c and "attain" not in c]
    pcts = [labels[c] for c in cols if "pct" in c and not c.endswith("_pp")] + \
           [labels[c] for c in cols if c.endswith("attain")]
    pps = [labels[c] for c in cols if c.endswith("_pp")]
    qtys = [labels[c] for c in cols if c.startswith(("quantity", "lines"))]
    units = [labels[c] for c in cols if c.startswith(("price", "unit_cost"))]

    styler = ui.style_table(table, money_cols=money + units, pct_cols=pcts,
                            pp_cols=pps, qty_cols=qtys,
                            highlight=[c for c in (labels["sales_delta"],
                                                   labels["margin_pct_delta_pp"])
                                       if c in table.columns])
    st.dataframe(styler, width="stretch", height=440)
    ui.download_button(t("download_table"), {"Detail": table},
                       f"{level}_{ctx.current_year}.xlsx", key=f"dl_{key}")


def render(ctx, mode: str = "customer") -> None:
    level = ctx.group_level
    if mode == "customer" and level not in ("customer", "enterprise"):
        level = "customer"
    if mode == "product" and level not in ("product", "product_family", "item_code"):
        level = "product_family"

    df = ctx.compare(level)
    if df.empty:
        st.info(t("no_data"))
        return

    label = ctx.label_for(level)
    st.markdown(f"### {t('dim_title', level=label, cur=ctx.current_year, base=ctx.base_year)}")
    ui.note(t("dim_note", n=f"{len(df):,}",
              new=int((df["status"] == "nuevo").sum()),
              lost=int((df["status"] == "perdido").sum()),
              mat=T.money_compact(ctx.materiality) if ctx.materiality
              else t("no_threshold")))

    top = st.columns(2)
    with top[0]:
        st.plotly_chart(
            charts.diverging_bars(df, level, "sales_delta",
                                  t("dim_top_var"), top_n=ctx.top_n),
            width="stretch", key=f"dimension_{mode}_1")
    with top[1]:
        contrib = bridges.contribution_by_group(ctx.tidy, ctx.current_year,
                                                ctx.base_year, level, top_n=8)
        fake_bridge = {
            "start": float(df["sales_base"].sum()),
            "end": float(df["sales_cur"].sum()),
            "steps": {str(r[level]): float(r["delta"]) for _, r in contrib.iterrows()
                      if abs(r["delta"]) > 0},
            "labels": {},
        }
        st.plotly_chart(
            charts.waterfall(fake_bridge, t("dim_contrib", level=label.lower()),
                             horizontal=True),
            width="stretch", key=f"dimension_{mode}_2")

    st.plotly_chart(
        charts.quadrant(df, "sales_delta_pct", "margin_pct_cur", "sales_cur", level,
                        t("dim_quadrant", level=label.lower()),
                        x_ref=0.0, top_n=max(ctx.top_n * 2, 30)),
        width="stretch", key=f"dimension_{mode}_3")
    ui.note(t("dim_quadrant_note"))

    if mode == "product":
        fam = ctx.compare("product_family")
        fam_plot = fam.copy()
        fam_plot["margin_delta_pp"] = fam_plot.get("margin_pct_delta_pp", 0)
        st.plotly_chart(
            charts.treemap(fam_plot, ["product_family"], "sales_cur", "margin_delta_pp",
                           t("dim_treemap")),
            width="stretch", key=f"dimension_{mode}_4")
        st.plotly_chart(
            charts.scatter_price_volume(df.rename(columns={level: "label"}).assign(
                **{level: df[level]})[[level] + [c for c in df.columns if c != level]],
                t("dim_scatter")),
            width="stretch", key=f"dimension_{mode}_5")
        mb = bridges.margin_bridge(ctx.tidy, ctx.current_year, ctx.base_year,
                                   ["product_family", "item_code"])
        st.plotly_chart(
            charts.waterfall(mb, t("dim_prod_bridge")),
            width="stretch", key=f"dimension_{mode}_6")

    lost = df[df["status"] == "perdido"].sort_values("sales_base", ascending=False)
    if not lost.empty:
        with st.expander(t("dim_churn", n=len(lost), level=label.lower(),
                           year=ctx.current_year,
                           amount=T.money_compact(lost["sales_base"].sum()))):
            churn = lost[[level, "sales_base", "profit_base"]].copy()
            churn.columns = [label, f'{t("sales")} {ctx.base_year}',
                             f'{t("profit")} {ctx.base_year}']
            st.dataframe(
                ui.style_table(churn, money_cols=list(churn.columns[1:]), pct_cols=[]),
                width="stretch",
            )

    if ctx.second_level:
        with st.expander(t("dim_cross", a=label, b=ctx.label_for(ctx.second_level))):
            cross = MX.compare(ctx.tidy, [level, ctx.second_level],
                               ctx.current_year, ctx.base_year, ctx.include_open)
            cross = MX.apply_materiality(cross, ctx.materiality)
            pivot = cross.pivot_table(index=level, columns=ctx.second_level,
                                      values="sales_delta_pct", aggfunc="mean")
            pivot = pivot.loc[pivot.abs().sum(axis=1).sort_values(ascending=False)
                              .head(ctx.top_n).index]
            st.plotly_chart(
                charts.heatmap(pivot, t("dim_cross_chart")),
                width="stretch", key=f"dimension_{mode}_7")

    st.markdown(f"#### {t('dim_detail')}")
    _render_table(ctx, df, level, key=mode)
'''

_MODULES["views.deviations"] = r'''"""Tab 5 — Deviation radar: everything off track, ranked by USD, not by percent."""

from __future__ import annotations

import numpy as np
import pandas as pd
import streamlit as st

from core import charts, metrics as MX, theme as T, ui
from core.i18n import t


def _classify(row: pd.Series) -> str:
    if row["status"] == "perdido":
        return t("type_churn")
    if row["status"] == "nuevo":
        return t("type_new")
    q0, q1 = row.get("quantity_base", 0), row.get("quantity_cur", 0)
    p0, p1 = row.get("price_base", np.nan), row.get("price_cur", np.nan)
    c0, c1 = row.get("unit_cost_base", np.nan), row.get("unit_cost_cur", np.nan)
    vol_effect = (q1 - q0) * (p0 if p0 == p0 else 0)
    price_effect = ((p1 - p0) * q1) if (p0 == p0 and p1 == p1) else 0.0
    cost_effect = (-(c1 - c0) * q1) if (c0 == c0 and c1 == c1) else 0.0
    ranked = {t("type_volume"): abs(vol_effect), t("type_price"): abs(price_effect),
              t("type_cost"): abs(cost_effect)}
    return max(ranked, key=ranked.get)


def build_deviation_table(ctx, level: str) -> pd.DataFrame:
    df = ctx.compare(level).copy()
    if df.empty:
        return df
    df["tipo"] = df.apply(_classify, axis=1)
    df["impacto_ventas"] = df["sales_delta"]
    df["impacto_profit"] = df.get("profit_delta", 0)
    if "sales_vs_bdg" in df.columns:
        df["impacto_budget"] = df["sales_vs_bdg"]
    else:
        df["impacto_budget"] = np.nan
    df["impacto_abs"] = df["impacto_ventas"].abs()
    return df.sort_values("impacto_abs", ascending=False)


def render(ctx) -> None:
    level = ctx.group_level
    df = build_deviation_table(ctx, level)
    if df.empty:
        st.info(t("no_data"))
        return

    st.markdown(f"### {t('dev_title')}")
    ui.note(t("dev_note"))

    c1, c2, c3 = st.columns([2, 1, 1])
    tipos = sorted(df["tipo"].unique().tolist())
    sel = c1.multiselect(t("dev_type"), tipos, default=tipos, key="dev_tipo")
    dir_opts = {"all": t("dev_all"), "neg": t("dev_negative"), "pos": t("dev_positive")}
    direction = c2.selectbox(t("dev_direction"), list(dir_opts),
                             format_func=dir_opts.get, key="dev_dir")
    against_opts = {"base": t("dev_base_year"), "budget": t("budget")}
    against = c3.selectbox(t("dev_against"), list(against_opts),
                           format_func=against_opts.get, key="dev_against")
    against_label = against_opts[against]

    view = df[df["tipo"].isin(sel)]
    metric_col = "impacto_ventas" if against == "base" else "impacto_budget"
    if metric_col not in view.columns or view[metric_col].isna().all():
        st.warning(t("dev_no_budget"))
        metric_col = "impacto_ventas"
        against_label = t("dev_base_year")
    if direction == "neg":
        view = view[view[metric_col] < 0]
    elif direction == "pos":
        view = view[view[metric_col] > 0]

    if view.empty:
        st.info(t("dev_none"))
        return

    total_neg = view[view[metric_col] < 0][metric_col].sum()
    total_pos = view[view[metric_col] > 0][metric_col].sum()
    k1, k2, k3, k4 = st.columns(4)
    k1.markdown(ui.kpi_card(t("dev_neg_total"), T.money_compact(abs(total_neg)),
                            [(t("dev_records", n=int((view[metric_col] < 0).sum())),
                              None, True)]), unsafe_allow_html=True)
    k2.markdown(ui.kpi_card(t("dev_pos_total"), T.money_compact(total_pos),
                            [(t("dev_records", n=int((view[metric_col] > 0).sum())),
                              None, True)]), unsafe_allow_html=True)
    k3.markdown(ui.kpi_card(t("dev_net"), T.signed(view[metric_col].sum()),
                            [(t("dev_against_sub", what=against_label.lower()),
                              None, True)]), unsafe_allow_html=True)
    top_share = view[metric_col].abs().nlargest(5).sum() / view[metric_col].abs().sum() \
        if view[metric_col].abs().sum() else np.nan
    k4.markdown(ui.kpi_card(t("dev_top5"), T.pct(top_share, 0),
                            [(t("dev_top5_sub"), None, True)]),
                unsafe_allow_html=True)

    st.plotly_chart(
        charts.diverging_bars(view, level, metric_col,
                              t("dev_chart", what=against_label.lower()),
                              top_n=ctx.top_n),
        width="stretch", key="deviations_1")

    by_type = view.groupby("tipo")[metric_col].sum().sort_values()
    bridge = {
        "start": 0.0,
        "end": float(by_type.sum()),
        "steps": {k: float(v) for k, v in by_type.items() if abs(v) > 0},
        "labels": {},
    }
    st.plotly_chart(
        charts.waterfall(bridge, t("dev_compose")),
        width="stretch", key="deviations_2")

    cols = [level, "tipo", "sales_cur", "sales_base", "impacto_ventas",
            "sales_delta_pct", "margin_pct_cur", "margin_pct_delta_pp",
            "quantity_delta_pct", "price_delta_pct", "impacto_budget"]
    cols = [c for c in cols if c in view.columns]
    table = view[cols].copy()
    impact = t("dev_net") + " USD"
    table.columns = [ctx.label_for(level), t("dev_type"),
                     f'{t("sales")} {ctx.current_year}', f'{t("sales")} {ctx.base_year}',
                     impact, f'Δ {t("sales")} %', t("margin"), f'Δ {t("margin")} pp',
                     f'Δ {t("volume")} %', f'Δ {t("price")} %',
                     f'Δ {t("budget")}'][:len(cols)]
    st.dataframe(
        ui.style_table(
            table,
            money_cols=[c for c in table.columns
                        if t("sales") in c or c == impact or c == f'Δ {t("budget")}'],
            pct_cols=[c for c in table.columns
                      if c.endswith("%") or c == t("margin")],
            pp_cols=[c for c in table.columns if "pp" in c],
            highlight=[impact],
        ),
        width="stretch", height=440,
    )
    ui.download_button(t("download_table"), {"Deviations": table},
                       f"desviaciones_{ctx.current_year}.xlsx", key="dl_dev")
'''

_MODULES["views.strategy"] = r'''"""Tab 6 — Strategy bullets and next steps, generated from the filtered numbers."""

from __future__ import annotations

import datetime as dt

import pandas as pd
import streamlit as st

from core import bridges, insights, theme as T, ui
from core.i18n import t
from core.forecast import landing_forecast, portfolio_pace

def _sections():
    return [
        ("diagnostico", t("st_diagnosis"), t("st_diagnosis_c")),
        ("riesgos", t("st_risks"), t("st_risks_c")),
        ("oportunidades", t("st_opps"), t("st_opps_c")),
        ("acciones", t("st_actions"), t("st_actions_c")),
    ]


def _markdown_report(ctx, bullets: dict[str, list[str]]) -> str:
    stamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = [
        "# " + t("st_report_title", cur=ctx.current_year, base=ctx.base_year),
        t("st_report_meta", stamp=stamp,
          level=ctx.label_for(ctx.group_level).lower()),
        "",
    ]
    for key, title, _ in _sections():
        items = bullets.get(key) or []
        if not items:
            continue
        lines.append(f"## {title}")
        lines += [f"- {b}" for b in items]
        lines.append("")
    return "\n".join(lines)


def render(ctx) -> None:
    # Budget only attributes at group level, so the forecast always runs there.
    cust_level = ctx.group_level if ctx.group_level in ("enterprise", "customer") \
        else "enterprise"
    forecast_level = "enterprise"
    prod_level = "product_family"

    cmp_cust = ctx.compare(cust_level)
    cmp_prod = ctx.compare(prod_level)
    if cmp_cust.empty:
        st.info(t("no_data"))
        return

    sb = bridges.sales_bridge(ctx.tidy, ctx.current_year, ctx.base_year)
    mb = bridges.margin_bridge(ctx.tidy, ctx.current_year, ctx.base_year)

    pace = None
    forecast = None
    if ctx.has_both:
        try:
            prior = ctx.current_year - 1
            pace = portfolio_pace(ctx.ytd.tidy, ctx.fy.tidy, ctx.current_year, prior)
            forecast = landing_forecast(ctx.ytd.tidy, ctx.fy.tidy,
                                        ctx.current_year, prior, forecast_level)
        except Exception:
            pace, forecast = None, None

    bullets = insights.build_all(cmp_cust, cmp_prod, sb, mb, pace, forecast, cust_level)

    st.markdown(f"### {t('st_title')}")
    ui.note(t("st_note", cur=ctx.current_year, base=ctx.base_year,
              level=ctx.label_for(cust_level).lower()))

    for key, title, caption in _sections():
        items = bullets.get(key) or []
        if not items:
            continue
        st.markdown(f"#### {title}")
        st.caption(caption)
        for b in items:
            st.markdown(f"- {ui.md_escape(b)}")
        st.write("")

    st.divider()
    report = _markdown_report(ctx, bullets)
    edited = st.text_area(t("st_edit"), report, height=320, key="strat_edit")

    c1, c2 = st.columns(2)
    c1.download_button(
        t("st_dl_md"), data=edited.encode("utf-8"),
        file_name=f"estrategia_{ctx.current_year}.md", mime="text/markdown",
        key="dl_strategy_md",
    )
    flat = pd.DataFrame(
        [{"section": title, "bullet": b}
         for key, title, _ in _sections() for b in (bullets.get(key) or [])]
    )
    with c2:
        ui.download_button(t("st_dl_xlsx"), {"Strategy": flat},
                           f"estrategia_{ctx.current_year}.xlsx", key="dl_strategy_xlsx")
'''

_MODULES["views.dataquality"] = r'''"""Tab 7 — Data & quality: what was parsed, what was pruned, what does not reconcile."""

from __future__ import annotations

import pandas as pd
import streamlit as st

from core import theme as T, ui
from core.forecast import cross_file_diagnosis
from core.i18n import t

NOTES_ES = (
    "- **`Cost` y `Price` del export son valores unitarios, no totales.** El costo "
    "total se deriva como ventas − profit.\n"
    "- **Margen y precio nunca se promedian.** Se recalculan como Σ profit ÷ Σ ventas "
    "y Σ ventas ÷ Σ volumen.\n"
    "- **El budget del archivo YTD es anual**, no prorrateado al período: el avance se "
    "lee contra el año completo y la barra lleva un marcador de ritmo esperado.\n"
    "- **El budget se carga contra un cliente marcador `<GRUPO> []`**, no contra la "
    "cuenta real: se atribuye a nivel Cliente (grupo) y por producto, y queda "
    "desactivado si agrupas por cuenta individual.\n"
    "- **Las columnas de variación, % y forecast se ignoran**: la app las recalcula."
)

NOTES_EN = (
    "- **`Cost` and `Price` in the export are per-unit values, not totals.** Total cost "
    "is derived as sales − profit.\n"
    "- **Margin and price are never averaged.** They are recomputed as Σ profit ÷ Σ sales "
    "and Σ sales ÷ Σ volume.\n"
    "- **The YTD file's budget is annual**, not prorated to the period: attainment reads "
    "against the full year and the bar carries an expected-pace marker.\n"
    "- **Budget is loaded against a placeholder customer `<GROUP> []`**, not the real "
    "account: it is attributed at customer-group and product level, and disabled when "
    "grouping by individual account.\n"
    "- **Variance, % and forecast columns are ignored**: the app recomputes them."
)


def _file_panel(parsed, title: str) -> None:
    if parsed is None:
        st.caption(t("dq_not_loaded", title=title))
        return
    st.markdown(f"**{title}** · `{parsed.filename}`")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric(t("dq_rows"), f"{parsed.n_raw_rows:,}")
    c2.metric(t("dq_leaves"), f"{parsed.n_leaf_rows:,}")
    pruned = parsed.n_raw_rows - parsed.n_leaf_rows
    c3.metric(t("dq_pruned"), f"{pruned:,}",
              delta=f"-{pruned/parsed.n_raw_rows:.0%}" if parsed.n_raw_rows else None)
    c4.metric(t("dq_bands"), f"{len(parsed.years)}")

    totals = parsed.year_totals.copy()
    totals.index.name = "Año"
    show = totals.reset_index()
    show.columns = ["Año", t("sales"), t("profit"), t("volume"), t("budget"),
                    t("open_orders")]
    show[t("margin")] = (show[t("profit")] / show[t("sales")]).where(show[t("sales")] != 0)
    st.dataframe(
        ui.style_table(show,
                       money_cols=[t("sales"), t("profit"), t("budget"), t("open_orders")],
                       pct_cols=[t("margin")], qty_cols=[t("volume")]),
        width="stretch",
    )

    profile = parsed.profile or {}
    with st.expander(t("dq_recognised")):
        a, b = st.columns(2)
        a.markdown(
            f"**{t('dq_sheet')}:** `{profile.get('sheet', '—')}`  \n"
            f"**{t('dq_header_row')}:** {profile.get('header_row', '—')}  \n"
            f"**{t('dq_year_source')}:** {profile.get('year_source', '—')}"
        )
        dims = profile.get("dimensions", {})
        a.markdown(f"**{t('dq_dims')}:**  \n" + ("  \n".join(
            f"`{v}` → {k}" for k, v in dims.items()) or "—"))
        b.markdown(f"**{t('dq_metrics')}:**  \n" +
                   (", ".join(f"`{m}`" for m in profile.get("metrics", [])) or "—"))
        ignored = profile.get("ignored_columns", [])
        if ignored:
            b.markdown(
                f"**{t('dq_ignored', n=profile.get('n_ignored_columns', len(ignored)))}:**  \n"
                + ", ".join(f"`{c}`" for c in ignored[:25])
                + (" …" if profile.get("n_ignored_columns", 0) > 25 else "")
            )

    for w in parsed.warnings:
        st.caption(f"• {w}")
    st.write("")


def render(ctx) -> None:
    st.markdown(f"### {t('dq_title')}")
    ui.note(t("dq_note"))

    _file_panel(ctx.ytd, t("file_ytd"))
    _file_panel(ctx.fy, t("file_fy"))

    st.divider()
    st.markdown(f"#### {t('dq_notes')}")
    st.markdown(NOTES_ES if st.session_state.get("lang", "es") == "es" else NOTES_EN)

    if ctx.ytd is not None and ctx.fy is not None:
        st.divider()
        prior = ctx.current_year - 1
        st.markdown(f"#### {t('dq_recon', year=prior)}")
        diag = cross_file_diagnosis(ctx.ytd.tidy, ctx.fy.tidy, prior, "enterprise")
        counts = diag["verdict"].value_counts()
        c1, c2, c3 = st.columns(3)
        c1.metric(t("dq_match"), int(counts.get("coincide", 0)))
        c2.metric(t("dq_coherent"), int(counts.get("coherente (YTD < FY)", 0)))
        c3.metric(t("dq_inconsistent"), int(counts.get("base inconsistente", 0)))

        total_ytd = float(diag["ytd_file"].sum())
        total_fy = float(diag["fy_file"].sum())
        if total_ytd > total_fy:
            st.error(t("dq_recon_error", year=prior,
                       ytd=T.money_compact(total_ytd), fy=T.money_compact(total_fy)),
                     icon="⚠️")
        d = diag.reset_index()
        d.columns = [ctx.label_for("enterprise"), t("file_ytd"), t("file_fy"),
                     "Δ", "Δ %", "—"]
        st.dataframe(
            ui.style_table(d, money_cols=[t("file_ytd"), t("file_fy"), "Δ"],
                           pct_cols=["Δ %"], highlight=["Δ"]),
            width="stretch", height=420,
        )
        ui.download_button(t("download_table"), {"Reconciliation": d},
                           f"conciliacion_{prior}.xlsx", key="dl_recon")
'''


# --------------------------------------------------------------------------- #
# Loader: build real module objects so every qualified reference keeps working.
# --------------------------------------------------------------------------- #
def _install() -> None:
    for package in ("core", "views"):
        if package not in sys.modules:
            pkg = types.ModuleType(package)
            pkg.__path__ = []          # marks it as a package
            pkg.__file__ = "<bundled>"
            sys.modules[package] = pkg

    for name, source in _MODULES.items():
        module = types.ModuleType(name)
        module.__file__ = "<bundled>"
        module.__package__ = name.rsplit(".", 1)[0]
        sys.modules[name] = module
        exec(compile(source, f"<bundled:{name}>", "exec"), module.__dict__)
        package, _, leaf = name.rpartition(".")
        setattr(sys.modules[package], leaf, module)


_install()

from core import session, theme as T          # noqa: E402
from core.context import build_sidebar        # noqa: E402
from core.i18n import t                       # noqa: E402
from core.parser import parse_export          # noqa: E402
from views import (backlog, customer, dataquality, deviations,   # noqa: E402
                   dimension, fullyear, overview, strategy)


st.set_page_config(
    page_title="Robertet · Sales Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

T.register_template()
session.init()
st.markdown(T.CSS, unsafe_allow_html=True)


# --------------------------------------------------------------------------- #
# Header
# --------------------------------------------------------------------------- #
def header() -> None:
    logo = T.logo_data_uri()
    img = f'<img src="{logo}" alt="Robertet"/>' if logo else ""
    st.markdown(
        f'<div class="rb-header">{img}'
        f'<div><div class="rb-title">{t("app_title")}</div>'
        f'<div class="rb-sub">{t("app_sub")}</div></div></div>',
        unsafe_allow_html=True,
    )
    st.markdown(f'<div class="rb-privacy">{t("privacy_banner")}</div>',
                unsafe_allow_html=True)


# --------------------------------------------------------------------------- #
# Sidebar: session controls + uploads
# --------------------------------------------------------------------------- #
def sidebar_session() -> None:
    st.sidebar.markdown(f"### {t('session')}")
    # The widget writes straight into session_state["lang"], so a language
    # change is picked up by every t() call on the same rerun.
    st.sidebar.radio(
        t("language"), ["es", "en"], horizontal=True, key="lang",
        format_func=lambda v: "Español" if v == "es" else "English",
    )

    st.session_state["idle_minutes"] = st.sidebar.slider(
        t("idle_timeout"), min_value=5, max_value=120,
        value=st.session_state.get("idle_minutes", session.DEFAULT_IDLE_MINUTES), step=5,
    )
    left = session.seconds_left()
    st.sidebar.caption(f"{t('idle_left')} {int(left // 60)} min {int(left % 60):02d} s")

    if not st.session_state.get("confirm_clear"):
        if st.sidebar.button(t("clear_all"), width="stretch", type="secondary"):
            st.session_state["confirm_clear"] = True
            st.rerun()
    else:
        st.sidebar.warning(t("clear_warning"))
        c1, c2 = st.sidebar.columns(2)
        if c1.button(t("clear_confirm"), width="stretch", type="primary"):
            session.clear_all(keep_preferences=True)
            st.session_state["just_cleared"] = True
            st.rerun()
        if c2.button(t("cancel"), width="stretch"):
            st.session_state["confirm_clear"] = False
            st.rerun()

    st.sidebar.divider()


def sidebar_uploads() -> None:
    epoch = st.session_state.get("uploader_epoch", 0)
    st.sidebar.markdown(f"### {t('upload_title')}")

    ytd_file = st.sidebar.file_uploader(
        t("upload_ytd"), type=["xlsx", "xlsm"], key=f"up_ytd_{epoch}",
        help=t("upload_help"),
    )
    fy_file = st.sidebar.file_uploader(
        t("upload_fy"), type=["xlsx", "xlsm"], key=f"up_fy_{epoch}",
        help=t("upload_help"),
    )

    for slot, uploaded in (("ytd", ytd_file), ("fy", fy_file)):
        if uploaded is None:
            continue
        if st.session_state.get(f"{slot}_name") == uploaded.name and \
                st.session_state.get(slot) is not None:
            continue
        try:
            with st.spinner(t("processing", name=uploaded.name)):
                parsed = parse_export(uploaded.getvalue(), uploaded.name)
            session.store(slot, parsed, uploaded.name)
        except Exception as exc:  # noqa: BLE001 - surfaced to the user verbatim
            st.sidebar.error(t("upload_error", name=uploaded.name, error=exc))

    for slot, label in (("ytd", "YTD"), ("fy", "Full Year")):
        parsed = st.session_state.get(slot)
        if parsed is not None:
            years = parsed.substantive_years
            st.sidebar.success(
                t("file_loaded", label=label, rows=f"{parsed.n_leaf_rows:,}",
                  y0=years[0], y1=years[-1]), icon="✅",
            )
    st.sidebar.divider()


# --------------------------------------------------------------------------- #
# Landing screen
# --------------------------------------------------------------------------- #
def welcome() -> None:
    st.markdown(f"#### {t('how_title')}")
    c1, c2, c3 = st.columns(3)
    c1.markdown(t("how_1"))
    c2.markdown(t("how_2"))
    c3.markdown(t("how_3"))
    st.divider()
    st.info(t("privacy_long"), icon="🔒")


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #
def main() -> None:
    header()

    if session.enforce_idle_timeout():
        st.warning(t("auto_wiped"), icon="⏱️")
    if st.session_state.pop("just_cleared", False):
        st.success(t("cleared"), icon="🗑️")

    sidebar_session()
    sidebar_uploads()

    if not session.has_data():
        st.info(t("no_files"), icon="📄")
        welcome()
        return

    session.touch()
    ctx = build_sidebar(st.session_state.get("ytd"), st.session_state.get("fy"))

    tabs = st.tabs([
        f"📊 {t('tab_overview')}",
        f"🏷️ {t('tab_client')}",
        f"📦 {t('tab_backlog')}",
        f"📐 {t('tab_fy')}",
        f"👥 {t('tab_customers')}",
        f"🧪 {t('tab_products')}",
        f"🎯 {t('tab_deviations')}",
        f"💡 {t('tab_strategy')}",
        f"🔧 {t('tab_data')}",
    ])
    with tabs[0]:
        overview.render(ctx)
    with tabs[1]:
        customer.render(ctx)
    with tabs[2]:
        backlog.render(ctx)
    with tabs[3]:
        fullyear.render(ctx)
    with tabs[4]:
        dimension.render(ctx, mode="customer")
    with tabs[5]:
        dimension.render(ctx, mode="product")
    with tabs[6]:
        deviations.render(ctx)
    with tabs[7]:
        strategy.render(ctx)
    with tabs[8]:
        dataquality.render(ctx)


if __name__ == "__main__":
    main()
