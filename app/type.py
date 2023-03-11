import datetime
from pydantic import BaseModel


class Article(BaseModel):
    title: str
    link: str
    issueDate: datetime.date | None
    issueTime: datetime.time | None
