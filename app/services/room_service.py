from flask import jsonify
from app.repositories.room_repository import RoomRepository
from app.schemas.room_schema import RoomSchema


class RoomService:

    @staticmethod
    def add_room(data):
        room_repository = RoomRepository()
        try:
            room_data = RoomSchema(**data).dict()
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        room_id = room_repository.save(room_data)
        return {"id": room_id}, 201

    @staticmethod
    def get_rooms():
        room_repository = RoomRepository()
        rooms = room_repository.get_all()
        for room in rooms:
            room["_id"] = str(room["_id"])
        return rooms

    @staticmethod
    def get_room(room_id):
        room_repository = RoomRepository()
        room = room_repository.get_by_id(room_id)
        if room:
            room["_id"] = str(room["_id"])
            return room, 200
        return jsonify({"error": "Room not found"}), 400

    @staticmethod
    def update_room(room_id, data):
        room_repository = RoomRepository()
        try:
            room_data = RoomSchema(**data).dict(exclude_unset=True)
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        updated_room = room_repository.update(room_id, room_data)
        if updated_room:
            updated_room["_id"] = str(updated_room["_id"])
            return updated_room, 200
        return jsonify({"error": "Room not found"}), 404

    @staticmethod
    def delete_room(room_id):
        room_repository = RoomRepository()
        success = room_repository.delete(room_id)
        if success:
            return jsonify({"message": "Room deleted"}), 204
        return jsonify({"error": "Room not found"}), 404
