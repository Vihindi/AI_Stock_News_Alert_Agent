import csv
import os

CSV_FILE = "processed_articles.csv"

def init_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["link", "ticker", "title"])

def is_processed(link):
    if not os.path.exists(CSV_FILE):
        return False
    with open(CSV_FILE, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["link"] == link:
                return True
    return False

def mark_as_processed(link, ticker, title):
    with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([link, ticker, title])
