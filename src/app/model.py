from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from src.app.database import Base

class MediaFile(Base):
    __tablename__ = "media_files"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, nullable=False)
    media_type = Column(String, nullable=False)  # audio, video, image
    content_type = Column(String, nullable=False)  # audio/mp3, image/jpeg и т.д.
    created_at = Column(DateTime(timezone=True), server_default=func.now())
