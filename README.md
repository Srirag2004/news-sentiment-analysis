# Automated Company News Sentiment & Stock Prediction Application

## 1. Introduction & Problem Statement
In an era where financial markets are heavily influenced by real-time news, staying updated with company-related articles is crucial. However, manually scanning multiple news sources and analyzing sentiment trends is inefficient. This project automates the process by fetching company-specific news, summarizing key insights, conducting sentiment analysis, and predicting stock trends based on the overall sentiment. The application also offers text-to-speech (TTS) functionality in Hindi for enhanced accessibility.

## 2. Key Features
- **Automated News Retrieval:** Gathers the latest articles based on the input company name.  
- **Summarization Engine:** Extracts essential information using NLP-based models.  
- **Sentiment Assessment:** Classifies news as positive, negative, or neutral.  
- **Trend Analysis:** Compares sentiment across multiple articles.  
- **Stock Forecasting:** Predicts potential stock movement based on sentiment scores.  
- **Hindi TTS Conversion:** Converts summarized news into Hindi speech.  
- **Interactive UI:** Developed using Streamlit for seamless user experience.  
- **API-First Design:** Enables integration with external applications.  
- **Cloud Deployment:** Hosted on Hugging Face Spaces for easy access.  

## 3. Project Setup
Follow these steps to install and run the application.

### 3.1 Prerequisites
Ensure you have the following installed:
- Python 3.9+
- pip (Python package manager)
- Virtual Environment (venv)

### 3.2 Installation Steps
1. **Clone the repository:**  
   ```bash
   git clone https://github.com/Srirag2004/news-sentiment-analysis.git
   cd news-sentiment-analysis
   ```
2. **Create and Activate a Virtual Environment:**  
   ```bash
   python -m venv venv
   source venv/bin/activate   # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```
3. **Install Required Dependencies:**  
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the FastAPI Server:**  
   ```bash
   uvicorn backend:app --host 0.0.0.0 --port 8000 --reload
   ```
   
## 4. Model Details
### 4.1 Summarization Model
- Uses **NLP-based models** to extract essential information from news articles.
- Provides concise and relevant summaries for easy consumption.

### 4.2 Sentiment Analysis Model
- Utilizes **TextBlob** and **RoBERTa** to determine sentiment polarity.
- Classifies news into **positive, negative, or neutral** categories.
- Outputs confidence scores for each classification.

### 4.3 Text-to-Speech (TTS) Model
- Uses **gTTS (Google Text-to-Speech)** for converting summarized news into Hindi speech.
- Enhances accessibility by providing an audio version of news summaries.

## 5. API Development
### 5.1 Endpoints & Usage
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/fetch-news` | GET | Extracts news articles from sources |
| `/summarize` | POST | Summarizes the extracted news |
| `/analyze-sentiment` | POST | Provides sentiment analysis results |
| `/text_to_speech` | POST | Converts news into an audio file |

### 5.2 Accessing APIs via Postman
1. Open Postman.
2. Set the Base URL: `https://srirag12-news-api.hf.space/news?company=comapanyname`
3. Choose the relevant endpoint (GET or POST).
4. For POST requests, pass the JSON payload in the request body.
5. Click Send to receive the response.

