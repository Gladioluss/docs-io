from fastapi import FastAPI
from app.core.config import settings


app = FastAPI(title=settings.API_TITLE)

print(settings.ASYNC_DATABASE_URI)