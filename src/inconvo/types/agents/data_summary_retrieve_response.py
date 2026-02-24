# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DataSummaryRetrieveResponse"]


class DataSummaryRetrieveResponse(BaseModel):
    data_summary: str = FieldInfo(alias="dataSummary")
    """A human-readable summary of data available to the agent"""
