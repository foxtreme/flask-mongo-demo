from flask import Blueprint, request, jsonify
from app.services.room_service import RoomService

bp = Blueprint("rooms", __name__)


@bp.route("/rooms", methods=["POST"])
def add_room():
    data = request.get_json()
    result = RoomService.add_room(data)
    return jsonify(result), 201 if result else 400


@bp.route("/rooms", methods=["GET"])
def get_rooms():
    rooms = RoomService.get_rooms()
    return jsonify(rooms), 200


@bp.route("/rooms/<string:room_id>", methods=["GET"])
def get_room(room_id):
    room = RoomService.get_room(room_id)
    if room:
        return jsonify(room), 200
    return jsonify({"error": "Room not found"}), 404


@bp.route("/rooms/<string:room_id>", methods=["PUT"])
def update_room(room_id):
    data = request.get_json()
    updated_room = RoomService.update_room(room_id, data)
    if updated_room:
        return jsonify(updated_room), 200
    return jsonify({"error": "Room not found"}), 404


@bp.route("/rooms/<string:room_id>", methods=["DELETE"])
def delete_room(room_id):
    success = RoomService.delete_room(room_id)
    if success:
        return jsonify({"message": "Room deleted"}), 200
    return jsonify({"error": "Room not found"}), 404
