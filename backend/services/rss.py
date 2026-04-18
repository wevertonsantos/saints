import feedparser
from core.config import settings

def fetch_urls():
    data = feedparser.parse(settings.RSS_URL)

    urls = []

    for entry in data.entries:
        urls.append(entry.link)

    return urls