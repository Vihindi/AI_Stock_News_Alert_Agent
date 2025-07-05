import os

import streamlit as st
from sheets import fetch_tickers
from news import fetch_news
from streamlit_gemini import evaluate_impact
from telegram_bot import send_alert
from db_csv import init_csv, is_processed, mark_as_processed

# RSS feeds
RSS_FEEDS = [
    'https://finance.yahoo.com/news/rssindex',
    'https://www.cnbc.com/id/100003114/device/rss/rss.html'
]

# Ticker to company name mapping
TICKER_TO_NAME = {
    "AAPL": "Apple",
    "MSFT": "Microsoft",
    "GOOGL": "Google",
    "TSLA": "Tesla",
    "AMZN": "Amazon",
    "NFLX": "Netflix",
}

def match_news(articles, tickers):
    matched = []
    for article in articles:
        for ticker in tickers:
            company_name = TICKER_TO_NAME.get(ticker.upper(), "")
            if company_name and company_name.upper() in article['title'].upper():
                matched.append({**article, 'ticker': ticker})
    return matched

# Initialize CSV "DB"
init_csv()

st.title("📈 AI Stock News Alert Agent")

if st.button("Fetch and Display Matched News"):
    tickers = fetch_tickers()
    news_items = fetch_news(RSS_FEEDS)
    matched_news = match_news(news_items, tickers)

    if not matched_news:
        st.warning("No matched news found.")
    else:
        st.success(f"Total matched articles: {len(matched_news)}")

        new_articles = []
        processed_articles = []

        for news in matched_news:
            link = news['link']
            if is_processed(link):
                processed_articles.append(news)
            else:
                new_articles.append(news)

        # Show new articles
        st.subheader("🟢 New Articles")
        if not new_articles:
            st.info("No new articles to show.")
        else:
            for news in new_articles:
                impact = evaluate_impact(news['summary'])
                with st.expander(f"{news['ticker']} — {news['title']}"):
                    st.write(f"**Summary:** {news['summary']}")
                    st.write(f"[Read full article]({news['link']})")
                    st.write(f"**Impact Score:** {'🚨' * impact} ({impact})")

                    if st.button(f"Send Alert for {news['ticker']}", key=news['link']):
                        send_alert(news['ticker'], news['summary'], news['link'], impact)
                        mark_as_processed(news['link'], news['ticker'], news['title'])
                        st.success("✅ Alert sent and marked as processed!")

        # Show processed articles
        st.subheader("⚪ Already Processed Articles")
        if not processed_articles:
            st.info("No processed articles yet.")
        else:
            for news in processed_articles:
                with st.expander(f"{news['ticker']} — {news['title']}"):
                    st.write(f"**Summary:** {news['summary']}")
                    st.write(f"[Read full article]({news['link']})")
                    st.write("✅ Already processed.")

else:
    st.info("Click **Fetch and Display Matched News** to load articles.")
