import os
import aiofiles
from fastapi import UploadFile, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.app.schemas import MediaFileCreate
from src.app.repository import save_media_file

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

async def   handle_media_upload(file: UploadFile, db: AsyncSession, allowed_type: str):
    if not file.content_type.startswith(allowed_type):
        raise HTTPException(status_code=400, detail=f"Ожидается тип: {allowed_type}/*")

    file_path = os.path.join(UPLOAD_DIR, file.filename)
    
    async with aiofiles.open(file_path, "wb") as out_file:
        content = await file.read()
        await out_file.write(content)

    media_data = MediaFileCreate(
        filename=file.filename,
        media_type=allowed_type,
        content_type=file.content_type
    )
    return await save_media_file(db, media_data)
