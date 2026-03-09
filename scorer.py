"""
JournalFit AI — Intelligent Journal Scorer
Multi-layer weighted ranking engine
"""

import re
import math
from typing import List, Dict, Any, Optional
from journal_db import JOURNAL_DB


# Priority mode weights: (scope_match, metric, practical)
PRIORITY_WEIGHTS = {
    "Fast publication":   (0.40, 0.20, 0.40),
    "High impact":        (0.40, 0.45, 0.15),
    "Balanced":           (0.40, 0.30, 0.30),
    "Easy acceptance":    (0.40, 0.10, 0.50),
    "Highly indexed":     (0.40, 0.40, 0.20),
}

MAX_IF = 30.0          # Normalisation cap for impact factor
MAX_REVIEW_DAYS = 150  # Max review time in db


def _tokenize(text: str) -> List[str]:
    """Lowercase + split text into tokens."""
    text = text.lower()
    tokens = re.findall(r"[a-z0-9]+", text)
    return tokens


def _token_frequency(tokens: List[str]) -> Dict[str, float]:
    freq: Dict[str, float] = {}
    for t in tokens:
        freq[t] = freq.get(t, 0) + 1
    return freq


def _cosine_similarity(vec_a: Dict[str, float], vec_b: Dict[str, float]) -> float:
    """Cosine similarity between two frequency vectors."""
    dot = sum(vec_a.get(k, 0) * vec_b.get(k, 0) for k in vec_b)
    mag_a = math.sqrt(sum(v * v for v in vec_a.values()))
    mag_b = math.sqrt(sum(v * v for v in vec_b.values()))
    if mag_a == 0 or mag_b == 0:
        return 0.0
    return dot / (mag_a * mag_b)


def _scope_score(user_tokens: Dict[str, float], journal: Dict[str, Any]) -> float:
    """Layer A: scope keyword match score [0, 1]."""
    scope_text = " ".join(journal["scope_keywords"]) + " " + journal.get("aims", "")
    journal_tokens = _token_frequency(_tokenize(scope_text))

    # Exact substring bonus for multi-word keyphrases
    scope_lower = scope_text.lower()
    # Check how many user phrases appear verbatim
    phrase_bonus = 0.0
    for phrase_len in [2, 3, 4]:
        all_user_tokens = list(user_tokens.keys())
        for i in range(len(all_user_tokens) - phrase_len + 1):
            phrase = " ".join(all_user_tokens[i:i + phrase_len])
            if phrase in scope_lower:
                phrase_bonus += 0.08 * phrase_len

    cosine = _cosine_similarity(user_tokens, journal_tokens)
    return min(1.0, cosine + phrase_bonus)


def _metric_score(journal: Dict[str, Any]) -> float:
    """Layer B: metric strength score [0, 1]."""
    # Impact factor normalized
    if_score = min(journal["impact_factor"] / MAX_IF, 1.0)

    # Quartile score
    q_map = {"Q1": 1.0, "Q2": 0.75, "Q3": 0.50, "Q4": 0.25}
    q_score = q_map.get(journal["quartile"], 0.25)

    return 0.6 * if_score + 0.4 * q_score


def _practical_score(journal: Dict[str, Any], priority: str) -> float:
    """Layer C: publication practicality score [0, 1]."""
    review_days = journal["avg_review_days"]
    freq = journal["frequency"]

    # Speed score: lower review days = higher score
    speed = 1.0 - (review_days / MAX_REVIEW_DAYS)
    speed = max(0.0, min(1.0, speed))

    # Frequency score
    freq_map = {
        "Weekly": 1.0,
        "Biweekly": 0.80,
        "Monthly": 0.60,
        "Quarterly": 0.30,
    }
    freq_score = freq_map.get(freq, 0.5)

    return 0.7 * speed + 0.3 * freq_score


