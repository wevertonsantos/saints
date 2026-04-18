import feedparser
from core.config import settings

def fetch_titles_news():
    data = feedparser.parse(settings.RSS_URL)

    entries_list = []

    for entry in data.entries:
        entries_list.append(entry.title)

    return entries_list