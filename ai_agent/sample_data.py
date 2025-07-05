import csv

sample_news = [
    {
        "ticker": "GOOGL",
        "headline": "Google announces breakthrough in quantum computing",
        "summary": "Google's latest research paper details a new quantum processor that reportedly solves a calculation in record time.",
        "link": "https://www.blog.google/technology/quantum/quantum-supremacy/"
    },
    {
        "ticker": "AAPL",
        "headline": "Apple faces new lawsuit over App Store policies",
        "summary": "A class-action lawsuit has been filed against Apple, alleging monopolistic practices in its App Store.",
        "link": "https://www.reuters.com/technology/apple-hit-new-app-store-lawsuit-2023-06-12/"
    },
    {
        "ticker": "TSLA",
        "headline": "Tesla recalls over 500,000 vehicles due to software issue",
        "summary": "Tesla has issued a recall for Model 3 and Model S vehicles to fix a software bug in its full self-driving beta.",
        "link": "https://www.reuters.com/business/autos-transportation/tesla-recalls-vehicles-over-software-issue-2023-01-27/"
    },
    {
        "ticker": "AMZN",
        "headline": "Amazon to acquire major robotics firm",
        "summary": "Amazon announced its intention to acquire 'RoboFuture Inc.' for $5 billion to boost warehouse automation.",
        "link": "https://www.wsj.com/articles/amazon-acquires-robotics-firm-11658482861"
    },
    {
        "ticker": "MSFT",
        "headline": "Microsoft wins massive $22 billion US Army contract",
        "summary": "Microsoft will supply the US Army with over 120,000 AR headsets based on its HoloLens tech.",
        "link": "https://www.cnbc.com/2021/03/31/microsoft-wins-contract-to-supply-us-army-ar-headsets.html"
    },
    {
        "ticker": "NFLX",
        "headline": "Netflix reports subscriber growth slowdown, shares tumble",
        "summary": "Netflix announced a slowdown in new subscriber growth, sending shares down by over 10% in after-hours trading.",
        "link": "https://www.cnbc.com/2021/07/20/netflix-nflx-earnings-q2-2021.html"
    },
]

def create_sample_csv():
    csv_file = "processed_articles.csv"  # directly in root directory

    # Create CSV and write header
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["link", "ticker", "title"])

        for article in sample_news:
            writer.writerow([article["link"], article["ticker"], article["headline"]])

    print(f"✅ Sample CSV '{csv_file}' created successfully in root directory.")

if __name__ == "__main__":
    create_sample_csv()
