from fastapi import FastAPI, Request

from app.news import router as news_router

app = FastAPI()
app.include_router(news_router)


@app.get('/')
def check():
    return {'Hello': 'World!'}
