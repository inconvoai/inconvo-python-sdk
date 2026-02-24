# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .chart import Chart
from .table import Table
from ...._models import BaseModel

__all__ = ["ResponseCreateResponse"]


class ResponseCreateResponse(BaseModel):
    id: str

    conversation_id: str = FieldInfo(alias="conversationId")

    message: str

    type: Literal["text", "chart", "table", "error"]

    chart: Optional[Chart] = None
    """Charts use vega V5 spec https://vega.github.io/schema/vega/v5.json"""

    table: Optional[Table] = None