### **Expected Output**
```{
    "Company": "tesla",
    "Articles": [
        {
            "Title": "Tesla owners are trading in their EVs at record levels, Edmunds says - CNBC",
            "Summary": "<a href=\"https://news.google.com/rss/articles/CBMipwFBVV95cUxPVU1YNm10bkFHTDliYUpLd2tqWmdpR0pkX2MzcWJrOUx6akllTVRVYlhYaHljZlV2NHZ5aVprRlhrZkZNVF9YQ2NIX3liRURBUUFSd094N2R1OTBCYlh1aDdqa29EQnNXdDZCNUdfenJsLVc0Uko0SDVhbnJpVGxtY1JpcEVPOE14bVV2NmpLcnVuRG1Zc2J3NTFCMDFzRzJDTjBZZW9CWdIBrAFBVV95cUxPbXBMS3FHaEVNTzVpV1dNdTJOaDZIeUFvM2xUM1B3elhBZUh2elVIUWpnUW5mVXkxNDcyclROV1BleWtVX2FIdXlWMk8tc0drQ1Z6dl9KamxGenlUcjg1X2dTdWl6QXVvWVlDWXdLMXZJWmY2bzVEd1J1WWhnZlBvblRJSl90MFJIcF9hcDhoQW5hdExjb0lkYmtFWkI5eEtNMVhJVXNKb2hibDJq?oc=5\" target=\"_blank\">Tesla owners are trading in their EVs at record levels, Edmunds says</a>&nbsp;&nbsp;<font color=\"#6f6f6f\">CNBC</font>",
            "Sentiment": "Neutral",
            "Topics": [
                "_blank tesla",
                "tesla",
                "trading evs",
                "tesla owners",
                "evs record"
            ]
        },
        {
            "Title": "Tesla Recalls Nearly All Cybertrucks Over Stainless Steel Panels Falling Off - The New York Times",
            "Summary": "<a href=\"https://news.google.com/rss/articles/CBMifEFVX3lxTE43aTloZ2UwSzVQSWdTMTRTSXp6Tko3VlFGVlJUcjlzdDdOMzhMZ0xvS1ppZkItLWxZX3ZxU2U3RUlSSlhVdDRWd1JTZ2RscUVka3JaUFMyWXpJU21GVl92OVpreGs4RHlCdjAzZnZqeUI2V1hzQ25GRVlXM2I?oc=5\" target=\"_blank\">Tesla Recalls Nearly All Cybertrucks Over Stainless Steel Panels Falling Off</a>&nbsp;&nbsp;<font color=\"#6f6f6f\">The New York Times</font>",
            "Sentiment": "Negative",
            "Topics": [
                "tesla recalls",
                "_blank tesla",
                "tesla",
                "cybertrucks stainless",
                "steel panels"
            ]
        },
        {
            "Title": "Tesla Recalls Most Cybertrucks - The Wall Street Journal",
            "Summary": "<a href=\"https://news.google.com/rss/articles/CBMif0FVX3lxTE92a3NRMVg5cGlDMVdNS1h1OFhLdmpYc0g4NWhBYmlqX0NfcWNoY0hySXV0UmJ3Q2xNMllrSkdOSlk0dk9jYWZQNDZrWUZjNDAtUm03TUhvTkhEaFNYMVhCeWZDVVo3dGN1TVRNQ2tEWDFOMV8teUE5ZlZZczFYbkE?oc=5\" target=\"_blank\">Tesla Recalls Most Cybertrucks</a>&nbsp;&nbsp;<font color=\"#6f6f6f\">The Wall Street Journal</font>",
            "Sentiment": "Neutral",
            "Topics": [
                "_blank tesla",
                "tesla",
                "tesla recalls",
                "recalls cybertrucks",
                "cybertrucks"
            ]
        },
        {
            "Title": "In latest blow to Tesla, regulators recall nearly all Cybertrucks - The Associated Press",
            "Summary": "<a href=\"https://news.google.com/rss/articles/CBMioAFBVV95cUxNWVlJUGRoV0hpRHhsV0liSXpjZlM5UHU0TnluclM1eTVTeDVsRUwyTjhMT3ZScGtrNl9BX1hQcE0zRWhWSW5pcXg5aF9uSF9yaVh2TVJMdjNjWEktenBCc09JRVpXWnRTVmVwRW9HaFdiUVYzQjl3ZnM4N3dSS190WG8wZjlGeWdQMmVzcVdaQWlhc2RoNTMwcnBOWjRKZ29E?oc=5\" target=\"_blank\">In latest blow to Tesla, regulators recall nearly all Cybertrucks</a>&nbsp;&nbsp;<font color=\"#6f6f6f\">The Associated Press</font>",
            "Sentiment": "Neutral",
            "Topics": [
                "tesla regulators",
                "tesla",
                "regulators recall",
                "cybertrucks",
                "nearly cybertrucks"
            ]
        },
        {
            "Title": "Tesla faces a ‘brand crisis tornado.’ The one guy who can fix it is MIA - CNN",
            "Summary": "<a href=\"https://news.google.com/rss/articles/CBMiiAFBVV95cUxPZXhtVEIyNWJ4RzlQMDJNYVJsRVJNOG9Xek95MENndk1TZExpdjhxMXBfcjlwMWd0X2NqSDVQSVA4M1EzTW5QLUNUSlZ2OWpkVF8wR05RYjA1X0MxdmhqeFRwTTZJdENxVFFnU2lhR2ZidllieG4wajdteE1ZYWtsV3pjVVZhcGdY0gF_QVVfeXFMUEZWS1QzZTBweVk3YU5UclRKYldCU2twcWJBVU9UNnpaSkx5UXNEazlSVlpUUWJFVHFtRFp3ZWxSWTQ3eW9xeUFNRnJzQUxFTWVJZXBGek1ZVC1BbHZjeVVKSG5BNGJuMFIzN0FMNDl2TmI2QTRtUVN1eE55Z0dKYw?oc=5\" target=\"_blank\">Tesla faces a ‘brand crisis tornado.’ The one guy who can fix it is MIA</a>&nbsp;&nbsp;<font color=\"#6f6f6f\">CNN</font>",
            "Sentiment": "Negative",
            "Topics": [
                "_blank tesla",
                "tesla faces",
                "tesla",
                "href",
                "crisis tornado"
            ]
        },
        {
            "Title": "US attorney general to bring charges for Tesla damage, citing ‘domestic terrorism’ - The Guardian US",
            "Summary": "<ol><li><a href=\"https://news.google.com/rss/articles/CBMiiAFBVV95cUxON2k5bUJaSGJNRjBFcURIWndSQkN4a2dnR0Fna1hid05waEwzOF9FaFlMSTBUQXotQk5aanpSeUFMQnFXU3FSSVBxMU5YWnZOMUlFeHEyd2FqLUNKakVMc0dFdEtyVllqbjFHUkxKTjN3NmVxTnRSNE0xakZBeHBFMG13dTF1MlBM?oc=5\" target=\"_blank\">US attorney general to bring charges for Tesla damage, citing ‘domestic terrorism’</a>&nbsp;&nbsp;<font color=\"#6f6f6f\">The Guardian US</font></li><li><a href=\"https://news.google.com/rss/articles/CBMingFBVV95cUxNRWtsajg1czZPUmhkVjJmNWxlSTQ1OXpYcmxhRGRvdGRHWFhVTGJsQWE3d3NfTi1UbC10SUxRZlRobDN1em1uR3FmcWl3dVY3bElOaWk0SDFJMy1Zd1hwVno3OVA2NlQ3T0FOWXhRMmhEU1lUQi0xd05hRktHZG53ZDJQa1FWbTRrVmlUeGt2cTgxb29EQXNJVFdGR3NOZw?oc=5\" target=\"_blank\">3 people face federal charges for Tesla attacks. Are such acts domestic terrorism?</a>&nbsp;&nbsp;<font color=\"#6f6f6f\">NPR</font></li><li><a href=\"https://news.google.com/rss/articles/CBMiugFBVV95cUxPd2w2OXUxemxKTjNpTkxCV003MFlzOW5HLVBnNGw3b0pNTzJuT01QNVprWnI1Slg2Z0VWNDlfTDRSemN0dXFFZ1BMWEFjQ3hZcUJOMjhodmYzZjlYVjRwMGg5RnFjdWFBVGNESmVrMkROM2V0SnZDelN5Yms5c1RYcE5TdlUzTEpEVHhINk4wWlJ1TXlidHUybkM5UFUyWkNINzdMaVkzV2ZnZm1RZWZPcHFtdXRHY3o1TGfSAb8BQVVfeXFMTlNZMDRzUDl2UVFxT2Ffb09RQmtuYU1GQkxpVzR4OWw4M3hfLTVZeTBRMHhGc29nNXpZdzh5NzNFTWItZEVSME9TVFozaFEyN0R1YjJNVlk1Z0t5VHBqSVcwdkRyeUpqOTJXRGdOSEtIUnAtbTZNV0NuQ2pnUTRTdzE5VHBwZTA5MTlZdXB1U1dvcHQwWDJGTWdLMDRNeDVpaExPMXpFWGxwNFppckgwSmRJYkRkc0JRRjZ4VlZfRFk?oc=5\" target=\"_blank\">Dems who have spoken passionately against domestic terrorism go silent as Tesla torchers are charged</a>&nbsp;&nbsp;<font color=\"#6f6f6f\">Fox News</font></li></ol>",
            "Sentiment": "Negative",
            "Topics": [
                "tesla attacks",
                "domestic terrorism",
                "attacks acts",
                "charges tesla",
                "tesla damage"
            ]
        },
        {
            "Title": "Lutnick urges Fox News viewers to buy Tesla stock, raising ethics questions - The Washington Post",
            "Summary": "<ol><li><a href=\"https://news.google.com/rss/articles/CBMiwgFBVV95cUxNcGU1RkRnVE1FXzFiMXo3REJKQUE5anZmNFJ4SHVpU2RfRFZGemZGVjdLUWdpd0xZWnFvYVltZmFaZ0lqTEM5TjVwMHV1TFRROXFiR191SmNCelptNEF2enZWRGJtMDE2X3Bwdkp6d1pHc1JJTXJiR2JJR1VYUVpOUFFZaU4xc2Yza2RFTUF6YjVJajVnQ0JBbk1EaVpSS05RSzBqclZIa3AydHd0TUVqYmZCeFhnZWlHTEN4dk5tMXVqQQ?oc=5\" target=\"_blank\">Lutnick urges Fox News viewers to buy Tesla stock, raising ethics questions</a>&nbsp;&nbsp;<font color=\"#6f6f6f\">The Washington Post</font></li><li><a href=\"https://news.google.com/rss/articles/CBMie0FVX3lxTFBtZTlnVS1heVJCVTZSLUJqS0pJa0lobm9PZWZ2SkR3ZlN1LWV3bEtuV2szRG1ZcFpyWkMtTEdBY0ZGcWNSNVZ4eGI4VGpvV2dkZXIwaHc4cjllWWI1VnM2MkZNSG5KLU8xWFh1aHRLa1JDdXgtaTdnemJtVQ?oc=5\" target=\"_blank\">Lutnick’s Pitch to Buy Tesla Stock Is Unprecedented and Alarming, Historians Say</a>&nbsp;&nbsp;<font color=\"#6f6f6f\">Barron's</font></li><li><a href=\"https://news.google.com/rss/articles/CBMiuAFBVV95cUxOcGcwQzlEOExuRGJBWUhkVzdhSnIyYVlwNEJwOFBTVllpbl9lNDg1RHEtU0xSSmhFYVJaZGlfTTlPTVFCZzhiZHhzTUJ2ek9MZ1NNMURnYTdKU3YxaDJDMHo2TkNKRUZkQzBRWVRJOFN2bVdDWWg4TTd6ek8wNGYwYTE2WmRqWlBkUW1WYmprNFRTd3R2WUNOTFdTYXpZTEJ0S1haUzJGV18wY2NNSE1pNGFQMHcxU2FK?oc=5\" target=\"_blank\">Musk Tells Tesla Employees Hang On to Stock After 50% Plunge</a>&nbsp;&nbsp;<font color=\"#6f6f6f\">Bloomberg</font></li></ol>",
            "Sentiment": "Negative",
            "Topics": [
                "tesla stock",
                "tells tesla",
                "tesla employees",
                "buy tesla",
                "stock unprecedented"
            ]
        },
        {
            "Title": "80 Teslas damaged at Hamilton dealership, largest car vandalism reported in Canada against the U.S. company - CBC.ca",
            "Summary": "<a href=\"https://news.google.com/rss/articles/CBMiiwFBVV95cUxQS3hVbnFLN2ltXzV5Ui1Jc0s5Y0EwSjZEeV8yQlAyTHJSYm8ta1hBcTFfVnpyX2lCX1JYZkJiZlA3STVUU0Nfb2Z1Z2ZKMU5xeTdLeEJHUlFuRFA0RnBMbEZDX1VXZXhxV2tid3FYYmo2X25uaWI0MFBOT1dsejdTVFhfWnBCbE1RUzJJ0gFHQVVfeXFMTVMyRWotRHFmdEtSWTNnNUdVZ241QTlWbWdOeTctWGJ0Ry1vcTY1cWt1REVIdjJUZ2lMczBVWnQ3cTJWVWtYLVU?oc=5\" target=\"_blank\">80 Teslas damaged at Hamilton dealership, largest car vandalism reported in Canada against the U.S. company</a>&nbsp;&nbsp;<font color=\"#6f6f6f\">CBC.ca</font>",
            "Sentiment": "Negative",
            "Topics": [
                "teslas damaged",
                "car vandalism",
                "damaged hamilton",
                "teslas",
                "vandalism reported"
            ]
        },
        {
            "Title": "Tesla Vandalism Surges in Canada as Trump and Musk Face Backlash - The New York Times",
            "Summary": "<a href=\"https://news.google.com/rss/articles/CBMijAFBVV95cUxQLTNHZU5GZXl5YVluUmpzdkxvR3oxY2FxZWxhVjl2UTJWTXpWY0FoX1VKMTRsTV9fbFMwMHFDMmVnbVVIU1lLdnZNTHA3WHhVNDVpQ2dCNUlMTkJzOVNKSFhtRGNZNGs1OHdXOW00TThxREZfaWxnQTQtX3BsUWJ1ems2TU1ucmZabUlvZg?oc=5\" target=\"_blank\">Tesla Vandalism Surges in Canada as Trump and Musk Face Backlash</a>&nbsp;&nbsp;<font color=\"#6f6f6f\">The New York Times</font>",
            "Sentiment": "Neutral",
            "Topics": [
                "tesla vandalism",
                "_blank tesla",
                "trump musk",
                "musk face",
                "href"
            ]
        },
        {
            "Title": "Tesla owners alarmed by Dogequest website listing personal information - NBC News",
            "Summary": "<a href=\"https://news.google.com/rss/articles/CBMingFBVV95cUxQa3NBMkxkS3pYQzBVVlVqWWVTYmlGem51cFJJVGJnMjg0WFhPMlByTUh0WXh0c3dHRDVFNVNtQjlpdkFYTGNmeXdjenNzVzJTV0xzXzVEbG9uSTM4ekdvSF96LUxxalE2S2dOR0dCTTRpd3dXU1VjdTRCVmkxS0xUdkJFNlNqRVFxcXNvaFR6NXRhdW9YU2QySk9wYnlUUdIBVkFVX3lxTE1FcEJlaVFKLS1vcnZxZFdQM05OSklPa0R4QlpNNVg1bHVEV3lJTDZmWW5BNW13QWtsMS02R1lYdFNSSUdtOVJ1MU9GTFN4aXpFdU5MRmZB?oc=5\" target=\"_blank\">Tesla owners alarmed by Dogequest website listing personal information</a>&nbsp;&nbsp;<font color=\"#6f6f6f\">NBC News</font>",
            "Sentiment": "Negative",
            "Topics": [
                "_blank tesla",
                "tesla owners",
                "tesla",
                "dogequest website",
                "alarmed dogequest"
            ]
        }
    ],
    "Comparative Sentiment Score": {
        "Sentiment Distribution": {
            "Positive": 0,
            "Negative": 6,
            "Neutral": 4
        },
        "Coverage Differences": [
            {
                "Comparison": "Article 1 covers ['_blank tesla', 'tesla', 'trading evs', 'tesla owners', 'evs record'], while Article 2 focuses on ['tesla recalls', '_blank tesla', 'tesla', 'cybertrucks stainless', 'steel panels'].",
                "Sentiment Impact": "Article 1 has a Neutral sentiment, while Article 2 has a Negative sentiment.",
                "Stock Impact": "This may create uncertainty in stock trends."
            },
            {
                "Comparison": "Article 2 covers ['tesla recalls', '_blank tesla', 'tesla', 'cybertrucks stainless', 'steel panels'], while Article 3 focuses on ['_blank tesla', 'tesla', 'tesla recalls', 'recalls cybertrucks', 'cybertrucks'].",
                "Sentiment Impact": "Article 2 has a Negative sentiment, while Article 3 has a Neutral sentiment.",
                "Stock Impact": "This may create uncertainty in stock trends."
            },
            {
                "Comparison": "Article 3 covers ['_blank tesla', 'tesla', 'tesla recalls', 'recalls cybertrucks', 'cybertrucks'], while Article 4 focuses on ['tesla regulators', 'tesla', 'regulators recall', 'cybertrucks', 'nearly cybertrucks'].",
                "Sentiment Impact": "Article 3 has a Neutral sentiment, while Article 4 has a Neutral sentiment.",
                "Stock Impact": "The sentiment consistency may stabilize stock movements."
            },
            {
                "Comparison": "Article 4 covers ['tesla regulators', 'tesla', 'regulators recall', 'cybertrucks', 'nearly cybertrucks'], while Article 5 focuses on ['_blank tesla', 'tesla faces', 'tesla', 'href', 'crisis tornado'].",
                "Sentiment Impact": "Article 4 has a Neutral sentiment, while Article 5 has a Negative sentiment.",
                "Stock Impact": "This may create uncertainty in stock trends."
            },
            {
                "Comparison": "Article 5 covers ['_blank tesla', 'tesla faces', 'tesla', 'href', 'crisis tornado'], while Article 6 focuses on ['tesla attacks', 'domestic terrorism', 'attacks acts', 'charges tesla', 'tesla damage'].",
                "Sentiment Impact": "Article 5 has a Negative sentiment, while Article 6 has a Negative sentiment.",
                "Stock Impact": "The sentiment consistency may stabilize stock movements."
            },
            {
                "Comparison": "Article 6 covers ['tesla attacks', 'domestic terrorism', 'attacks acts', 'charges tesla', 'tesla damage'], while Article 7 focuses on ['tesla stock', 'tells tesla', 'tesla employees', 'buy tesla', 'stock unprecedented'].",
                "Sentiment Impact": "Article 6 has a Negative sentiment, while Article 7 has a Negative sentiment.",
                "Stock Impact": "The sentiment consistency may stabilize stock movements."
            },
            {
                "Comparison": "Article 7 covers ['tesla stock', 'tells tesla', 'tesla employees', 'buy tesla', 'stock unprecedented'], while Article 8 focuses on ['teslas damaged', 'car vandalism', 'damaged hamilton', 'teslas', 'vandalism reported'].",
                "Sentiment Impact": "Article 7 has a Negative sentiment, while Article 8 has a Negative sentiment.",
                "Stock Impact": "The sentiment consistency may stabilize stock movements."
            },
            {
                "Comparison": "Article 8 covers ['teslas damaged', 'car vandalism', 'damaged hamilton', 'teslas', 'vandalism reported'], while Article 9 focuses on ['tesla vandalism', '_blank tesla', 'trump musk', 'musk face', 'href'].",
                "Sentiment Impact": "Article 8 has a Negative sentiment, while Article 9 has a Neutral sentiment.",
                "Stock Impact": "This may create uncertainty in stock trends."
            },
            {
                "Comparison": "Article 9 covers ['tesla vandalism', '_blank tesla', 'trump musk', 'musk face', 'href'], while Article 10 focuses on ['_blank tesla', 'tesla owners', 'tesla', 'dogequest website', 'alarmed dogequest'].",
                "Sentiment Impact": "Article 9 has a Neutral sentiment, while Article 10 has a Negative sentiment.",
                "Stock Impact": "This may create uncertainty in stock trends."
            }
        ],
        "Topic Overlap": {
            "Common Topics": [
                "_blank tesla",
                "href",
                "cybertrucks",
                "tesla owners",
                "tesla",
                "tesla recalls"
            ],
            "Unique Topics in Article 1": [
                "trading evs",
                "evs record"
            ],
            "Unique Topics in Article 2": [
                "cybertrucks stainless",
                "steel panels"
            ],
            "Unique Topics in Article 3": [
                "recalls cybertrucks"
            ],
            "Unique Topics in Article 4": [
                "nearly cybertrucks",
                "tesla regulators",
                "regulators recall"
            ],
            "Unique Topics in Article 5": [
                "crisis tornado",
                "tesla faces"
            ],
            "Unique Topics in Article 6": [
                "attacks acts",
                "tesla damage",
                "tesla attacks",
                "domestic terrorism",
                "charges tesla"
            ],
            "Unique Topics in Article 7": [
                "tells tesla",
                "stock unprecedented",
                "tesla stock",
                "buy tesla",
                "tesla employees"
            ],
            "Unique Topics in Article 8": [
                "teslas",
                "car vandalism",
                "teslas damaged",
                "vandalism reported",
                "damaged hamilton"
            ],
            "Unique Topics in Article 9": [
                "musk face",
                "tesla vandalism",
                "trump musk"
            ],
            "Unique Topics in Article 10": [
                "dogequest website",
                "alarmed dogequest"
            ]
        }
    },
    "Final Sentiment Analysis": "Final Sentiment Analysis: tesla's latest news coverage is mostly Negative. Stock prices may decrease.",
    "Audio": "summary.mp3"
    
}
```

