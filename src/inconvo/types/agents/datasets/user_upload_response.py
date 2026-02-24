# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["UserUploadResponse", "File"]


class File(BaseModel):
    name: str

    path: str

    size: int


class UserUploadResponse(BaseModel):
    file: File

    error: Optional[str] = None
