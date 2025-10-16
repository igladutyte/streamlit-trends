from __future__ import annotations

from typing import Dict, List, Sequence, Tuple

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

DEFAULT_TEMPLATE = "plotly_white"


def make_daily_volume_chart(daily_articles: Sequence[Dict]) -> go.Figure:
    """
    Returns a dual-line chart for article volume and unique outlets over time.
    """
    df = pd.DataFrame(daily_articles)
    df["date"] = pd.to_datetime(df["date"])

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=df["date"],
            y=df["article_count"],
            mode="lines+markers",
            name="Articles",
        )
    )

    fig.update_layout(
        title="Daily Coverage Volume",
        xaxis_title="Date",
        yaxis=dict(title="Articles"),
        legend=dict(orientation="h", yanchor="bottom",
                    y=1.02, xanchor="right", x=1),
        margin=dict(l=40, r=40, t=60, b=40),
        height=380,
    )
    fig.update_layout(template=DEFAULT_TEMPLATE)
    return fig


def make_sentiment_chart(sentiment_timeline: Sequence[Dict]) -> go.Figure:
    """
    Returns a stacked area chart for sentiment proportions over time.
    """
    df = pd.DataFrame(sentiment_timeline)
    df["date"] = pd.to_datetime(df["date"])

    fig = go.Figure()
    for col, color in [("negative", "#EF553B"), ("neutral", "#636EFA"), ("positive", "#00CC96")]:
        fig.add_trace(
            go.Scatter(
                x=df["date"],
                y=df[col],
                mode="lines",
                line=dict(color=color),
                stackgroup="one",
                name=col.capitalize(),
            )
        )

    fig.update_layout(
        title="Sentiment Share Over Time",
        xaxis_title="Date",
        yaxis_title="Share",
        yaxis=dict(range=[0, 1], ticksuffix=""),
        legend=dict(orientation="h", yanchor="bottom",
                    y=1.02, xanchor="right", x=1),
        margin=dict(l=40, r=40, t=60, b=40),
        height=340,
    )
    fig.update_layout(template=DEFAULT_TEMPLATE)
    return fig


def make_weekly_keywords_chart(weekly_keyword_data: Dict, selected_keywords: Sequence[str]) -> go.Figure:
    """
    Returns a multi-series line chart for weekly keyword counts.
    """
    weeks = weekly_keyword_data.get("weeks", [])
    series = weekly_keyword_data.get("keywords", {})

    df_rows: List[Dict] = []
    for keyword in selected_keywords:
        values = series.get(keyword, [])
        for w, v in zip(weeks, values):
            df_rows.append({"week": w, "keyword": keyword, "count": v})
    df = pd.DataFrame(df_rows)

    if df.empty:
        return go.Figure()

    fig = px.line(df, x="week", y="count", color="keyword",
                  markers=True, title="Weekly Keyword Coverage")
    fig.update_layout(margin=dict(l=40, r=40, t=60, b=40), height=360, legend=dict(
        orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1), template=DEFAULT_TEMPLATE)
    return fig


def split_emerging_declining(keyword_trends: Sequence[Dict]) -> Tuple[pd.DataFrame, pd.DataFrame]:
    df = pd.DataFrame(keyword_trends)
    emerging_df = df[df["trend"].isin(["surging", "rising"])].copy()
    declining_df = df[df["trend"] == "declining"].copy()
    emerging_df.sort_values(by="change_percent", ascending=False, inplace=True)
    declining_df.sort_values(by="change_percent", ascending=True, inplace=True)
    return emerging_df, declining_df


def make_emerging_declining_bars(keyword_trends: Sequence[Dict]) -> Tuple[go.Figure, go.Figure]:
    """
    Returns bar charts for emerging and declining topics.
    """
    emerging_df, declining_df = split_emerging_declining(keyword_trends)

    fig_emerging = px.bar(
        emerging_df.head(10),
        x="change_percent",
        y="keyword",
        orientation="h",
        title="Top Emerging Topics",
        text="change_percent",
        color_discrete_sequence=["#00CC96"],
    )
    fig_emerging.update_layout(margin=dict(
        l=40, r=40, t=60, b=40), height=360, template=DEFAULT_TEMPLATE)
    fig_emerging.update_traces(
        texttemplate="%{text:.1f}%", textposition="outside")
    fig_emerging.update_yaxes(autorange="reversed")

    fig_declining = px.bar(
        declining_df.head(10),
        x="change_percent",
        y="keyword",
        orientation="h",
        title="Top Declining Topics",
        text="change_percent",
        color_discrete_sequence=["#EF553B"],
    )
    fig_declining.update_layout(margin=dict(
        l=40, r=40, t=60, b=40), height=360, template=DEFAULT_TEMPLATE)
    fig_declining.update_traces(
        texttemplate="%{text:.1f}%", textposition="outside")
    fig_declining.update_yaxes(autorange="reversed")

    return fig_emerging, fig_declining


def make_industry_distribution_chart(industry_distribution: Sequence[Dict]) -> go.Figure:
    df = pd.DataFrame(industry_distribution)
    fig = px.bar(df.sort_values("article_count", ascending=False), x="article_count",
                 y="industry", orientation="h", title="Articles by Industry")
    fig.update_layout(margin=dict(l=40, r=40, t=60, b=40),
                      height=400, template=DEFAULT_TEMPLATE)
    fig.update_yaxes(autorange="reversed")
    return fig


def make_geography_chart(geographic_distribution: Sequence[Dict]) -> go.Figure:
    df = pd.DataFrame(geographic_distribution)
    fig = px.bar(df.sort_values("article_count", ascending=False),
                 x="article_count", y="region", orientation="h", title="Articles by Region")
    fig.update_layout(margin=dict(l=40, r=40, t=60, b=40),
                      height=400, template=DEFAULT_TEMPLATE)
    fig.update_yaxes(autorange="reversed")
    return fig


def make_methods_chart(technical_methods: Sequence[Dict]) -> go.Figure:
    df = pd.DataFrame(technical_methods)
    fig = px.bar(df.sort_values("count", ascending=False), x="count",
                 y="method", orientation="h", title="Attack Methods (Coverage Mentions)")
    fig.update_layout(margin=dict(l=40, r=40, t=60, b=40),
                      height=420, template=DEFAULT_TEMPLATE)
    fig.update_yaxes(autorange="reversed")
    return fig


def format_summary_kpis(summary_stats: Dict) -> List[Tuple[str, str]]:
    """
    Returns a list of (label, value) pairs for quick KPI display.
    """
    return [
        ("Total Articles",
         f"{summary_stats.get('total_articles_analyzed', 0):,}"),
        ("Change vs Prev", f"{summary_stats.get('percent_change', 0)}%"),
        ("Active Narratives",
         f"{summary_stats.get('active_threat_narratives', 0):,}"),
        ("Unique Outlets",
         f"{summary_stats.get('unique_media_outlets', 0):,}"),
        ("Regions Covered",
         f"{summary_stats.get('geographic_regions_covered', 0):,}"),
    ]
