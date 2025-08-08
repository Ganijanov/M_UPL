from sqlalchemy.ext.asyncio import AsyncSession
from src.app.model import MediaFile
from src.app.schemas import MediaFileCreate

async def save_media_file(db: AsyncSession, media_data: MediaFileCreate) -> MediaFile:
    media = MediaFile(**media_data.model_dump())
    db.add(media)
    await db.commit()
    await db.refresh(media)
    return media
