from typing import List, Optional
from pydantic import BaseModel, Field


class SourceItem(BaseModel):
    label: str
    kind: str
    url: Optional[str] = None


class ResultCard(BaseModel):
    title: str
    relevance_score: int = Field(ge=0, le=100)
    findings: str
    impression: str
    tags: List[str]
    sources: List[SourceItem]


class QueryResponse(BaseModel):
    query_text: str
    normalized_query: str
    report: str
    results: List[ResultCard]
    history_label: str


class HistoryEntry(BaseModel):
    title: str
    subtitle: str


class HealthResponse(BaseModel):
    status: str
