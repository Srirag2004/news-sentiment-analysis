"""Utility Functions for News Analysis"""
import base64
import asyncio
from io import BytesIO
from collections import Counter

from deep_translator import GoogleTranslator
from gtts import gTTS

def _get_stock_prediction(dominant_sentiment: str) -> str:
    """
    Predict stock movement based on dominant sentiment.

    Args:
        dominant_sentiment (str): Dominant sentiment.

    Returns:
        str: Stock price prediction.
    """
    if dominant_sentiment == "Positive":
        return "Stock prices may increase."
    elif dominant_sentiment == "Negative":
        return "Stock prices may decrease."
    return "Stock prices may remain constant."

def _generate_coverage_differences(articles: list) -> list:
    """
    Generate coverage differences between articles.

    Args:
        articles (list): List of news articles.

    Returns:
        list: Coverage differences and sentiment impacts.
    """
    if len(articles) <= 1:
        return []

    return [
        {
            "Comparison": (
                f"Article {i+1} covers {articles[i]['topics']}, "
                f"while Article {i+2} focuses on {articles[i+1]['topics']}."
            ),
            "Sentiment Impact": (
                f"Article {i+1} has a {articles[i]['sentiment']} sentiment, "
                f"while Article {i+2} has a {articles[i+1]['sentiment']} sentiment."
            ),
            "Stock Impact": (
                "This may create uncertainty in stock trends."
                if articles[i]['sentiment'] != articles[i+1]['sentiment']
                else "The sentiment consistency may stabilize stock movements."
            )
        }
        for i in range(len(articles) - 1)
    ]

async def generate_audio(text: str) -> str:
    """
    Generate audio in a non-blocking way.

    Args:
        text (str): Text to convert to audio.

    Returns:
        str: Base64 encoded audio.
    """
    try:
        # First try to translate to Hindi
        try:
            translated_summary = await asyncio.to_thread(
                GoogleTranslator(source="en", target="hi").translate,
                text
            )
        except Exception:
            translated_summary = text  # Fall back to English if translation fails

        # Generate audio data in memory
        mp3_fp = BytesIO()
        tts = await asyncio.to_thread(
            gTTS,
            text=translated_summary,
            lang="hi" if translated_summary != text else "en"
        )
        await asyncio.to_thread(tts.write_to_fp, mp3_fp)
        mp3_fp.seek(0)

        # Convert to base64
        audio_bytes = await asyncio.to_thread(mp3_fp.read)
        return base64.b64encode(audio_bytes).decode('utf-8')
    except Exception as e:
        print(f"Error generating audio: {str(e)}")
        return ""

def process_articles(articles: list, company: str) -> tuple:
    """
    Process articles for sentiment and topic analysis.

    Args:
        articles (list): List of news articles.
        company (str): Company name.

    Returns:
        tuple: Sentiment counts, structured articles, and analysis results.
    """
    from news_sentiment_analysis import analyze_sentiment  # Local import to avoid circular dependency

    sentiment_counts = {"Positive": 0, "Negative": 0, "Neutral": 0}
    structured_articles = []
    all_topics = []
    topic_sets = []
    unique_topics = {}

    for article in articles:
        sentiment = analyze_sentiment(article["summary"])
        article["sentiment"] = sentiment
        sentiment_counts[sentiment] += 1
        all_topics.extend(article["topics"])
        topic_sets.append(set(article["topics"]))

    # Topic frequency and analysis
    topic_freq = Counter(all_topics)
    common_topics = {
        topic for topic, freq in topic_freq.items() if freq > 1
    } or set(topic_freq.keys())

    for i, article in enumerate(articles):
        unique_topics[f"Unique Topics in Article {i+1}"] = list(
            set(article["topics"]) - common_topics
        )

    # Coverage differences
    coverage_differences = _generate_coverage_differences(articles)

    # Structured articles
    for article in articles:
        structured_articles.append({
            "Title": article["title"],
            "Summary": article["summary"],
            "Sentiment": article["sentiment"],
            "Topics": article["topics"],
        })

    # Sentiment and stock prediction
    dominant_sentiment = max(sentiment_counts, key=sentiment_counts.get)
    stock_prediction = _get_stock_prediction(dominant_sentiment)
    sentiment_summary = (
        f"Final Sentiment Analysis: {company}'s latest news coverage is "
        f"mostly {dominant_sentiment}. {stock_prediction}"
    )

    return sentiment_counts, structured_articles, {
        "Final Sentiment Analysis": sentiment_summary,
        "Coverage Differences": coverage_differences,
        "Topic Overlap": {
            "Common Topics": list(common_topics),
            **unique_topics
        }
    }

def create_empty_result(company: str) -> dict:
    """
    Create an empty result when no articles are found.

    Args:
        company (str): Company name.

    Returns:
        dict: Empty result dictionary.
    """
    return {
        "Company": company,
        "Articles": [],
        "Comparative Sentiment Score": {
            "Sentiment Distribution": {"Positive": 0, "Negative": 0, "Neutral": 0},
            "Topic Overlap": {"Common Topics": [], "Unique Topics": {}}
        },
        "Final Sentiment Analysis": f"No significant news coverage found for {company}.",
        "Audio": "",
        "AudioBase64": ""
    }
