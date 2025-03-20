# News Sentiment Analysis

## Overview
This project is a web-based application that extracts news articles related to a given company, performs sentiment analysis, and provides a summarized report. Additionally, it includes a text-to-speech (TTS) feature to convert the summaries into Hindi speech.

## Features
- **News Extraction:** Retrieves news articles based on the company name provided by the user.
- **Sentiment Analysis:** Categorizes articles into positive, negative, or neutral sentiment.
- **Summarization:** Generates concise summaries of the articles.
- **Comparative Analysis:** Compares sentiments across multiple articles for deeper insights.
- **Text-to-Speech (TTS):** Converts summarized text into Hindi audio.
- **User-Friendly Interface:** Built with Streamlit for easy interaction.
- **API Development:** Backend developed using FastAPI for seamless data processing.

## Tech Stack

### **Backend Framework**
- FastAPI
- Uvicorn (ASGI server)

### **Programming Language**
- Python

### **Machine Learning & NLP Libraries**
- Transformers (Hugging Face)
- VaderSentiment
- KeyBERT
- LangDetect
- Summarization Pipeline (Facebook BART)

### **Web Scraping & News Fetching**
- Feedparser

### **Frontend Framework**
- Streamlit

### **Data Visualization**
- Plotly Express
- Matplotlib
- Pandas

### **Audio Generation**
- gTTS (Google Text-to-Speech)
- Google Translator

### **Additional Libraries**
- Requests (HTTP requests)
- Base64 (encoding/decoding)
- Threading
- Re (Regular Expressions)

### **Deployment & Hosting**
- Hosted on Hugging Face Spaces: [News Sentiment Analysis](https://huggingface.co/spaces/srirag12/news-sentiment-analysis)
- Local development supported

### **Caching**
- In-memory dictionary-based caching

### **Middleware**
- CORS middleware (FastAPI)

## Installation & Setup

### **Prerequisites**
- Python 3.8+
- Required libraries (installed via `requirements.txt`)

### **Steps to Run Locally**
1. **Clone the Repository**
   ```bash
   git clone <GitHub-repo-link>
   cd News-Sentiment-Analysis
   ```
2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Application**
   ```bash
   streamlit run app.py
   ```

## API Development

### **API Endpoints**
- `/fetch_news`: Fetches and extracts news articles.
- `/analyze_sentiment`: Performs sentiment analysis.
- `/compare_sentiment`: Conducts comparative analysis.
- `/generate_tts`: Converts summarized text to Hindi speech.

### **API Usage**
- APIs can be accessed via Postman or any REST client.
- Example request using `curl`:
  ```bash
  curl -X POST "http:127.0.0.1:8026/news" -d '{"company": "Tesla"}' -H "Content-Type: application/json"
  ```

## Model Details

- **Summarization:** Facebook BART model (Hugging Face Transformers)
- **Sentiment Analysis:** VADER & DistilBERT
- **TTS:** Google Text-to-Speech (gTTS) for Hindi

## Assumptions & Limitations

- Only non-JavaScript-based news websites are scraped.
- Sentiment analysis accuracy depends on the dataset used.
- TTS output is currently limited to Hindi.

## Contribution Guidelines
- Fork the repository and create a feature branch.
- Follow PEP8 coding standards.
- Provide proper documentation in the code.
- Submit a pull request with a detailed description.

## License
This project is licensed under the MIT License.

## Acknowledgements
- Hugging Face for NLP models.
- Streamlit for UI development.
- Open-source TTS models for speech synthesis.
