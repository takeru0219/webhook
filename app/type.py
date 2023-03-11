import datetime
from pydantic import BaseModel


class Article(BaseModel):
    title: str
    link: str
    issuedate: datetime.date
    issuetime: datetime.time | None
