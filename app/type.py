import datetime
from pydantic import BaseModel


class Article(BaseModel):
    title: str
    link: str
    issueDate: datetime.date | None
    issueTime: datetime.time | None


class MelonChart(BaseModel):
    title: str
    artist: str

    def format(self):
        return f'{self.title} / {self.artist}'
