from __future__ import annotations

from typing import List, Dict, Any

import streamlit as st
import pandas as pd
import plotly.express as px


from mock_data import (
    get_market_snapshot,
    get_hero_insights,
    get_major_incidents,
    get_attack_type_breakdown,
    get_cost_intelligence,
    get_seasonal_patterns,
    get_time_of_week_patterns,
    get_emerging_narratives,
    get_chat_response,
)

# New visual-rich layout data
from cyber_mocup_data_new import visual_dashboard_layout, visual_design_system


st.set_page_config(
    page_title="Trends – Cyber Coverage Intelligence", layout="wide")

# Global style polish
st.markdown(
    """
    <style>
    .stApp { font-size: 0.95rem; }
    .markdown-text-container p { line-height: 1.5; font-size: 0.95rem; }
    .markdown-text-container li { font-size: 0.95rem; }
    .markdown-text-container h2 { font-size: 1.25rem; }
    .markdown-text-container h3 { font-size: 1.1rem; }
    .markdown-text-container h4 { font-size: 1.0rem; }
    .badge { display:inline-block; padding:2px 8px; border-radius:999px; font-size:0.7rem; border:1px solid #e5e7eb; background:#f8fafc; margin-right:6px; }
    .tag { display:inline-block; padding:2px 8px; border-radius:6px; font-size:0.7rem; background:#eef2ff; color:#3730a3; margin-right:6px; }
    .card { padding: 1rem 1.2rem; border: 1px solid #EEE; border-radius: 12px; background: #FFFFFF; box-shadow: 0 1px 2px rgba(0,0,0,0.04); }
    .muted { color: #6b7280; }
    .hero-label { font-size:0.85rem; color:#6b7280; }
    .hero-title { font-size:1.0rem; font-weight:600; margin-top:4px; }
    .spacer { height: 14px; }
    /* Visual cards */
    .viz-card { padding: 1rem 1.2rem; border-radius: 12px; background: #FFFFFF; border: 1px solid #EEE; box-shadow: 0 1px 2px rgba(0,0,0,0.04); }
    .viz-pill { display:inline-block; padding:2px 8px; border-radius:999px; font-size:0.7rem; border:1px solid #e5e7eb; background:#f8fafc; margin-right:6px; }
    .viz-accent { border-left: 6px solid var(--accent, #3B82F6); }
    .kpi { font-weight:600; font-size:0.95rem; }
    .insight { background:#eef6ff; color:#1e40af; padding:12px 14px; border-radius:10px; border:1px solid #dbeafe; }
    .chip { display:inline-block; padding:4px 10px; border-radius:999px; background:#f1f5f9; border:1px solid #e2e8f0; color:#334155; font-size:0.75rem; margin-right:6px; margin-bottom:6px; }
    .section-gap { margin-top: 24px; }
    </style>
    """,
    unsafe_allow_html=True,
)


def chunk_list(items: List[dict], chunk_size: int) -> List[List[dict]]:
    return [items[i:i + chunk_size] for i in range(0, len(items), chunk_size)]


def section_spacer() -> None:
    st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)
    st.markdown("<div class='section-gap'></div>", unsafe_allow_html=True)


def section_title(title: str, subtitle: str | None = None) -> None:
    st.markdown(f"### {title}")
    if subtitle:
        st.caption(subtitle)


def render_insight(text: str) -> None:
    st.markdown(f"<div class='insight'>{text}</div>", unsafe_allow_html=True)
    section_spacer()


# ==========================
# Visual sections (new)
# ==========================
def render_week_summary() -> None:
    section_title("This Month's Summary", None)

    st.markdown(
        "This month’s coverage accelerated on the back of overlapping zero‑day disclosures and visible operational disruptions. Transportation remained the highest‑severity sector as airport outages sustained attention, while the Asahi ransomware incident continued to anchor cost discussions with unusual public transparency. The narrative is shifting from data exposure to business continuity and platform concentration risk—organizations are judged by time‑to‑restore more than breach size."
    )

    kpis = [
        {"label": "Coverage change", "value": "+18%", "caption": "vs prior month"},
        {"label": "Top severity sector", "value": "Transportation",
            "caption": "airport outages & recovery lags"},
        {"label": "Highest cost incident",
            "value": "Asahi (¥2.3B)", "caption": "ransomware & disclosure"},
    ]
    cols = st.columns(3)
    for col, k in zip(cols, kpis):
        with col:
            st.markdown(
                f"<div class='viz-card'><div class='hero-label'>{k['label']}</div><div class='hero-title'>{k['value']}</div><div class='muted'>{k['caption']}</div></div>",
                unsafe_allow_html=True,
            )
    section_spacer()


