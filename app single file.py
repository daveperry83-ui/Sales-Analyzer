"""Robertet LATAM — Sales Analytics · build de un solo archivo.

© 2026 [Titular de derechos]. Todos los derechos reservados. / All rights reserved.
Software propietario — ver LICENSE. Uso licenciado; prohibida su reproducción o
distribución sin autorización escrita. Contacto: katyasam13@gmail.com

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

# © 2026 [Titular de derechos]. Todos los derechos reservados. / All rights reserved.
# Robertet LATAM Sales Analytics — software propietario. Ver LICENSE.
# Uso licenciado; prohibida su reproducción o distribución sin autorización escrita.
# Contacto: katyasam13@gmail.com


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
      padding: 0.9rem 1rem 0.9rem 0.85rem; height: 100%;
      border-left: 4px solid {RULE}; transition: border-color .15s;
  }}
  .rb-acc-up {{ border-left-color: {POSITIVE}; }}
  .rb-acc-down {{ border-left-color: {NEGATIVE}; }}
  .rb-acc-flat {{ border-left-color: {MUTED}; }}
  .rb-card .rb-label {{ color: {MUTED}; font-size: 0.74rem; text-transform: uppercase;
      letter-spacing: 0.06em; margin-bottom: 0.2rem; }}
  .rb-card .rb-value {{ color: {NAVY}; font-size: 1.55rem; font-weight: 650; line-height: 1.1; }}
  .rb-card .rb-delta {{ font-size: 0.8rem; margin-top: 0.35rem; font-variant-numeric: tabular-nums; }}
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

_MODULES["core.i18n_ptfr"] = r'''"""Complete Portuguese and French translations, merged into i18n.STRINGS.

