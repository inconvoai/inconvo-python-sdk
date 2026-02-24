from __future__ import annotations

from typing import Any

import httpx
import pytest

from inconvo import Inconvo, AsyncInconvo
from inconvo.resources.agents.conversations.response.response import (
    ResponseCreateEventStream,
    AsyncResponseCreateEventStream,
)


SSE_PAYLOAD = b"""data: {"type":"response.created","id":"resp_123"}

data: not-json

data: [DONE]

data: {"type":"response.progress","id":"resp_123","message":"Hello"}

"""


def test_response_create_stream_dispatches_to_sse_stream(client: Inconvo) -> None:
    resource = client.agents.conversations.response
    captured: dict[str, Any] = {}
    sentinel = object()

    def fake_post(path: str, **kwargs: Any) -> object:
        captured["path"] = path
        captured["kwargs"] = kwargs
        return sentinel

    resource._post = fake_post  # type: ignore[method-assign]

    result = resource.create(
        conversation_id="conversation_id",
        agent_id="agentId",
        message="message",
        stream=True,
    )

    assert result is sentinel
    assert captured["path"] == "/agents/agentId/conversations/conversation_id/response"
    assert captured["kwargs"]["stream"] is True
    assert captured["kwargs"]["stream_cls"] is ResponseCreateEventStream
    assert captured["kwargs"]["options"]["headers"]["Accept"] == "text/event-stream"


def test_response_create_event_stream_skips_done_and_malformed(client: Inconvo) -> None:
    response = httpx.Response(200, content=SSE_PAYLOAD)
    stream = ResponseCreateEventStream(cast_to=dict, response=response, client=client)

    events = list(stream)

    assert [event["type"] for event in events] == ["response.created", "response.progress"]
    assert events[1]["message"] == "Hello"
    assert response.is_closed is True


@pytest.mark.asyncio
async def test_async_response_create_stream_dispatches_to_sse_stream(async_client: AsyncInconvo) -> None:
    resource = async_client.agents.conversations.response
    captured: dict[str, Any] = {}
    sentinel = object()

    async def fake_post(path: str, **kwargs: Any) -> object:
        captured["path"] = path
        captured["kwargs"] = kwargs
        return sentinel

    resource._post = fake_post  # type: ignore[method-assign]

    result = await resource.create(
        conversation_id="conversation_id",
        agent_id="agentId",
        message="message",
        stream=True,
    )

    assert result is sentinel
    assert captured["path"] == "/agents/agentId/conversations/conversation_id/response"
    assert captured["kwargs"]["stream"] is True
    assert captured["kwargs"]["stream_cls"] is AsyncResponseCreateEventStream
    assert captured["kwargs"]["options"]["headers"]["Accept"] == "text/event-stream"


@pytest.mark.asyncio
async def test_async_response_create_event_stream_skips_done_and_malformed(async_client: AsyncInconvo) -> None:
    response = httpx.Response(200, content=SSE_PAYLOAD)
    stream = AsyncResponseCreateEventStream(cast_to=dict, response=response, client=async_client)

    events = [event async for event in stream]

    assert [event["type"] for event in events] == ["response.created", "response.progress"]
    assert events[1]["message"] == "Hello"
    assert response.is_closed is True
