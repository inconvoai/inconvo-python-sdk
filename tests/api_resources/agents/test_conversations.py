# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from inconvo import Inconvo, AsyncInconvo
from tests.utils import assert_matches_type
from inconvo.pagination import SyncConversationsCursor, AsyncConversationsCursor
from inconvo.types.agents import (
    InconvoConversation,
    ConversationListResponse,
    ConversationCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConversations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Inconvo) -> None:
        conversation = client.agents.conversations.create(
            agent_id="agentId",
            user_identifier="user_123",
        )
        assert_matches_type(ConversationCreateResponse, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Inconvo) -> None:
        conversation = client.agents.conversations.create(
            agent_id="agentId",
            user_identifier="user_123",
            user_context={"foo": "string"},
        )
        assert_matches_type(ConversationCreateResponse, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Inconvo) -> None:
        response = client.agents.conversations.with_raw_response.create(
            agent_id="agentId",
            user_identifier="user_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = response.parse()
        assert_matches_type(ConversationCreateResponse, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Inconvo) -> None:
        with client.agents.conversations.with_streaming_response.create(
            agent_id="agentId",
            user_identifier="user_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = response.parse()
            assert_matches_type(ConversationCreateResponse, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Inconvo) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.conversations.with_raw_response.create(
                agent_id="",
                user_identifier="user_123",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Inconvo) -> None:
        conversation = client.agents.conversations.retrieve(
            conversation_id="conversation_id",
            agent_id="agentId",
        )
        assert_matches_type(InconvoConversation, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Inconvo) -> None:
        response = client.agents.conversations.with_raw_response.retrieve(
            conversation_id="conversation_id",
            agent_id="agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = response.parse()
        assert_matches_type(InconvoConversation, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Inconvo) -> None:
        with client.agents.conversations.with_streaming_response.retrieve(
            conversation_id="conversation_id",
            agent_id="agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = response.parse()
            assert_matches_type(InconvoConversation, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Inconvo) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.conversations.with_raw_response.retrieve(
                conversation_id="conversation_id",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conversation_id` but received ''"):
            client.agents.conversations.with_raw_response.retrieve(
                conversation_id="",
                agent_id="agentId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Inconvo) -> None:
        conversation = client.agents.conversations.list(
            agent_id="agentId",
        )
        assert_matches_type(SyncConversationsCursor[ConversationListResponse], conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Inconvo) -> None:
        conversation = client.agents.conversations.list(
            agent_id="agentId",
            cursor="cursor",
            limit=1,
            user_context={"foo": "string"},
            user_identifier="userIdentifier",
        )
        assert_matches_type(SyncConversationsCursor[ConversationListResponse], conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Inconvo) -> None:
        response = client.agents.conversations.with_raw_response.list(
            agent_id="agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = response.parse()
        assert_matches_type(SyncConversationsCursor[ConversationListResponse], conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Inconvo) -> None:
        with client.agents.conversations.with_streaming_response.list(
            agent_id="agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = response.parse()
            assert_matches_type(SyncConversationsCursor[ConversationListResponse], conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Inconvo) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.conversations.with_raw_response.list(
                agent_id="",
            )


class TestAsyncConversations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncInconvo) -> None:
        conversation = await async_client.agents.conversations.create(
            agent_id="agentId",
            user_identifier="user_123",
        )
        assert_matches_type(ConversationCreateResponse, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncInconvo) -> None:
        conversation = await async_client.agents.conversations.create(
            agent_id="agentId",
            user_identifier="user_123",
            user_context={"foo": "string"},
        )
        assert_matches_type(ConversationCreateResponse, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncInconvo) -> None:
        response = await async_client.agents.conversations.with_raw_response.create(
            agent_id="agentId",
            user_identifier="user_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = await response.parse()
        assert_matches_type(ConversationCreateResponse, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncInconvo) -> None:
        async with async_client.agents.conversations.with_streaming_response.create(
            agent_id="agentId",
            user_identifier="user_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = await response.parse()
            assert_matches_type(ConversationCreateResponse, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncInconvo) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.conversations.with_raw_response.create(
                agent_id="",
                user_identifier="user_123",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncInconvo) -> None:
        conversation = await async_client.agents.conversations.retrieve(
            conversation_id="conversation_id",
            agent_id="agentId",
        )
        assert_matches_type(InconvoConversation, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncInconvo) -> None:
        response = await async_client.agents.conversations.with_raw_response.retrieve(
            conversation_id="conversation_id",
            agent_id="agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = await response.parse()
        assert_matches_type(InconvoConversation, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncInconvo) -> None:
        async with async_client.agents.conversations.with_streaming_response.retrieve(
            conversation_id="conversation_id",
            agent_id="agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = await response.parse()
            assert_matches_type(InconvoConversation, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncInconvo) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.conversations.with_raw_response.retrieve(
                conversation_id="conversation_id",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conversation_id` but received ''"):
            await async_client.agents.conversations.with_raw_response.retrieve(
                conversation_id="",
                agent_id="agentId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncInconvo) -> None:
        conversation = await async_client.agents.conversations.list(
            agent_id="agentId",
        )
        assert_matches_type(AsyncConversationsCursor[ConversationListResponse], conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncInconvo) -> None:
        conversation = await async_client.agents.conversations.list(
            agent_id="agentId",
            cursor="cursor",
            limit=1,
            user_context={"foo": "string"},
            user_identifier="userIdentifier",
        )
        assert_matches_type(AsyncConversationsCursor[ConversationListResponse], conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncInconvo) -> None:
        response = await async_client.agents.conversations.with_raw_response.list(
            agent_id="agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = await response.parse()
        assert_matches_type(AsyncConversationsCursor[ConversationListResponse], conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncInconvo) -> None:
        async with async_client.agents.conversations.with_streaming_response.list(
            agent_id="agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = await response.parse()
            assert_matches_type(AsyncConversationsCursor[ConversationListResponse], conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncInconvo) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.conversations.with_raw_response.list(
                agent_id="",
            )