def _generate_explanation(
    journal: Dict[str, Any],
    user_title: str,
    user_area: str,
    scope_match: float
) -> str:
    """Generate a human-readable scope match explanation."""
    name = journal["name"]
    quartile = journal["quartile"]
    impact_factor = journal["impact_factor"]

    # Find overlapping keywords
    user_text = (user_title + " " + user_area).lower()
    matching = []
    for kw in journal["scope_keywords"]:
        if any(word in user_text for word in kw.lower().split()):
            matching.append(kw)
        if len(matching) >= 3:
            break

    if not matching:
        matching = journal["scope_keywords"][:2]

    match_str = ", ".join(matching[:3])

    if scope_match >= 0.5:
        return (
            f"Strong thematic alignment with your work on {user_area.lower()}. "
            f"This {quartile} journal (IF {impact_factor}) actively covers {match_str}."
        )
    elif scope_match >= 0.25:
        return (
            f"Good fit for {user_area.lower()} research. "
            f"The journal publishes work in {match_str}, matching your study's scope."
        )
    else:
        return (
            f"Potential fit — this journal covers {match_str} with impact factor {impact_factor}. "
            f"Review scope carefully before submission."
        )


def _strategy_tag(suitability_score: int, quartile: str, impact_factor: float) -> str:
    """Determine submission strategy tag."""
    if suitability_score >= 70 and quartile in ("Q1",) and impact_factor >= 5.0:
        return "Ambitious target"
    elif suitability_score >= 60:
        return "Strong target"
    else:
        return "Safe target"


def rank_journals(
    title: str,
    area: str,
    keywords: str,
    priority: Optional[str] = "Balanced",
    article_type: Optional[str] = "Scientific"
) -> List[Dict[str, Any]]:
    """
    Main scoring and ranking function.
    Returns all journals sorted by weighted suitability score.
    """
    # Prepare user query tokens
    user_text = f"{title} {area} {keywords}"
    user_tokens = _token_frequency(_tokenize(user_text))

    resolved_priority = priority if priority in PRIORITY_WEIGHTS else "Balanced"
    w_scope, w_metric, w_practical = PRIORITY_WEIGHTS[resolved_priority]

    scored = []
    for journal in JOURNAL_DB:
        # 1. Filter by Article Type
        # Default types if missing: Scientific + [Experimental/Computational if in name/aims]
        supported = journal.get("supported_types", ["Scientific"])
        lower_name = journal["name"].lower()
        lower_aims = journal.get("aims", "").lower()
        
        if "computational" in lower_name or "computational" in lower_aims:
            supported.append("Computational")
        if "experimental" in lower_name or "experimental" in lower_aims:
            supported.append("Experimental")
        if any(kw in lower_name or kw in lower_aims for kw in ["review", "surveys", "trends"]):
            supported.append("Review")
        
        # Most journals support Scientific articles
        if "Scientific" not in supported:
            supported.append("Scientific")

        if article_type != "Any" and article_type not in supported:
            continue

        # 2. Scoring
        s_scope = _scope_score(user_tokens, journal)
        s_metric = _metric_score(journal)
        s_practical = _practical_score(journal, resolved_priority)

        weighted = w_scope * s_scope + w_metric * s_metric + w_practical * s_practical

        suitability_pct = min(99, max(1, round(weighted * 100)))

        explanation = _generate_explanation(journal, title, area, s_scope)
        tag = _strategy_tag(suitability_pct, journal["quartile"], journal["impact_factor"])

        # Default URL if missing (searching publisher/name)
        url = journal.get("url", f"https://www.google.com/search?q={journal['name'].replace(' ', '+')}+journal+homepage")

        scored.append({
            "name": journal["name"],
            "publisher": journal["publisher"],
            "impact_factor": journal["impact_factor"],
            "quartile": journal["quartile"],
            "avg_review_days": journal["avg_review_days"],
            "frequency": journal["frequency"],
            "suitability_score": suitability_pct,
            "scope_explanation": explanation,
            "strategy_tag": tag,
            "url": url,
            "aims": journal.get("aims", "Journal aims and scope details."),
            "sample_paper": journal.get("sample_paper", f"Recent research in {journal['name']}"),
            "_raw_scope": s_scope,
        })

    # Sort descending by suitability score
    scored.sort(key=lambda x: x["suitability_score"], reverse=True)

    # Remove internal scoring field
    for item in scored:
        item.pop("_raw_scope", None)

    return scored
