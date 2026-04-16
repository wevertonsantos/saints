from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, Cookie, Response
from sqlalchemy.orm import Session

from db.database import get_db, SessionLocal
from models.news import News
from schemas.news import NewsResponse

router = APIRouter(
    prefix="/news",
    tags=["news"]
)

# /api/news/endpoint

@router.get("/",response_model=list[NewsResponse])
def get_news(db: Session = Depends(get_db)):
    news = db.query(News).all()
    if not news:
        raise HTTPException(status_code=404,detail="News not found")
    
    return news