Kept identical across languages on purpose (business terms the user uses as-is):
budget, YTD, Full Year, one-pager, pace, Δ. Product and customer names are DATA,
never translated. This module fills every remaining UI string so no view mixes
languages.
"""

# © 2026 [Titular de derechos]. Todos los derechos reservados. / All rights reserved.
# Robertet LATAM Sales Analytics — software propietario. Ver LICENSE.

TRANSLATIONS = {
    # ---- evolution ----
    "ev_note": {"pt": "Compara o YTD deste mês com o YTD do mês passado. A diferença é o movimento do mês; o arquivo traz também o ano anterior, então cada mês é avaliado contra o mês anterior e contra o mesmo mês do ano passado.",
                "fr": "Compare le YTD de ce mois au YTD du mois dernier. La différence est le mouvement du mois ; le fichier contient aussi l'année précédente, donc chaque mois est jugé face au mois précédent et au même mois l'an dernier."},
    "ev_need_prev": {"pt": "Carregue o arquivo do mês passado em «Mês anterior (YTD)» no painel lateral para habilitar esta vista.",
                     "fr": "Chargez le fichier du mois dernier dans « Mois précédent (YTD) » dans le panneau latéral pour activer cette vue."},
    "ev_how": {"pt": "Como obter o arquivo do mês passado?", "fr": "Comment obtenir le fichier du mois dernier ?"},
    "ev_how_body": {"pt": "A cada fechamento, **salve** o export YTD que você baixa. No mês seguinte, carregue o novo em «Arquivo YTD» e o anterior em «Mês anterior». Com dois fechamentos já funciona. O app não guarda histórico, então o arquivamento depende de você.",
                    "fr": "À chaque clôture, **enregistrez** l'export YTD que vous téléchargez. Le mois suivant, chargez le nouveau dans « Fichier YTD » et le précédent dans « Mois précédent ». Deux clôtures suffisent. L'app ne garde aucun historique, l'archivage dépend donc de vous."},
    "ev_err_year": {"pt": "O arquivo do mês passado não contém o ano {year}. Você carregou o arquivo correto?",
                    "fr": "Le fichier du mois dernier ne contient pas l'année {year}. Avez-vous chargé le bon fichier ?"},
    "ev_err_swapped": {"pt": "O arquivo do «mês passado» ({prev}) tem mais vendas que o de «este mês» ({now}). Parece que foram carregados invertidos: o mais recente vai em «Arquivo YTD».",
                       "fr": "Le fichier « mois dernier » ({prev}) a plus de ventes que celui de « ce mois » ({now}). Ils semblent inversés : le plus récent va dans « Fichier YTD »."},
    "ev_err_same": {"pt": "Os dois arquivos têm o mesmo total: parecem ser o mesmo fechamento. Carregue dois meses distintos.",
                    "fr": "Les deux fichiers ont le même total : ils semblent être la même clôture. Chargez deux mois différents."},
    "ev_vs_year_ago": {"pt": "{v} vs mesmo mês do ano passado", "fr": "{v} vs même mois l'an dernier"},
    "ev_month_profit": {"pt": "profit do mês {v}", "fr": "profit du mois {v}"},
    "ev_landing_move": {"pt": "Aterrissagem projetada", "fr": "Atterrissage projeté"},
    "ev_landing_delta": {"pt": "{v} vs o mês passado", "fr": "{v} vs le mois dernier"},
    "ev_drv_sales": {"pt": "Pontuação de vendas {v}", "fr": "Score de ventes {v}"},
    "ev_drv_margin": {"pt": "Pontuação de margem {v}", "fr": "Score de marge {v}"},
    "ev_movers": {"pt": "Quem acelerou e quem freou (vendas do mês)", "fr": "Qui a accéléré et qui a ralenti (ventes du mois)"},
    "ev_accelerating": {"pt": "Contribuíram este mês", "fr": "Ont contribué ce mois"},
    "ev_slowing": {"pt": "Subtraíram este mês", "fr": "Ont réduit ce mois"},
    "ev_month_year_ago": {"pt": "Mesmo mês ano passado", "fr": "Même mois l'an dernier"},
    "ev_month_this": {"pt": "Este mês", "fr": "Ce mois"},
    "ev_vs_year_chart": {"pt": "Vendas do mês: este ano vs ano passado", "fr": "Ventes du mois : cette année vs l'an dernier"},
    "ev_yoy_note": {"pt": "O mês contribuiu {now} contra {py} do mesmo mês do ano passado ({yoy}).",
                    "fr": "Le mois a contribué {now} contre {py} au même mois l'an dernier ({yoy})."},
    "ev_alerts": {"pt": "Alertas de mudança de tendência", "fr": "Alertes de changement de tendance"},
    "ev_alert_slow": {"pt": "**{name}** contribuiu {now} este mês, contra {py} no mesmo mês do ano passado: está desacelerando.",
                      "fr": "**{name}** a contribué {now} ce mois, contre {py} au même mois l'an dernier : il ralentit."},
    "ev_alert_margin": {"pt": "**{name}** vendeu {sales} este mês, mas sua margem caiu {pp} contra o mesmo mês do ano passado.",
                        "fr": "**{name}** a vendu {sales} ce mois, mais sa marge a chuté de {pp} face au même mois l'an dernier."},
    "ev_alert_stall": {"pt": "**{name}** não faturou este mês; no mesmo mês do ano passado fez {py}.",
                       "fr": "**{name}** n'a pas facturé ce mois ; au même mois l'an dernier il a fait {py}."},
    "ev_detail": {"pt": "Detalhe mensal", "fr": "Détail mensuel"},
    "ev_col_month": {"pt": "Vendas mês", "fr": "Ventes mois"},
    "ev_col_month_py": {"pt": "Mês ano passado", "fr": "Mois l'an dernier"},
    "ev_col_yoy": {"pt": "Δ vs ano passado", "fr": "Δ vs l'an dernier"},
    "ev_col_margin": {"pt": "Margem mês", "fr": "Marge mois"},
    "ev_col_margin_pp": {"pt": "Δ margem pp", "fr": "Δ marge pp"},
    "ev_col_ytd_prev": {"pt": "YTD mês passado", "fr": "YTD mois dernier"},
    "ev_col_ytd_now": {"pt": "YTD agora", "fr": "YTD maintenant"},
    "ev_col_mom": {"pt": "Δ YTD %", "fr": "Δ YTD %"},
    # ---- upload / session / welcome ----
    "upload_error": {"pt": "Não foi possível ler {name}: {error}", "fr": "Impossible de lire {name} : {error}"},
    "processing": {"pt": "Processando {name}…", "fr": "Traitement de {name}…"},
    "file_loaded": {"pt": "{label}: {rows} linhas · {y0}–{y1}", "fr": "{label} : {rows} lignes · {y0}–{y1}"},
    "auto_wiped": {"pt": "A sessão foi apagada automaticamente por inatividade.", "fr": "La session a été effacée automatiquement pour inactivité."},
    "how_1": {"pt": "**1 · Carregar**\n\nDois exports do BI: o YTD do ano em curso contra o ano anterior, e o histórico multi-ano / Full Year. Pode-se trabalhar com um só, com funcionalidade reduzida.",
              "fr": "**1 · Charger**\n\nDeux exports du BI : le YTD de l'année en cours face à la précédente, et l'historique multi-années / Full Year. On peut travailler avec un seul, avec des fonctions réduites."},
    "how_2": {"pt": "**2 · Filtrar**\n\nLigue e desligue métricas, mude o agrupamento, restrinja clientes e famílias. Todo o painel reage, como uma tabela dinâmica.",
              "fr": "**2 · Filtrer**\n\nActivez et désactivez des mesures, changez le regroupement, restreignez clients et familles. Tout le tableau réagit, comme un tableau croisé."},
    "how_3": {"pt": "**3 · Decidir**\n\nPontes de preço, volume e custo; desvios ordenados por dólares; e bullets de estratégia calculados sobre seu filtro.",
              "fr": "**3 · Décider**\n\nPonts de prix, volume et coût ; écarts classés par dollars ; et puces de stratégie calculées sur votre filtre."},
    "privacy_long": {"pt": "**Privacidade.** Os arquivos são processados em memória. Nada é escrito em disco, não há banco de dados nem histórico. Ao fechar a aba, ao atingir o tempo de inatividade ou ao clicar «Apagar tudo», não sobra rastro.",
                     "fr": "**Confidentialité.** Les fichiers sont traités en mémoire. Rien n'est écrit sur disque, pas de base de données ni d'historique. À la fermeture de l'onglet, au délai d'inactivité ou en cliquant « Tout effacer », aucune trace ne subsiste."},
    "filter_customer_help": {"pt": "Vazio = todos. Filtre por grupo para conservar o budget, que é carregado nesse nível.",
                             "fr": "Vide = tous. Filtrez par groupe pour conserver le budget, chargé à ce niveau."},
    "filter_account_help": {"pt": "Vazio = todas as contas do grupo. O budget do grupo é conservado.",
                            "fr": "Vide = tous les comptes du groupe. Le budget du groupe est conservé."},
    "filter_active": {"pt": "🔎 Filtro ativo · {n} linhas", "fr": "🔎 Filtre actif · {n} lignes"},
    "include_open_help": {"pt": "Soma os pedidos já tomados e ainda não faturados a vendas, profit e volume.",
                          "fr": "Ajoute les commandes déjà prises et non encore facturées aux ventes, profit et volume."},
    "materiality_help": {"pt": "Oculta linhas abaixo deste valor em ambos os períodos.", "fr": "Masque les lignes sous ce montant sur les deux périodes."},
    "budget_level_note": {"pt": "ℹ️ O budget é carregado a nível de grupo, não por conta individual: neste agrupamento as comparações vs budget ficam desativadas.",
                          "fr": "ℹ️ Le budget est chargé au niveau du groupe, pas par compte individuel : dans ce regroupement les comparaisons vs budget sont désactivées."},
    # ---- bridge effects ----
    "eff_volume": {"pt": "Efeito volume", "fr": "Effet volume"},
    "eff_price": {"pt": "Efeito preço", "fr": "Effet prix"},
    "eff_cost": {"pt": "Efeito custo", "fr": "Effet coût"},
    "eff_new": {"pt": "Entradas cliente-item", "fr": "Entrées client-article"},
    "eff_lost": {"pt": "Saídas cliente-item", "fr": "Sorties client-article"},
    "eff_other": {"pt": "Outros", "fr": "Autres"},
    # ---- overview ----
    "ov_title": {"pt": "Resumo {cur} vs {base}", "fr": "Résumé {cur} vs {base}"},
    "ov_note": {"pt": "Base: {basis} · Agrupamento: {level} · {n} clientes no filtro.", "fr": "Base : {basis} · Regroupement : {level} · {n} clients dans le filtre."},
    "basis_invoiced": {"pt": "faturado", "fr": "facturé"},
    "basis_sold_open": {"pt": "faturado + carteira aberta", "fr": "facturé + carnet de commandes"},
    "ov_sales_bar": {"pt": "Vendas vs budget anual", "fr": "Ventes vs budget annuel"},
    "ov_profit_bar": {"pt": "Profit vs budget anual", "fr": "Profit vs budget annuel"},
    "ov_qty_bar": {"pt": "Volume vs budget anual", "fr": "Volume vs budget annuel"},
    "ov_pace_sub": {"pt": "marcador = ritmo esperado a esta altura", "fr": "repère = rythme attendu à ce stade"},
    "ov_sales_bridge": {"pt": "Ponte de vendas {base} → {cur}", "fr": "Pont des ventes {base} → {cur}"},
    "ov_margin_bridge": {"pt": "Ponte de margem {base} → {cur}", "fr": "Pont de marge {base} → {cur}"},
    "ov_bridge_note": {"pt": "As vendas {dir} {amount} ({pct}), com {driver} como componente dominante ({value}).",
                       "fr": "Les ventes {dir} de {amount} ({pct}), avec {driver} comme composante dominante ({value})."},
    "dir_up": {"pt": "sobem", "fr": "augmentent"},
    "dir_down": {"pt": "caem", "fr": "baissent"},
    "ov_margin_note": {"pt": "Efeito preço {price} · efeito custo {cost}. A margem se move principalmente por {cause}.",
                       "fr": "Effet prix {price} · effet coût {cost}. La marge évolue surtout par {cause}."},
    "cause_price": {"pt": "preço", "fr": "le prix"},
    "cause_cost": {"pt": "custo unitário", "fr": "le coût unitaire"},
    "ov_budget_gap": {"pt": "Gap vs budget por {level}", "fr": "Écart vs budget par {level}"},
    "ov_stack": {"pt": "Faturado + carteira vs budget por {level}", "fr": "Facturé + carnet vs budget par {level}"},
    "ov_stack_note": {"pt": "A barra sólida é o faturado; a hachurada, os {open} já vendidos e pendentes de embarque. Somados dão {so}. {n} {level} alcançam ou superam seu budget contando a carteira.",
                      "fr": "La barre pleine est le facturé ; la hachurée, les {open} déjà vendus en attente d'expédition. Ensemble ils font {so}. {n} {level} atteignent ou dépassent leur budget en comptant le carnet."},
    "cl_stack": {"pt": "Faturado + carteira vs budget por família", "fr": "Facturé + carnet vs budget par famille"},
    "ov_backlog_card": {"pt": "Carteira aberta vs gap de budget", "fr": "Carnet ouvert vs écart de budget"},
    "ov_backlog_delta": {"pt": "cobre {pct} do gap de {gap}", "fr": "couvre {pct} de l'écart de {gap}"},
    # ---- backlog ----
    "bl_title": {"pt": "Carteira aberta — pedidos tomados e ainda não faturados", "fr": "Carnet de commandes — commandes prises et non encore facturées"},
    "bl_note": {"pt": "É negócio já ganho: o impacto que terá ao ser faturado, contra o budget e contra o ano base.",
                "fr": "C'est du chiffre déjà gagné : l'impact qu'il aura une fois facturé, face au budget et à l'année de base."},
    "bl_none": {"pt": "O arquivo ativo não traz carteira aberta (coluna Open Orders vazia ou ausente).",
                "fr": "Le fichier actif n'a pas de carnet ouvert (colonne Open Orders vide ou absente)."},
    "bl_total": {"pt": "Carteira aberta total", "fr": "Carnet ouvert total"},
    "bl_share": {"pt": "Carteira sobre faturado", "fr": "Carnet sur facturé"},
    "bl_groups": {"pt": "{n} de {total} com carteira", "fr": "{n} sur {total} avec carnet"},
    "bl_coverage": {"pt": "Cobertura do gap", "fr": "Couverture de l'écart"},
    "bl_coverage_sub": {"pt": "gap de budget {gap}", "fr": "écart de budget {gap}"},
    "bl_profit": {"pt": "Profit em carteira", "fr": "Profit dans le carnet"},
    "bl_margin_sub": {"pt": "margem da carteira {pct}", "fr": "marge du carnet {pct}"},
    "bl_bridge": {"pt": "Do faturado ao budget: quanto a carteira fecha", "fr": "Du facturé au budget : combien le carnet comble"},
    "bl_bridge_note": {"pt": "Faturado {inv} + carteira {open} = {so}, contra um budget de {bdg}. A carteira cobre {cov} do gap e deixa {left} por conseguir.",
                       "fr": "Facturé {inv} + carnet {open} = {so}, face à un budget de {bdg}. Le carnet couvre {cov} de l'écart et laisse {left} à conquérir."},
    "bl_stack": {"pt": "Faturado e carteira por {level}", "fr": "Facturé et carnet par {level}"},
    "bl_rank": {"pt": "Maior carteira aberta por {level}", "fr": "Plus grand carnet ouvert par {level}"},
    "bl_effect": {"pt": "Efeito da carteira sobre a variação vs {base}", "fr": "Effet du carnet sur la variation vs {base}"},
    "bl_effect_note": {"pt": "Sem carteira a variação é {without}; com carteira passa a {with_}. A carteira inverte o sinal em {n} {level}.",
                       "fr": "Sans carnet la variation est {without} ; avec carnet elle devient {with_}. Le carnet inverse le signe pour {n} {level}."},
    "bl_table": {"pt": "Detalhe da carteira", "fr": "Détail du carnet"},
    "bl_col_open": {"pt": "Carteira", "fr": "Carnet"},
    "bl_col_share": {"pt": "% sobre faturado", "fr": "% du facturé"},
    "bl_col_so": {"pt": "Faturado + carteira", "fr": "Facturé + carnet"},
    "bl_col_cover": {"pt": "Avanço com carteira", "fr": "Avancement avec carnet"},
    # ---- full year ----
    "fy_trend": {"pt": "Tendência multi-ano", "fr": "Tendance pluriannuelle"},
    "fy_trend_note": {"pt": "Do arquivo histórico, internamente consistente: anos {y0}–{y1}. Bandas ocultas por vazias ou parciais: {hidden}.",
                      "fr": "Du fichier historique, cohérent en interne : années {y0}–{y1}. Bandes masquées car vides ou partielles : {hidden}."},
    "fy_sales_year": {"pt": "Vendas por ano", "fr": "Ventes par année"},
    "fy_sales_margin": {"pt": "Vendas e margem por ano", "fr": "Ventes et marge par année"},
    "fy_cagr": {"pt": "CAGR de vendas {y0}–{y1}: {cagr} · margem {m0} → {m1} ({pp}).",
                "fr": "CAGR des ventes {y0}–{y1} : {cagr} · marge {m0} → {m1} ({pp})."},
    "fy_need_ytd": {"pt": "Carregue também o arquivo YTD para habilitar o forecast de aterrissagem.",
                    "fr": "Chargez aussi le fichier YTD pour activer la prévision d'atterrissage."},
    "fy_basis_warn": {"pt": "**Aviso de base de data.** Os dois arquivos não batem em {year}: {bad} grupos mostram um YTD maior que seu ano completo, o que é impossível na mesma base. Projetam-se individualmente {ok} de {total} grupos; o resto usa o índice da carteira e fica marcado como indicativo. {match} coincidem exatamente entre arquivos.",
                      "fr": "**Avertissement de base de date.** Les deux fichiers ne concordent pas en {year} : {bad} groupes montrent un YTD supérieur à leur année complète, impossible sur une même base. {ok} groupes sur {total} sont projetés individuellement ; le reste utilise l'indice du portefeuille et est marqué comme indicatif. {match} coïncident exactement entre fichiers."},
    "fy_share_done": {"pt": "% do FY {year} já alcançado", "fr": "% du FY {year} déjà atteint"},
    "fy_share_sub": {"pt": "ritmo do ano passado a esta altura: {pace}", "fr": "rythme de l'an dernier à ce stade : {pace}"},
    "fy_attain": {"pt": "Avanço de budget", "fr": "Avancement du budget"},
    "fy_pace_sub": {"pt": "pace esperado {pace}", "fr": "pace attendu {pace}"},
    "fy_landing_sub": {"pt": "{delta} vs budget", "fr": "{delta} vs budget"},
    "fy_projectable": {"pt": "Grupos projetáveis", "fr": "Groupes projetables"},
    "fy_inconsistent": {"pt": "{n} com base inconsistente", "fr": "{n} à base incohérente"},
    "fy_bullet": {"pt": "Aterrissagem {cur} vs budget e vs FY {prior}", "fr": "Atterrissage {cur} vs budget et vs FY {prior}"},
    "fy_landing_by": {"pt": "Aterrissagem por {level}", "fr": "Atterrissage par {level}"},
    "fy_level_note": {"pt": "O budget é carregado a nível de grupo, então a aterrissagem é calculada por Cliente (grupo) mesmo que você agrupe por conta.",
                      "fr": "Le budget est chargé au niveau du groupe, donc l'atterrissage se calcule par Client (groupe) même si vous groupez par compte."},
    "fy_progress": {"pt": "Alcançado vs objetivo (maior entre budget e FY {prior})", "fr": "Atteint vs objectif (le plus grand entre budget et FY {prior})"},
    "fy_gap_chart": {"pt": "Gap projetado no fechamento vs budget", "fr": "Écart projeté à la clôture vs budget"},
    "fy_gap_note": {"pt": "{n} {level} projetam fechar abaixo do budget, num total de {total}.",
                    "fr": "{n} {level} devraient clôturer sous le budget, pour un total de {total}."},
    "fy_diag_title": {"pt": "Diagnóstico de base entre arquivos (por que alguns não se projetam)", "fr": "Diagnostic de base entre fichiers (pourquoi certains ne sont pas projetés)"},
    "fy_diag_caption": {"pt": "«Coincide» = mesma cifra em ambos os arquivos. «Base inconsistente» = o YTD supera o ano completo, sinal de que os arquivos usam campos de data distintos. Para eliminá-lo por completo, exporte o Full Year do ano anterior com o mesmo relatório que gera o arquivo YTD.",
                        "fr": "« Coïncide » = même chiffre dans les deux fichiers. « Base incohérente » = le YTD dépasse l'année complète, signe que les fichiers utilisent des champs de date différents. Pour l'éliminer, exportez le Full Year de l'année précédente avec le même rapport que le fichier YTD."},
    # ---- client sheet ----
    "cl_title": {"pt": "Ficha do cliente", "fr": "Fiche client"},
    "cl_pick": {"pt": "Cliente (grupo)", "fr": "Client (groupe)"},
    "cl_note": {"pt": "Posição {rank} de {total} por vendas · {share} do faturamento total · {accounts} conta(s): {names}",
                "fr": "Rang {rank} sur {total} par ventes · {share} du chiffre total · {accounts} compte(s) : {names}"},
    "cl_no_activity": {"pt": "{client} não tem atividade nos anos selecionados.", "fr": "{client} n'a aucune activité sur les années sélectionnées."},
    "cl_no_budget": {"pt": "sem budget carregado para este cliente", "fr": "aucun budget chargé pour ce client"},
    "cl_budget_note": {"pt": "Faltam {gap} para o budget. Tem {open} em carteira aberta, que cobre {cover} desse gap.",
                       "fr": "Il manque {gap} pour le budget. {open} en carnet ouvert, couvrant {cover} de cet écart."},
    "cl_landing_note": {"pt": "Aterrissagem {landing}, calculada com {source} ({index} do ano se alcança a esta altura). Gap vs budget: {gap}.",
                        "fr": "Atterrissage {landing}, calculé avec {source} ({index} de l'année est atteint à ce stade). Écart vs budget : {gap}."},
    "cl_own_index": {"pt": "seu próprio índice de sazonalidade", "fr": "son propre indice de saisonnalité"},
    "cl_portfolio_index": {"pt": "o índice da carteira (este cliente não é projetável sozinho)", "fr": "l'indice du portefeuille (ce client n'est pas projetable seul)"},
    "cl_history": {"pt": "Histórico do cliente por ano", "fr": "Historique du client par année"},
    "cl_why": {"pt": "Por que se moveu {delta}", "fr": "Pourquoi il a bougé de {delta}"},
    "cl_bridge_note": {"pt": "Volume {volume} · preço {price}. O movimento é sobretudo de {cause}.", "fr": "Volume {volume} · prix {price}. Le mouvement vient surtout de {cause}."},
    "cl_products": {"pt": "O que compra", "fr": "Ce qu'il achète"},
    "cl_alerts": {"pt": "Alertas desta conta", "fr": "Alertes de ce compte"},
    "cl_alert_lost": {"pt": "**{n} itens deixaram de ser comprados** ({total} no ano base): {names}.",
                      "fr": "**{n} articles ne sont plus achetés** ({total} l'année de base) : {names}."},
    "cl_alert_new": {"pt": "**{n} itens novos** contribuem {total} neste período.", "fr": "**{n} nouveaux articles** contribuent {total} sur cette période."},
    "cl_alert_margin": {"pt": "**Margem {cur}** contra {base} do ano base ({pp}).", "fr": "**Marge {cur}** face à {base} de l'année de base ({pp})."},
    "cl_alert_price": {"pt": "**Queda de preço**: {name} baixa {pct} sobre {sales} de vendas.", "fr": "**Baisse de prix** : {name} chute de {pct} sur {sales} de ventes."},
    "cl_alert_backlog": {"pt": "**{total} em carteira aberta** já ganhos, pendentes de embarque.", "fr": "**{total} en carnet ouvert** déjà gagnés, en attente d'expédition."},
    "cl_alert_gap": {"pt": "**Projeta fechar {total} abaixo do seu budget.**", "fr": "**Devrait clôturer {total} sous son budget.**"},
    # ---- dimension ----
    "dim_title": {"pt": "{level} · {cur} vs {base}", "fr": "{level} · {cur} vs {base}"},
    "dim_note": {"pt": "{n} registros no filtro · {new} novos · {lost} perdidos · limite de materialidade {mat}.",
                 "fr": "{n} enregistrements dans le filtre · {new} nouveaux · {lost} perdus · seuil de matérialité {mat}."},
    "dim_top_var": {"pt": "Maiores variações de vendas", "fr": "Plus grandes variations de ventes"},
    "dim_contrib": {"pt": "Contribuição ao delta por {level}", "fr": "Contribution au delta par {level}"},
    "dim_quadrant": {"pt": "Crescimento vs margem por {level}", "fr": "Croissance vs marge par {level}"},
    "dim_quadrant_note": {"pt": "Tamanho da bolha = vendas do período atual. Quadrante inferior direito: crescem, mas com margem baixa — candidatos a revisão de preço.",
                          "fr": "Taille de la bulle = ventes de la période actuelle. Quadrant en bas à droite : croissance mais marge faible — candidats à une révision de prix."},
    "dim_treemap": {"pt": "Famílias por vendas, coloridas por variação de margem", "fr": "Familles par ventes, colorées par variation de marge"},
    "dim_scatter": {"pt": "Preço vs volume — onde subiu o preço e perdeu quilos", "fr": "Prix vs volume — où le prix a monté et le volume baissé"},
    "dim_prod_bridge": {"pt": "Ponte de margem a nível produto", "fr": "Pont de marge au niveau produit"},
    "dim_churn": {"pt": "⚠️ {n} {level} sem atividade em {year} — {amount} em jogo", "fr": "⚠️ {n} {level} sans activité en {year} — {amount} en jeu"},
    "dim_cross": {"pt": "Cruzamento {a} × {b}", "fr": "Croisement {a} × {b}"},
    "dim_cross_chart": {"pt": "Variação % de vendas", "fr": "Variation % des ventes"},
    "dim_detail": {"pt": "Detalhe", "fr": "Détail"},
    "quad_stars": {"pt": "Estrelas", "fr": "Étoiles"},
    "quad_defend": {"pt": "Defender margem", "fr": "Défendre la marge"},
    "quad_price": {"pt": "Revisar preço", "fr": "Réviser le prix"},
    "quad_rescue": {"pt": "Resgatar", "fr": "Sauver"},
    "axis_growth": {"pt": "Crescimento vs ano base", "fr": "Croissance vs année de base"},
    "axis_margin": {"pt": "Margem %", "fr": "Marge %"},
    "axis_dprice": {"pt": "Δ preço unitário", "fr": "Δ prix unitaire"},
    "axis_dvolume": {"pt": "Δ volume", "fr": "Δ volume"},
    # ---- deviations ----
    "dev_title": {"pt": "Radar de desvios", "fr": "Radar des écarts"},
    "dev_note": {"pt": "Ordenado por impacto em dólares, não por porcentagem: uma queda de 300% sobre uma conta de 400 USD não deveria encabeçar nenhuma lista.",
                 "fr": "Classé par impact en dollars, pas en pourcentage : une chute de 300 % sur un compte de 400 USD ne devrait jamais être en tête."},
    "dev_type": {"pt": "Tipo de desvio", "fr": "Type d'écart"},
    "dev_direction": {"pt": "Direção", "fr": "Direction"},
    "dev_against": {"pt": "Medir contra", "fr": "Mesurer contre"},
    "dev_all": {"pt": "Todos", "fr": "Tous"},
    "dev_negative": {"pt": "Negativos", "fr": "Négatifs"},
    "dev_positive": {"pt": "Positivos", "fr": "Positifs"},
    "dev_base_year": {"pt": "Ano base", "fr": "Année de base"},
    "dev_no_budget": {"pt": "O arquivo ativo não traz budget; mede-se contra o ano base.", "fr": "Le fichier actif n'a pas de budget ; on mesure contre l'année de base."},
    "dev_neg_total": {"pt": "Desvio negativo total", "fr": "Écart négatif total"},
    "dev_pos_total": {"pt": "Desvio positivo total", "fr": "Écart positif total"},
    "dev_net": {"pt": "Líquido", "fr": "Net"},
    "dev_records": {"pt": "{n} registros", "fr": "{n} enregistrements"},
    "dev_against_sub": {"pt": "contra {what}", "fr": "contre {what}"},
    "dev_top5": {"pt": "Concentração top 5", "fr": "Concentration top 5"},
    "dev_top5_sub": {"pt": "do movimento absoluto", "fr": "du mouvement absolu"},
    "dev_chart": {"pt": "Maiores desvios vs {what}", "fr": "Plus grands écarts vs {what}"},
    "dev_compose": {"pt": "Composição do desvio por tipo", "fr": "Composition de l'écart par type"},
    "dev_none": {"pt": "Nenhum registro atende a estes critérios.", "fr": "Aucun enregistrement ne remplit ces critères."},
    "type_churn": {"pt": "Perda de cliente", "fr": "Perte de client"},
    "type_new": {"pt": "Cliente novo", "fr": "Nouveau client"},
    "type_volume": {"pt": "Volume", "fr": "Volume"},
    "type_price": {"pt": "Preço", "fr": "Prix"},
    "type_cost": {"pt": "Custo", "fr": "Coût"},
    # ---- strategy ----
    "st_title": {"pt": "Estratégia e próximos passos", "fr": "Stratégie et prochaines étapes"},
    "st_note": {"pt": "Gerado sobre o filtro ativo: {cur} vs {base}, agrupado por {level}. Mude os filtros e os bullets se recalculam.",
                "fr": "Généré sur le filtre actif : {cur} vs {base}, groupé par {level}. Changez les filtres et les puces se recalculent."},
    "st_diagnosis": {"pt": "🔍 Diagnóstico", "fr": "🔍 Diagnostic"},
    "st_diagnosis_c": {"pt": "O que aconteceu, quantificado.", "fr": "Ce qui s'est passé, quantifié."},
    "st_risks": {"pt": "⚠️ Riscos", "fr": "⚠️ Risques"},
    "st_risks_c": {"pt": "O que pode piorar se ninguém agir.", "fr": "Ce qui peut empirer si personne n'agit."},
    "st_opps": {"pt": "🌱 Oportunidades", "fr": "🌱 Opportunités"},
    "st_opps_c": {"pt": "Onde está o upside disponível.", "fr": "Où se trouve le potentiel disponible."},
    "st_actions": {"pt": "🎯 Ações sugeridas", "fr": "🎯 Actions suggérées"},
    "st_actions_c": {"pt": "Priorizadas por dólares em jogo.", "fr": "Priorisées par dollars en jeu."},
    "st_edit": {"pt": "Editar antes de exportar", "fr": "Modifier avant d'exporter"},
    "st_dl_md": {"pt": "Baixar resumo (Markdown)", "fr": "Télécharger le résumé (Markdown)"},
    "st_dl_xlsx": {"pt": "Baixar bullets (Excel)", "fr": "Télécharger les puces (Excel)"},
    "st_report_title": {"pt": "Análise de vendas {cur} vs {base}", "fr": "Analyse des ventes {cur} vs {base}"},
    "st_report_meta": {"pt": "_Gerado {stamp} · agrupamento por {level}_", "fr": "_Généré {stamp} · regroupement par {level}_"},
    # ---- data & quality ----
    "dq_title": {"pt": "Dados e qualidade", "fr": "Données et qualité"},
    "dq_note": {"pt": "O export do BI é uma tabela dinâmica com subtotais embutidos. Tudo o que você vê é calculado sobre as linhas folha; os subtotais são recalculados, nunca somados.",
                "fr": "L'export du BI est un tableau croisé avec des sous-totaux intégrés. Tout ce que vous voyez est calculé sur les lignes feuilles ; les sous-totaux sont recalculés, jamais additionnés."},
    "dq_not_loaded": {"pt": "{title}: não carregado.", "fr": "{title} : non chargé."},
    "dq_rows": {"pt": "Linhas no arquivo", "fr": "Lignes dans le fichier"},
    "dq_leaves": {"pt": "Linhas folha analisadas", "fr": "Lignes feuilles analysées"},
    "dq_pruned": {"pt": "Subtotais podados", "fr": "Sous-totaux élagués"},
    "dq_bands": {"pt": "Bandas de ano", "fr": "Bandes d'année"},
    "dq_recognised": {"pt": "O que o parser reconheceu", "fr": "Ce que le parser a reconnu"},
    "dq_sheet": {"pt": "Planilha", "fr": "Feuille"},
    "dq_header_row": {"pt": "Linha de cabeçalho", "fr": "Ligne d'en-tête"},
    "dq_year_source": {"pt": "Origem do ano", "fr": "Origine de l'année"},
    "dq_dims": {"pt": "Dimensões detectadas", "fr": "Dimensions détectées"},
    "dq_metrics": {"pt": "Métricas detectadas", "fr": "Mesures détectées"},
    "dq_ignored": {"pt": "Colunas ignoradas ({n})", "fr": "Colonnes ignorées ({n})"},
    "dq_notes": {"pt": "Notas de interpretação", "fr": "Notes d'interprétation"},
    "dq_recon": {"pt": "Conciliação entre arquivos · {year}", "fr": "Réconciliation entre fichiers · {year}"},
    "dq_match": {"pt": "Coincidem", "fr": "Coïncident"},
    "dq_coherent": {"pt": "Coerentes (YTD < FY)", "fr": "Cohérents (YTD < FY)"},
    "dq_inconsistent": {"pt": "Base inconsistente", "fr": "Base incohérente"},
    "dq_recon_error": {"pt": "O total {year} do arquivo YTD ({ytd}) supera o do arquivo Full Year ({fy}). Na mesma base de data isso é impossível, então os dois exports usam campos distintos. O forecast lida com isso marcando cada grupo, mas a solução de fundo é exportar o Full Year do ano anterior com o mesmo relatório que gera o arquivo YTD.",
                       "fr": "Le total {year} du fichier YTD ({ytd}) dépasse celui du fichier Full Year ({fy}). Sur une même base de date c'est impossible, donc les deux exports utilisent des champs différents. La prévision le gère en marquant chaque groupe, mais la vraie solution est d'exporter le Full Year de l'année précédente avec le même rapport que le fichier YTD."},
    # ---- insights ----
    "ins_nodata": {"pt": "Sem dados suficientes para diagnosticar com os filtros atuais.", "fr": "Pas assez de données pour diagnostiquer avec les filtres actuels."},
    "ins_headline": {"pt": "**Vendas {cur}** contra {base} do ano base: {delta} ({pct}).", "fr": "**Ventes {cur}** face à {base} de l'année de base : {delta} ({pct})."},
    "ins_driver": {"pt": "O movimento se explica sobretudo por **{driver}** ({value}). Volume {volume}, preço {price}.",
                   "fr": "Le mouvement s'explique surtout par **{driver}** ({value}). Volume {volume}, prix {price}."},
    "ins_margin": {"pt": "**Margem {cur}** vs {base} ({pp}). O componente dominante é o **{cause}** (preço {price}, custo {cost} em profit).",
                   "fr": "**Marge {cur}** vs {base} ({pp}). La composante dominante est **{cause}** (prix {price}, coût {cost} en profit)."},
    "ins_concentration": {"pt": "**3 contas concentram {pct} do movimento total**: {names}.", "fr": "**3 comptes concentrent {pct} du mouvement total** : {names}."},
    "ins_pace": {"pt": "**Avanço de budget {att}** contra um pace esperado de {pace} a esta altura: {verdict} do ritmo. Aterrissagem projetada {landing} vs budget {budget}.",
                 "fr": "**Avancement du budget {att}** face à un pace attendu de {pace} à ce stade : {verdict} du rythme. Atterrissage projeté {landing} vs budget {budget}."},
    "ins_above": {"pt": "acima", "fr": "au-dessus"},
    "ins_below": {"pt": "abaixo", "fr": "en dessous"},
    "ins_attain": {"pt": "**Avanço de budget {att}** sobre o budget anual de {budget}.", "fr": "**Avancement du budget {att}** sur le budget annuel de {budget}."},
    "ins_top_product": {"pt": "A nível produto, **{name}** é o maior movimento individual ({value}).", "fr": "Au niveau produit, **{name}** est le plus grand mouvement individuel ({value})."},
    "ins_churn": {"pt": "**Churn: {n} contas sem faturamento neste período** que valiam {total}. A maior: {name} ({value}).",
                  "fr": "**Churn : {n} comptes sans facturation cette période** valant {total}. Le plus grand : {name} ({value})."},
    "ins_margin_erosion": {"pt": "**Erosão de margem em {n} contas materiais** (queda > 3 pp). A mais severa: {name} com {pp} sobre {sales} de vendas.",
                           "fr": "**Érosion de marge sur {n} comptes matériels** (baisse > 3 pp). Le pire : {name} avec {pp} sur {sales} de ventes."},
    "ins_concentration_risk": {"pt": "**Concentração {level}** (Herfindahl {hhi}). O maior cliente pesa {pct} do faturamento do período.",
                               "fr": "**Concentration {level}** (Herfindahl {hhi}). Le plus gros client pèse {pct} du chiffre de la période."},
    "ins_conc_high": {"pt": "alta", "fr": "élevée"},
    "ins_conc_mid": {"pt": "moderada", "fr": "modérée"},
    "ins_conc_low": {"pt": "baixa", "fr": "faible"},
    "ins_budget_short": {"pt": "**{n} grupos projetam fechar abaixo do seu budget**, num total de {total}. O maior gap: {name} ({value}).",
                         "fr": "**{n} groupes devraient clôturer sous leur budget**, pour un total de {total}. Le plus grand écart : {name} ({value})."},
    "ins_unprojectable": {"pt": "⚠️ **{n} de {total} grupos não são projetáveis** por diferença de base entre os dois arquivos; usam o índice da carteira e sua aterrissagem é indicativa, não auditável.",
                          "fr": "⚠️ **{n} groupes sur {total} ne sont pas projetables** en raison de la différence de base entre les deux fichiers ; ils utilisent l'indice du portefeuille et leur atterrissage est indicatif, non auditable."},
    "ins_product_drop": {"pt": "**Produto em retrocesso material**: {name} cai {value} ({pct}).", "fr": "**Produit en net recul** : {name} chute de {value} ({pct})."},
    "ins_growing": {"pt": "**{n} contas em crescimento** contribuem +{total}. As três maiores: {detail}.", "fr": "**{n} comptes en croissance** apportent +{total}. Les trois plus grands : {detail}."},
    "ins_rich_products": {"pt": "**Produtos de margem alta e baixa penetração** — candidatos a impulsionar: {detail}.", "fr": "**Produits à forte marge et faible pénétration** — à pousser : {detail}."},
    "ins_new_accounts": {"pt": "**{n} contas novas** somam {total}. Consolidar o segundo pedido é a conversão que define se ficam na carteira.",
                         "fr": "**{n} nouveaux comptes** totalisent {total}. Concrétiser la deuxième commande est la conversion qui décide s'ils restent."},
    "ins_backlog": {"pt": "**{total} em carteira aberta** distribuídos em {n} contas: negócio já ganho, só aguardando embarque.",
                    "fr": "**{total} en carnet ouvert** répartis sur {n} comptes : chiffre déjà gagné, en attente d'expédition."},
    "ins_recover": {"pt": "**Recuperar run-rate em {n} contas rentáveis** (margem > 40%) devolveria até {total} de faturamento sem sacrificar margem.",
                    "fr": "**Récupérer le run-rate sur {n} comptes rentables** (marge > 40 %) rendrait jusqu'à {total} de chiffre sans sacrifier la marge."},
    "act_churn": {"pt": "**30 dias · Recuperação de churn** — contatar {names}. Em jogo {total}. Dono: comercial da conta.",
                  "fr": "**30 jours · Récupération du churn** — contacter {names}. {total} en jeu. Responsable : commercial du compte."},
    "act_cost": {"pt": "**30 dias · Revisão de custos** — o efeito custo drena {value} de profit. Revisar contratos de compra e repassar à lista de preços onde o contrato permitir.",
                 "fr": "**30 jours · Revue des coûts** — l'effet coût draine {value} de profit. Revoir les contrats d'achat et répercuter sur les tarifs là où le contrat le permet."},
    "act_price": {"pt": "**60 dias · Repricing seletivo** — o efeito preço subtrai {value}. Priorizar itens com volume estável e elasticidade baixa antes de tocar contas em risco.",
                  "fr": "**60 jours · Repricing sélectif** — l'effet prix retire {value}. Prioriser les articles à volume stable et faible élasticité avant de toucher aux comptes à risque."},
    "act_volume": {"pt": "**60 dias · Plano de volume** — perderam-se {value} em quilos. Definir meta de reposição por conta e produto.",
                   "fr": "**60 jours · Plan de volume** — {value} perdus en volume. Définir un objectif de reconstitution par compte et produit."},
    "act_backlog": {"pt": "**Contínuo · Conversão de carteira** — {total} em pedidos abertos. Assegurar data de embarque para que caiam dentro do exercício.",
                    "fr": "**Continu · Conversion du carnet** — {total} en commandes ouvertes. Sécuriser la date d'expédition pour qu'elles tombent dans l'exercice."},
    "act_budget": {"pt": "**90 dias · Fechar o gap de budget** — plano conta a conta para os 5 maiores gaps projetados ({total}). Revisão quinzenal com acompanhamento da carteira aberta.",
                   "fr": "**90 jours · Combler l'écart de budget** — plan compte par compte pour les 5 plus grands écarts projetés ({total}). Revue bimensuelle avec suivi du carnet."},
    # ---- one-pager ----
    "op_tab_title": {"pt": "Pontuação de progresso e one-pager executivo", "fr": "Score de progression et one-pager exécutif"},
    "op_note": {"pt": "A pontuação mistura vendas e margem: 100 significa aterrissar exatamente no budget. Não tem teto — projetar 15% acima marca 115.",
                "fr": "Le score mêle ventes et marge : 100 signifie atterrir exactement sur le budget. Sans plafond — projeter 15 % au-dessus donne 115."},
    "op_title": {"pt": "Resumo executivo de vendas", "fr": "Résumé exécutif des ventes"},
    "op_generated": {"pt": "Gerado", "fr": "Généré"},
    "op_confidential": {"pt": "Uso interno Robertet", "fr": "Usage interne Robertet"},
    "op_vs_budget": {"pt": "Avanço contra budget anual", "fr": "Avancement vs budget annuel"},
    "op_up": {"pt": "Maiores contribuições", "fr": "Plus grandes contributions"},
    "op_down": {"pt": "Maiores quedas", "fr": "Plus grandes baisses"},
    "op_worst_scores": {"pt": "Pontuações mais baixas", "fr": "Scores les plus bas"},
    "op_why": {"pt": "Por quê", "fr": "Pourquoi"},
    "op_actions": {"pt": "Diagnóstico e ações", "fr": "Diagnostic et actions"},
    "op_bridge": {"pt": "Efeito volume {volume} · efeito preço {price} sobre a variação do ano.", "fr": "Effet volume {volume} · effet prix {price} sur la variation de l'année."},
    "op_backlog_line": {"pt": "Carteira aberta {open}. Aterrissagem projetada {land} contra um budget de {bdg}.", "fr": "Carnet ouvert {open}. Atterrissage projeté {land} face à un budget de {bdg}."},
    "op_footer": {"pt": "Fontes: {ytd} · {fy}. Cifras em USD. O budget é carregado a nível de grupo de cliente. Margem e preço são recalculados a partir de seus componentes, nunca promediados. Documento gerado em memória; nenhuma cópia é armazenada.",
                  "fr": "Sources : {ytd} · {fy}. Chiffres en USD. Le budget est chargé au niveau du groupe client. Marge et prix sont recalculés à partir de leurs composantes, jamais moyennés. Document généré en mémoire ; aucune copie n'est stockée."},
    "op_export": {"pt": "Exportar one-pager", "fr": "Exporter le one-pager"},
    "op_download": {"pt": "⬇ Baixar one-pager (HTML)", "fr": "⬇ Télécharger le one-pager (HTML)"},
    "op_print_hint": {"pt": "Abra no navegador e use Ctrl+P → «Salvar como PDF». Já vem configurado em A4 horizontal, uma única página.",
                      "fr": "Ouvrez-le dans le navigateur et faites Ctrl+P → « Enregistrer en PDF ». Déjà réglé en A4 paysage, une seule page."},
    "op_preview": {"pt": "Pré-visualização", "fr": "Aperçu"},
    # ---- scoring ----
    "sc_weight_sales": {"pt": "Peso de vendas (%)", "fr": "Poids des ventes (%)"},
    "sc_weight_margin": {"pt": "Peso de margem", "fr": "Poids de la marge"},
    "sc_weight_help": {"pt": "O resto vai para margem. Padrão 60 / 40.", "fr": "Le reste va à la marge. Par défaut 60 / 40."},
    "sc_landing_vs": {"pt": "aterrissagem {land} vs budget {bdg}", "fr": "atterrissage {land} vs budget {bdg}"},
    "sc_margin_vs": {"pt": "margem {cur} vs budget {bdg}", "fr": "marge {cur} vs budget {bdg}"},
    "sc_surplus": {"pt": "Projeta {v} acima do budget.", "fr": "Projette {v} au-dessus du budget."},
    "sc_shortfall": {"pt": "Projeta {v} abaixo do budget.", "fr": "Projette {v} sous le budget."},
    "sc_drag_sales": {"pt": "As vendas são o que puxa a pontuação para baixo.", "fr": "Ce sont les ventes qui tirent le score vers le bas."},
    "sc_drag_margin": {"pt": "A margem é o que puxa a pontuação para baixo.", "fr": "C'est la marge qui tire le score vers le bas."},
    "sc_drag_both": {"pt": "Vendas e margem puxam parelho.", "fr": "Ventes et marge tirent à égalité."},
    "sc_method_projected": {"pt": "Calculado sobre a aterrissagem projetada ({index} do ano se alcança a esta altura).", "fr": "Calculé sur l'atterrissage projeté ({index} de l'année est atteint à ce stade)."},
    "sc_method_raw": {"pt": "Sem arquivo histórico: usa-se o faturado mais a carteira, não uma aterrissagem projetada.", "fr": "Sans fichier historique : on utilise le facturé plus le carnet, pas un atterrissage projeté."},
    "sc_no_budget": {"pt": "Não há budget no filtro atual, então não é possível calcular a pontuação. Agrupe por Cliente (grupo) ou remova o filtro de contas.",
                     "fr": "Aucun budget dans le filtre actuel, le score ne peut donc pas être calculé. Groupez par Client (groupe) ou retirez le filtre de comptes."},
    "sc_chart": {"pt": "Distância ao budget por {level} (0 = no budget)", "fr": "Distance au budget par {level} (0 = sur budget)"},
    "sc_chart_note": {"pt": "Cada barra é a pontuação menos 100: à direita, projetam superar seu budget; à esquerda, ficar aquém.",
                      "fr": "Chaque barre est le score moins 100 : à droite, projeté au-dessus du budget ; à gauche, en dessous."},
    "sc_material_note": {"pt": "Listam-se os grupos que pesam ao menos 1% do budget total; os de budget simbólico são omitidos para não encabeçar o ranking com ruído.",
                         "fr": "Seuls les groupes pesant au moins 1 % du budget total sont listés ; les budgets symboliques sont omis pour ne pas polluer le classement."},
    "sc_all_portfolio": {"pt": "Portfólio completo", "fr": "Portefeuille complet"},
    # ---- common leftovers ----
    "col_current": {"pt": "atual", "fr": "actuel"},
    "col_base": {"pt": "base", "fr": "base"},
    "status_new": {"pt": "novo", "fr": "nouveau"},
    "status_lost": {"pt": "perdido", "fr": "perdu"},
    "status_kept": {"pt": "contínuo", "fr": "continu"},
    "vs_budget": {"pt": "vs budget", "fr": "vs budget"},
    "vs_base_year": {"pt": "vs {year}", "fr": "vs {year}"},
    "footer_copyright": {"pt": "© 2026 · Software proprietário · uso licenciado. Dados processados em memória; nenhuma cópia é armazenada.",
                         "fr": "© 2026 · Logiciel propriétaire · usage sous licence. Données traitées en mémoire ; aucune copie n'est stockée."},
}


def merge_into(strings: dict) -> None:
    for key, tr in TRANSLATIONS.items():
        strings.setdefault(key, {}).update(tr)
'''

_MODULES["core.i18n"] = r'''"""Bilingual strings for the whole app — labels, chart titles and prose.

