from pydantic import BaseModel
from datetime import datetime

class MediaFileBase(BaseModel):
    filename: str
    media_type: str
    content_type: str

class MediaFileCreate(MediaFileBase):
    pass

class MediaFileOut(MediaFileBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True  # Pydantic v2