def render_sector_rankings_simple() -> None:
    section_title("Sector Rankings", "Quick view: vulnerability vs cost")

    # Granularity selector (UI only; static data so we don't change values now)
    _ = st.selectbox("Granularity", [
                     "Last 30 Days", "Weekly", "Daily"], index=0, key="granularity_sectors")

    # Vulnerability rankings come from sector_matrix in visual layout
    sector_matrix = visual_dashboard_layout.get(
        "sector_matrix", {}).get("matrix_data", [])
    df_vuln = pd.DataFrame(sector_matrix)
    if not df_vuln.empty:
        df_vuln_sorted = df_vuln.sort_values(
            "vulnerability_score", ascending=False)

    # Cost rankings by industry: derive from sector_matrix avg_cost ranges
    import re as _re

    def _parse_cost_to_millions(text: str) -> float | None:
        if not isinstance(text, str):
            return None
        # Normalize currency symbols and delimiters, e.g., "$5M-$15M", "€5M-€50M", "¥2.3B ($15M+)"
        cleaned = text.replace(",", "")
        # Extract both B and M units anywhere in the string
        pairs = _re.findall(
            r"([0-9]+(?:\.[0-9]+)?)\s*([MB])", cleaned, flags=_re.IGNORECASE)
        if not pairs:
            return None
        values: List[float] = []
        for n, u in pairs:
            try:
                v = float(n)
            except Exception:
                continue
            if u.upper() == "B":
                v *= 1000.0
            values.append(v)
        if not values:
            return None
        return sum(values) / len(values) if len(values) > 1 else values[0]

    df_cost = pd.DataFrame()
    if not df_vuln.empty and "avg_cost" in df_vuln.columns:
        df_cost = df_vuln[["sector", "avg_cost"]].copy()
        df_cost["cost_m"] = df_cost["avg_cost"].apply(_parse_cost_to_millions)
        df_cost = df_cost.dropna(subset=["cost_m"]).sort_values(
            "cost_m", ascending=False)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**By Vulnerability Score**")
        if not df_vuln.empty:
            fig1 = px.bar(df_vuln_sorted.head(10), x="vulnerability_score", y="sector", orientation="h",
                          labels={"vulnerability_score": "Score",
                                  "sector": "Sector"},
                          title=None, color="vulnerability_score",
                          color_continuous_scale=["#F59E0B", "#EA580C", "#DC2626"])
            fig1.update_layout(margin=dict(l=20, r=10, t=10, b=10), height=360)
            fig1.update_yaxes(autorange="reversed")
            st.plotly_chart(fig1, use_container_width=True)
        else:
            st.info("No sector vulnerability data available.")

    with col2:
        st.markdown("**By Estimated Cost (USD $M)**")
        if not df_cost.empty:
            fig2 = px.bar(df_cost.head(10), x="cost_m", y="sector", orientation="h",
                          labels={
                              "cost_m": "Typical Cost ($M)", "sector": "Sector"},
                          title=None, color="cost_m",
                          color_continuous_scale=[[0, "#e0f2fe"], [1, "#0284c7"]])
            fig2.update_layout(margin=dict(l=20, r=10, t=10, b=10), height=360)
            fig2.update_yaxes(autorange="reversed")
            st.plotly_chart(fig2, use_container_width=True)
        else:
            st.info("No cost data available.")

    # Insights under the two sector charts (data‑aware)
    icol1, icol2 = st.columns(2)
    sector_rows = {row.get("sector"): row for row in (sector_matrix or [])}
    with icol1:
        vuln_text = ""
        try:
            if not df_vuln.empty:
                top_vuln = df_vuln_sorted.iloc[0]
                sname = str(top_vuln.get("sector", "Top sector"))
                score = top_vuln.get("vulnerability_score", "")
                why = sector_rows.get(sname, {}).get("why_targeted", "")
                recents = sector_rows.get(sname, {}).get(
                    "recent_incidents", [])
                recent_str = f" Recent example: {recents[0]}" if recents else ""
                vuln_text = f"{sname} leads vulnerability ({score}). {why}{recent_str}"
        except Exception:
            pass
        if not vuln_text:
            vuln_text = "Vulnerability concentrates where disruption is highly visible and dependencies are complex."
        render_insight(vuln_text)
    with icol2:
        cost_text = ""
        try:
            if not df_cost.empty:
                top_cost = df_cost.sort_values(
                    "cost_m", ascending=False).iloc[0]
                sname = str(top_cost.get("sector", "Top cost sector"))
                costm = float(top_cost.get("cost_m", 0.0))
                trend_note = sector_rows.get(sname, {}).get("trend_note", "")
                cost_text = f"{sname} shows highest typical incident cost (~{costm:.0f}M). {trend_note}"
        except Exception:
            pass
        if not cost_text:
            cost_text = "Typical incident cost skews to operational disruption and reputation; recovery planning beats ransom debates."
        render_insight(cost_text)

    section_spacer()


