from app import mongo
from bson import ObjectId


class BaseRepository:

    def __init__(self, collection_name):
        self.collection = mongo.db[collection_name]

    def save(self, entity):
        result = self.collection.insert_one(entity)
        return str(result.inserted_id)

    def get_by_id(self, entity_id):
        return self.collection.find_one({"_id": ObjectId(entity_id)})

    def get_all(self):
        return list(self.collection.find())

    def update(self, entity_id, update_data):
        self.collection.update_one({"_id": ObjectId(entity_id)}, {"$set": update_data})
        return self.get_by_id(entity_id)

    def delete(self, entity_id):
        result = self.collection.delete_one({"_id": ObjectId(entity_id)})
        return result.deleted_count > 0
