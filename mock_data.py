from __future__ import annotations

from typing import Dict, List, Optional, Tuple

from cyber_mockup_data import (
    market_intelligence_snapshot,
)


# Snapshot-level getters

def get_market_snapshot() -> Dict:
    return market_intelligence_snapshot


def get_hero_insights() -> List[Dict]:
    return market_intelligence_snapshot.get("hero_insights", [])


# Attack landscape getters

def get_attack_landscape() -> Dict:
    return market_intelligence_snapshot.get("attack_landscape", {})


def get_major_incidents() -> List[Dict]:
    return get_attack_landscape().get("major_incidents_this_period", [])


def get_attack_type_breakdown() -> Dict:
    return get_attack_landscape().get("attack_type_breakdown", {})


def get_cost_intelligence() -> Dict:
    return get_attack_landscape().get("cost_intelligence", {})


# Timing intelligence getters

def get_timing_intelligence() -> Dict:
    return market_intelligence_snapshot.get("timing_intelligence", {})


def get_seasonal_patterns() -> List[Dict]:
    return get_timing_intelligence().get("seasonal_patterns", [])


def get_time_of_week_patterns() -> Dict:
    return get_timing_intelligence().get("time_of_week_patterns", {})


# Emerging narratives

def get_emerging_narratives() -> List[Dict]:
    return market_intelligence_snapshot.get("emerging_narratives", [])


# Minimal chat mock (fallback)
_chat_responses: Dict[str, Dict] = {
    "trending": {
        "query_variants": ["what's trending", "top trends", "trending topics"],
        "response": "Key narratives: Manufacturing frontline, Transportation disruptions, Deepfake authentication crisis, Platform concentration risk."
    },
    "incidents": {
        "query_variants": ["major incidents", "recent attacks", "what happened"],
        "response": "Recent major incidents include JLR (supply chain), Asahi (ransomware), German procurement (DDoS), and multi-airport system outages."
    },
}

_default_chat_response = "Ask about: trending narratives or major incidents. This chat is simulated."


def match_chat_category(query: str) -> Optional[str]:
    q = query.strip().lower()
    best_category: Optional[str] = None
    best_score = 0

    for category, data in _chat_responses.items():
        score = 0
        for variant in data.get("query_variants", []):
            if variant in q:
                score += len(variant)
        if score > best_score:
            best_score = score
            best_category = category
    return best_category


def get_chat_response(query: str) -> Tuple[str, Optional[str]]:
    category = match_chat_category(query)
    if category is None:
        return _default_chat_response, None
    return _chat_responses[category]["response"], category


__all__ = [
    # snapshot
    "get_market_snapshot",
    "get_hero_insights",
    # attack landscape
    "get_attack_landscape",
    "get_major_incidents",
    "get_attack_type_breakdown",
    "get_cost_intelligence",
    # timing
    "get_timing_intelligence",
    "get_seasonal_patterns",
    "get_time_of_week_patterns",
    # emerging
    "get_emerging_narratives",
    # chat
    "get_chat_response",
]
