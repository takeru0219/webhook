import os
import slackweb

from app.type import Article


def post_articles(
    articles: list[Article],
    username: str
):
    # Slackに流す
    slack = slackweb.Slack(url=os.environ["SLACK_URL"])
    attachments = []

    for article in articles:
        formatted_time = article.issuetime if article.issuetime else '付紙面'
        attachments.append({
            'title': article.title,
            'title_link': article.link,
            'text': f'{article.issuedate} {formatted_time}',
            'color': 'good'
        })

    slack.notify(
        text='アクセスランキング',
        username=username,
        attachments=attachments
    )
