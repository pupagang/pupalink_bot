from pupabot.models.search import EntryModel

from typing import List, Optional


class SearchService:
    def __init__(self, collection) -> None:
        self.collection = collection

    async def add(self, search: EntryModel) -> None:
        await self.collection.insert_one(search.dict())

    async def search(self, name: str) -> Optional[List[dict]]:
        result = await self.collection.find({"name": name}).sort("name")

        if result:
            result_list = await result.to_list(length=10)
            return result_list
        else:
            return None