`t("key", value=…)` returns the string for the active language and applies
`str.format` with whatever keyword arguments are passed, so sentences that embed
numbers stay translatable instead of being concatenated in code.
"""

# © 2026 [Titular de derechos]. Todos los derechos reservados. / All rights reserved.
# Robertet LATAM Sales Analytics — software propietario. Ver LICENSE.
# Uso licenciado; prohibida su reproducción o distribución sin autorización escrita.
# Contacto: katyasam13@gmail.com


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
    "footer_copyright": {"es": "© 2026 · Software propietario · uso licenciado. Datos procesados en memoria; no se almacena copia.",
                         "en": "© 2026 · Proprietary software · licensed use. Data processed in memory; no copy is stored.",
                         "pt": "© 2026 · Software proprietário · uso licenciado. Dados processados em memória; nenhuma cópia é armazenada.",
                         "fr": "© 2026 · Logiciel propriétaire · usage sous licence. Données traitées en mémoire ; aucune copie n'est stockée."},

    # ----------------------------------------------------------- evolution --
    "tab_evolution":   {"es": "Evolución mensual", "en": "Monthly evolution"},
    "ev_title":        {"es": "Evolución mes a mes", "en": "Month-over-month evolution"},
    "ev_note":         {"es": "Compara el YTD de este mes contra el YTD del mes pasado. La diferencia es el movimiento del mes; el archivo trae además el año anterior, así que cada mes se juzga contra el mes previo y contra el mismo mes del año pasado.",
                        "en": "Compares this month's YTD against last month's YTD. The difference is the month's movement; the file also carries last year, so each month is judged against the prior month and against the same month a year ago."},
    "ev_need_prev":    {"es": "Carga el archivo del mes pasado en «Mes anterior (YTD)» en el panel lateral para habilitar esta vista.",
                        "en": "Load last month's file under “Previous month (YTD)” in the sidebar to enable this view."},
    "ev_how":          {"es": "¿Cómo tener el archivo del mes pasado?", "en": "How to get last month's file?"},
    "ev_how_body":     {"es": "Cada cierre, **guarda** el export YTD que descargas. Al mes siguiente subes el nuevo en «Archivo YTD» y el anterior en «Mes anterior». Con dos cierres ya funciona. La app no guarda historial, así que el archivado depende de ti.",
                        "en": "Each close, **save** the YTD export you download. Next month you load the new one under “YTD file” and the previous one under “Previous month”. Two closes are enough. The app keeps no history, so archiving is up to you."},
    "ev_err_year":     {"es": "El archivo del mes pasado no contiene el año {year}. ¿Subiste el archivo correcto?",
                        "en": "Last month's file has no {year} data. Did you load the right file?"},
    "ev_err_swapped":  {"es": "El archivo del «mes pasado» ({prev}) tiene más ventas que el de «este mes» ({now}). Parece que los subiste al revés: el más reciente va en «Archivo YTD».",
                        "en": "The “last month” file ({prev}) has more sales than “this month” ({now}). They look swapped: the newer one goes under “YTD file”."},
    "ev_err_same":     {"es": "Los dos archivos tienen el mismo total: parecen ser el mismo cierre. Sube dos meses distintos.",
                        "en": "Both files share the same total: they look like the same close. Load two different months."},
    "ev_verdict":      {"es": "Veredicto del mes", "en": "Month verdict"},
    "ev_improving":    {"es": "mejorando", "en": "improving"},
    "ev_declining":    {"es": "retrocediendo", "en": "declining"},
    "ev_stable":       {"es": "estable", "en": "stable"},
    "ev_month_sales":  {"es": "Ventas del mes", "en": "Month sales"},
    "ev_vs_year_ago":  {"es": "{v} vs mismo mes del año pasado", "en": "{v} vs same month last year"},
    "ev_month_margin": {"es": "Margen del mes", "en": "Month margin"},
    "ev_month_profit": {"es": "profit del mes {v}", "en": "month profit {v}"},
    "ev_landing_move": {"es": "Aterrizaje proyectado", "en": "Projected landing"},
    "ev_landing_delta": {"es": "{v} vs el mes pasado", "en": "{v} vs last month"},
    "ev_drv_sales":    {"es": "Puntaje de ventas {v}", "en": "Sales score {v}"},
    "ev_drv_margin":   {"es": "Puntaje de margen {v}", "en": "Margin score {v}"},
    "ev_movers":       {"es": "Quién aceleró y quién se frenó (ventas del mes)",
                        "en": "Who accelerated and who slowed (month sales)"},
    "ev_accelerating": {"es": "Aportaron este mes", "en": "Contributed this month"},
    "ev_slowing":      {"es": "Restaron este mes", "en": "Detracted this month"},
    "ev_month_year_ago": {"es": "Mismo mes año pasado", "en": "Same month last year"},
    "ev_month_this":   {"es": "Este mes", "en": "This month"},
    "ev_vs_year_chart": {"es": "Ventas del mes: este año vs el año pasado",
                         "en": "Month sales: this year vs last year"},
    "ev_yoy_note":     {"es": "El mes aportó {now} contra {py} del mismo mes del año pasado ({yoy}).",
                        "en": "The month contributed {now} against {py} in the same month last year ({yoy})."},
    "ev_alerts":       {"es": "Alertas de cambio de tendencia", "en": "Trend-change alerts"},
    "ev_alert_slow":   {"es": "**{name}** aportó {now} este mes, contra {py} el mismo mes del año pasado: se está desacelerando.",
                        "en": "**{name}** contributed {now} this month, against {py} a year ago: it is decelerating."},
    "ev_alert_margin": {"es": "**{name}** vendió {sales} este mes pero su margen cayó {pp} contra el mismo mes del año pasado.",
                        "en": "**{name}** sold {sales} this month but its margin fell {pp} versus the same month last year."},
    "ev_alert_stall":  {"es": "**{name}** no facturó este mes; el mismo mes del año pasado hizo {py}.",
                        "en": "**{name}** did not bill this month; a year ago it did {py} in the same month."},
    "ev_detail":       {"es": "Detalle mensual", "en": "Monthly detail"},
    "ev_col_month":    {"es": "Ventas mes", "en": "Month sales"},
    "ev_col_month_py": {"es": "Mes año pasado", "en": "Month last year"},
    "ev_col_yoy":      {"es": "Δ vs año pasado", "en": "Δ vs last year"},
    "ev_col_margin":   {"es": "Margen mes", "en": "Month margin"},
    "ev_col_margin_pp": {"es": "Δ margen pp", "en": "Δ margin pp"},
    "ev_col_ytd_prev": {"es": "YTD mes pasado", "en": "YTD last month"},
    "ev_col_ytd_now":  {"es": "YTD ahora", "en": "YTD now"},
    "ev_col_mom":      {"es": "Δ YTD %", "en": "Δ YTD %"},

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
    "data_source_help": {"es": "Elige contra qué se compara tu acumulado del año actual. «Archivo YTD»: contra el mismo período del año anterior (manzanas con manzanas). «Full Year»: contra el año completo anterior, para ver cuánto del año llevas recorrido y proyectar el cierre. Tu venta actual no cambia, solo el punto de comparación. El budget y la cartera se toman del archivo activo (normalmente el YTD, que trae el budget anual completo).",
                         "en": "Choose what your current-year running total is compared against. “YTD file”: the same period last year (apples to apples). “Full Year”: the whole prior year, to see how far into the year you are and project the close. Your actual sales don't change, only the comparison basis. Budget and backlog come from the active file (usually the YTD file, which carries the full annual budget)."},
    "fy_intro":        {"es": "Ventas **YTD {cur}** (acumulado al mes analizado) comparadas contra el **año completo {prior}**. El budget mostrado es el **budget anual**; el aterrizaje proyecta el cierre del año.",
                        "en": "**YTD {cur}** sales (running total to the analysed month) compared against **full-year {prior}**. The budget shown is the **annual budget**; the landing projects the year-end close."},
    "sc_budget_src":   {"es": "Budget anual (full year) usado: {total} · fuente: {file}. El landing se mide siempre contra el budget anual, no contra un budget YTD.",
                        "en": "Annual (full-year) budget used: {total} · source: {file}. The landing is always measured against the annual budget, never a YTD budget."},
    "dq_recon_ok":     {"es": "Total reconciliado con el export en {n} año(s): la suma de la app coincide con el gran total del pivote (diferencia ≤ {pct} %). Números confiables.",
                        "en": "Total reconciled with the export across {n} year(s): the app's sum matches the pivot grand total (difference ≤ {pct} %). Figures are trustworthy."},
    "dq_recon_gap":    {"es": "⚠️ El total no cuadra con el export en: {years}. Probablemente el pivote no está completamente expandido (profundidad despareja): algunas ramas se perdieron. Vuelve a exportar con todos los niveles expandidos.",
                        "en": "⚠️ The total does not match the export for: {years}. The pivot is likely not fully expanded (uneven depth): some branches were dropped. Re-export with all levels expanded."},
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
    "ov_stack":        {"es": "Facturado + cartera vs budget por {level}",
                        "en": "Invoiced + backlog vs budget by {level}"},
    "ov_stack_note":   {"es": "La barra sólida es lo facturado; la rayada, los {open} ya vendidos y pendientes de embarque. Sumados dan {so}. {n} {level} alcanzan o superan su budget contando la cartera.",
                        "en": "The solid bar is what is invoiced; the hatched one is the {open} already sold and awaiting shipment. Together they reach {so}. {n} {level} meet or beat their budget once backlog is counted."},
    "cl_stack":        {"es": "Facturado + cartera vs budget por familia",
                        "en": "Invoiced + backlog vs budget by family"},
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

    # ------------------------------------------------------------ one-pager --
    "tab_onepager":    {"es": "Puntaje y one-pager", "en": "Score & one-pager"},
    "op_tab_title":    {"es": "Puntaje de progreso y one-pager ejecutivo",
                        "en": "Progress score and executive one-pager"},
    "op_note":         {"es": "El puntaje mezcla ventas y margen: 100 significa aterrizar exactamente en budget. No tiene tope — proyectar 15% por encima marca 115.",
                        "en": "The score blends sales and margin: 100 means landing exactly on budget. It is uncapped — projecting 15% above scores 115."},
    "op_title":        {"es": "Resumen ejecutivo de ventas", "en": "Executive sales summary"},
    "op_generated":    {"es": "Generado", "en": "Generated"},
    "op_confidential": {"es": "Uso interno Robertet", "en": "Robertet internal use"},
    "op_vs_budget":    {"es": "Avance contra budget anual", "en": "Progress against annual budget"},
    "op_up":           {"es": "Mayores aportes", "en": "Largest gains"},
    "op_down":         {"es": "Mayores caídas", "en": "Largest drops"},
    "op_worst_scores": {"es": "Puntajes más bajos", "en": "Lowest scores"},
    "op_why":          {"es": "Por qué", "en": "Why"},
    "op_actions":      {"es": "Diagnóstico y acciones", "en": "Diagnosis and actions"},
    "op_bridge":       {"es": "Efecto volumen {volume} · efecto precio {price} sobre la variación del año.",
                        "en": "Volume effect {volume} · price effect {price} on the year-on-year change."},
    "op_backlog_line": {"es": "Cartera abierta {open}. Aterrizaje proyectado {land} contra un budget de {bdg}.",
                        "en": "Open orders {open}. Projected landing {land} against a budget of {bdg}."},
    "op_footer":       {"es": "Fuentes: {ytd} · {fy}. Cifras en USD. El budget está cargado a nivel grupo de cliente. Margen y precio se recalculan desde sus componentes, nunca se promedian. Documento generado en memoria; no se almacena ninguna copia.",
                        "en": "Sources: {ytd} · {fy}. Figures in USD. Budget is loaded at customer-group level. Margin and price are recomputed from their components, never averaged. Generated in memory; no copy is stored."},
    "op_export":       {"es": "Exportar one-pager", "en": "Export one-pager"},
    "op_download":     {"es": "⬇ Descargar one-pager (HTML)", "en": "⬇ Download one-pager (HTML)"},
    "op_print_hint":   {"es": "Ábrelo en el navegador y usa Ctrl+P → «Guardar como PDF». Ya viene configurado en A4 horizontal, una sola página.",
                        "en": "Open it in the browser and press Ctrl+P → “Save as PDF”. It is already set to A4 landscape, single page."},
    "op_preview":      {"es": "Vista previa", "en": "Preview"},

    # -------------------------------------------------------------- scoring --
    "sc_title":        {"es": "Puntaje", "en": "Score"},
    "sc_sales_score":  {"es": "Puntaje ventas", "en": "Sales score"},
    "sc_margin_score": {"es": "Puntaje margen", "en": "Margin score"},
    "sc_weight_sales": {"es": "Peso de ventas (%)", "en": "Sales weight (%)"},
    "sc_weight_margin": {"es": "Peso de margen", "en": "Margin weight"},
    "sc_weight_help":  {"es": "El resto va a margen. Por defecto 60 / 40.",
                        "en": "The rest goes to margin. Default 60 / 40."},
    "sc_band_on":      {"es": "En budget", "en": "On budget"},
    "sc_band_close":   {"es": "Cerca", "en": "Close"},
    "sc_band_risk":    {"es": "En riesgo", "en": "At risk"},
    "sc_band_critical": {"es": "Crítico", "en": "Critical"},
    "sc_landing_vs":   {"es": "aterrizaje {land} vs budget {bdg}",
                        "en": "landing {land} vs budget {bdg}"},
    "sc_margin_vs":    {"es": "margen {cur} vs budget {bdg}",
                        "en": "margin {cur} vs budget {bdg}"},
    "sc_surplus":      {"es": "Proyecta {v} por encima del budget.",
                        "en": "Projected {v} above budget."},
    "sc_shortfall":    {"es": "Proyecta {v} por debajo del budget.",
                        "en": "Projected {v} below budget."},
    "sc_drag_sales":   {"es": "Las ventas son las que arrastran el puntaje.",
                        "en": "Sales are what drag the score down."},
    "sc_drag_margin":  {"es": "El margen es el que arrastra el puntaje.",
                        "en": "Margin is what drags the score down."},
    "sc_drag_both":    {"es": "Ventas y margen tiran parejo.",
                        "en": "Sales and margin pull evenly."},
    "sc_method_projected": {"es": "Calculado sobre el aterrizaje proyectado ({index} del año se logra a esta altura).",
                            "en": "Computed on the projected landing ({index} of the year is booked by this point)."},
    "sc_method_raw":   {"es": "Sin archivo histórico: se usa lo facturado más la cartera, no un aterrizaje proyectado.",
                        "en": "No historical file: invoiced plus backlog is used, not a projected landing."},
    "sc_no_budget":    {"es": "No hay budget en el filtro actual, así que no se puede calcular el puntaje. Agrupa por Cliente (grupo) o quita el filtro de cuentas.",
                        "en": "There is no budget in the current filter, so the score cannot be computed. Group by customer group or clear the account filter."},
    "sc_chart":        {"es": "Distancia al budget por {level} (0 = en budget)",
                        "en": "Distance to budget by {level} (0 = on budget)"},
    "sc_chart_note":   {"es": "Cada barra es el puntaje menos 100: a la derecha, proyectan superar su budget; a la izquierda, quedarse cortos.",
                        "en": "Each bar is the score minus 100: to the right, projected above budget; to the left, short of it."},
    "sc_material_note": {"es": "Se listan los grupos que pesan al menos 1% del budget total; los de budget simbólico se omiten para no encabezar el ranking con ruido.",
                         "en": "Only groups worth at least 1% of total budget are listed; token budgets are left out so noise never tops the ranking."},
    "sc_all_portfolio": {"es": "Portafolio completo", "en": "Full portfolio"},

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


# Fallback chains: a missing pt reads es first (closest), fr reads en first.
_FALLBACK = {
    "es": ["es", "en"],
    "en": ["en", "es"],
    "pt": ["pt", "es", "en"],
    "fr": ["fr", "en", "es"],
}


def _resolve(entry: dict, lang: str, key: str) -> str:
    for l in _FALLBACK.get(lang, ["es", "en"]):
        if l in entry and entry[l]:
            return entry[l]
    return entry.get("es", key)


def t(key: str, **kwargs) -> str:
    entry = STRINGS.get(key)
    if entry is None:
        return key
    text = _resolve(entry, language(), key)
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
    if not meta:
        return key
    return _resolve(meta, language(), key)


def set_language(lang: str) -> None:
    st.session_state["lang"] = lang


# --------------------------------------------------------------------------- #
# Portuguese and French for the strings a user sees at a glance. Deep analytical
# prose (bridge notes, insight bullets) falls back per _FALLBACK above.
# --------------------------------------------------------------------------- #
_PT_FR = {
    "app_title": {"pt": "Análise de Vendas LATAM", "fr": "Analyse des Ventes LATAM"},
    "app_sub": {"pt": "Vendas · Margem · Budget — sessão efêmera",
                "fr": "Ventes · Marge · Budget — session éphémère"},
    "privacy_banner": {"pt": "🔒 Dados em memória. Nada é salvo em disco e tudo é apagado ao fechar a sessão.",
                       "fr": "🔒 Données en mémoire. Rien n'est enregistré sur disque ; tout est effacé à la fermeture."},
    "language": {"pt": "Idioma", "fr": "Langue"},
    "cancel": {"pt": "Cancelar", "fr": "Annuler"},
    "none": {"pt": "(nenhuma)", "fr": "(aucune)"},
    "empty_all": {"pt": "Vazio = todos", "fr": "Vide = tous"},
    "upload_title": {"pt": "Carregar arquivos", "fr": "Charger les fichiers"},
    "upload_ytd": {"pt": "Arquivo YTD (ano atual vs ano anterior)",
                   "fr": "Fichier YTD (année en cours vs précédente)"},
    "upload_fy": {"pt": "Arquivo histórico / Full Year (multi-ano)",
                  "fr": "Fichier historique / Full Year (multi-années)"},
    "upload_prev": {"pt": "Mês anterior (YTD do fechamento passado)",
                    "fr": "Mois précédent (YTD de la clôture passée)"},
    "upload_help": {"pt": "Export do BI em Excel. O app reconhece o formato mesmo que mudem nomes de coluna, idioma ou ordem.",
                    "fr": "Export du BI en Excel. L'app reconnaît le format même si les noms de colonnes, la langue ou l'ordre changent."},
    "upload_prev_help": {"pt": "Opcional. O mesmo export YTD baixado no mês passado. Habilita a aba de evolução mensal.",
                         "fr": "Optionnel. Le même export YTD téléchargé le mois dernier. Active l'onglet d'évolution mensuelle."},
    "no_files": {"pt": "Carregue ao menos um arquivo para começar.",
                 "fr": "Chargez au moins un fichier pour commencer."},
    "file_ytd": {"pt": "Arquivo YTD", "fr": "Fichier YTD"},
    "file_fy": {"pt": "Arquivo histórico / Full Year", "fr": "Fichier historique / Full Year"},
    "prev_short": {"pt": "Mês anterior", "fr": "Mois précédent"},
    "session": {"pt": "Sessão", "fr": "Session"},
    "clear_all": {"pt": "🗑️ Apagar tudo", "fr": "🗑️ Tout effacer"},
    "clear_confirm": {"pt": "Confirmar exclusão", "fr": "Confirmer la suppression"},
    "clear_warning": {"pt": "Serão removidos os arquivos e toda a análise desta sessão.",
                      "fr": "Les fichiers et toute l'analyse de cette session seront supprimés."},
    "cleared": {"pt": "Sessão apagada. Nenhum dado permanece em memória.",
                "fr": "Session effacée. Aucune donnée ne subsiste en mémoire."},
    "idle_left": {"pt": "Auto-exclusão em", "fr": "Effacement auto dans"},
    "idle_timeout": {"pt": "Minutos de inatividade antes de apagar",
                     "fr": "Minutes d'inactivité avant effacement"},
    "how_title": {"pt": "Como funciona", "fr": "Comment ça marche"},
    "comparison": {"pt": "Base de comparação", "fr": "Base de comparaison"},
    "data_source": {"pt": "Fonte de dados", "fr": "Source de données"},
    "data_source_help": {"pt": "Escolha contra o que seu acumulado do ano atual é comparado. «Arquivo YTD»: contra o mesmo período do ano anterior (maçãs com maçãs). «Full Year»: contra o ano completo anterior, para ver quanto do ano já percorreu e projetar o fechamento. Sua venda atual não muda, apenas o ponto de comparação. O budget e a carteira vêm do arquivo ativo (normalmente o YTD, que traz o budget anual completo).",
                         "fr": "Choisissez ce à quoi votre cumul de l'année en cours est comparé. « Fichier YTD » : la même période l'an dernier (à périmètre comparable). « Full Year » : l'année complète précédente, pour voir où vous en êtes dans l'année et projeter la clôture. Vos ventes réelles ne changent pas, seule la base de comparaison. Le budget et le carnet proviennent du fichier actif (généralement le fichier YTD, qui porte le budget annuel complet)."},
    "fy_intro": {"pt": "Vendas **YTD {cur}** (acumulado até o mês analisado) comparadas contra o **ano completo {prior}**. O budget mostrado é o **budget anual**; a aterrissagem projeta o fechamento do ano.",
                 "fr": "Ventes **YTD {cur}** (cumul jusqu'au mois analysé) comparées à l'**année complète {prior}**. Le budget affiché est le **budget annuel** ; l'atterrissage projette la clôture de l'année."},
    "sc_budget_src": {"pt": "Budget anual (full year) usado: {total} · fonte: {file}. A aterrissagem é sempre medida contra o budget anual, nunca contra um budget YTD.",
                      "fr": "Budget annuel (full year) utilisé : {total} · source : {file}. L'atterrissage est toujours mesuré face au budget annuel, jamais un budget YTD."},
    "dq_recon_ok": {"pt": "Total reconciliado com o export em {n} ano(s): a soma do app coincide com o total geral do pivô (diferença ≤ {pct} %). Números confiáveis.",
                    "fr": "Total réconcilié avec l'export sur {n} année(s) : la somme de l'app correspond au total général du TCD (écart ≤ {pct} %). Chiffres fiables."},
    "dq_recon_gap": {"pt": "⚠️ O total não bate com o export em: {years}. O pivô provavelmente não está totalmente expandido (profundidade irregular): algumas ramificações se perderam. Exporte novamente com todos os níveis expandidos.",
                     "fr": "⚠️ Le total ne correspond pas à l'export pour : {years}. Le TCD n'est probablement pas entièrement développé (profondeur inégale) : certaines branches ont été perdues. Réexportez avec tous les niveaux développés."},
    "current_year": {"pt": "Ano atual", "fr": "Année en cours"},
    "base_year": {"pt": "Ano base", "fr": "Année de base"},
    "dimensions": {"pt": "Dimensões", "fr": "Dimensions"},
    "group_by": {"pt": "Agrupar por", "fr": "Grouper par"},
    "second_dim": {"pt": "Dimensão secundária", "fr": "Dimension secondaire"},
    "filter_customer": {"pt": "Filtrar cliente (grupo)", "fr": "Filtrer client (groupe)"},
    "filter_account": {"pt": "…ou contas dentro do grupo", "fr": "…ou comptes dans le groupe"},
    "filter_family": {"pt": "Filtrar famílias", "fr": "Filtrer familles"},
    "top_n": {"pt": "Top N nos gráficos", "fr": "Top N dans les graphiques"},
    "metrics": {"pt": "Métricas (ligar / desligar)", "fr": "Mesures (activer / désactiver)"},
    "metrics_help": {"pt": "Desligue o que não quiser ver; some de KPIs, gráficos e tabelas.",
                     "fr": "Désactivez ce que vous ne voulez pas voir ; disparaît des KPI, graphiques et tableaux."},
    "basis": {"pt": "Base de cálculo", "fr": "Base de calcul"},
    "include_open": {"pt": "Incluir carteira aberta (Sold & Open)",
                     "fr": "Inclure le carnet de commandes (Sold & Open)"},
    "materiality": {"pt": "Limite de materialidade (USD)", "fr": "Seuil de matérialité (USD)"},
    "unit": {"pt": "Unidade de volume", "fr": "Unité de volume"},
    # tabs
    "tab_overview": {"pt": "Resumo", "fr": "Résumé"},
    "tab_client": {"pt": "Ficha do cliente", "fr": "Fiche client"},
    "tab_backlog": {"pt": "Carteira", "fr": "Carnet"},
    "tab_evolution": {"pt": "Evolução mensal", "fr": "Évolution mensuelle"},
    "tab_fy": {"pt": "YTD vs Full Year", "fr": "YTD vs Full Year"},
    "tab_customers": {"pt": "Clientes", "fr": "Clients"},
    "tab_products": {"pt": "Produtos", "fr": "Produits"},
    "tab_deviations": {"pt": "Desvios", "fr": "Écarts"},
    "tab_strategy": {"pt": "Estratégia", "fr": "Stratégie"},
    "tab_onepager": {"pt": "Pontuação e one-pager", "fr": "Score et one-pager"},
    "tab_data": {"pt": "Dados e qualidade", "fr": "Données et qualité"},
    # levels
    "level_enterprise": {"pt": "Cliente (grupo)", "fr": "Client (groupe)"},
    "level_customer": {"pt": "Cliente (conta)", "fr": "Client (compte)"},
    "level_product_family": {"pt": "Família de produto", "fr": "Famille de produit"},
    "level_product": {"pt": "Produto", "fr": "Produit"},
    "level_item_code": {"pt": "Código de item", "fr": "Code d'article"},
    # measures
    "sales": {"pt": "Vendas", "fr": "Ventes"},
    "profit": {"pt": "Lucro", "fr": "Profit"},
    "margin": {"pt": "Margem", "fr": "Marge"},
    "volume": {"pt": "Volume", "fr": "Volume"},
    "price": {"pt": "Preço", "fr": "Prix"},
    "budget": {"pt": "Budget", "fr": "Budget"},
    "invoiced": {"pt": "Faturado", "fr": "Facturé"},
    "open_orders": {"pt": "Carteira aberta", "fr": "Carnet de commandes"},
    "sold_open": {"pt": "Faturado + carteira", "fr": "Facturé + carnet"},
    "landing": {"pt": "Aterrissagem projetada", "fr": "Atterrissage projeté"},
    "achieved": {"pt": "Alcançado", "fr": "Atteint"},
    "missing": {"pt": "Falta", "fr": "Restant"},
    "rest": {"pt": "Resto", "fr": "Reste"},
    "start": {"pt": "Início", "fr": "Début"},
    "end": {"pt": "Final", "fr": "Fin"},
    "real": {"pt": "Real", "fr": "Réel"},
    # common
    "download_table": {"pt": "Baixar tabela (Excel)", "fr": "Télécharger le tableau (Excel)"},
    "download_excel": {"pt": "Baixar Excel", "fr": "Télécharger Excel"},
    "no_data": {"pt": "Sem dados para os filtros atuais.", "fr": "Aucune donnée pour les filtres actuels."},
    "no_metrics": {"pt": "Ative ao menos uma métrica no painel lateral.",
                   "fr": "Activez au moins une mesure dans le panneau latéral."},
    "needs_fy": {"pt": "Esta vista precisa do arquivo histórico / Full Year.",
                 "fr": "Cette vue nécessite le fichier historique / Full Year."},
    "needs_ytd": {"pt": "Esta vista precisa do arquivo YTD.", "fr": "Cette vue nécessite le fichier YTD."},
    "status": {"pt": "Estado", "fr": "Statut"},
    "no_threshold": {"pt": "sem limite", "fr": "aucun seuil"},
    # score / evolution headline labels
    "sc_title": {"pt": "Pontuação", "fr": "Score"},
    "sc_sales_score": {"pt": "Pontuação vendas", "fr": "Score ventes"},
    "sc_margin_score": {"pt": "Pontuação margem", "fr": "Score marge"},
    "sc_band_on": {"pt": "No budget", "fr": "Sur budget"},
    "sc_band_close": {"pt": "Perto", "fr": "Proche"},
    "sc_band_risk": {"pt": "Em risco", "fr": "À risque"},
    "sc_band_critical": {"pt": "Crítico", "fr": "Critique"},
    "ev_title": {"pt": "Evolução mês a mês", "fr": "Évolution mois par mois"},
    "ev_verdict": {"pt": "Veredicto do mês", "fr": "Verdict du mois"},
    "ev_improving": {"pt": "melhorando", "fr": "en amélioration"},
    "ev_declining": {"pt": "recuando", "fr": "en recul"},
    "ev_stable": {"pt": "estável", "fr": "stable"},
    "ev_month_sales": {"pt": "Vendas do mês", "fr": "Ventes du mois"},
    "ev_month_margin": {"pt": "Margem do mês", "fr": "Marge du mois"},
}

for _k, _tr in _PT_FR.items():
    STRINGS.setdefault(_k, {}).update(_tr)

# Full Portuguese/French coverage so no view mixes languages.
try:
    from core.i18n_ptfr import merge_into as _merge_ptfr
    _merge_ptfr(STRINGS)
except Exception:
    pass
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

# © 2026 [Titular de derechos]. Todos los derechos reservados. / All rights reserved.
# Robertet LATAM Sales Analytics — software propietario. Ver LICENSE.
# Uso licenciado; prohibida su reproducción o distribución sin autorización escrita.
# Contacto: katyasam13@gmail.com


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
    "sales":      {"es": "Ventas", "en": "Sales", "pt": "Vendas", "fr": "Ventes", "fmt": "money", "default": True},
    "profit":     {"es": "Profit", "en": "Profit", "pt": "Lucro", "fr": "Profit", "fmt": "money", "default": True},
    "margin_pct": {"es": "Margen %", "en": "Margin %", "pt": "Margem %", "fr": "Marge %", "fmt": "pct", "default": True},
    "quantity":   {"es": "Volumen", "en": "Volume", "pt": "Volume", "fr": "Volume", "fmt": "qty", "default": True},
    "price":      {"es": "Precio unitario", "en": "Unit price", "pt": "Preço unitário", "fr": "Prix unitaire", "fmt": "unit", "default": True},
    "unit_cost":  {"es": "Costo unitario", "en": "Unit cost", "pt": "Custo unitário", "fr": "Coût unitaire", "fmt": "unit", "default": False},
    "lines":      {"es": "Líneas", "en": "Order lines", "pt": "Linhas", "fr": "Lignes", "fmt": "int", "default": False},
    "sales_open": {"es": "Cartera abierta", "en": "Open orders", "pt": "Carteira aberta", "fr": "Carnet", "fmt": "money", "default": False},
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

# © 2026 [Titular de derechos]. Todos los derechos reservados. / All rights reserved.
# Robertet LATAM Sales Analytics — software propietario. Ver LICENSE.
# Uso licenciado; prohibida su reproducción o distribución sin autorización escrita.
# Contacto: katyasam13@gmail.com


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

# © 2026 [Titular de derechos]. Todos los derechos reservados. / All rights reserved.
# Robertet LATAM Sales Analytics — software propietario. Ver LICENSE.
# Uso licenciado; prohibida su reproducción o distribución sin autorización escrita.
# Contacto: katyasam13@gmail.com


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
    reconciliation: dict = field(default_factory=dict)  # per-year leaf vs export total

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
# Reconciliation
# --------------------------------------------------------------------------- #
def _group_marker_col(body: pd.DataFrame, dim_cols: dict[str, int]) -> int | None:
    """The column that flags a top-level group subtotal with a 'Total' token.

    In the pivot, the group total sits on the column immediately after the top
    dimension (e.g. 'Enterprise W/ Code'), which reads 'Total' on that row. We
    scan from just after the top dimension up to the next real dimension and take
    the first column that actually carries subtotal tokens.
    """
    order = [d for d in DIMENSIONS if d in dim_cols]
    if not order:
        return None
    top = dim_cols[order[0]]
    deeper = [c for c in dim_cols.values() if c > top]
    stop = min(deeper) if deeper else top + 3
    for col in range(top + 1, stop):
        if col in body.columns and _clean_dimension(body[col]).map(is_subtotal).fillna(False).any():
            return col
    return None


def _reconcile(body: pd.DataFrame, dim_cols: dict[str, int],
               blocks: dict[int, dict[str, int]], year_totals: pd.DataFrame) -> dict:
    """Per-year: leaf sum (what the app uses) vs the export's own group total."""
    marker = _group_marker_col(body, dim_cols)
    if marker is None:
        return {}
    grp_mask = _clean_dimension(body[marker]).map(is_subtotal).fillna(False)
    if not grp_mask.any():
        return {}
    out: dict = {}
    for year, cols in blocks.items():
        if "sales" not in cols:
            continue
        export_total = float(_to_number(body[cols["sales"]])[grp_mask].sum())
        leaf_total = float(year_totals.loc[year, "sales"]) if year in year_totals.index else 0.0
        if abs(export_total) < 1.0:
            continue
        out[int(year)] = {
            "leaf": leaf_total,
            "export": export_total,
            "diff": leaf_total - export_total,
            "diff_pct": abs(leaf_total - export_total) / abs(export_total),
        }
    return out


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

    # --- reconciliation: leaf sum vs the export's own group subtotals ---------
    # A partial/uneven pivot expansion would drop the collapsed branches and make
    # the leaf sum fall short of the export's real total. We recover an
    # INDEPENDENT total from the top-level subtotal rows (the ones the pivot
    # prints per group) and compare, so any shortfall is flagged instead of
    # silently trusted. The group-subtotal row is the one whose column right
    # after the enterprise dimension carries a "Total" token.
    reconciliation = _reconcile(body, dim_cols, blocks, year_totals)

    parsed = ParsedExport(
        tidy=tidy,
        years=sorted(blocks),
        n_leaf_rows=int(leaf_mask.sum()),
        n_raw_rows=n_raw,
        filename=filename,
        warnings=warnings,
        year_totals=year_totals,
        profile=profile,
        reconciliation=reconciliation,
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

# © 2026 [Titular de derechos]. Todos los derechos reservados. / All rights reserved.
# Robertet LATAM Sales Analytics — software propietario. Ver LICENSE.
# Uso licenciado; prohibida su reproducción o distribución sin autorización escrita.
# Contacto: katyasam13@gmail.com


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

# © 2026 [Titular de derechos]. Todos los derechos reservados. / All rights reserved.
# Robertet LATAM Sales Analytics — software propietario. Ver LICENSE.
# Uso licenciado; prohibida su reproducción o distribución sin autorización escrita.
# Contacto: katyasam13@gmail.com


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

# © 2026 [Titular de derechos]. Todos los derechos reservados. / All rights reserved.
# Robertet LATAM Sales Analytics — software propietario. Ver LICENSE.
# Uso licenciado; prohibida su reproducción o distribución sin autorización escrita.
# Contacto: katyasam13@gmail.com


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
    backlog: float = 0.0,
) -> go.Figure:
    """Attainment bar against budget, with an expected-pace marker.

    `backlog` stacks a second segment on top of what is already invoiced —
    orders booked but not yet billed. It is drawn in its own colour and hatched,
    so the eye never confuses money in the bank with money still to ship.
    """
    if not target or target <= 0 or value is None:
        return _empty(t("budget"))
    share = value / target
    backlog = float(backlog or 0.0)
    extra = max(backlog, 0.0) / target
    colour = T.POSITIVE if (pace is None or share >= pace) else (
        T.WARNING if share >= (pace or 0) * 0.9 else T.NEGATIVE
    )
    fmt = formatter or T.money_compact

    fig = go.Figure()
    # Track first, then the widest segment, then narrower ones on top: with
    # barmode="overlay" a stacked look comes from drawing back to front.
    fig.add_trace(go.Bar(x=[1.0], y=[""], orientation="h", marker=dict(color="#EDF1F5"),
                         hoverinfo="skip", showlegend=False, width=0.52))
    if extra > 0:
        fig.add_trace(go.Bar(
            x=[share + extra], y=[""], orientation="h", width=0.52,
            name=t("open_orders"), showlegend=True,
            marker=dict(color=T.AZURE, line=dict(color=T.NAVY, width=1),
                        pattern=dict(shape="/", size=8, solidity=0.30,
                                     fgcolor="#FFFFFF", bgcolor=T.AZURE)),
            hovertemplate=f"{t('sold_open')}: {fmt(value + backlog)}"
                          f" · {share + extra:.1%}<extra></extra>",
        ))
    fig.add_trace(go.Bar(
        x=[share], y=[""], orientation="h", width=0.52,
        name=t("invoiced"), showlegend=extra > 0,
        marker=dict(color=colour),
        hovertemplate=f"{t('invoiced')}: {fmt(value)} · {share:.1%}<extra></extra>",
    ))

    if pace is not None and not np.isnan(pace):
        fig.add_shape(type="line", x0=pace, x1=pace, y0=-0.42, y1=0.42, layer="above",
                      line=dict(color=T.NAVY, width=2, dash="dot"))
        fig.add_annotation(x=pace, y=0.46, text=f"{pace:.0%}", showarrow=False,
                           font=dict(size=11, color=T.NAVY), yanchor="bottom")

    label = f"{share:.0%} · {fmt(value)} / {fmt(target)}"
    if extra > 0:
        label += f"   +{fmt(backlog)} → {share + extra:.0%}"
    fig.update_layout(
        barmode="overlay", height=150 if extra > 0 else 132,
        title=dict(text=title, font=dict(size=14)),
        xaxis=dict(range=[0, max(1.15, (share + extra) * 1.1)], tickformat=".0%",
                   showgrid=False, zeroline=False),
        yaxis=dict(showticklabels=False, showgrid=False),
        margin=dict(l=4, r=4, t=58 if extra > 0 else 44, b=28),
        showlegend=extra > 0,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, x=0,
                    font=dict(size=11), traceorder="reversed"),
    )
    fig.add_annotation(x=0, y=-0.62, text=f"{label}   {subtitle}", showarrow=False,
                       xanchor="left", font=dict(size=11, color=T.MUTED))
    return fig


