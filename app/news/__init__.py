from fastapi import APIRouter, status
from fastapi.responses import Response

from app.news.nikkei import get_nikkeitrend
from app.news.asahi import get_asahitrend
from app.slack.post import post_articles

router = APIRouter(prefix='/news')


def base_function(fn, source_name: str):
    """ 各項目に共通の部分をまとめた

    Args:
        fn (function): 記事を取ってくるためのメソッド
        source_name (str): Slackに投稿するときの表示名

    Returns:
        _type_: _description_
    """
    try:
        data = fn()
        post_articles(
            data,
            source_name)
        return Response(status_code=status.HTTP_200_OK)
    except Exception as e:
        return Response(e, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

@router.get('/nikkei')
def nikkei_ranking():
    base_function(
        get_nikkeitrend,
        '日本経済新聞 電子版'
    )


@router.get('/asahi')
def asahi_ranking():
    base_function(
        get_asahitrend,
        '朝日新聞'
    )

@router.get('/nishinippon')
def nishinippon_ranking():
    pass


@router.get('/nytimes_chinese')
def nytimes_chinese_ranking():
    pass
