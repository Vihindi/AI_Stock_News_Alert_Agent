import feedparser

def fetch_news(rss_urls):
    articles = []
    for url in rss_urls:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            # Try summary first
            summary = entry.get('summary')
            # If not present, try description
            if not summary:
                summary = entry.get('description', '')
            # If still not present, fallback to title
            if not summary:
                summary = entry.get('title', '')
            print(f"Fetched article: {entry.get('title', 'No Title')} - Summary: {summary[:50]}...")  # Debugging line
            articles.append({
                'title': entry.get('title', ''),
                'summary': summary,
                'link': entry.get('link', '')
            })
    print(f"Total articles fetched: {len(articles)}")  # Debugging line
    return articles
