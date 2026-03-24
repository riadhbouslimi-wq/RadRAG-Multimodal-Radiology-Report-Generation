from typing import List, Optional
from fastapi import FastAPI, File, Form, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from retrieval import compose_report, normalize_query, retrieve_candidates
from schema import HealthResponse, HistoryEntry, QueryResponse


app = FastAPI(title="RadRAG Demo API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

_HISTORY: List[HistoryEntry] = [
    HistoryEntry(title="Interpret this wrist X-ray (suspected fracture)", subtitle="+ 1 image")
]


@app.get("/api/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="ok")


@app.get("/api/history", response_model=List[HistoryEntry])
def history() -> List[HistoryEntry]:
    return _HISTORY[:20]


@app.post("/api/query", response_model=QueryResponse)
async def query(
    text: str = Form(default=""),
    image: Optional[UploadFile] = File(default=None),
) -> QueryResponse:
    normalized = normalize_query(text)
    results = retrieve_candidates(text)
    report = compose_report(text, results)

    history_title = text.strip() or (image.filename if image else "Untitled query")
    _HISTORY.insert(0, HistoryEntry(title=history_title[:48], subtitle="+ 1 image" if image else "text only"))
    del _HISTORY[20:]

    return QueryResponse(
        query_text=text,
        normalized_query=normalized,
        report=report,
        results=results,
        history_label=history_title,
    )