## 6. API Usage (Third-Party Integrations)
### 6.1 RSS Feed Parsing (`feedparser`)
- **Purpose:** Extracts news articles from sources like CNN, BBC, etc.
- **Library Used:** `feedparser`
- **Integration:** Used in `news_scraper.py` to fetch real-time news.

### 6.2 Language Detection (`langdetect`)
- **Purpose:** Detects the language of an article before processing.
- **Library Used:** `langdetect`
- **Integration:** Helps filter out unsupported languages.

## 7. Assumptions & Limitations
### 7.1 Assumptions
- All news articles are well-formatted and in English.
- Sentiment analysis works accurately for general news content.
- The summarization model provides concise yet informative outputs.
- The TTS model accurately converts text to Hindi speech.

### 7.2 Limitations
- Sentiment analysis might not be 100% accurate for financial news due to nuanced language.
- Stock movement predictions are based purely on sentiment and do not factor in external financial indicators.
- TTS is limited to Hindi and may need enhancements for better pronunciation.

## 8. Conclusion & Future Scope
This project simplifies real-time financial news tracking and sentiment-based stock forecasting. By integrating AI-powered NLP, sentiment analysis, and Hindi TTS, the application provides users with valuable insights for informed decision-making.

### Future Enhancements:
- Support for multiple languages in TTS.
- Integration with additional financial APIs for stock data validation.
- Enhanced deep learning models for better sentiment accuracy.

## 9. Deployment & Resources
- **Deployment Link:** [Hugging Face Spaces](https://huggingface.co/spaces/srirag12/news-sentiment-analysis)
- **GitHub Repository:** [GitHub](https://github.com/Srirag2004/news-sentiment-analysis)
- **License:** MIT
- **Contributors:** Srirag Punnamaraju
