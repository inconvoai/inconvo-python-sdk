# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .chart import Chart
from .table import Table
from ...._models import BaseModel

__all__ = ["ResponseRetrieveResponse", "Input", "Output", "Trace"]


class Input(BaseModel):
    message: str
    """The input message"""

    user_context: Optional[Dict[str, object]] = FieldInfo(alias="userContext", default=None)
    """Additional context as key-value pairs (null when user context is disabled)"""


class Output(BaseModel):
    text: str
    """The response text"""

    type: Literal["text", "chart", "table", "error"]
    """Type of the output"""

    chart: Optional[Chart] = None
    """Charts use vega V5 spec https://vega.github.io/schema/vega/v5.json"""

    table: Optional[Table] = None


class Trace(BaseModel):
    input: object
    """Input data for the trace step"""

    name: str
    """Name of the trace step"""

    output: object
    """Output data from the trace step"""


class ResponseRetrieveResponse(BaseModel):
    id: str
    """Unique identifier for the response"""

    input: Input

    output: Output

    trace: List[Trace]
    """Array of trace steps"""
