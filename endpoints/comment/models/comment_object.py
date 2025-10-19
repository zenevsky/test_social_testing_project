from dataclasses import dataclass, asdict, field
from typing import Optional, Any


@dataclass
class Comment:
    message: Optional[Any] = "Calvin Klein – Between love and madness lies obsession."


@dataclass
class CreateCommentPayload:
    Comment: Optional[Comment] = field(default_factory=Comment)
    objectModel: Optional[Any] = "humhub\\modules\\post\\models\\Post"
    objectId: Optional[Any] = None

    def to_dict(self) -> dict:
        data = asdict(self)
        return data


@dataclass
class UpdateCommentPayload:
    Comment: Optional[Comment] = field(default_factory=Comment)

    def to_dict(self) -> dict:
        data = asdict(self)
        return data
