import feedparser
from core.config import settings

def fetch_entries():
    data = feedparser.parse(settings.RSS_URL)

    entries = []

    for entry in data.entries[:2]:
        if entry.tags[0]['term'] not in settings.RSS_TAGS:
            entries.append({'category':entry.tags[0]['term'],'url':entry.link})

    return entries