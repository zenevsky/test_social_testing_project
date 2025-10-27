from typing import List, Optional
from pydantic import BaseModel, Field, ConfigDict


class User(BaseModel):
    id: int
    guid: str
    display_name: str
    url: str


class Likes(BaseModel):
    total: int


class File(BaseModel):
    pass


class Comment(BaseModel):
    id: int
    message: str
    object_model: str = Field(..., alias="objectModel")
    object_id: int = Field(..., alias="objectId")
    created_by: User = Field(..., alias="createdBy")
    created_at: str = Field(..., alias="createdAt")
    likes: Likes
    files: List[File]

    model_config = ConfigDict(validate_by_name=True)


class Comments(BaseModel):
    total: int
    latest: List[Comment]


class Metadata(BaseModel):
    id: int
    guid: str
    object_model: str
    object_id: int
    visibility: int
    state: int
    archived: bool
    hidden: bool
    pinned: bool
    locked_comments: bool
    created_by: User
    created_at: str
    updated_by: User
    updated_at: str
    scheduled_at: Optional[str]
    url: str
    contentcontainer_id: int
    stream_channel: str


class Content(BaseModel):
    id: int
    metadata: Metadata
    comments: Comments
    likes: Likes
    topics: List[str]
    files: List[File]


class Post(BaseModel):
    id: int
    message: str
    content: Content


class Links(BaseModel):
    self: str
    first: str
    last: str
    next: str = None



class DataContainerModel(BaseModel):
    total: int
    page: int
    pages: int
    links: Links
    results: List[Post]
