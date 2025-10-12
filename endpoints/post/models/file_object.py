from dataclasses import dataclass
from typing import List, Optional


@dataclass
class FileItem:
    path: str
    file_name: str
    mime_type: str


@dataclass
class UploadFilePayload:
    files: List[FileItem]
    hidden_in_stream: Optional[List[str]] = None

    def to_dict(self) -> dict:
        return {
            "files": [f.file_name for f in self.files],
            "hiddenInStream": self.hidden_in_stream or [],
        }
