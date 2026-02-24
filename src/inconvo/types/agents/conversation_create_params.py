# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ConversationCreateParams"]


class ConversationCreateParams(TypedDict, total=False):
    user_identifier: Required[Annotated[str, PropertyInfo(alias="userIdentifier")]]
    """
    Unique identifier for the end-user (1-256 chars). Allowed characters:
    alphanumeric, underscore, hyphen, period, at symbol.
    """

    user_context: Annotated[Dict[str, Union[str, float, bool]], PropertyInfo(alias="userContext")]
    """
    Optional context key-values for additional filtering/tenancy. Required when User
    Context status is ENABLED. Must be omitted when User Context status is DISABLED.
    Requests fail when User Context is UNSET.
    """
