import os
from datetime import datetime, timezone, timedelta
import slackweb

from app.type import Article


def post_articles(
    articles: list[Article],
    source: str
):
    # Slackに流す
    slack = slackweb.Slack(url=os.environ["SLACK_URL"])
    text = ''

    for article in articles:
        formatted_date = article.issueDate if article.issueDate else '不明'
        formatted_time = article.issueTime if article.issueTime else ''
        text += f'<{article.link}|{article.title.strip()}> ({formatted_date} {formatted_time})\n'

    now = datetime.now(timezone(timedelta(hours=9)))
    slack.notify(
        text=f"""
        {source}（日本時間{now.hour}時）
        ```
        {text.strip()}
        ```
        """,
        source=source,
    )
