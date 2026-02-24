# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ResponseCreateParams"]


class ResponseCreateParams(TypedDict, total=False):
    agent_id: Required[Annotated[str, PropertyInfo(alias="agentId")]]

    message: Required[str]

    stream: bool
    """
    If true and the client sets `Accept: text/event-stream`, the API returns an SSE
    stream instead of a single JSON body.
    """
