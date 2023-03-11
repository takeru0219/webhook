import os
import re
import requests

import slackweb
from bs4 import BeautifulSoup


def get_nikkeitrend():
    # 取得 -> BeautifulSoupに渡す
    url = 'https://www.nikkei.com/access/'
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    # soup内の処理
    data_array = soup.find_all(class_='m-miM32_item')
    titles = []
    links = []
    issuedates = []

    for i, article_data in enumerate(data_array):
        if i < 10:
            rawtitle = article_data.find(class_='m-miM32_itemTitleText').text.strip().replace('\u3000', ' ')
            processedtitle = re.sub('［.+］', '', rawtitle)
            titles.append(processedtitle)
            links.append(article_data.find('a').get('href'))
            issuedates.append(article_data.find(class_='m-miM32_itemDate').text)

    # Slackに流す
    slack = slackweb.Slack(url=os.environ["SLACK_URL"])
    attachments = []

    for title, link, issuedate in zip(titles, links, issuedates):
        attachments.append({
            'title': title,
            'title_link': 'http://www.nikkei.com' + link,
            'text': issuedate,
            'color': 'good'
        })

    slack.notify(
        text='アクセスランキング',
        username='日本経済新聞 電子版',
        attachments=attachments
    )