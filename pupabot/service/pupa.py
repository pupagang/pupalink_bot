from pupalink import Session
from pupalink.metadata import Book


class PupalinkService:
    def __init__(self, pupa: Session) -> None:
        self.pupa = pupa

    async def search_book(self, book_name: str) -> list[Book]:
        return await self.pupa.search_book(book_name)

    async def download_book(self, book: Book) -> bytes:
        return await self.pupa.download_book(book)

    async def close(self):
        await self.pupa.close()
