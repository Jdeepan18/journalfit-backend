from pydantic import BaseModel
from typing import Optional, List


class RecommendRequest(BaseModel):
    title: Optional[str] = ""
    area: str                           # required — minimum needed for matching
    keywords: Optional[str] = ""
    priority: Optional[str] = "Balanced"
    article_type: Optional[str] = "Scientific"


class JournalResult(BaseModel):
    name: str
    publisher: str
    impact_factor: float
    quartile: str
    avg_review_days: int
    frequency: str
    suitability_score: int
    scope_explanation: str
    strategy_tag: str
    url: str = ""
    aims: str = ""
    sample_paper: str = ""


class RecommendResponse(BaseModel):
    journals: List[JournalResult]
    total_analyzed: int
