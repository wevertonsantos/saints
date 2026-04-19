from db.database import SessionLocal
from models.news import News
from services.generator import generate_news

def insert_news(title, content, category,url):
    db = SessionLocal()
    
    news = News(title=title, content=content, category=category,url=url)

    db.add(news)
    
    db.commit()
    
    db.close()

def save_news():
    db = SessionLocal()

    for news in generate_news():

        if not db.query(News).filter(News.url == news['url']).first():
            insert_news(news['title'],news['content'],news['category'],news['url'])
            
    db.close()