def render_threat_heatmap_viz() -> None:
    data = visual_dashboard_layout.get("threat_heatmap", {})
    items = data.get("heatmap_data", [])
    section_title(data.get("title", "Threat Landscape"),
                  data.get("description", ""))

    # Grid of colored cards (2 or 3 per row depending on width)
    for row in chunk_list(items, 3):
        cols = st.columns(len(row))
        for col, item in zip(cols, row):
            color = item.get("color", "#EEE")
            with col:
                st.markdown(
                    f"<div class='viz-card viz-accent' style='--accent:{color}'>"
                    f"<div class='hero-title'>{item.get('icon', '')} {item.get('threat_category', '')}</div>"
                    f"<div class='muted'>Severity: <b>{item.get('severity', '')}</b> &nbsp; | &nbsp; Coverage: <b>{item.get('coverage_intensity', '')}</b></div>"
                    f"<div class='muted'>Avg cost: {item.get('avg_cost', '')}</div>"
                    f"<div class='muted'>Recent: {item.get('recent_victim', '')} — {item.get('impact', '')}</div>"
                    f"</div>",
                    unsafe_allow_html=True,
                )
    section_spacer()


def render_attack_timeline_viz() -> None:
    block = visual_dashboard_layout.get("attack_timeline", {})
    section_title(block.get("title", "Attack Timeline"),
                  block.get("subtitle", ""))
    events = block.get("timeline_events", [])
    if not events:
        return

    # Bubble chart: X=date, Y=coverage volume, size=estimated cost
    def parse_coverage(value: str) -> float:
        if not isinstance(value, str):
            return 0.0
        digits = "".join(ch for ch in value if ch.isdigit())
        try:
            return float(digits) if digits else 0.0
        except Exception:
            return 0.0

    def parse_cost_to_millions(value: str) -> float:
        if not isinstance(value, str):
            return 0.0
        v = value
        if "$" in value and "(" in value:
            v = value[value.find("$"):]
        num = ""
        unit = ""
        for ch in v:
            if ch.isdigit() or ch == ".":
                num += ch
            elif ch.upper() in ("M", "B"):
                unit = ch.upper()
                break
        try:
            x = float(num) if num else 0.0
        except Exception:
            x = 0.0
        return x * 1000.0 if unit == "B" else x

    severity_to_color = {
        "critical": visual_design_system["color_palette"]["severity_colors"]["critical"],
        "high": visual_design_system["color_palette"]["severity_colors"]["high"],
        "medium": visual_design_system["color_palette"]["severity_colors"]["medium"],
        "warning": "#F59E0B",
        "info": visual_design_system["color_palette"]["severity_colors"]["info"],
        "emerging_critical": visual_design_system["color_palette"]["severity_colors"]["critical"],
    }

    df_rows: List[Dict[str, Any]] = []
    for e in events:
        coverage_raw = e.get("coverage", "")
        cost_raw = e.get("cost", e.get("total_cost", ""))
        df_rows.append({
            "date": e.get("date"),
            "event": e.get("event", e.get("note", "")),
            "victim": e.get("victim", e.get("victims", "")),
            "severity": e.get("severity", "info"),
            "coverage": parse_coverage(coverage_raw),
            "cost_m": parse_cost_to_millions(cost_raw),
        })

    df = pd.DataFrame(df_rows)
    try:
        df["date_parsed"] = pd.to_datetime(
            df["date"] + f" {pd.Timestamp.today().year}")
    except Exception:
        df["date_parsed"] = df["date"]

    # Controls
    col_g, col_avg = st.columns(2)
    with col_g:
        granularity = st.selectbox(
            "Granularity", ["Daily", "Weekly"], index=0, key="timeline_granularity")
    with col_avg:
        show_avg = st.toggle("Show moving average",
                             value=True, key="timeline_show_avg")

    # Aggregate by chosen granularity and stack by severity
    if granularity == "Weekly":
        week_start = (
            df["date_parsed"] - pd.to_timedelta(df["date_parsed"].dt.weekday, unit="D")).dt.normalize()
        df["period"] = week_start
    else:
        df["period"] = df["date_parsed"].dt.normalize()

    grouped = (
        df.groupby(["period", "severity"], as_index=False)
        .agg(coverage=("coverage", "sum"), cost_m=("cost_m", "sum"))
        .sort_values("period")
    )
    totals = grouped.groupby("period", as_index=False)["coverage"].sum().rename(
        columns={"coverage": "total_coverage"})

    fig = px.bar(
        grouped,
        x="period",
        y="coverage",
        color="severity",
        text=grouped["cost_m"].round(0).astype(int).astype(str) + "M",
        color_discrete_map=severity_to_color,
        labels={"coverage": "Coverage (articles)", "period": "Date"},
        title=None,
    )
    fig.update_traces(textposition="outside")

    # Moving average overlay (daily only)
    if show_avg and granularity == "Daily" and not totals.empty:
        totals = totals.sort_values("period")
        totals["ma"] = totals["total_coverage"].rolling(
            3, min_periods=1).mean()
        import plotly.graph_objects as go
        fig.add_trace(
            go.Scatter(
                x=totals["period"], y=totals["ma"], mode="lines", name="3-day avg",
                line=dict(color="#111827", width=2)
            )
        )

    fig.update_layout(margin=dict(l=40, r=40, t=10, b=40), height=440,
                      xaxis=dict(tickangle=-30), barmode="stack",
                      legend=dict(orientation="h", y=1.05, x=1, xanchor="right"))
    st.plotly_chart(fig, use_container_width=True)
    st.caption("How to read: stacked bars show coverage by severity per period; optional line shows 3-day moving average of total coverage.")
    section_spacer()


