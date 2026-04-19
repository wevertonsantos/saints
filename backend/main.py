from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from db.database import create_tables

from routers import news

from core.config import settings

from apscheduler.schedulers.background import BackgroundScheduler

from db.insert import save_news

app = FastAPI(
    title="Saints API",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(news.router,prefix=settings.API_PREFIX)

create_tables()

scheduler = BackgroundScheduler()

scheduler.add_job(save_news, 'interval', hours=1)
scheduler.start()

save_news()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app",host="0.0.0.0", port=8000,reload=True)