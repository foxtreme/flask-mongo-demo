from pydantic import BaseModel, Field
from typing import List, Optional


class EnemySchema(BaseModel):
    name: str
    level: int
    type: str


class DimensionsSchema(BaseModel):
    width: int
    length: int
    height: int


class RoomSchema(BaseModel):
    name: str
    dimensions: DimensionsSchema
    hostile: bool
    enemies: List[EnemySchema]
    treasure: Optional[List[str]] = Field(default=[])
