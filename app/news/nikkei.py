import datetime as dt
import re
import requests

from bs4 import BeautifulSoup
from app.type import Article
from app.news import scrape


def get_nikkei_trend() -> list[Article]:
    soup = scrape('https://www.nikkei.com/access/')

    # soup内の処理
    data_array = soup.find_all(class_='m-miM32_item')
    ret_articles = []

    for i, article_data in enumerate(data_array):
        if i < 10:
            rawtitle = article_data.find(
                class_='m-miM32_itemTitleText').text.strip().replace('\u3000', ' ')
            processed_title = re.sub('［.+］', '', rawtitle)

            issued_at = article_data.find(class_='m-miM32_itemDate').text
            # ネット記事の場合は「yyyy/mm/dd HH:MM」新聞記事の場合は「yyyy/mm/dd付」
            if '付' in issued_at:
                # 新聞記事の場合の処理
                issued_at = dt.datetime.strptime(issued_at, '%Y/%m/%d付')
                issued_time = None
            else:
                issued_at = dt.datetime.strptime(issued_at, '%Y/%m/%d %H:%M')
                issued_time = issued_at.time()

            ret_articles.append(Article(
                title=processed_title,
                link='http://www.nikkei.com' +
                article_data.find('a').get('href'),
                issueDate=issued_at.date(),
                issueTime=issued_time,
            ))

    return ret_articles
