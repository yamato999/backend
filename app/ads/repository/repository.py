from typing import Any

from bson.objectid import ObjectId
from pymongo.database import Database
from pymongo.results import DeleteResult, UpdateResult


class AdsRepository:
    def __init__(self, database: Database):
        self.database = database

    def create_ad(self, user_id: str, data: dict[str, Any]):
        data["user_id"] = ObjectId(user_id)
        insert_result = self.database["shanyraks"].insert_one(data)
        return insert_result.inserted_id

    def get_ad(self, ad_id: str):
        return self.database["shanyraks"].find_one({"_id": ObjectId(ad_id)})

    def update_ad(self, ad_id: str, user_id: str, data: dict[str, Any]) -> UpdateResult:
        return self.database["shanyraks"].update_one(
            filter={"_id": ObjectId(ad_id), "user_id": ObjectId(user_id)},
            update={
                "$set": data,
            },
        )

    def delete_ad(self, ad_id: str, user_id: str) -> DeleteResult:
        return self.database["shanyraks"].delete_one(
            {"_id": ObjectId(ad_id), "user_id": ObjectId(user_id)}
        )