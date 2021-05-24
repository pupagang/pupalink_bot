class PupalinkService:
    def __init__(self, pupa) -> None:
        self.pupa = pupa

    async def search_book(self, book_name: str) -> list:
        return await self.pupa.search_book(book_name)

    async def download_book(self, book):
        self.pupa.download_book(book)

    async def get_cover(book) -> str:
        return book.get_cover()