def render_geography_viz() -> None:
    block = visual_dashboard_layout.get("geographic_map", {})
    section_title(block.get("title", "Geography"), block.get("subtitle", ""))
    regions = block.get("map_data", {})
    rows: List[Dict[str, Any]] = []
    for name, r in regions.items():
        rows.append({
            "region": name.replace("_", " ").title(),
            "coverage_count": r.get("coverage_count", 0),
            "percentage": r.get("percentage", 0),
            "trend": r.get("trend", ""),
        })
    if rows:
        df = pd.DataFrame(rows)
        df.sort_values("coverage_count", ascending=False, inplace=True)
        fig = px.bar(df, x="coverage_count", y="region", orientation="h", title="Coverage by Region",
                     text="percentage")
        fig.update_traces(texttemplate="%{text:.1f}%", textposition="outside")
        fig.update_yaxes(autorange="reversed")
        fig.update_layout(margin=dict(l=40, r=40, t=40, b=40), height=420)
        st.plotly_chart(fig, use_container_width=True)
    section_spacer()


def render_geo_and_cost_row() -> None:
    col1, col2 = st.columns(2)
    with col1:
        render_geography_viz()
    with col2:
        render_cost_dashboard_viz()
    # Insights below each graph (aligned with the two columns)
    icol1, icol2 = st.columns(2)
    with icol1:
        render_insight(
            "APAC’s share growth signals a structural rebalancing of cyber coverage—journalism capacity and incident volume are converging, not spiking randomly.")
    with icol2:
        cb = visual_dashboard_layout.get(
            "cost_dashboard", {}).get("cost_breakdown_visual", {})
        cost_key = cb.get("key_insight")
        if cost_key:
            render_insight(cost_key)


