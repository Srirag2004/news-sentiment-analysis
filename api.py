"""FastAPI News Analysis and Audio Generation Service."""
import asyncio
import time

import uvicorn
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

from news_extractor import fetch_news
from utils import (
    process_articles, 
    generate_audio, 
    create_empty_result
)

# FastAPI Setup with performance optimizations
app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Cache to store recent results
NEWS_CACHE = {}
CACHE_EXPIRY = 60 * 15  # 15 minutes

@app.get("/news")
async def get_news(company: str = Query(..., description="Enter company name")):
    """
    Fetch and analyze news for a given company.

    Args:
        company (str): Name of the company to search for.

    Returns:
        dict: Comprehensive news analysis and sentiment report.
    """
    cache_key = company.lower().strip()
    current_time = time.time()

    # Return cached result if available and not expired
    if (cache_key in NEWS_CACHE and
            (current_time - NEWS_CACHE[cache_key]["timestamp"]) < CACHE_EXPIRY):
        return NEWS_CACHE[cache_key]["data"]

    # Fetch fresh data asynchronously
    articles = await asyncio.to_thread(fetch_news, company)

    if not articles:
        result = create_empty_result(company)
        NEWS_CACHE[cache_key] = {
            "data": result,
            "timestamp": current_time
        }
        return result

    # Sentiment and Topic Analysis
    sentiment_counts, structured_articles, analysis_result = process_articles(
        articles, company
    )

    # Generate audio as base64 string asynchronously
    audio_base64 = await generate_audio(analysis_result["Final Sentiment Analysis"])

    result = {
        "Company": company,
        "Articles": structured_articles,
        "Comparative Sentiment Score": {
            "Sentiment Distribution": sentiment_counts,
            "Coverage Differences": analysis_result.get("Coverage Differences", []),
            "Topic Overlap": analysis_result.get("Topic Overlap", {})
        },
        "Final Sentiment Analysis": analysis_result["Final Sentiment Analysis"],
        "Audio": "",
        "AudioBase64": audio_base64
    }

    # Cache the result
    NEWS_CACHE[cache_key] = {
        "data": result,
        "timestamp": current_time
    }

    return result

@app.get("/healthcheck")
async def healthcheck():
    """
    Endpoint to check if the service is running.

    Returns:
        dict: Service status and cache size.
    """
    return {"status": "healthy", "cache_size": len(NEWS_CACHE)}

@app.on_event("startup")
@app.on_event("shutdown")
async def cleanup_cache():
    """
    Clean expired cache entries periodically.
    """
    current_time = time.time()
    expired_keys = [
        key for key, value in NEWS_CACHE.items()
        if (current_time - value["timestamp"]) >= CACHE_EXPIRY
    ]
    for key in expired_keys:
        del NEWS_CACHE[key]

# Add this to make the app runnable with uvicorn directly
if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=7860, reload=True)
