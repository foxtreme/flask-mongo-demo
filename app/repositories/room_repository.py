from app.repositories.base_repository import BaseRepository


class RoomRepository(BaseRepository):

    def __init__(self):
        super().__init__("rooms")
