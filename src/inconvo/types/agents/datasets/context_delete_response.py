# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["ContextDeleteResponse"]


class ContextDeleteResponse(BaseModel):
    file: str

    success: bool

    error: Optional[str] = None
