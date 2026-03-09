```python
import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import RecommendRequest, RecommendResponse, JournalResult
from scorer import rank_journals
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="JournalFit AI API",
    description="Intelligent journal recommendation engine for researchers",
    version="1.1.0"
)

# Production-safe CORS handling
cors_origins = [
    origin.strip()
    for origin in os.getenv("CORS_ORIGINS", "http://localhost:3000").split(",")
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check():
    return {
        "status": "active",
        "service": "JournalFit AI Neural Scorer",
        "version": "1.1.0",
        "environment": os.getenv("ENVIRONMENT", "production")
    }


@app.post("/recommend", response_model=RecommendResponse)
def recommend(request: RecommendRequest):
    # Strict validation and sanitization
    area = request.area.strip()

    if not area or len(area) < 3:
        raise HTTPException(
            status_code=400,
            detail="Research area is too short or missing."
        )

    if len(area) > 500:
        raise HTTPException(
            status_code=400,
            detail="Research area exceeds maximum allowed length."
        )

    try:
        all_journals = rank_journals(
            title=(request.title or "").strip()[:500],
            area=area,
            keywords=(request.keywords or "").strip()[:500],
            priority=request.priority or "Balanced"
        )

    except Exception as e:
        print(f"Neural Scoring Error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="An internal ranking error occurred. Please try again."
        )

    top5 = all_journals[:5]
    more = all_journals[5:15]

    return RecommendResponse(
        journals=[JournalResult(**j) for j in (top5 + more)],
        total_analyzed=len(all_journals)
    )
```
