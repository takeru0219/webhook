from fastapi import APIRouter

from app.news.nikkei import get_nikkei_trend
from app.news.asahi import get_asahi_trend
from app.news.nishinippon import get_nishinippon_trend
from app.news import base_function

router = APIRouter(prefix='/news')


@router.get('/nikkei')
def nikkei_ranking():
    base_function(get_nikkei_trend, '日本経済新聞 電子版')


@router.get('/asahi')
def asahi_ranking():
    base_function(get_asahi_trend, '朝日新聞')


@router.get('/nishinippon')
def nishinippon_ranking():
    pass


@router.get('/nytimes_chinese')
def nytimes_chinese_ranking():
    pass
