from fastapi import FastAPI

from app.news.api import router as news_router

app = FastAPI()
app.include_router(news_router)


@app.get('/')
def check():
    return {'Hello': 'World!'}
