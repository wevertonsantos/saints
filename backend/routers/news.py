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