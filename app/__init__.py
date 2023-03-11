from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def check():
    return {'Hello': 'World!'}


@app.get('/news/nikkei')
def nikkei_ranking():
    pass


@app.get('/news/asahi')
def asahi_ranking():
    pass


@app.get('/news/nishinippon')
def nishinippon_ranking():
    pass


@app.get('/news/nytimes_chinese')
def nytimes_chinese_ranking():
    pass
