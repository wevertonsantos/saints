from datetime import datetime
from pydantic import BaseModel

class NewsResponse(BaseModel):
    title: str
    content: str
    created_at: datetime
    category: str