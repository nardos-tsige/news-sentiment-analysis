# news-sentiment-analysis

**Predicting stock price moves with news sentiment analysis**

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

## 📌 Overview

This project analyzes whether financial news headlines can predict stock price movements. Built for Nova Financial Solutions as part of 10 Academy's AI Mastery program.

**Key findings:**
- News volume peaks at market open (10 AM) and Tuesdays
- Technology stocks (AAPL, TSLA, AMZN) dominate coverage  
- AAPL technical indicators show mildly bullish outlook (62/100)
- Hybrid sentiment-technical strategy recommended

## 📊 Repository Structure

├── notebooks/
│ ├── 01_eda_news.ipynb # EDA on 1.4M news articles
│ ├── 02_technical_indicators.ipynb # SMA, RSI, MACD, Bollinger Bands
│ └── 03_sentiment_correlation.ipynb # VADER sentiment + correlation
├── reports/
│ ├── INTERIM_REPORT.md
│ └── FINAL_REPORT.md
├── data/raw/ # Datasets (gitignored)
├── requirements.txt
└── LICENSE


## 🚀 Quick Start
```bash
# Clone
git clone https://github.com/nardos-tsige/news-sentiment-analysis.git

# Setup
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate
pip install -r requirements.txt

# Run notebooks
jupyter notebook notebooks/

📈 Key Results
Metric	                    |                Finding
Articles analyzed                          	 1,407,328
Unique stocks	                               6,204
AAPL technical score	                       62/100 (Mildly Bullish)
Golden Cross	                               ✅ Detected
Recommended strategy	                       Sentiment-Technical Hybrid

📝 Reports
(Interim Report)[https://github.com/nardos-tsige/news-sentiment-analysis/blob/main/reports/INTERIM_REPORT.md] - Task 1 & 2 findings

(Final Report)[https://github.com/nardos-tsige/news-sentiment-analysis/blob/main/reports/FINAL_REPORT.MD] - Complete analysis + recommendations

🔧 Technologies
Python, Pandas, NumPy

Matplotlib, Seaborn

VADER (NLTK) for sentiment

YFinance for stock data

Git & GitHub for version control

📄 License
MIT © (Nardos Tsige)[https://github.com/nardos-tsige]

Course: 10 Academy - Artificial Intelligence Mastery
Client: Nova Financial Solutions


---

## How to Add to GitHub:

### Method 1: VS Code (Quick)

```powershell
cd C:\Users\HP\news-sentiment-analysis

# Create README.md with the content above
# Then run:
git add README.md
git commit -m "docs: add professional README"
git push origin main
git push origin task-1
git push origin task-2
git push origin task-3
