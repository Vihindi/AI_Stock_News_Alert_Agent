import schedule
import time
from sheets import fetch_tickers
from news import fetch_news
from gemini_eval import evaluate_impact
from telegram_bot import send_alert
from db_csv import init_csv, is_processed, mark_as_processed

RSS_FEEDS = [
    'https://finance.yahoo.com/news/rssindex',
    'https://www.cnbc.com/id/100003114/device/rss/rss.html'
]

def match_news(articles, tickers):
    matched = []
    for article in articles:
        for ticker in tickers:
            if ticker.upper() in article['title'].upper():
                matched.append({**article, 'ticker': ticker})
    return matched

def run_agent():
    print("🔄 Running Stock Alert Agent...")
    tickers = fetch_tickers()
    news_items = fetch_news(RSS_FEEDS)
    matched_news = match_news(news_items, tickers)

    for news in matched_news:
        fake_link = news['link']

        if is_processed(fake_link):
            continue

        impact = evaluate_impact(news['summary'])
        send_alert(news['ticker'], news['summary'], news['link'], impact)
        mark_as_processed(fake_link, news['ticker'], news['title'])

if __name__ == "__main__":
    init_csv()
    print("🚀 Stock Alert Agent with CSV running...")
    run_agent()
    print("⏰ Scheduled to run every 10 minutes...")
    schedule.every(0.2).minutes.do(run_agent)

    while True:
        schedule.run_pending()
        time.sleep(1)
