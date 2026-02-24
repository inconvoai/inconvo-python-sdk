# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ConversationListParams"]


class ConversationListParams(TypedDict, total=False):
    cursor: str

    limit: int

    user_context: Annotated[Dict[str, Union[str, float, bool]], PropertyInfo(alias="userContext")]
    """
    Arbitrary userContext filters, encoded as a deep object. Example: GET
    /conversations?userContext[userId]=42&userContext[orgId]=12
    """

    user_identifier: Annotated[str, PropertyInfo(alias="userIdentifier")]
    """Filter by user identifier"""
