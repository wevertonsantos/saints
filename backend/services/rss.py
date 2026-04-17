import feedparser
from core.config import settings

def fetch_news():
    data = feedparser.parse(settings.RSS_URL)

    entries_list = []

    for entry in data.entries:
        entries_list.append({"title":entry.title,"link":entry.link})

    return entries_list