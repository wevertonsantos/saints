from datetime import datetime
from pydantic import BaseModel

class NewsResponse(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime
    category: str