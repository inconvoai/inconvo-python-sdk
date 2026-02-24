# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["FeedbackUpdateParams"]


class FeedbackUpdateParams(TypedDict, total=False):
    agent_id: Required[Annotated[str, PropertyInfo(alias="agentId")]]

    conversation_id: Required[str]

    response_id: Required[str]

    comment: str

    rating: Literal["positive", "negative"]
