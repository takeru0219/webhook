import requests
from bs4 import BeautifulSoup

from fastapi import status
from fastapi.responses import Response

from app.slack.post import post_articles


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
        post_articles(data, source_name)
        return Response(status_code=status.HTTP_200_OK)
    except Exception as e:
        return Response(e, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


def scrape(url: str) -> BeautifulSoup:
    """ URLをもとに、スクレイピングした結果を返す

    Args:
        url (str): スクレイピングしたいURL

    Returns:
        BeautifulSoup: スクレイピングした結果
    """
    url = 'https://www.asahi.com/whatsnew/ranking/'
    response = requests.get(url)

    return BeautifulSoup(response.content, 'html.parser')
