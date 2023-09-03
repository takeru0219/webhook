from fastapi import FastAPI

from app.news import router as news_router
from app.information import router as info_router

app = FastAPI()
app.include_router(news_router)
app.include_router(info_router)


@app.get('/')
def check():
    return {'Hello': 'World!'}
