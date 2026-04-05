from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, Cookie, Response
from sqlalchemy.orm import Session

from db.database import get_db, SessionLocal
from models.new import New
from schemas.new import NewResponse

router = APIRouter(
    prefix="/news",
    tags=["news"]
)

# /api/news/endpoint

@router.get("/news",response_model=NewResponse)
def get_news():
    db: Session = Depends(get_db)
    news = db.query(New).first()
    if not news:
        raise HTTPException(status_code=404,detail="News not found")
    
    return news