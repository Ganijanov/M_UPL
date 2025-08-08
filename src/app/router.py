from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.app.service     import handle_media_upload
from src.app.schemas import MediaFileOut
from src.app.deeps import get_db

router = APIRouter(prefix="/media", tags=["Media"])

@router.post("/upload-audio", response_model=MediaFileOut)
async def upload_audio(
    file: UploadFile = File(...), db: AsyncSession = Depends(get_db)
):
    return await handle_media_upload(file, db, allowed_type="audio")

@router.post("/upload-photo", response_model=MediaFileOut)
async def upload_photo(
    file: UploadFile = File(...), db: AsyncSession = Depends(get_db)
):
    return await handle_media_upload(file, db, allowed_type="image")

@router.post("/upload-video", response_model=MediaFileOut)
async def upload_video(
    file: UploadFile = File(...), db: AsyncSession = Depends(get_db)
):
    return await handle_media_upload(file, db, allowed_type="video")