def budget_stack(
    df: pd.DataFrame, label_col: str, invoiced_col: str, backlog_col: str,
    budget_col: str, title: str, top_n: int = 15,
) -> go.Figure:
    """Invoiced + backlog stacked per group, with the budget as a marker.

    Answers "where does what we already have, plus what we have already sold,
    land against the target" for every group on one axis.
    """
    needed = [c for c in (invoiced_col, backlog_col, budget_col) if c in df.columns]
    if df.empty or invoiced_col not in df.columns:
        return _empty()
    d = df.copy()
    for c in needed:
        d[c] = pd.to_numeric(d[c], errors="coerce").fillna(0.0)
    d["_rank"] = d[[c for c in needed]].max(axis=1)
    d = d.sort_values("_rank", ascending=False).head(top_n).sort_values("_rank")
    if d.empty:
        return _empty()

    fig = go.Figure()
    fig.add_trace(go.Bar(
        y=_trunc(d[label_col], 30), x=d[invoiced_col], orientation="h",
        name=t("invoiced"), marker=dict(color=T.NAVY),
        hovertemplate="%{y}<br>%{x:$,.0f}<extra></extra>",
    ))
    if backlog_col in d.columns and d[backlog_col].abs().sum() > 0:
        fig.add_trace(go.Bar(
            y=_trunc(d[label_col], 30), x=d[backlog_col], orientation="h",
            name=t("open_orders"),
            marker=dict(color=T.AZURE, line=dict(color=T.NAVY, width=1),
                        pattern=dict(shape="/", size=8, solidity=0.30,
                                     fgcolor="#FFFFFF", bgcolor=T.AZURE)),
            hovertemplate="%{y}<br>%{x:$,.0f}<extra></extra>",
        ))
    if budget_col in d.columns and d[budget_col].abs().sum() > 0:
        fig.add_trace(go.Scatter(
            y=_trunc(d[label_col], 30), x=d[budget_col], mode="markers",
            name=t("budget"),
            marker=dict(symbol="diamond-tall", size=13, color="white",
                        line=dict(color=T.NEGATIVE, width=2)),
            hovertemplate="%{y}<br>" + t("budget") + " %{x:$,.0f}<extra></extra>",
        ))

    span = float(d[needed].to_numpy().max()) or 1.0
    fig.update_layout(
        title=title, barmode="stack", height=max(320, 28 * len(d) + 140),
        xaxis=dict(tickprefix="$", tickformat=",.2s", range=[0, span * 1.12]),
        yaxis=dict(automargin=True),
        legend=dict(orientation="h", yanchor="bottom", y=1.0, x=0),
    )
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
        number={"prefix": "$", "valueformat": ",.0f", "font": {"size": 22}},
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
    fig.update_layout(height=160, margin=dict(l=8, r=24, t=52, b=20),
                      title=dict(text=title, font=dict(size=13, color=T.MUTED),
                                 x=0, xanchor="left"))
    fig.update_traces(title=dict(text=""))   # title moved to the layout, above the bar
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

