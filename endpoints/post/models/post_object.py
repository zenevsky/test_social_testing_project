from dataclasses import dataclass, asdict, field
from datetime import datetime
from typing import List, Optional, Any

@dataclass
class Topic:
    name: Optional[Any] = "News"

@dataclass
class Metadata:
    visibility: Optional[Any] = None
    state: Optional[Any] = None
    archived: Optional[Any] = None
    hidden: Optional[Any] = None
    pinned: Optional[Any] = None
    locked_comments: Optional[Any] = None
    scheduled_at: Optional[Any] = None
    created_at: Optional[Any] = None

@dataclass
class Content:
    metadata: Optional[Any] = field(default_factory=Metadata)
    topics: Optional[Any] = field(default_factory=list)

@dataclass
class Data:
    message: Optional[Any] = "Calvin Klein – Between love and madness lies obsession."
    content: Optional[Any] = field(default_factory=Content)

@dataclass
class PostPayload:
    data: Optional[Any] = field(default_factory=Data)

    def to_dict(self) -> dict:
        def serialize(obj):
            if isinstance(obj, dict):
                return {k: serialize(v) for k, v in obj.items()}
            elif isinstance(obj, list):
                return [serialize(i) for i in obj]
            elif isinstance(obj, datetime):
                return obj.strftime("%Y-%m-%d %H:%M:%S")
            else:
                return obj
        return serialize(asdict(self))