def render_cost_dashboard_viz() -> None:
    block = visual_dashboard_layout.get("cost_dashboard", {})
    section_title(block.get("title", "Cost Intelligence"),
                  block.get("subtitle", ""))

    # Cost components pie
    cb = block.get("cost_breakdown_visual", {})
    components = cb.get("cost_components", [])
    if components:
        df = pd.DataFrame(components)
        fig = px.pie(df, names="category", values="percentage", title=cb.get("example_incident", "Cost Breakdown"),
                     hole=0.35)
        st.plotly_chart(fig, use_container_width=True)

    section_spacer()


def render_sector_matrix_viz() -> None:
    block = visual_dashboard_layout.get("sector_matrix", {})
    section_title(block.get("title", "Industry Vulnerability"),
                  block.get("subtitle", ""))
    items = block.get("matrix_data", [])
    if items:
        df = pd.DataFrame(items)
        fig = px.bar(df.sort_values("vulnerability_score", ascending=True),
                     x="vulnerability_score", y="sector", orientation="h",
                     color="vulnerability_score", color_continuous_scale=["#F59E0B", "#EA580C", "#DC2626"],
                     title="Vulnerability Score by Sector")
        fig.update_layout(margin=dict(l=40, r=40, t=40, b=40), height=460)
        st.plotly_chart(fig, use_container_width=True)
    section_spacer()


def render_emerging_radar_viz() -> None:
    block = visual_dashboard_layout.get("emerging_threat_radar", {})
    section_title(block.get("title", "Emerging Threats"),
                  block.get("subtitle", ""))
    quads = block.get("radar_quadrants", {})

    def parse_growth(val: str) -> float:
        if not isinstance(val, str):
            return 0.0
        digits = "".join(ch for ch in val if (ch.isdigit() or ch == "."))
        try:
            return float(digits) if digits else 0.0
        except Exception:
            return 0.0

    rows: List[Dict[str, Any]] = []
    for quad_name, entries in quads.items():
        for e in entries:
            pos = e.get("position", {})
            rows.append({
                "threat": e.get("threat", ""),
                "urgency": pos.get("urgency", 0),
                "maturity": pos.get("maturity", 0),
                "quadrant": quad_name.replace("_", " ").title(),
                "growth": parse_growth(e.get("growth_rate", "")),
                "stage": e.get("current_stage", ""),
            })

    if rows:
        df = pd.DataFrame(rows)
        # Filters
        selected_quads = st.multiselect(
            "Quadrants",
            options=sorted(df["quadrant"].unique().tolist()),
            default=sorted(df["quadrant"].unique().tolist()),
            key="radar_quadrants_filter",
        )
        if selected_quads:
            df = df[df["quadrant"].isin(selected_quads)]

        fig = px.scatter(
            df,
            x="urgency",
            y="maturity",
            color="quadrant",
            symbol="quadrant",
            size="growth",
            hover_data={"threat": True, "growth": True, "stage": True},
            title="Threat Radar (Urgency vs Maturity)",
            size_max=48,
        )
        fig.update_layout(margin=dict(l=40, r=40, t=40, b=40), height=440,
                          legend=dict(orientation="h", y=1.05, x=1, xanchor="right"))
        st.plotly_chart(fig, use_container_width=True)
        st.caption("How to read: position = urgency vs maturity; bubble size = growth rate (% change); color/symbol = quadrant. Use the filter to focus.")
    section_spacer()


