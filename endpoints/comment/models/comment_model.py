from typing import List, Optional
from pydantic import BaseModel


class Links(BaseModel):
    self: str
    first: str
    last: str


class CreatedBy(BaseModel):
    id: int
    guid: str
    display_name: str
    url: str


class Likes(BaseModel):
    total: int


class Comment(BaseModel):
    id: int
    message: str
    objectModel: str
    objectId: int
    createdBy: CreatedBy
    createdAt: str
    likes: Likes
    files: List


class DataContainerModel(BaseModel):
    total: int
    page: int
    pages: int
    links: Links
    results: List[Comment]
