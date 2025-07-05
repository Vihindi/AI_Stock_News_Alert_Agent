import csv

def fetch_tickers():
    tickers = set()
    with open("processed_articles.csv", mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            tickers.add(row["ticker"])
    return list(tickers)