def render_incidents_text_section() -> None:
    block = visual_dashboard_layout.get("incidents_showcase", {})
    section_title(block.get("title", "Featured Incidents"),
                  block.get("subtitle", ""))
    for inc in block.get("featured_incidents", []):
        st.markdown(f"**{inc.get('title', '')}** — {inc.get('tagline', '')}")
        stats = inc.get("hero_stats", {})
        # Render chips from hero stats
        chips = []
        for k, v in stats.items():
            label = f"{k.replace('_', ' ').title()}: {v}"
            chips.append(f"<span class='chip'>{label}</span>")
        if chips:
            st.markdown(" ".join(chips), unsafe_allow_html=True)
        # Compose narrative paragraph
        why = inc.get("why_this_matters", {})
        impact = inc.get("business_impact", {})
        paragraph_parts = []
        if why:
            paragraph_parts.append(" ".join(why.values()))
        if impact:
            paragraph_parts.append(
                "Impact: " + ", ".join([f"{k.replace('_', ' ')} {v}" for k, v in impact.items()]))
        if paragraph_parts:
            st.markdown(" ".join(paragraph_parts))
        lessons = inc.get("key_lessons", [])
        if lessons:
            st.caption("Lessons: " + "; ".join(lessons))
        # Incident-specific insight
        if "Asahi" in inc.get("title", ""):
            render_insight(
                "Primary cost driver: reputation and regulatory. Public transparency reset expectations in APAC; earnings timing magnified pressure.")
        elif "Jaguar Land Rover" in inc.get("title", ""):
            render_insight(
                "Primary impact: operational disruption across just-in-time manufacturing. Single portal failure cascaded into multi-facility downtime.")
        elif "Brussels Airport" in inc.get("title", ""):
            render_insight(
                "Coverage persisted despite attribution ambiguity—public-facing chaos and passenger impact trump technical certainty.")
        else:
            render_insight(
                "Primary driver varies by case; operational disruption and recovery tempo shape the narrative more than raw data volume.")
        st.markdown("---")
    section_spacer()


def render_key_points_summary() -> None:
    st.markdown("### Key Points – TL;DR")
    bullets: List[str] = []
    # Pull a few high-signal insights from the new layout
    try:
        cost_key = visual_dashboard_layout.get("cost_dashboard", {}).get(
            "cost_breakdown_visual", {}).get("key_insight")
        if cost_key:
            bullets.append(cost_key)
    except Exception:
        pass
    try:
        geo_note = visual_dashboard_layout.get("geographic_map", {}).get(
            "map_data", {}).get("asia_pacific", {}).get("special_note")
        if geo_note:
            bullets.append(f"APAC: {geo_note}")
    except Exception:
        pass
    try:
        em = visual_dashboard_layout.get("emerging_threat_radar", {}).get(
            "radar_quadrants", {}).get("critical_emerging", [])
        if em:
            bullets.append(
                f"Emerging: {em[0].get('threat')} — {em[0].get('urgency')}")
    except Exception:
        pass
    try:
        tm = visual_dashboard_layout.get(
            "attack_timeline", {}).get("timeline_events", [])
        if tm:
            bullets.append(
                "Coverage velocity peaks around zero-day clusters; plan fast patch playbooks.")
    except Exception:
        pass

    if bullets:
        for b in bullets:
            st.markdown(f"- {b}")
    section_spacer()


def render_sidebar() -> None:
    st.sidebar.header("Filters")
    st.sidebar.caption("Static filters for prototype")
    snapshot = get_market_snapshot()
    st.sidebar.selectbox("Period", [snapshot.get("period", "Last 30 Days")])
    st.sidebar.selectbox(
        "Focus", ["All", "Threats", "Sectors", "Geography"], index=0)
    st.sidebar.divider()
    st.sidebar.subheader("Settings (placeholder)")
    st.sidebar.toggle("Dark mode", value=False, disabled=True)


