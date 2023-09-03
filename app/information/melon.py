import datetime as dt
import re
import requests

from bs4 import BeautifulSoup
from app.type import MelonChart


def get_melon():
    # 取得 -> BeautifulSoupに渡す
    url = 'https://www.melon.com/chart/index.htm'
    response = requests.get(
        url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'})

    soup = BeautifulSoup(response.content, 'html.parser')

    # soup内の処理
    data_array = soup.find_all(class_='lst50')
    ret_songs = []

    for i, song_data in enumerate(data_array):
        if i < 20:
            song_title = song_data.find(
                class_='ellipsis rank01').find('a').text.strip().replace('\u3000', ' ')

            song_artist = song_data.find(
                class_='ellipsis rank02').find('a').text.strip().replace('\u3000', ' ')

            ret_songs.append(MelonChart(
                title=song_title,
                artist=song_artist,
            ))

    return ret_songs
