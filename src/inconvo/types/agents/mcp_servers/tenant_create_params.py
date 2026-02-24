# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["TenantCreateParams"]


class TenantCreateParams(TypedDict, total=False):
    agent_id: Required[Annotated[str, PropertyInfo(alias="agentId")]]

    tenant: Required[Dict[str, Dict[str, object]]]
    """Arbitrary key-value mapping.

    - Keys are strings.
    - Values are JSON objects with arbitrary properties.
    """
