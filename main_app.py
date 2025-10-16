from __future__ import annotations

from typing import List

import streamlit as st

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
    </style>
    """,
    unsafe_allow_html=True,
)


def chunk_list(items: List[dict], chunk_size: int) -> List[List[dict]]:
    return [items[i:i + chunk_size] for i in range(0, len(items), chunk_size)]


def section_spacer() -> None:
    st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)


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

    tab1, tab2 = st.tabs(["Insights", "Chat"])
    with tab1:
        render_insights_tab()
    with tab2:
        render_chat_tab()


if __name__ == "__main__":
    main()
