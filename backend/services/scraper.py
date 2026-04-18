from newspaper import Article
from services.rss import fetch_entries

def extract_articles():
    articles = []

    for entry in fetch_entries():
        article = Article(entry['url'])
        article.download()
        article.parse()
        articles.append({'category':entry['category'],'title':article.title,'content':article.text})

    return articles