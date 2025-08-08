import uvicorn
from fastapi import FastAPI
from src.app.router import router
from src.app.database import engine , Base


app = FastAPI(title="Media Upload API")

# Роутеры
app.include_router(router)

# Создание таблиц при старте
@app.on_event("startup")
async def startup_event():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
