from newspaper import Article
from services.rss import fetch_urls

def extract_articles():
    articles = []

    for url in fetch_urls():
        article = Article(url)
        article.download()
        article.parse()
        articles.append({'title':article.title,'content':article.text})

    return articles