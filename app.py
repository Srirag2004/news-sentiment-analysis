import os
import threading
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import requests
import streamlit as st
import uvicorn
from backendapis import app
from collections import Counter
import re
import base64

def run_fastapi() -> None:
    uvicorn.run(app, host="127.0.0.1", port=8026)

# Start FastAPI server in a background thread
BACKEND_THREAD = threading.Thread(target=run_fastapi, daemon=True)
BACKEND_THREAD.start()

# Configure page settings
st.set_page_config(
    page_title="Sentiment Analysis Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# New CSS with Bootstrap and custom design elements
st.markdown("""
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet">
<style>
body {
    font-family: 'Roboto', sans-serif;
    background-color: #E3F2FD;
    color: #333;
}
.stApp {
    background-color: #E3F2FD;
}
.header {
    background-color: #2c3e50;
    color: #ecf0f1;
    padding: 20px;
    margin-bottom: 20px;
    border-radius: 5px;
}
.article-card {
    transition: all 0.3s ease;
    margin-bottom: 20px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    height: 100%;
}
.article-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 15px rgba(0,0,0,0.15);
}
.sentiment-badge {
    display: inline-block;
    padding: 5px 10px;
    border-radius: 5px;
    font-weight: bold;
}
.sentiment-positive {
    background-color: #28a745;
    color: white;
}
.sentiment-neutral {
    background-color: #6c757d;
    color: white;
}
.sentiment-negative {
    background-color: #dc3545;
    color: white;
}
.audio-container {
    background-color: #f8f9fa;
    border-radius: 10px;
    padding: 20px;
    margin-bottom: 20px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

# Set up API base URL
API_BASE_URL = "http://127.0.0.1:8026"

# Function to convert company name with spaces to underscore format
def format_company_name(name):
    # Remove special characters but keep the words intact
    cleaned_name = re.sub(r'[^\w\s]', '', name)
    # Replace spaces with underscores while keeping original words
    formatted_name = cleaned_name.strip().replace(' ', '_')
    return formatted_name

# Header Section
st.markdown("""
<div class="header">
    <h1>Sentiment Analysis Dashboard</h1>
    <p>Discover insights from company news with our AI-powered sentiment analysis tool.</p>
</div>
""", unsafe_allow_html=True)

# Initialize session state for analyze button
if 'analyze_clicked' not in st.session_state:
    st.session_state.analyze_clicked = False

# Search Bar
st.markdown('<div class="container"><div class="row"><div class="col-md-12">', unsafe_allow_html=True)
company_name = st.text_input("", placeholder="Enter company name (e.g., Tesla, Microsoft)", label_visibility="collapsed", key="company_input")
analyze_button = st.button("Analyze")
st.markdown('</div></div></div>', unsafe_allow_html=True)

# Main Analysis Logic
if analyze_button:
    # Set the flag to trigger page refresh
    st.session_state.analyze_clicked = True
    st.rerun()

# Only proceed with analysis after page refresh
if st.session_state.analyze_clicked and company_name:
    # Reset the flag
    st.session_state.analyze_clicked = False

    # Format company name
    formatted_company_name = format_company_name(company_name)

    with st.spinner("Fetching news and analyzing sentiment..."):
        try:
            response = requests.get(f"{API_BASE_URL}/news", params={"company": formatted_company_name})
            if response.status_code == 200:
                data = response.json()
                
                if not data.get("Articles"):
                    st.warning(f"No significant news coverage found for {company_name}.")
                else:
                    df = pd.DataFrame(data["Articles"])
                    sentiment_mapping = {"Positive": 1, "Neutral": 0, "Negative": -1}
                    df["sentiment_score"] = df["Sentiment"].map(sentiment_mapping)
                    
                    sentiment_counts = df["Sentiment"].value_counts()
                    total_articles = len(df)
                    positive_percent = round((sentiment_counts.get("Positive", 0) / total_articles) * 100, 1)
                    negative_percent = round((sentiment_counts.get("Negative", 0) / total_articles) * 100, 1)
                    neutral_percent = round((sentiment_counts.get("Neutral", 0) / total_articles) * 100, 1)
                    
                    # Sentiment Overview
                    st.markdown('<div class="container">', unsafe_allow_html=True)
                    st.markdown('<h2>Sentiment Overview</h2>', unsafe_allow_html=True)
                    fig_pie = px.pie(
                        names=sentiment_counts.index, 
                        values=sentiment_counts.values,
                        color=sentiment_counts.index,
                        color_discrete_map={
                            "Positive": "#2ecc71", 
                            "Neutral": "#95a5a6", 
                            "Negative": "#e74c3c"
                        },
                        hole=0.3
                    )
                    st.plotly_chart(fig_pie, use_container_width=True)
                    
                    # Sentiment Analysis Summary
                    st.markdown('<h2>Sentiment Analysis Summary</h2>', unsafe_allow_html=True)
                    final_sentiment = data["Final Sentiment Analysis"]
                    st.write(final_sentiment)
                    
                    # Stock Recommendation
                    st.markdown('<h2>Stock Recommendation</h2>', unsafe_allow_html=True)
                    stock_rec_fig = px.line(
                        x=['🟢Buy', '🟡Hold', '🔴Sell'], 
                        y=[positive_percent, neutral_percent, negative_percent],
                        markers=True,
                        labels={'x': 'Recommendation', 'y': 'Percentage'},
                        title='Stock Recommendation Trend'
                    )
                    stock_rec_fig.update_traces(line=dict(color='#3498db'))
                    st.plotly_chart(stock_rec_fig, use_container_width=True)
                    
                    # Audio Summary
                    st.markdown('<h2>Audio Summary</h2>', unsafe_allow_html=True)
                    st.markdown('<div class="container audio-container">', unsafe_allow_html=True)
                    audio_base64 = data.get('AudioBase64', '')
                    if audio_base64:
                        # Decode base64 audio
                        audio_bytes = base64.b64decode(audio_base64)
                        
                        # Display audio player
                        st.audio(audio_bytes, format='audio/mp3')
                    else:
                        st.warning("Audio summary not available.")
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                    # News Articles with Bootstrap Cards
                    st.markdown('<h2>News Articles</h2>', unsafe_allow_html=True)
                    
                    # Ensure we always have an even number of articles
                    articles = data["Articles"]
                    if len(articles) % 2 != 0:
                        articles.append(None)  # Add a None to make it even
                    
                    # Create rows with 2 cards each
                    for i in range(0, len(articles), 2):
                        st.markdown('<div class="row">', unsafe_allow_html=True)
                        
                        # First card in the row
                        if articles[i] is not None:
                            article = articles[i]
                            # Determine sentiment badge class
                            if article['Sentiment'] == 'Positive':
                                sentiment_badge_class = 'sentiment-positive'
                            elif article['Sentiment'] == 'Neutral':
                                sentiment_badge_class = 'sentiment-neutral'
                            else:
                                sentiment_badge_class = 'sentiment-negative'
                            
                            st.markdown(f'''
                            <div class="col-md-6 mb-4">
                                <div class="card article-card h-100">
                                    <div class="card-body d-flex flex-column">
                                        <h5 class="card-title">{article['Title']}</h5>
                                        <p class="card-text flex-grow-1">{article['Summary']}</p>
                                        <div class="mt-auto">
                                            <span class="sentiment-badge {sentiment_badge_class}">
                                                {article['Sentiment']} Sentiment
                                            </span>
                                            <p class="card-text mt-2">
                                                <small class="text-muted">Topics: {', '.join(article['Topics'])}</small>
                                            </p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            ''', unsafe_allow_html=True)
                        
                        # Second card in the row
                        if articles[i+1] is not None:
                            article = articles[i+1]
                            # Determine sentiment badge class
                            if article['Sentiment'] == 'Positive':
                                sentiment_badge_class = 'sentiment-positive'
                            elif article['Sentiment'] == 'Neutral':
                                sentiment_badge_class = 'sentiment-neutral'
                            else:
                                sentiment_badge_class = 'sentiment-negative'
                            
                            st.markdown(f'''
                            <div class="col-md-6 mb-4">
                                <div class="card article-card h-100">
                                    <div class="card-body d-flex flex-column">
                                        <h5 class="card-title">{article['Title']}</h5>
                                        <p class="card-text flex-grow-1">{article['Summary']}</p>
                                        <div class="mt-auto">
                                            <span class="sentiment-badge {sentiment_badge_class}">
                                                {article['Sentiment']} Sentiment
                                            </span>
                                            <p class="card-text mt-2">
                                                <small class="text-muted">Topics: {', '.join(article['Topics'])}</small>
                                            </p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            ''', unsafe_allow_html=True)
                        
                        st.markdown('</div>', unsafe_allow_html=True)
                    
                    # Common Keywords
                    st.markdown('<h2>Common Keywords in Articles</h2>', unsafe_allow_html=True)
                    text = " ".join(article for article in df["Summary"].fillna("") if article)
                    if text.strip():
                        words = re.findall(r'\w+', text.lower())
                        stop_words = set(['the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by'])
                        filtered_words = [word for word in words if word not in stop_words]
                        word_counts = Counter(filtered_words)
                        top_words = dict(sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:10])
                        
                        fig_bar = go.Figure(data=[
                            go.Bar(x=list(top_words.keys()), y=list(top_words.values()), marker_color='#3498db')
                        ])
                        fig_bar.update_layout(xaxis_title='Words', yaxis_title='Frequency')
                        st.plotly_chart(fig_bar, use_container_width=True)
                    else:
                        st.info("No descriptions available to generate a word cloud.")
                    
                    st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.error(f"Failed to fetch data: {response.status_code}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
elif st.session_state.analyze_clicked:
    st.warning("Please enter a company name.")
    # Reset the flag
    st.session_state.analyze_clicked = False

# Footer
st.markdown("""
<div class="container">
    <div class="text-center mt-4 mb-4">
        © 2025 Sentiment Analysis Dashboard | created by srirag
    </div>
</div>
""", unsafe_allow_html=True)

if __name__ == "__main__":
    pass