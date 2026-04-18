from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from db.database import get_db

from models.news import News

from schemas.news import NewsResponse

router = APIRouter(
    prefix="/news"
)

@router.get("/",response_model=list[NewsResponse])
def get_news(db: Session = Depends(get_db)):
    return db.query(News).all()

@router.get("/{news_id}", response_model=NewsResponse)
def get_news_by_id(news_id: int, db: Session = Depends(get_db)):
    news = db.query(News).filter(News.id == news_id).first()
    if not news:
        raise HTTPException(status_code=404, detail="News not found")
    return news