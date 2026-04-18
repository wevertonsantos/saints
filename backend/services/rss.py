import feedparser
from core.config import settings

def fetch_entries():
    data = feedparser.parse(settings.RSS_URL)

    entries = []

    for entry in data.entries:
        if entry.tags[0]['term'] != settings.RSS_TAG:
            entries.append({'category':entry.tags[0]['term'],'url':entry.link})

    return entries