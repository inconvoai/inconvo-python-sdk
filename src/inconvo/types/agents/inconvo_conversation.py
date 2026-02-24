# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .conversations.chart import Chart
from .conversations.table import Table

__all__ = ["InconvoConversation", "Message"]


class Message(BaseModel):
    message: str

    type: Literal["text", "chart", "table", "error"]

    id: Optional[str] = None
    """Present on Inconvo responses only"""

    chart: Optional[Chart] = None
    """Charts use vega V5 spec https://vega.github.io/schema/vega/v5.json"""

    table: Optional[Table] = None


class InconvoConversation(BaseModel):
    id: str

    context: Optional[Dict[str, Union[str, float, bool]]] = None
    """User context values (null when user context is disabled)"""

    messages: List[Message]

    user_identifier: Optional[str] = FieldInfo(alias="userIdentifier", default=None)
    """Unique identifier for the end-user (may be null for legacy conversations)"""
