from pydantic import BaseModel
from typing import List


class EntryModel(BaseModel):
    authors: List[str]
    book: str
    isbn: str
    cover: str
