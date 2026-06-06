import requests
from bs4 import BeautifulSoup
import json
import os

def scrape_news(url="https://news.ycombinator.com/"):
    """
    Simple scraper for Hacker News front page.
    """
    print(f"Scraping {url}...")
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        stories = []
        
        for row in soup.select('.athing'):
            title_elem = row.select_one('.titleline > a')
            if title_elem:
                stories.append({
                    'title': title_elem.text,
                    'url': title_elem['href']
                })
        
        return stories
    except Exception as e:
        print(f"Error during scraping: {e}")
        return []

def save_to_json(data, filename="news_data.json"):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Saved {len(data)} items to {filename}")

if __name__ == "__main__":
    news = scrape_news()
    if news:
        save_to_json(news)