# © 2026 [Titular de derechos]. Todos los derechos reservados. / All rights reserved.
# Robertet LATAM Sales Analytics — software propietario. Ver LICENSE.
# Uso licenciado; prohibida su reproducción o distribución sin autorización escrita.
# Contacto: katyasam13@gmail.com


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


def _goodness(direction, higher_is_better) -> str:
    if direction is None or (isinstance(direction, float) and np.isnan(direction)) \
            or direction == 0:
        return "flat"
    return "up" if (direction > 0) == higher_is_better else "down"


def kpi_card(label: str, value: str, deltas: list[tuple[str, float, bool]] | None = None) -> str:
    rows = ""
    accent = "flat"
    for i, (text, direction, higher_is_better) in enumerate(deltas or []):
        good = _goodness(direction, higher_is_better)
        if i == 0:
            accent = good                              # card stripe follows the lead metric
        arrow = "▲ " if good == "up" else "▼ " if good == "down" else ""
        rows += f'<div class="rb-delta rb-{good}">{arrow}{html_escape(str(text))}</div>'
    return (
        f'<div class="rb-card rb-acc-{accent}"><div class="rb-label">{label}</div>'
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

# © 2026 [Titular de derechos]. Todos los derechos reservados. / All rights reserved.
# Robertet LATAM Sales Analytics — software propietario. Ver LICENSE.
# Uso licenciado; prohibida su reproducción o distribución sin autorización escrita.
# Contacto: katyasam13@gmail.com


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

_MODULES["core.scoring"] = r'''"""Progress score: a hybrid of sales and margin, where 100 = on budget.

Two components, each anchored at 100 when it lands exactly on budget:

    sales score  = projected sales landing ÷ sales budget × 100
    margin score = margin % achieved ÷ margin % budgeted × 100
    score        = w_sales · sales score + w_margin · margin score

The sales side answers "where is the year heading", so it is built on the
landing forecast (YTD ÷ seasonality index), not on raw attainment: 66 in August
means the year is projected to close at 66% of budget, not that 66% is booked.

The margin side is a ratio, so it needs no seasonal projection — a margin of
41% against a budgeted 47% scores 87 whatever month it is.

Splitting them matters: growing 10% by discounting shows up as a high sales
score dragged down by a low margin one, which a single number would hide. There
is no upper cap; the floor is 10 so a near-dead account still lands on the scale.
"""

# © 2026 [Titular de derechos]. Todos los derechos reservados. / All rights reserved.
# Robertet LATAM Sales Analytics — software propietario. Ver LICENSE.
# Uso licenciado; prohibida su reproducción o distribución sin autorización escrita.
# Contacto: katyasam13@gmail.com


from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
import pandas as pd

from core import metrics as MX
from core.forecast import landing_forecast, portfolio_pace

FLOOR = 10.0
LEVEL = "enterprise"
DEFAULT_WEIGHTS = (0.60, 0.40)          # sales, margin

BANDS = [
    (100.0, "on_budget"),
    (90.0, "close"),
    (75.0, "at_risk"),
    (0.0, "critical"),
]

BAND_COLOURS = {
    "on_budget": "#1F7A5A",
    "close": "#4E8C4A",
    "at_risk": "#C08A2E",
    "critical": "#B03A2E",
}


def band_of(score: float) -> str:
    if score is None or (isinstance(score, float) and np.isnan(score)):
        return "critical"
    for threshold, name in BANDS:
        if score >= threshold:
            return name
    return "critical"


def _ratio_score(value: float, target: float) -> float:
    if not target or target <= 0 or value is None or np.isnan(value):
        return float("nan")
    return max(FLOOR, 100.0 * value / target)


def blend(sales_score: float, margin_score: float,
          weights: tuple[float, float] = DEFAULT_WEIGHTS) -> float:
    """Weighted mean that degrades gracefully when one side is unavailable."""
    ws, wm = weights
    pairs = [(sales_score, ws), (margin_score, wm)]
    usable = [(s, w) for s, w in pairs if s is not None and not np.isnan(s)]
    if not usable:
        return float("nan")
    total_w = sum(w for _, w in usable)
    if total_w <= 0:
        return float("nan")
    return sum(s * w for s, w in usable) / total_w


@dataclass
class Score:
    value: float                      # blended, 100 = on budget, uncapped
    sales_score: float
    margin_score: float
    weights: tuple[float, float]
    landing: float
    budget: float
    ytd: float
    backlog: float
    margin: float                     # achieved margin %
    margin_budget: float              # budgeted margin %
    projected: bool                   # False when there is no seasonality index
    index: float = float("nan")
    band: str = "critical"
    components: dict = field(default_factory=dict)
    by_group: pd.DataFrame | None = None

    @property
    def surplus(self) -> float:
        return self.landing - self.budget

    @property
    def colour(self) -> str:
        return BAND_COLOURS[self.band]

    def material(self, min_share: float = 0.01) -> pd.DataFrame | None:
        """Groups worth naming: at least `min_share` of the total budget."""
        if self.by_group is None or self.by_group.empty:
            return self.by_group
        keep = self.by_group[self.by_group["weight"] >= min_share]
        return keep if not keep.empty else self.by_group

    @property
    def drag(self) -> str:
        """Which side is pulling the score down — the sentence writes itself."""
        s, m = self.sales_score, self.margin_score
        if np.isnan(s) or np.isnan(m):
            return "none"
        if abs(s - m) < 3:
            return "both"
        return "margin" if m < s else "sales"


def _seasonality(ctx) -> tuple[float, bool]:
    if not ctx.has_both:
        return float("nan"), False
    try:
        pace = portfolio_pace(ctx.ytd.tidy, ctx.fy.tidy,
                              ctx.current_year, ctx.current_year - 1)
        idx = pace.get("pace_index") if pace else None
        if idx and not np.isnan(idx) and idx > 0:
            return float(idx), True
    except Exception:
        pass
    return float("nan"), False


def _group_scores(ctx, index: float, projected: bool,
                  weights: tuple[float, float]) -> pd.DataFrame | None:
    """Per-group hybrid score, so the worst offenders are nameable."""
    block = ctx.slice_year(ctx.current_year)
    grouped = MX.aggregate(block, LEVEL)
    # Override the per-group budget with the **annual** budget (see Context).
    abg = ctx.annual_budget_by(LEVEL)
    if abg is not None:
        gi = grouped.set_index(LEVEL)
        for col in ("sales_bdg", "profit_bdg", "qty_bdg", "margin_bdg_pct"):
            if col in abg.columns:
                gi[col] = abg[col].reindex(gi.index)
        grouped = gi.reset_index()
    grouped = grouped[grouped["sales_bdg"].fillna(0) > 0].copy()
    if grouped.empty:
        return None

    landing_by_group = None
    if ctx.has_both:
        try:
            fc = landing_forecast(ctx.ytd.tidy, ctx.fy.tidy,
                                  ctx.current_year, ctx.current_year - 1, LEVEL)
            landing_by_group = fc["landing"]
        except Exception:
            landing_by_group = None

    grouped = grouped.set_index(LEVEL)
    invoiced = grouped["sales"].fillna(0.0)
    backlog = grouped["sales_open"].fillna(0.0)
    if landing_by_group is not None:
        landing = landing_by_group.reindex(grouped.index)
    elif projected and index > 0:
        landing = invoiced / index
    else:
        landing = invoiced
    grouped["landing"] = np.maximum(landing.fillna(invoiced), invoiced + backlog)
    grouped["budget"] = grouped["sales_bdg"]
    grouped["ytd_current"] = invoiced

    grouped["sales_score"] = [
        _ratio_score(l, b) for l, b in zip(grouped["landing"], grouped["budget"])
    ]
    grouped["margin_score"] = [
        _ratio_score(m, mb) for m, mb in zip(grouped["margin_pct"],
                                             grouped["margin_bdg_pct"])
    ]
    grouped["score"] = [
        blend(s, m, weights)
        for s, m in zip(grouped["sales_score"], grouped["margin_score"])
    ]
    grouped["band"] = grouped["score"].map(band_of)
    # USD at stake, not the score itself: a $25 budget scoring 10 is noise,
    # a $365K budget scoring 79 is the meeting.
    grouped["gap"] = grouped["landing"] - grouped["budget"]
    grouped["weight"] = grouped["budget"] / grouped["budget"].sum()
    return grouped.sort_values("gap")


def compute(ctx, weights: tuple[float, float] = DEFAULT_WEIGHTS) -> Score:
    """Score the active filter. Uses both files when available."""
    cur = MX.totals(ctx.slice_year(ctx.current_year))
    ann = ctx.annual_budget_totals()
    ytd = float(cur.get("sales") or 0.0)
    backlog = float(cur.get("sales_open") or 0.0)
    # Budget is the ANNUAL (full-year) budget — the landing is a full-year
    # projection, so it must be measured against the full-year target, never a
    # YTD / to-date budget.
    budget = float(ann.get("sales_bdg") or 0.0)
    margin = float(cur.get("margin_pct") or np.nan)
    margin_budget = float(ann.get("margin_bdg_pct") or np.nan)

    index, projected = _seasonality(ctx)
    landing = ytd / index if projected and index > 0 else ytd
    # Never project below what is already invoiced plus what is already sold.
    landing = max(landing, ytd + backlog)

    sales_score = _ratio_score(landing, budget)
    margin_score = _ratio_score(margin, margin_budget)
    value = blend(sales_score, margin_score, weights)

    components: dict[str, dict] = {}
    for key, value_col, budget_col, open_col in (
        ("sales", "sales", "sales_bdg", "sales_open"),
        ("profit", "profit", "profit_bdg", "profit_open"),
        ("quantity", "quantity", "qty_bdg", "qty_open"),
    ):
        v = float(cur.get(value_col) or 0.0)
        b = float(ann.get(budget_col) or 0.0)   # annual budget component
        o = float(cur.get(open_col) or 0.0)
        land = max(v / index if projected and index > 0 else v, v + o)
        components[key] = {
            "ytd": v, "backlog": o, "budget": b, "landing": land,
            "score": _ratio_score(land, b),
            "attainment": (v / b) if b else float("nan"),
        }
    components["margin"] = {
        "ytd": margin, "backlog": 0.0, "budget": margin_budget,
        "landing": margin, "score": margin_score,
        "attainment": margin / margin_budget if margin_budget else float("nan"),
    }

    return Score(
        value=value, sales_score=sales_score, margin_score=margin_score,
        weights=weights, landing=landing, budget=budget, ytd=ytd, backlog=backlog,
        margin=margin, margin_budget=margin_budget,
        projected=projected, index=index, band=band_of(value),
        components=components,
        by_group=_group_scores(ctx, index, projected, weights),
    )
'''

_MODULES["core.evolution"] = r'''"""Month-over-month evolution from two YTD snapshots.

The app stores nothing between sessions, so "last month" is a file the user
kept: the same YTD export downloaded a month earlier. Both snapshots are
year-to-date for the same year, so the movement *in* the latest month is their
difference:

    month(this)      = YTD_now(2026) − YTD_prev(2026)
    month(last year) = YTD_now(2025) − YTD_prev(2025)

That recovers a monthly figure without the Month column the BI cannot produce,
and — because the YTD file carries both year bands — it also yields the same
month a year ago, so a month can be judged against both its predecessor and its
year-ago self.
"""

# © 2026 [Titular de derechos]. Todos los derechos reservados. / All rights reserved.
# Robertet LATAM Sales Analytics — software propietario. Ver LICENSE.
# Uso licenciado; prohibida su reproducción o distribución sin autorización escrita.
# Contacto: katyasam13@gmail.com


from __future__ import annotations

from dataclasses import replace

import numpy as np
import pandas as pd

from core import metrics as MX, scoring

LEVEL = "enterprise"
MATCH_TOL = 0.005


def _ytd(tidy: pd.DataFrame, year: int, level: str) -> pd.DataFrame:
    block = tidy[(tidy["year"] == year) & (tidy[level] != "N/D")]
    cols = ["sales", "profit", "quantity", "sales_open", "sales_bdg"]
    cols = [c for c in cols if c in block.columns]
    agg = block.groupby(level, dropna=False)[cols].sum(min_count=1).fillna(0.0)
    return agg


def validate(now_tidy: pd.DataFrame, prev_tidy: pd.DataFrame, year: int) -> dict:
    """Guard against a swapped or mismatched pair before computing anything."""
    now_total = float(now_tidy[now_tidy["year"] == year]["sales"].fillna(0).sum())
    prev_total = float(prev_tidy[prev_tidy["year"] == year]["sales"].fillna(0).sum())
    ok_years = year in set(prev_tidy["year"].unique())
    swapped = prev_total > now_total * (1 + MATCH_TOL)
    identical = abs(now_total - prev_total) <= now_total * MATCH_TOL and now_total > 0
    return {
        "ok": ok_years and not swapped and not identical,
        "swapped": swapped, "identical": identical, "year_missing": not ok_years,
        "now_total": now_total, "prev_total": prev_total,
    }


def month_table(now_tidy: pd.DataFrame, prev_tidy: pd.DataFrame,
                current_year: int, level: str = LEVEL) -> pd.DataFrame:
    """One row per group: the month's movement, this year and a year ago."""
    prior = current_year - 1
    now_cur = _ytd(now_tidy, current_year, level)
    prev_cur = _ytd(prev_tidy, current_year, level)
    now_py = _ytd(now_tidy, prior, level)
    prev_py = _ytd(prev_tidy, prior, level)

    idx = now_cur.index.union(prev_cur.index).union(now_py.index).union(prev_py.index)
    frame = pd.DataFrame(index=idx)

    def diff(a, b, col):
        return a.reindex(idx)[col].fillna(0.0) - b.reindex(idx)[col].fillna(0.0) \
            if col in a.columns else pd.Series(0.0, index=idx)

    frame["ytd_now"] = now_cur.reindex(idx)["sales"].fillna(0.0)
    frame["ytd_prev"] = prev_cur.reindex(idx)["sales"].fillna(0.0)
    frame["month_sales"] = diff(now_cur, prev_cur, "sales")
    frame["month_profit"] = diff(now_cur, prev_cur, "profit")
    frame["month_qty"] = diff(now_cur, prev_cur, "quantity")
    frame["month_sales_py"] = diff(now_py, prev_py, "sales")
    frame["month_profit_py"] = diff(now_py, prev_py, "profit")

    # Margin of the month itself, recomputed from its own components.
    with np.errstate(divide="ignore", invalid="ignore"):
        frame["month_margin"] = np.where(frame["month_sales"] != 0,
                                         frame["month_profit"] / frame["month_sales"], np.nan)
        frame["month_margin_py"] = np.where(frame["month_sales_py"] != 0,
                                            frame["month_profit_py"] / frame["month_sales_py"],
                                            np.nan)
        frame["mom_growth"] = np.where(frame["ytd_prev"] != 0,
                                       (frame["ytd_now"] - frame["ytd_prev"]) / frame["ytd_prev"].abs(),
                                       np.nan)
        frame["yoy_month"] = np.where(frame["month_sales_py"] != 0,
                                      (frame["month_sales"] - frame["month_sales_py"])
                                      / frame["month_sales_py"].abs(), np.nan)

    frame["margin_delta_pp"] = (frame["month_margin"] - frame["month_margin_py"]) * 100
    return frame.sort_values("month_sales", ascending=False)


def totals(now_tidy: pd.DataFrame, prev_tidy: pd.DataFrame,
           current_year: int) -> dict:
    """Portfolio-level month figures."""
    tbl = month_table(now_tidy, prev_tidy, current_year, LEVEL)
    month_sales = float(tbl["month_sales"].sum())
    month_profit = float(tbl["month_profit"].sum())
    month_sales_py = float(tbl["month_sales_py"].sum())
    return {
        "month_sales": month_sales,
        "month_profit": month_profit,
        "month_margin": month_profit / month_sales if month_sales else np.nan,
        "month_sales_py": month_sales_py,
        "yoy": (month_sales - month_sales_py) / abs(month_sales_py)
        if month_sales_py else np.nan,
        "ytd_now": float(tbl["ytd_now"].sum()),
        "ytd_prev": float(tbl["ytd_prev"].sum()),
    }


def score_pair(ctx, prev_parsed) -> tuple:
    """Score this month's snapshot and last month's, for the headline verdict."""
    now_score = scoring.compute(ctx, ctx_weights(ctx))
    prev_ctx = replace(
        ctx, tidy=prev_parsed.tidy, ytd=prev_parsed,
        selected_groups=[], selected_accounts=[],
    )
    prev_score = scoring.compute(prev_ctx, ctx_weights(ctx))
    return now_score, prev_score


def ctx_weights(ctx) -> tuple[float, float]:
    import streamlit as st
    w = st.session_state.get("sc_w", int(scoring.DEFAULT_WEIGHTS[0] * 100))
    return (w / 100.0, 1 - w / 100.0)


def movers(tbl: pd.DataFrame, column: str, improving: bool, n: int = 6,
           min_abs: float = 0.0) -> pd.DataFrame:
    d = tbl[tbl[column].abs() > min_abs]
    d = d[d[column] > 0] if improving else d[d[column] < 0]
    return d.reindex(d[column].abs().sort_values(ascending=False).index).head(n)


def trend_alerts(tbl: pd.DataFrame) -> list[dict]:
    """Sign flips and margin swings — the changes a month view exists to catch."""
    alerts: list[dict] = []
    # This month positive but a year ago it was bigger — decelerating winners.
    slowing = tbl[(tbl["month_sales"] > 0) & (tbl["month_sales_py"] > 0)
                  & (tbl["month_sales"] < tbl["month_sales_py"] * 0.7)
                  & (tbl["month_sales_py"] > 5_000)]
    for name, r in slowing.sort_values("month_sales_py", ascending=False).head(3).iterrows():
        alerts.append({"kind": "slow", "name": name,
                       "now": r["month_sales"], "py": r["month_sales_py"]})
    # Margin of the month eroded hard versus the same month last year.
    eroding = tbl[(tbl["margin_delta_pp"] < -4) & (tbl["month_sales"] > 10_000)]
    for name, r in eroding.sort_values("margin_delta_pp").head(3).iterrows():
        alerts.append({"kind": "margin", "name": name,
                       "pp": r["margin_delta_pp"], "sales": r["month_sales"]})
    # Stopped buying this month but was active a year ago.
    stalled = tbl[(tbl["month_sales"] <= 0) & (tbl["month_sales_py"] > 10_000)]
    for name, r in stalled.sort_values("month_sales_py", ascending=False).head(3).iterrows():
        alerts.append({"kind": "stall", "name": name, "py": r["month_sales_py"]})
    return alerts
'''

_MODULES["core.onepager"] = r'''"""Executive one-pager: a self-contained HTML page that prints to one A4 sheet.

No JavaScript, no external assets, no chart library — every bar is hand-written
SVG. That keeps the file small, makes it render identically in any browser, and
means Ctrl+P → Save as PDF produces exactly what the screen shows.
"""

# © 2026 [Titular de derechos]. Todos los derechos reservados. / All rights reserved.
# Robertet LATAM Sales Analytics — software propietario. Ver LICENSE.
# Uso licenciado; prohibida su reproducción o distribución sin autorización escrita.
# Contacto: katyasam13@gmail.com


from __future__ import annotations

import datetime as dt
import html

import numpy as np
import pandas as pd

from core import bridges, metrics as MX, scoring, theme as T
from core.i18n import t

M = T.money_compact


def _e(text) -> str:
    return html.escape(str(text))


def _pct(v, d=0) -> str:
    return "—" if v is None or (isinstance(v, float) and np.isnan(v)) else f"{v*100:,.{d}f}%"


# --------------------------------------------------------------------------- #
# SVG pieces
# --------------------------------------------------------------------------- #
def _split(sales_score: float, margin_score: float,
           weights: tuple[float, float]) -> str:
    """The two halves of the hybrid, so the blended number is auditable."""
    def one(label, value, weight):
        if value is None or np.isnan(value):
            return (f'<div class="split"><span>{_e(label)}</span>'
                    f'<b class="flat">—</b></div>')
        colour = scoring.BAND_COLOURS[scoring.band_of(value)]
        return (f'<div class="split"><span>{_e(label)} '
                f'<i>{weight*100:.0f}%</i></span>'
                f'<b style="color:{colour}">{value:,.0f}</b></div>')
    return (one(t("sales"), sales_score, weights[0])
            + one(t("margin"), margin_score, weights[1]))


def _gauge(score: float, colour: str) -> str:
    """Semicircular gauge, 0–150 sweep so an over-budget score still fits."""
    if score is None or np.isnan(score):
        return ""
    span = 150.0
    frac = max(0.0, min(1.0, score / span))
    r, cx, cy = 62, 76, 74
    start, end = np.pi, np.pi * (1 - frac)
    x1, y1 = cx + r * np.cos(start), cy + r * np.sin(start) * -1
    x2, y2 = cx + r * np.cos(end), cy + r * np.sin(end) * -1
    large = 0          # a semicircle never needs the large-arc flag
    budget_frac = 100.0 / span
    bx = cx + r * np.cos(np.pi * (1 - budget_frac))
    by = cy + r * np.sin(np.pi * (1 - budget_frac)) * -1
    return f"""
<svg viewBox="0 0 152 92" class="gauge">
  <path d="M {cx - r} {cy} A {r} {r} 0 0 1 {cx + r} {cy}" fill="none"
        stroke="#E6EBF1" stroke-width="13" stroke-linecap="round"/>
  <path d="M {x1:.1f} {y1:.1f} A {r} {r} 0 {large} 1 {x2:.1f} {y2:.1f}" fill="none"
        stroke="{colour}" stroke-width="13" stroke-linecap="round"/>
  <line x1="{bx:.1f}" y1="{by:.1f}" x2="{cx + (r + 9) * np.cos(np.pi * (1 - budget_frac)):.1f}"
        y2="{cy + (r + 9) * np.sin(np.pi * (1 - budget_frac)) * -1:.1f}"
        stroke="{T.NAVY}" stroke-width="2"/>
  <text x="{cx}" y="{cy - 8}" text-anchor="middle" class="gauge-value"
        fill="{colour}">{score:,.0f}</text>
  <text x="{cx}" y="{cy + 8}" text-anchor="middle" class="gauge-cap">/ 100 = budget</text>
</svg>"""


def _bar(label: str, invoiced: float, backlog: float, budget: float,
         pace: float | None, fmt=M) -> str:
    """Invoiced + backlog against the budget track, with a pace tick."""
    if not budget or budget <= 0:
        return ""
    top = max(1.0, (invoiced + backlog) / budget) * 1.04
    w = 100.0 / top                      # width of one budget-unit, in %
    inv_w = max(0.0, invoiced / budget) * w
    bl_w = max(0.0, backlog / budget) * w
    tick = (pace * w) if pace and not np.isnan(pace) else None
    attain = (invoiced + backlog) / budget
    parts = (f"{_e(fmt(invoiced))} + {_e(fmt(backlog))} / {_e(fmt(budget))}"
             if backlog else f"{_e(fmt(invoiced))} / {_e(fmt(budget))}")
    return f"""
<div class="bar-row">
  <div class="bar-head"><span>{_e(label)}</span>
    <span class="bar-num">{parts} · <b>{_pct(attain)}</b></span></div>
  <div class="bar-track">
    <div class="bar-budget" style="width:{w:.2f}%"></div>
    <div class="bar-inv" style="width:{inv_w:.2f}%"></div>
    <div class="bar-bl" style="left:{inv_w:.2f}%;width:{bl_w:.2f}%"></div>
    {f'<div class="bar-tick" style="left:{tick:.2f}%"></div>' if tick else ''}
  </div>
</div>"""


def _movers(rows: pd.DataFrame, label_col: str, value_col: str, positive: bool) -> str:
    if rows.empty:
        return '<div class="empty">—</div>'
    span = float(rows[value_col].abs().max()) or 1.0
    out = []
    for _, r in rows.iterrows():
        v = float(r[value_col])
        width = abs(v) / span * 100.0
        colour = T.POSITIVE if positive else T.NEGATIVE
        out.append(
            f'<div class="mover"><span class="mover-name">{_e(r[label_col])}</span>'
            f'<span class="mover-bar"><i style="width:{width:.1f}%;'
            f'background:{colour}"></i></span>'
            f'<span class="mover-val" style="color:{colour}">{_e(T.signed(v))}</span></div>'
        )
    return "".join(out)


def _score_chips(by_group: pd.DataFrame | None, n: int = 8) -> str:
    """Ranked by dollars at stake, so immaterial accounts never top the list."""
    if by_group is None or by_group.empty:
        return '<div class="empty">—</div>'
    rows = by_group.head(n)
    out = []
    for name, r in rows.iterrows():
        colour = scoring.BAND_COLOURS[r["band"]]
        out.append(
            f'<div class="chip-row"><span class="chip-name">{_e(name)}</span>'
            f'<span class="chip" style="background:{colour}">{r["score"]:,.0f}</span>'
            f'<span class="chip-gap">{_e(T.signed(r["gap"]))}</span></div>'
        )
    return "".join(out)


# --------------------------------------------------------------------------- #
# Page
# --------------------------------------------------------------------------- #
CSS = """
@page { size: A4 landscape; margin: 8mm; }
* { box-sizing: border-box; }
body { margin:0; font-family: Inter, "Segoe UI", Helvetica, Arial, sans-serif;
       color:#1B2530; background:#fff; font-size:10.5px; }
.sheet { width:281mm; min-height:194mm; margin:0 auto; padding:0; }
header { display:flex; align-items:center; gap:14px; border-bottom:2px solid #002856;
         padding-bottom:7px; margin-bottom:9px; }
header img { height:26px; }
h1 { font-size:15px; margin:0; color:#002856; letter-spacing:-.2px; }
.sub { color:#6B7A88; font-size:9px; margin-top:1px; }
.spacer { flex:1; }
.stamp { text-align:right; color:#6B7A88; font-size:8.5px; }
.grid { display:grid; grid-template-columns: 200px 1fr; gap:10px; }
.card { border:1px solid #DDE3EA; border-radius:6px; padding:8px 10px; background:#fff; }
.card h2 { font-size:9px; text-transform:uppercase; letter-spacing:.07em;
           color:#6B7A88; margin:0 0 6px 0; font-weight:600; }
.score-card { text-align:center; }
.gauge { width:100%; height:auto; }
.gauge-value { font-size:28px; font-weight:700; }
.gauge-cap { font-size:7px; fill:#6B7A88; }
.band { font-size:11px; font-weight:700; margin-top:2px; }
.score-note { color:#6B7A88; font-size:8px; margin-top:4px; line-height:1.35; }
.splits { display:flex; gap:6px; margin-top:6px; }
.split { flex:1; border:1px solid #DDE3EA; border-radius:5px; padding:3px 5px;
         display:flex; flex-direction:column; align-items:center; }
.split span { color:#6B7A88; font-size:7.5px; }
.split span i { font-style:normal; color:#A6B2BE; }
.split b { font-size:13px; line-height:1.2; }
.kpis { display:grid; grid-template-columns: repeat(5, 1fr); gap:7px; margin-bottom:9px; }
.kpi { border:1px solid #DDE3EA; border-radius:6px; padding:6px 8px; }
.kpi .l { color:#6B7A88; font-size:7.5px; text-transform:uppercase; letter-spacing:.06em; }
.kpi .v { color:#002856; font-size:17px; font-weight:650; line-height:1.15; }
.kpi .d { font-size:8px; margin-top:1px; }
.up { color:#1F7A5A; } .down { color:#B03A2E; } .flat { color:#6B7A88; }
.bar-row { margin-bottom:7px; }
.bar-head { display:flex; justify-content:space-between; font-size:9.5px;
            margin-bottom:2px; }
.bar-head span:first-child { font-weight:600; color:#002856; }
.bar-num { color:#6B7A88; }
.bar-track { position:relative; height:15px; background:#F2F5F8; border-radius:3px; }
.bar-budget { position:absolute; height:100%; background:#E6EBF1; border-radius:3px; }
.bar-inv { position:absolute; height:100%; background:#002856; border-radius:3px 0 0 3px; }
.bar-bl { position:absolute; height:100%; background:repeating-linear-gradient(
            45deg, #2E7EB3, #2E7EB3 3px, #ffffff 3px, #ffffff 6px); }
.bar-tick { position:absolute; top:-3px; height:21px; width:2px; background:#002856; }
.cols { display:grid; grid-template-columns: 1fr 1fr 1fr; gap:10px; margin-top:9px; }
.mover { display:flex; align-items:center; gap:6px; margin-bottom:4.5px; font-size:9.5px; }
.mover-name { width:118px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap; }
.mover-bar { flex:1; height:7px; background:#F2F5F8; border-radius:2px; }
.mover-bar i { display:block; height:100%; border-radius:2px; }
.mover-val { width:58px; text-align:right; font-variant-numeric:tabular-nums; }
.chip-row { display:flex; align-items:center; gap:6px; margin-bottom:4.5px; font-size:9.5px; }
.chip-name { flex:1; overflow:hidden; text-overflow:ellipsis; white-space:nowrap; }
.chip { color:#fff; font-weight:700; border-radius:9px; padding:1px 6px; font-size:8px; }
.chip-gap { width:58px; text-align:right; color:#6B7A88;
            font-variant-numeric:tabular-nums; }
ul.bullets { margin:0; padding-left:13px; }
ul.bullets li { margin-bottom:5px; line-height:1.45; font-size:9.5px; }
.legend { display:flex; gap:12px; font-size:8px; color:#6B7A88; margin-top:5px; }
.legend i { display:inline-block; width:9px; height:9px; border-radius:2px;
            margin-right:3px; vertical-align:-1px; }
footer { margin-top:9px; border-top:1px solid #DDE3EA; padding-top:5px;
         color:#8896A4; font-size:7.5px; line-height:1.45; }
.empty { color:#8896A4; font-size:8.5px; }
@media print { .sheet { page-break-after: avoid; } }
"""


def build(ctx, bullets: dict[str, list[str]] | None = None) -> str:
    """Render the one-pager for the current filter. Returns an HTML string."""
    score = scoring.compute(ctx)
    cur = MX.totals(ctx.slice_year(ctx.current_year))
    base = MX.totals(ctx.slice_year(ctx.base_year))

    pace = score.index if score.projected else None
    level = ctx.group_level
    cmp_df = ctx.compare(level)

    # --- KPI strip ---
    def kpi(label, value, deltas):
        rows = "".join(
            f'<div class="d {cls}">{_e(txt)}</div>' for txt, cls in deltas)
        return (f'<div class="kpi"><div class="l">{_e(label)}</div>'
                f'<div class="v">{_e(value)}</div>{rows}</div>')

    def delta(cur_v, base_v, fmt=M, pp=False):
        if base_v in (None, 0) or (isinstance(base_v, float) and np.isnan(base_v)):
            return ("—", "flat")
        d = cur_v - base_v
        cls = "up" if d >= 0 else "down"
        if pp:
            return (f"{d*100:+.1f} pp vs {ctx.base_year}", cls)
        rel = d / abs(base_v)
        return (f"{T.signed(d, fmt)} ({rel*100:+.1f}%) vs {ctx.base_year}", cls)

    kpis = "".join([
        kpi(t("sales"), M(cur.get("sales")), [delta(cur.get("sales"), base.get("sales"))]),
        kpi(t("profit"), M(cur.get("profit")), [delta(cur.get("profit"), base.get("profit"))]),
        kpi(t("margin"), _pct(cur.get("margin_pct"), 1),
            [delta(cur.get("margin_pct"), base.get("margin_pct"), pp=True)]),
        kpi(t("volume"), T.qty(cur.get("quantity"), ctx.unit),
            [delta(cur.get("quantity"), base.get("quantity"),
                   fmt=lambda v: T.qty(v, ctx.unit))]),
        kpi(t("open_orders"), M(cur.get("sales_open")),
            [(f'{t("landing")}: {M(score.landing)}', "flat")]),
    ])

    # --- bars ---
    c = score.components
    bars = "".join([
        _bar(t("sales"), c["sales"]["ytd"], c["sales"]["backlog"],
             c["sales"]["budget"], pace),
        _bar(t("profit"), c["profit"]["ytd"], c["profit"]["backlog"],
             c["profit"]["budget"], pace),
        _bar(t("volume"), c["quantity"]["ytd"], c["quantity"]["backlog"],
             c["quantity"]["budget"], pace, fmt=lambda v: T.qty(v, ctx.unit)),
        _bar(t("margin"), c["margin"]["ytd"], 0.0, c["margin"]["budget"], None,
             fmt=lambda v: _pct(v, 1)),
    ])

    # --- movers ---
    movers = cmp_df.reindex(
        cmp_df["sales_delta"].abs().sort_values(ascending=False).index)
    ups = movers[movers["sales_delta"] > 0].head(8)
    downs = movers[movers["sales_delta"] < 0].head(8)

    # --- bridge one-liner ---
    sb = bridges.sales_bridge(ctx.tidy, ctx.current_year, ctx.base_year)
    vol_e, price_e = sb["steps"].get("volume", 0.0), sb["steps"].get("price", 0.0)

    # --- bullets ---
    items: list[str] = []
    for key in ("diagnostico", "riesgos", "acciones"):
        for b in (bullets or {}).get(key, [])[:2]:
            items.append(b)
    bullet_html = "".join(f"<li>{_md(b)}</li>" for b in items[:6]) or "<li>—</li>"

    band_label = {
        "on_budget": t("sc_band_on"), "close": t("sc_band_close"),
        "at_risk": t("sc_band_risk"), "critical": t("sc_band_critical"),
    }[score.band]

    logo = T.logo_data_uri()
    stamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M")
    scope = ", ".join(ctx.selected_groups) if ctx.selected_groups else t("sc_all_portfolio")

    drag_txt = {
        "sales": t("sc_drag_sales"), "margin": t("sc_drag_margin"),
        "both": t("sc_drag_both"), "none": "",
    }[score.drag]
    surplus_txt = (t("sc_surplus", v=M(abs(score.surplus)))
                   if score.surplus >= 0 else t("sc_shortfall", v=M(abs(score.surplus))))
    method = (t("sc_method_projected", index=_pct(score.index))
              if score.projected else t("sc_method_raw"))

    return f"""<!doctype html>
<html lang="{'es' if ctx.lang == 'es' else 'en'}">
<head><meta charset="utf-8"><title>{_e(t('op_title'))} · {ctx.current_year}</title>
<style>{CSS}</style></head>
<body><div class="sheet">
<header>
  {f'<img src="{logo}" alt="Robertet"/>' if logo else ''}
  <div><h1>{_e(t('op_title'))} · {ctx.current_year} vs {ctx.base_year}</h1>
    <div class="sub">{_e(scope)} · {_e(ctx.label_for(level))}</div></div>
  <div class="spacer"></div>
  <div class="stamp">{_e(t('op_generated'))} {stamp}<br/>{_e(t('op_confidential'))}</div>
</header>

<div class="grid">
  <div class="card score-card">
    <h2>{_e(t('sc_title'))}</h2>
    {_gauge(score.value, score.colour)}
    <div class="band" style="color:{score.colour}">{_e(band_label)}</div>
    <div class="splits">{_split(score.sales_score, score.margin_score, score.weights)}</div>
    <div class="score-note">{_e(drag_txt)}<br/>{_e(surplus_txt)}<br/>{_e(method)}</div>
  </div>
  <div>
    <div class="kpis">{kpis}</div>
    <div class="card">
      <h2>{_e(t('op_vs_budget'))}</h2>
      {bars}
      <div class="legend">
        <span><i style="background:#002856"></i>{_e(t('invoiced'))}</span>
        <span><i style="background:repeating-linear-gradient(45deg,#2E7EB3,#2E7EB3 3px,#fff 3px,#fff 6px)"></i>{_e(t('open_orders'))}</span>
        <span><i style="background:#E6EBF1"></i>{_e(t('budget'))}</span>
        {f'<span><i style="background:#002856;width:2px"></i>{_e(t("ov_pace_sub"))}</span>' if pace else ''}
      </div>
    </div>
  </div>
</div>

<div class="cols">
  <div class="card"><h2>{_e(t('op_up'))}</h2>{_movers(ups, level, 'sales_delta', True)}</div>
  <div class="card"><h2>{_e(t('op_down'))}</h2>{_movers(downs, level, 'sales_delta', False)}</div>
  <div class="card"><h2>{_e(t('op_worst_scores'))}</h2>{_score_chips(score.material())}</div>
</div>

<div class="cols" style="grid-template-columns: 1fr 1fr;">
  <div class="card"><h2>{_e(t('op_why'))}</h2>
    <ul class="bullets">
      <li>{_e(t('op_bridge', volume=T.signed(vol_e), price=T.signed(price_e)))}</li>
      <li>{_e(t('op_backlog_line', open=M(score.backlog),
                land=M(score.landing), bdg=M(score.budget)))}</li>
    </ul>
  </div>
  <div class="card"><h2>{_e(t('op_actions'))}</h2>
    <ul class="bullets">{bullet_html}</ul></div>
</div>

<footer>{_e(t('op_footer', ytd=ctx.ytd.filename if ctx.ytd else '—',
                fy=ctx.fy.filename if ctx.fy else '—'))}</footer>
</div></body></html>"""


def _md(text: str) -> str:
    """Minimal **bold** support inside bullets, everything else escaped."""
    safe = html.escape(str(text))
    parts = safe.split("**")
    return "".join(p if i % 2 == 0 else f"<b>{p}</b>" for i, p in enumerate(parts))
'''

_MODULES["core.session"] = r'''"""Ephemeral session state.

Design rule, non-negotiable: nothing this module holds ever reaches disk.
Uploads are consumed as bytes from memory, parsed into dataframes held only in
`st.session_state`, and dropped when the browser tab closes, when the idle
timer expires, or when the user hits "Clear everything".
"""

# © 2026 [Titular de derechos]. Todos los derechos reservados. / All rights reserved.
# Robertet LATAM Sales Analytics — software propietario. Ver LICENSE.
# Uso licenciado; prohibida su reproducción o distribución sin autorización escrita.
# Contacto: katyasam13@gmail.com


from __future__ import annotations

import gc
import time

import streamlit as st

# NOTE: uploader_epoch is deliberately NOT here — it is a widget-remount counter,
# not data. Wiping it to None would break the `+ 1` below.
DATA_KEYS = ("ytd", "fy", "prev", "ytd_name", "fy_name", "prev_name",
             "diagnosis")
DEFAULT_IDLE_MINUTES = 30


def init() -> None:
    st.session_state.setdefault("lang", "es")
    st.session_state.setdefault("ytd", None)
    st.session_state.setdefault("fy", None)
    st.session_state.setdefault("ytd_name", None)
    st.session_state.setdefault("fy_name", None)
    st.session_state.setdefault("prev", None)
    st.session_state.setdefault("prev_name", None)
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
    return (st.session_state.get("ytd") is not None
            or st.session_state.get("fy") is not None)


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
    st.session_state["uploader_epoch"] = (st.session_state.get("uploader_epoch") or 0) + 1
    st.session_state["confirm_clear"] = False

    try:
        st.cache_data.clear()
    except Exception:
        pass
    gc.collect()
    touch()
'''

_MODULES["core.context"] = r'''"""Sidebar state + the filtered slice every view reads from."""

# © 2026 [Titular de derechos]. Todos los derechos reservados. / All rights reserved.
# Robertet LATAM Sales Analytics — software propietario. Ver LICENSE.
# Uso licenciado; prohibida su reproducción o distribución sin autorización escrita.
# Contacto: katyasam13@gmail.com


from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
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
    selected_families: list[str] = field(default_factory=list)
    prev: object | None = None
    full: pd.DataFrame | None = None   # effective unfiltered frame (see below)
    budget_from_fy: bool = False       # reserved

    @property
    def has_both(self) -> bool:
        return self.ytd is not None and self.fy is not None

    # ---------------------------------------------------------------- budget --
    # The **annual** (full-year) budget is the figure the year is measured
    # against — the overview's attainment and the score's landing both compare to
    # it. Between the two uploaded files, the annual budget is the *larger*
    # current-year budget total: a YTD / to-date budget is always a fraction of
    # the annual, never more. Sourcing it this way is independent of which file
    # sits in which slot, so it stays correct however the user loads them. Only
    # the budget columns are taken from here; sales, profit and volume always
    # stay on the active file the user selected.
    def _annual_parsed(self):
        """The file that carries the ANNUAL (full-year) budget.

        Preference is the **Full Year** file, as the budget is a full-year target.
        The one guard: a budget can never be *partial* — if the other file's
        current-year budget total is materially larger, then the Full Year slot
        holds a partial/YTD budget and the larger one is the true annual figure,
        so that file is used instead (and the on-screen source label makes the
        choice visible)."""
        totals = {}
        for name, parsed in (("fy", self.fy), ("ytd", self.ytd)):
            if parsed is None or "sales_bdg" not in parsed.tidy:
                continue
            totals[name] = (parsed, float(
                parsed.tidy.loc[parsed.tidy["year"] == self.current_year,
                                "sales_bdg"].fillna(0).sum()))
        if not totals:
            return None
        fy = totals.get("fy")
        best = max(totals.values(), key=lambda pv: pv[1])
        # Use the Full Year file unless its budget is materially below the annual.
        if fy is not None and fy[1] > 0 and best[1] <= fy[1] * 1.01:
            return fy[0]
        return best[0]

    def annual_budget_source_name(self) -> str:
        parsed = self._annual_parsed()
        return getattr(parsed, "filename", "") or "—"

    def _annual_frame(self) -> pd.DataFrame | None:
        parsed = self._annual_parsed()
        if parsed is None:
            return None
        df = parsed.tidy[parsed.tidy["year"] == self.current_year]
        if self.selected_groups:
            df = df[df["enterprise"].isin(self.selected_groups)]
        if self.selected_accounts:
            df = df[df["customer"].isin(self.selected_accounts) | df["is_group_row"]]
        if self.selected_families:
            df = df[df["product_family"].isin(self.selected_families)]
        return df

    def annual_budget_totals(self) -> dict:
        df = self._annual_frame()
        if df is None or df.empty:
            return {"sales_bdg": 0.0, "profit_bdg": 0.0, "qty_bdg": 0.0,
                    "margin_bdg_pct": float("nan")}
        s = float(df["sales_bdg"].fillna(0).sum())
        pr = float(df["profit_bdg"].fillna(0).sum())
        q = float(df["qty_bdg"].fillna(0).sum())
        return {"sales_bdg": s, "profit_bdg": pr, "qty_bdg": q,
                "margin_bdg_pct": (pr / s) if s else float("nan")}

    def annual_budget_by(self, level: str) -> pd.DataFrame | None:
        df = self._annual_frame()
        if df is None or df.empty or level not in df.columns:
            return None
        g = df.groupby(level, dropna=False)[["sales_bdg", "profit_bdg", "qty_bdg"]] \
            .sum(min_count=1)
        g["margin_bdg_pct"] = g["profit_bdg"] / g["sales_bdg"].replace(0, np.nan)
        return g

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
        else:
            df = self._apply_annual_budget(df, level)
        return MX.apply_materiality(df, self.materiality)

    def _apply_annual_budget(self, df: pd.DataFrame, level: str) -> pd.DataFrame:
        """Replace the active file's current-year budget with the annual budget
        and re-derive everything that hangs off it, so every budget comparison
        (gap, attainment, budgeted margin) is against the full-year target."""
        abg = self.annual_budget_by(level)
        if abg is None or level not in df.columns:
            return df
        m = abg.reindex(df[level].values)
        for src_col, dst_col in (("sales_bdg", "sales_bdg_cur"),
                                 ("profit_bdg", "profit_bdg_cur"),
                                 ("qty_bdg", "qty_bdg_cur")):
            if dst_col in df.columns:
                df[dst_col] = m[src_col].to_numpy()
        if "sales_bdg_cur" in df.columns:
            df["sales_vs_bdg"] = df["sales_cur"] - df["sales_bdg_cur"]
            df["sales_bdg_attain"] = np.where(df["sales_bdg_cur"] != 0,
                                              df["sales_cur"] / df["sales_bdg_cur"], np.nan)
        if "profit_bdg_cur" in df.columns:
            df["profit_vs_bdg"] = df["profit_cur"] - df["profit_bdg_cur"]
        if {"profit_bdg_cur", "sales_bdg_cur"} <= set(df.columns):
            df["margin_bdg_pct"] = np.where(df["sales_bdg_cur"] != 0,
                                            df["profit_bdg_cur"] / df["sales_bdg_cur"], np.nan)
        return df

    def unfiltered(self):
        """The effective full tidy frame, ignoring the sidebar filters.

        The client sheet needs the whole portfolio to rank a client inside it.
        Uses the same current-year-from-FY overlay as the filtered frame so the
        client sheet shows the annual budget and the complete backlog too.
        """
        if self.full is not None:
            return self.full
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
        help=t("data_source_help"),
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

    # NOTE: the current-year budget already lives in each file's own current-year
    # band. In the real exports the YTD file carries the full **annual** budget
    # (e.g. 2026 budget 2.10M vs 1.39M YTD sales → 66%). The multi-year Full Year
    # export ships a *partial* budget for the open year, so pulling budget from it
    # inflates attainment. We therefore keep each file's own budget and never swap.
    used_fy = False

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
    full_effective = tidy_all      # unfiltered active-source frame
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
        selected_families=sel_families,
        prev=st.session_state.get("prev"),
        full=full_effective, budget_from_fy=used_fy,
    )
'''

_MODULES["views.evolution"] = r'''"""Tab — Monthly evolution: this month's YTD snapshot vs last month's."""

# © 2026 [Titular de derechos]. Todos los derechos reservados. / All rights reserved.
# Robertet LATAM Sales Analytics — software propietario. Ver LICENSE.
# Uso licenciado; prohibida su reproducción o distribución sin autorización escrita.
# Contacto: katyasam13@gmail.com


from __future__ import annotations

import numpy as np
import pandas as pd
import streamlit as st

from core import charts, evolution, scoring, theme as T, ui
from core.i18n import t

LEVEL = "enterprise"


def render(ctx) -> None:
    st.markdown(f"### {t('ev_title')}")
    ui.note(t("ev_note"))

    prev = st.session_state.get("prev")
    if prev is None:
        st.info(t("ev_need_prev"))
        with st.expander(t("ev_how")):
            st.markdown(t("ev_how_body"))
        return

    year = ctx.current_year
    check = evolution.validate(ctx.ytd.tidy, prev.tidy, year)
    if not check["ok"]:
        if check["year_missing"]:
            st.error(t("ev_err_year", year=year), icon="⚠️")
        elif check["swapped"]:
            st.error(t("ev_err_swapped",
                       now=T.money_compact(check["now_total"]),
                       prev=T.money_compact(check["prev_total"])), icon="⚠️")
        elif check["identical"]:
            st.warning(t("ev_err_same"), icon="⚠️")
        return

    tbl = evolution.month_table(ctx.ytd.tidy, prev.tidy, year, LEVEL)
    tot = evolution.totals(ctx.ytd.tidy, prev.tidy, year)
    now_score, prev_score = evolution.score_pair(ctx, prev)

    # --- verdict ------------------------------------------------------------
    ds = now_score.value - prev_score.value
    verdict = (t("ev_improving") if ds > 1 else
               t("ev_declining") if ds < -1 else t("ev_stable"))
    k1, k2, k3, k4 = st.columns(4)
    k1.markdown(ui.kpi_card(
        t("ev_verdict"), f"{prev_score.value:,.0f} → {now_score.value:,.0f}",
        [(f"{verdict} ({ds:+.0f})", ds, True)]), unsafe_allow_html=True)
    k2.markdown(ui.kpi_card(
        t("ev_month_sales"), T.money_compact(tot["month_sales"]),
        [(t("ev_vs_year_ago", v=T.pct(tot["yoy"], 0)), tot["yoy"], True)]),
        unsafe_allow_html=True)
    k3.markdown(ui.kpi_card(
        t("ev_month_margin"), T.pct(tot["month_margin"], 1),
        [(t("ev_month_profit", v=T.money_compact(tot["month_profit"])),
          tot["month_profit"], True)]), unsafe_allow_html=True)
    k4.markdown(ui.kpi_card(
        t("ev_landing_move"), T.money_compact(now_score.landing),
        [(t("ev_landing_delta", v=T.signed(now_score.landing - prev_score.landing)),
          now_score.landing - prev_score.landing, True)]), unsafe_allow_html=True)

    drivers = []
    if abs(now_score.sales_score - prev_score.sales_score) > 0.5:
        drivers.append(t("ev_drv_sales",
                         v=f"{prev_score.sales_score:,.0f}→{now_score.sales_score:,.0f}"))
    if abs(now_score.margin_score - prev_score.margin_score) > 0.5:
        drivers.append(t("ev_drv_margin",
                         v=f"{prev_score.margin_score:,.0f}→{now_score.margin_score:,.0f}"))
    if drivers:
        ui.note(" · ".join(drivers))

    st.divider()

    # --- improved vs worsened ------------------------------------------------
    st.markdown(f"#### {t('ev_movers')}")
    up = evolution.movers(tbl, "month_sales", improving=True, n=ctx.top_n)
    down = evolution.movers(tbl, "month_sales", improving=False, n=ctx.top_n)
    left, right = st.columns(2)
    with left:
        st.plotly_chart(
            charts.diverging_bars(up.reset_index(), LEVEL, "month_sales",
                                  t("ev_accelerating"), top_n=ctx.top_n),
            width="stretch", key="ev_up")
    with right:
        st.plotly_chart(
            charts.diverging_bars(down.reset_index(), LEVEL, "month_sales",
                                  t("ev_slowing"), top_n=ctx.top_n),
            width="stretch", key="ev_down")

    # --- month vs same month last year --------------------------------------
    comp = tbl[(tbl["month_sales"].abs() > 0) | (tbl["month_sales_py"].abs() > 0)].copy()
    comp = comp.reindex(comp["month_sales"].abs().sort_values(ascending=False).index)
    comp = comp.head(ctx.top_n).reset_index()
    fig = charts.grouped_bars(
        comp, LEVEL, {"month_sales_py": t("ev_month_year_ago"),
                      "month_sales": t("ev_month_this")},
        t("ev_vs_year_chart"), top_n=ctx.top_n)
    st.plotly_chart(fig, width="stretch", key="ev_yoy")
    ui.note(t("ev_yoy_note", now=T.money_compact(tot["month_sales"]),
              py=T.money_compact(tot["month_sales_py"]), yoy=T.pct(tot["yoy"], 0)))

    # --- trend alerts --------------------------------------------------------
    alerts = evolution.trend_alerts(tbl)
    if alerts:
        st.markdown(f"#### {t('ev_alerts')}")
        M = T.money_compact
        for a in alerts:
            if a["kind"] == "slow":
                st.markdown("- " + ui.md_escape(t(
                    "ev_alert_slow", name=a["name"], now=M(a["now"]), py=M(a["py"]))))
            elif a["kind"] == "margin":
                st.markdown("- " + ui.md_escape(t(
                    "ev_alert_margin", name=a["name"],
                    pp=f"{a['pp']:+.1f} pp", sales=M(a["sales"]))))
            elif a["kind"] == "stall":
                st.markdown("- " + ui.md_escape(t(
                    "ev_alert_stall", name=a["name"], py=M(a["py"]))))

    st.divider()

    # --- detail table --------------------------------------------------------
    st.markdown(f"#### {t('ev_detail')}")
    show = tbl.reset_index()
    show = show[[LEVEL, "month_sales", "month_sales_py", "yoy_month",
                 "month_margin", "margin_delta_pp", "ytd_prev", "ytd_now", "mom_growth"]]
    show.columns = [ctx.label_for(LEVEL), t("ev_col_month"), t("ev_col_month_py"),
                    t("ev_col_yoy"), t("ev_col_margin"), t("ev_col_margin_pp"),
                    t("ev_col_ytd_prev"), t("ev_col_ytd_now"), t("ev_col_mom")]
    st.dataframe(
        ui.style_table(
            show,
            money_cols=[t("ev_col_month"), t("ev_col_month_py"),
                        t("ev_col_ytd_prev"), t("ev_col_ytd_now")],
            pct_cols=[t("ev_col_yoy"), t("ev_col_margin"), t("ev_col_mom")],
            pp_cols=[t("ev_col_margin_pp")],
            highlight=[t("ev_col_month"), t("ev_col_margin_pp")]),
        width="stretch", height=420)
    ui.download_button(t("download_table"), {"Evolution": show},
                       f"evolucion_{year}.xlsx", key="dl_evolution")
'''

_MODULES["views.overview"] = r'''"""Tab 1 — Executive overview: KPIs, budget progress, bridges, landing."""

# © 2026 [Titular de derechos]. Todos los derechos reservados. / All rights reserved.
# Robertet LATAM Sales Analytics — software propietario. Ver LICENSE.
# Uso licenciado; prohibida su reproducción o distribución sin autorización escrita.
# Contacto: katyasam13@gmail.com


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
    ann = ctx.annual_budget_totals()   # annual (full-year) budget for the bars
    # Keep the invoiced-only figures: the budget bars always split invoiced from
    # backlog, whatever the sidebar toggle does to the KPI cards.
    invoiced = float(cur.get("sales") or 0)
    invoiced_profit = float(cur.get("profit") or 0)
    invoiced_qty = float(cur.get("quantity") or 0)
    open_sales = float(cur.get("sales_open") or 0)
    open_profit = float(cur.get("profit_open") or 0)
    open_qty = float(cur.get("qty_open") or 0)
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
    # Fold the standalone open-orders figure into the KPI row (with its budget-gap
    # coverage) instead of a lonely card on its own line further down.
    _budget = float(ann.get("sales_bdg") or 0)
    if open_sales and "sales_open" not in ctx.active_metrics:
        _gap = _budget - invoiced
        _cover = open_sales / _gap if _gap > 0 else np.nan
        cards.append(ui.kpi_card(
            t("open_orders"), T.money_compact(open_sales),
            [(t("ov_backlog_delta", pct=T.pct(_cover, 0),
                gap=T.money_compact(max(_gap, 0))),
              _cover if _cover == _cover else None, True)]))
    # Keep up to 6 on a single row; only wrap when there are genuinely more.
    per_row = len(cards) if len(cards) <= 6 else (len(cards) + 1) // 2
    for i in range(0, len(cards), per_row):
        ui.kpi_row(cards[i:i + per_row])

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

    budget = float(ann.get("sales_bdg") or 0)
    left, right = st.columns(2)
    with left:
        st.plotly_chart(
            charts.progress_bar(
                invoiced, budget, pace=pace_share, backlog=open_sales,
                title=t("ov_sales_bar"),
                subtitle=t("ov_pace_sub") if pace else "",
            ),
            width="stretch", key="overview_1")
        st.plotly_chart(
            charts.progress_bar(invoiced_profit, float(ann.get("profit_bdg") or 0),
                                pace=pace_share, backlog=open_profit,
                                title=t("ov_profit_bar")),
            width="stretch", key="overview_2")
    with right:
        st.plotly_chart(
            charts.progress_bar(invoiced_qty, float(ann.get("qty_bdg") or 0),
                                pace=pace_share, backlog=open_qty,
                                title=t("ov_qty_bar"),
                                formatter=lambda v: T.qty(v, ctx.unit)),
            width="stretch", key="overview_3")
        open_orders = open_sales
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

    # --- invoiced + backlog vs budget, group by group -----------------------
    cmp_df = ctx.compare()
    if "sales_open_cur" in cmp_df.columns and cmp_df["sales_open_cur"].abs().sum() > 0:
        st.plotly_chart(
            charts.budget_stack(
                cmp_df, ctx.group_level, "sales_cur", "sales_open_cur", "sales_bdg_cur",
                t("ov_stack", level=ctx.label_for(ctx.group_level).lower()),
                top_n=ctx.top_n,
            ),
            width="stretch", key="overview_8")
        covered = int(((cmp_df["sales_cur"].fillna(0) + cmp_df["sales_open_cur"].fillna(0))
                       >= cmp_df.get("sales_bdg_cur", 0).fillna(0)).sum()) \
            if "sales_bdg_cur" in cmp_df.columns else 0
        ui.note(t("ov_stack_note", open=T.money_compact(open_orders),
                  so=T.money_compact(invoiced + open_orders),
                  n=covered, level=ctx.label_for(ctx.group_level).lower()))

    # --- budget gap by group ------------------------------------------------
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

# © 2026 [Titular de derechos]. Todos los derechos reservados. / All rights reserved.
# Robertet LATAM Sales Analytics — software propietario. Ver LICENSE.
# Uso licenciado; prohibida su reproducción o distribución sin autorización escrita.
# Contacto: katyasam13@gmail.com


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
                charts.progress_bar(invoiced, budget, backlog=open_sales,
                                    title=t("ov_sales_bar")),
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

    if "sales_open_cur" in prod.columns and prod["sales_open_cur"].abs().sum() > 0:
        st.plotly_chart(
            charts.budget_stack(prod, "product_family", "sales_cur", "sales_open_cur",
                                "sales_bdg_cur", t("cl_stack"), top_n=ctx.top_n),
            width="stretch", key="cl_stack")

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

# © 2026 [Titular de derechos]. Todos los derechos reservados. / All rights reserved.
# Robertet LATAM Sales Analytics — software propietario. Ver LICENSE.
# Uso licenciado; prohibida su reproducción o distribución sin autorización escrita.
# Contacto: katyasam13@gmail.com


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

# © 2026 [Titular de derechos]. Todos los derechos reservados. / All rights reserved.
# Robertet LATAM Sales Analytics — software propietario. Ver LICENSE.
# Uso licenciado; prohibida su reproducción o distribución sin autorización escrita.
# Contacto: katyasam13@gmail.com


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

    prior_for_intro = ctx.current_year - 1
    st.markdown(f"### {t('tab_fy')}")
    ui.note(t("fy_intro", cur=ctx.current_year, prior=prior_for_intro))
    st.divider()

    fy_years = ctx.fy.substantive_years
    st.markdown(f"#### {t('fy_trend')}")
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

# © 2026 [Titular de derechos]. Todos los derechos reservados. / All rights reserved.
# Robertet LATAM Sales Analytics — software propietario. Ver LICENSE.
# Uso licenciado; prohibida su reproducción o distribución sin autorización escrita.
# Contacto: katyasam13@gmail.com


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

# © 2026 [Titular de derechos]. Todos los derechos reservados. / All rights reserved.
# Robertet LATAM Sales Analytics — software propietario. Ver LICENSE.
# Uso licenciado; prohibida su reproducción o distribución sin autorización escrita.
# Contacto: katyasam13@gmail.com


from __future__ import annotations

import numpy as np
import pandas as pd
import streamlit as st

from core import charts, metrics as MX, theme as T, ui
from core.i18n import t


# Stable classification keys (never translated) so a live language switch never
# invalidates the type filter's stored selection.
TYPE_KEYS = ["churn", "new", "volume", "price", "cost"]


def _type_label(key: str) -> str:
    return {"churn": t("type_churn"), "new": t("type_new"),
            "volume": t("type_volume"), "price": t("type_price"),
            "cost": t("type_cost")}.get(key, key)


def _classify(row: pd.Series) -> str:
    if row["status"] == "perdido":
        return "churn"
    if row["status"] == "nuevo":
        return "new"
    q0, q1 = row.get("quantity_base", 0), row.get("quantity_cur", 0)
    p0, p1 = row.get("price_base", np.nan), row.get("price_cur", np.nan)
    c0, c1 = row.get("unit_cost_base", np.nan), row.get("unit_cost_cur", np.nan)
    vol_effect = (q1 - q0) * (p0 if p0 == p0 else 0)
    price_effect = ((p1 - p0) * q1) if (p0 == p0 and p1 == p1) else 0.0
    cost_effect = (-(c1 - c0) * q1) if (c0 == c0 and c1 == c1) else 0.0
    ranked = {"volume": abs(vol_effect), "price": abs(price_effect),
              "cost": abs(cost_effect)}
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
    tipos = [k for k in TYPE_KEYS if k in set(df["tipo"])]
    sel = c1.multiselect(t("dev_type"), tipos, default=tipos, key="dev_tipo",
                         format_func=_type_label)
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
    by_type.index = [_type_label(k) for k in by_type.index]
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
    if "tipo" in table.columns:
        table["tipo"] = table["tipo"].map(_type_label)
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

# © 2026 [Titular de derechos]. Todos los derechos reservados. / All rights reserved.
# Robertet LATAM Sales Analytics — software propietario. Ver LICENSE.
# Uso licenciado; prohibida su reproducción o distribución sin autorización escrita.
# Contacto: katyasam13@gmail.com


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

_MODULES["views.onepager"] = r'''"""Tab — Executive score and one-page export."""

# © 2026 [Titular de derechos]. Todos los derechos reservados. / All rights reserved.
# Robertet LATAM Sales Analytics — software propietario. Ver LICENSE.
# Uso licenciado; prohibida su reproducción o distribución sin autorización escrita.
# Contacto: katyasam13@gmail.com


from __future__ import annotations

import datetime as dt

import numpy as np
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

from core import bridges, charts, insights, metrics as MX, onepager, scoring, theme as T, ui
from core.forecast import landing_forecast, portfolio_pace
from core.i18n import t


def _band_label(band: str) -> str:
    return {"on_budget": t("sc_band_on"), "close": t("sc_band_close"),
            "at_risk": t("sc_band_risk"), "critical": t("sc_band_critical")}[band]


def _bullets(ctx) -> dict[str, list[str]]:
    level = ctx.group_level if ctx.group_level in ("enterprise", "customer") else "enterprise"
    cmp_cust = ctx.compare(level)
    cmp_prod = ctx.compare("product_family")
    if cmp_cust.empty:
        return {}
    sb = bridges.sales_bridge(ctx.tidy, ctx.current_year, ctx.base_year)
    mb = bridges.margin_bridge(ctx.tidy, ctx.current_year, ctx.base_year)
    pace = forecast = None
    if ctx.has_both:
        try:
            prior = ctx.current_year - 1
            pace = portfolio_pace(ctx.ytd.tidy, ctx.fy.tidy, ctx.current_year, prior)
            forecast = landing_forecast(ctx.ytd.tidy, ctx.fy.tidy,
                                        ctx.current_year, prior, "enterprise")
        except Exception:
            pace = forecast = None
    return insights.build_all(cmp_cust, cmp_prod, sb, mb, pace, forecast, level)


def render(ctx) -> None:
    st.markdown(f"### {t('op_tab_title')}")
    ui.note(t("op_note"))

    c1, c2, _ = st.columns([1, 1, 2])
    w_sales = c1.slider(t("sc_weight_sales"), 0, 100,
                        int(scoring.DEFAULT_WEIGHTS[0] * 100), step=5,
                        key="sc_w", help=t("sc_weight_help"))
    weights = (w_sales / 100.0, 1 - w_sales / 100.0)
    c2.metric(t("sc_weight_margin"), f"{100 - w_sales}%")

    score = scoring.compute(ctx, weights)
    if np.isnan(score.value):
        st.info(t("sc_no_budget"))
        return

    # --- headline ------------------------------------------------------------
    k1, k2, k3, k4 = st.columns(4)
    k1.markdown(ui.kpi_card(
        t("sc_title"), f"{score.value:,.0f}",
        [(_band_label(score.band), score.value - 100, True)]), unsafe_allow_html=True)
    k2.markdown(ui.kpi_card(
        t("sc_sales_score"), f"{score.sales_score:,.0f}"
        if not np.isnan(score.sales_score) else "—",
        [(t("sc_landing_vs", land=T.money_compact(score.landing),
            bdg=T.money_compact(score.budget)),
          score.sales_score - 100 if not np.isnan(score.sales_score) else None, True)]),
        unsafe_allow_html=True)
    k3.markdown(ui.kpi_card(
        t("sc_margin_score"), f"{score.margin_score:,.0f}"
        if not np.isnan(score.margin_score) else "—",
        [(t("sc_margin_vs", cur=T.pct(score.margin, 1),
            bdg=T.pct(score.margin_budget, 1)),
          score.margin_score - 100 if not np.isnan(score.margin_score) else None, True)]),
        unsafe_allow_html=True)
    k4.markdown(ui.kpi_card(
        t("landing"), T.money_compact(score.landing),
        [(t("sc_surplus", v=T.money_compact(abs(score.surplus))) if score.surplus >= 0
          else t("sc_shortfall", v=T.money_compact(abs(score.surplus))),
          score.surplus, True)]), unsafe_allow_html=True)

    drag = {"sales": t("sc_drag_sales"), "margin": t("sc_drag_margin"),
            "both": t("sc_drag_both"), "none": ""}[score.drag]
    method = (t("sc_method_projected", index=T.pct(score.index, 0))
              if score.projected else t("sc_method_raw"))
    ui.note(f"{drag} {method}")
    st.caption(t("sc_budget_src", total=T.money_compact(score.budget),
                 file=ctx.annual_budget_source_name()))

    # --- score distribution --------------------------------------------------
    material = score.material()
    if material is not None and not material.empty:
        frame = material.reset_index()
        level_col = frame.columns[0]
        st.plotly_chart(
            charts.diverging_bars(
                frame.assign(delta=frame["score"] - 100), level_col, "delta",
                t("sc_chart", level=ctx.label_for("enterprise").lower()),
                top_n=ctx.top_n),
            width="stretch", key="op_scores")
        ui.note(t("sc_chart_note") + " " + t("sc_material_note"))

        table = frame[[level_col, "score", "sales_score", "margin_score",
                       "ytd_current", "landing", "budget", "gap",
                       "margin_pct", "margin_bdg_pct"]].copy()
        table.columns = [ctx.label_for("enterprise"), t("sc_title"),
                         t("sc_sales_score"), t("sc_margin_score"),
                         f"YTD {ctx.current_year}", t("landing"), t("budget"),
                         f'Δ {t("budget")}', t("margin"),
                         f'{t("margin")} {t("budget")}']
        st.dataframe(
            ui.style_table(
                table,
                money_cols=[f"YTD {ctx.current_year}", t("landing"), t("budget"),
                            f'Δ {t("budget")}'],
                pct_cols=[t("margin"), f'{t("margin")} {t("budget")}'],
                highlight=[t("sc_title"), f'Δ {t("budget")}']),
            width="stretch", height=340)

    st.divider()

    # --- one-pager -----------------------------------------------------------
    st.markdown(f"#### {t('op_export')}")
    html_doc = onepager.build(ctx, _bullets(ctx))
    stamp = dt.datetime.now().strftime("%Y%m%d")
    scope = "portafolio" if not ctx.selected_groups else "filtro"

    d1, d2 = st.columns([1, 3])
    d1.download_button(
        t("op_download"), data=html_doc.encode("utf-8"),
        file_name=f"onepager_{scope}_{ctx.current_year}_{stamp}.html",
        mime="text/html", key="dl_onepager", type="primary")
    d2.caption(t("op_print_hint"))

    with st.expander(t("op_preview"), expanded=True):
        components.html(html_doc, height=780, scrolling=True)
'''

_MODULES["views.dataquality"] = r'''"""Tab 7 — Data & quality: what was parsed, what was pruned, what does not reconcile."""

# © 2026 [Titular de derechos]. Todos los derechos reservados. / All rights reserved.
# Robertet LATAM Sales Analytics — software propietario. Ver LICENSE.
# Uso licenciado; prohibida su reproducción o distribución sin autorización escrita.
# Contacto: katyasam13@gmail.com


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
    "- **El avance y el score se miden contra el budget ANUAL (full year).** Cuando hay "
    "dos archivos con budgets distintos, se toma el mayor del año en curso (un budget "
    "parcial/YTD siempre es menor que el anual), sin importar en qué casilla esté cada "
    "archivo.\n"
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
    "- **Attainment and the score are measured against the ANNUAL (full-year) budget.** "
    "When the two files carry different budgets, the larger current-year budget is used "
    "(a partial/YTD budget is always smaller than the annual one), regardless of which "
    "slot each file sits in.\n"
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

    # --- reconciliation: parsed leaf total vs the export's own group total ----
    recon = parsed.reconciliation or {}
    if recon:
        TOL = 0.01
        bad = {y: r for y, r in recon.items() if r["diff_pct"] > TOL}
        if not bad:
            worst = max(r["diff_pct"] for r in recon.values())
            st.success(t("dq_recon_ok", n=len(recon), pct=f"{worst*100:.1f}"), icon="✅")
        else:
            years = ", ".join(
                f"{y} ({T.money_compact(r['diff'])}, {r['diff_pct']*100:.1f}%)"
                for y, r in sorted(bad.items()))
            st.warning(t("dq_recon_gap", years=years), icon="⚠️")

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
                   dimension, evolution, fullyear, onepager, overview, strategy)


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
    _lang_names = {"es": "🇪🇸 Español", "en": "🇬🇧 English",
                   "pt": "🇧🇷 Português", "fr": "🇫🇷 Français"}
    st.sidebar.selectbox(
        t("language"), ["es", "en", "pt", "fr"], key="lang",
        format_func=lambda v: _lang_names[v],
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
    prev_file = st.sidebar.file_uploader(
        t("upload_prev"), type=["xlsx", "xlsm"], key=f"up_prev_{epoch}",
        help=t("upload_prev_help"),
    )

    for slot, uploaded in (("ytd", ytd_file), ("fy", fy_file), ("prev", prev_file)):
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

    for slot, label in (("ytd", "YTD"), ("fy", "Full Year"), ("prev", t("prev_short"))):
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
        f"📈 {t('tab_evolution')}",
        f"📐 {t('tab_fy')}",
        f"👥 {t('tab_customers')}",
        f"🧪 {t('tab_products')}",
        f"🎯 {t('tab_deviations')}",
        f"💡 {t('tab_strategy')}",
        f"📄 {t('tab_onepager')}",
        f"🔧 {t('tab_data')}",
    ])
    with tabs[0]:
        overview.render(ctx)
    with tabs[1]:
        customer.render(ctx)
    with tabs[2]:
        backlog.render(ctx)
    with tabs[3]:
        evolution.render(ctx)
    with tabs[4]:
        fullyear.render(ctx)
    with tabs[5]:
        dimension.render(ctx, mode="customer")
    with tabs[6]:
        dimension.render(ctx, mode="product")
    with tabs[7]:
        deviations.render(ctx)
    with tabs[8]:
        strategy.render(ctx)
    with tabs[9]:
        onepager.render(ctx)
    with tabs[10]:
        dataquality.render(ctx)

    st.divider()
    st.caption(t("footer_copyright"))


if __name__ == "__main__":
    main()
