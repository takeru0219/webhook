from fastapi import APIRouter, status
from fastapi.responses import Response

from app.news.nikkei import get_nikkeitrend
from app.slack.post import post_articles

router = APIRouter(prefix='/news')


@router.get('/nikkei')
def nikkei_ranking():
    try:
        post_articles(
            get_nikkeitrend(),
            '日本経済新聞 電子版')
        return Response(status_code=status.HTTP_200_OK)
    except Exception as e:
        return Response(e, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@router.get('/asahi')
def asahi_ranking():
    pass


@router.get('/nishinippon')
def nishinippon_ranking():
    pass


@router.get('/nytimes_chinese')
def nytimes_chinese_ranking():
    pass
