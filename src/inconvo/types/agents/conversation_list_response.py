# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ConversationListResponse"]


class ConversationListResponse(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    title: Optional[str] = None

    user_context: Optional[Dict[str, Union[str, float, bool]]] = FieldInfo(alias="userContext", default=None)
    """User context values (null when user context is disabled)"""

    user_identifier: Optional[str] = FieldInfo(alias="userIdentifier", default=None)
    """Unique identifier for the end-user (may be null for legacy conversations)"""
