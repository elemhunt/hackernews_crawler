import os

import requests
from bs4 import BeautifulSoup
from hn_crawler.models import Entry

class HackerNewsCrawler:
    def __init__(self, url="https://news.ycombinator.com/"):
        self.url = url
        self.number_of_items_to_crawl = int(os.getenv("NUM_ITEMS_TO_CRAWL", 30))

    def fetch(self):
        response = requests.get(self.url)
        response.raise_for_status()
        return BeautifulSoup(response.text, "html.parser")

    def parse(self):
        soup = self.fetch()
        entries = []
        items = soup.select(".athing")
        subtexts = soup.select(".subtext")

        for i in range(min(self.number_of_items_to_crawl, len(items))):
            item = items[i]
            sub = subtexts[i]

            title = item.select_one(".titleline").text
            rank = int(item.select_one(".rank").text.strip(".").strip())
            points = int(sub.select_one(".score").text.replace(" points","")) if sub.select_one(".score") else 0
            comments_link = sub.select("a")[-1]
            comments_text = comments_link.text
            comments = int(comments_text.split()[0]) if "comment" in comments_text else 0

            entries.append(Entry(rank=rank, title=title, points=points, comments=comments))

        return entries