def render_hero_section() -> None:
    st.markdown("### Coverage Intelligence Snapshot")
    heroes = get_hero_insights()
    for hero in heroes:
        label = hero.get("label", "")
        value = hero.get("value", "")
        details = hero.get("details", {})
        why = hero.get("why_it_matters", "")
        examples = hero.get("article_examples", [])
        # Collapsible but expanded by default
        with st.expander(f"{label} — {value}", expanded=True):
            if details:
                for k, v in details.items():
                    if isinstance(v, list):
                        st.caption(
                            f"{k.replace('_', ' ').title()}: " + ", ".join(v))
                    else:
                        st.caption(f"{k.replace('_', ' ').title()}: {v}")
            if why:
                st.markdown("**Why it matters:** " + why)
            if examples:
                st.caption("Examples: " + " | ".join(examples))
    section_spacer()


def render_timing_intelligence() -> None:
    st.markdown("### Timing Intelligence")
    for sp in get_seasonal_patterns():
        title = f"{sp.get('season', '')} — Risk: {sp.get('risk_level', '')}"
        with st.expander(title, expanded=True):
            # badges/tags for quick scanning
            badges = []
            if sp.get("risk_level"):
                badges.append(sp.get("risk_level"))
            badges.append("Seasonal")
            ex_count = len(sp.get("examples", []) or [])
            if ex_count:
                badges.append(f"Examples: {ex_count}")
            st.markdown(" ".join(
                [f"<span class='badge'>{b}</span>" for b in badges]), unsafe_allow_html=True)

            st.markdown(sp.get("why_vulnerable", ""))
            if sp.get("historical_data"):
                st.caption("History: " + sp.get("historical_data"))
            if sp.get("examples"):
                st.caption("Examples: " + " | ".join(sp.get("examples", [])))
            if sp.get("attacker_strategy"):
                st.caption("Attacker strategy: " + sp.get("attacker_strategy"))
            if sp.get("defensive_recommendation"):
                st.markdown("**Recommendation:** " +
                            sp.get("defensive_recommendation"))

    tow = get_time_of_week_patterns()
    if tow:
        with st.expander("Time-of-Week Patterns", expanded=True):
            for name, block in tow.items():
                st.markdown(f"**{name.replace('_', ' ').title()}**")
                # risk + type tags
                tbadges = []
                if block.get("risk_level"):
                    tbadges.append(block.get("risk_level"))
                tbadges.append("Time-of-Week")
                exs = block.get("examples")
                if isinstance(exs, str) and exs:
                    tbadges.append("Has examples")
                st.markdown(" ".join(
                    [f"<span class='badge'>{b}</span>" for b in tbadges]), unsafe_allow_html=True)

                for k, v in block.items():
                    st.caption(f"{k.replace('_', ' ').title()}: {v}")
    section_spacer()


def render_major_incidents() -> None:
    st.markdown("### Major Incidents This Period")
    incidents = get_major_incidents()
    for row in chunk_list(incidents, 2):
        cols = st.columns(len(row))
        for col, inc in zip(cols, row):
            with col:
                title = f"{inc.get('victim', '')} — {inc.get('attack_type', '')} ({inc.get('date', '')})"
                with st.expander(title, expanded=False):
                    st.caption(f"Loss: {inc.get('financial_loss', '')}")
                    st.markdown(inc.get("how_it_happened", ""))
                    st.markdown("**Business impact:** " +
                                inc.get("business_impact", ""))
                    st.caption("Media angle: " + inc.get("media_angle", ""))
                    if inc.get("article_examples"):
                        st.caption("Examples: " +
                                   " | ".join(inc.get("article_examples", [])))
                    if inc.get("lessons"):
                        st.markdown("**Lessons:** " + inc.get("lessons", ""))
    section_spacer()


