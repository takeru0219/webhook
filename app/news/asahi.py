import datetime as dt
import requests

from bs4 import BeautifulSoup
from app.type import Article
from app.news import scrape


def get_asahi_trend() -> list[Article]:
    soup = scrape('https://www.asahi.com/whatsnew/ranking/')

    # soup内の処理
    data_array = soup.find_all(class_='Ranking')[0].find_all('dd')
    ret_articles = []

    for i, article_data in enumerate(data_array):
        # 10位まで取得
        if i < 10:
            # タイトルとリンクを取得
            title = article_data.find('a').text
            link = article_data.find('a').get('href')

            each_response = requests.get(link)
            each_soup = BeautifulSoup(each_response.content, 'html.parser')
            raw_issued_at_candidate = each_soup.find(class_='UDj4P')
            if raw_issued_at_candidate:
                # 発行日時が取れなかった時の処理
                raw_issued_at = raw_issued_at_candidate.text
                issued_at = dt.datetime.strptime(
                    raw_issued_at, '%Y年%m月%d日 %H時%M分')
            else:
                issued_at = None

            ret_articles.append(Article(
                title=title,
                link=link,
                issueDate=issued_at.date() if issued_at else None,
                issueTime=issued_at.time() if issued_at else None,
            ))

    return ret_articles