def render_emerging_section() -> None:
    st.markdown("### Emerging Narratives")
    items = get_emerging_narratives()
    for row in chunk_list(items, 2):
        cols = st.columns(len(row))
        for col, n in zip(cols, row):
            with col:
                # Collapsible but expanded by default
                with st.expander(n.get("narrative", ""), expanded=True):
                    badges = []
                    if n.get("current_state"):
                        badges.append(n.get("current_state"))
                    if n.get("opportunity_window"):
                        badges.append(n.get("opportunity_window"))
                    if badges:
                        st.markdown(" ".join(
                            [f"<span class='badge'>{b}</span>" for b in badges]), unsafe_allow_html=True)
                    for key in [
                        "key_incident",
                        "key_incidents",
                        "why_emerging",
                        "attacker_interest",
                        "cost_impact",
                    ]:
                        if n.get(key):
                            st.caption(
                                f"{key.replace('_', ' ').title()}: {n.get(key)}")
                    if n.get("coverage_examples"):
                        st.caption("Examples: " +
                                   " | ".join(n.get("coverage_examples", [])))
                    if n.get("thought_leadership_angle"):
                        st.markdown("**Angle:** " +
                                    n.get("thought_leadership_angle"))
    section_spacer()


def render_attack_type_breakdown() -> None:
    st.markdown("### Attack Type Breakdown")
    breakdown = get_attack_type_breakdown()
    items = list(breakdown.items())
    for row in chunk_list(items, 2):
        cols = st.columns(len(row))
        for col, (atype, block) in zip(cols, row):
            with col:
                with st.expander(atype.replace("_", " ").title(), expanded=True):
                    for k, v in block.items():
                        if isinstance(v, list):
                            st.caption(
                                f"{k.replace('_', ' ').title()}: " + ", ".join(v))
                        else:
                            st.caption(f"{k.replace('_', ' ').title()}: {v}")
    section_spacer()


def render_cost_intelligence() -> None:
    st.markdown("### Cost Intelligence")
    ci = get_cost_intelligence()
    for cat_key in ["direct_costs", "indirect_costs", "total_cost_analysis"]:
        block = ci.get(cat_key, {})
        if not block:
            continue
        with st.expander(cat_key.replace("_", " ").title(), expanded=True):
            if isinstance(block, dict):
                for k, v in block.items():
                    if isinstance(v, dict):
                        st.markdown(f"**{k.replace('_', ' ').title()}**")
                        for kk, vv in v.items():
                            st.caption(f"{kk.replace('_', ' ').title()}: {vv}")
                    else:
                        st.caption(f"{k.replace('_', ' ').title()}: {v}")
    section_spacer()


def render_insights_tab() -> None:
    st.markdown("## Insights")
    render_hero_section()
    # Timing immediately after snapshot
    render_timing_intelligence()
    # Then incidents and emerging
    render_major_incidents()
    render_emerging_section()
    # Then breakdown and costs
    render_attack_type_breakdown()
    render_cost_intelligence()


def render_visual_dashboard_tab() -> None:
    st.markdown("## Cyber Events Dashboard")
    render_week_summary()
    render_sector_rankings_simple()
    render_threat_heatmap_viz()
    render_geo_and_cost_row()
    render_incidents_text_section()
    render_key_points_summary()


def init_chat_state() -> None:
    if "chat_messages" not in st.session_state:
        st.session_state.chat_messages = []


def add_chat_message(role: str, content: str) -> None:
    st.session_state.chat_messages.append({"role": role, "content": content})


def render_chat_history() -> None:
    for msg in st.session_state.chat_messages:
        st.chat_message(msg["role"]).markdown(msg["content"])


def render_chat_tab() -> None:
    st.markdown("### Ask about the trends (simulated)")
    init_chat_state()
    render_chat_history()

    prompt = st.chat_input(
        "Type a question, e.g., 'What are the trending topics?'")
    if prompt:
        add_chat_message("user", prompt)
        response_text, matched_category = get_chat_response(prompt)
        add_chat_message("assistant", response_text)
        st.chat_message("assistant").markdown(response_text)


def main() -> None:
    # Ensure sidebar content renders on all pages
    render_sidebar()

    tab1, tab2, tab3 = st.tabs(["Visual Dashboard", "Insights", "Chat"])
    with tab1:
        render_visual_dashboard_tab()
    with tab2:
        render_insights_tab()
    with tab3:
        render_chat_tab()


if __name__ == "__main__":
    main()
