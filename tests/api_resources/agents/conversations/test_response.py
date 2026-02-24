# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from inconvo import Inconvo, AsyncInconvo
from tests.utils import assert_matches_type
from inconvo.types.agents.conversations import ResponseCreateResponse, ResponseRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestResponse:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Inconvo) -> None:
        response = client.agents.conversations.response.create(
            conversation_id="conversation_id",
            agent_id="agentId",
            message="message",
        )
        assert_matches_type(ResponseCreateResponse, response, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Inconvo) -> None:
        response = client.agents.conversations.response.create(
            conversation_id="conversation_id",
            agent_id="agentId",
            message="message",
            stream=True,
        )
        assert_matches_type(ResponseCreateResponse, response, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Inconvo) -> None:
        http_response = client.agents.conversations.response.with_raw_response.create(
            conversation_id="conversation_id",
            agent_id="agentId",
            message="message",
        )

        assert http_response.is_closed is True
        assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"
        response = http_response.parse()
        assert_matches_type(ResponseCreateResponse, response, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Inconvo) -> None:
        with client.agents.conversations.response.with_streaming_response.create(
            conversation_id="conversation_id",
            agent_id="agentId",
            message="message",
        ) as http_response:
            assert not http_response.is_closed
            assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"

            response = http_response.parse()
            assert_matches_type(ResponseCreateResponse, response, path=["response"])

        assert cast(Any, http_response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Inconvo) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.conversations.response.with_raw_response.create(
                conversation_id="conversation_id",
                agent_id="",
                message="message",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conversation_id` but received ''"):
            client.agents.conversations.response.with_raw_response.create(
                conversation_id="",
                agent_id="agentId",
                message="message",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Inconvo) -> None:
        response = client.agents.conversations.response.retrieve(
            response_id="response_id",
            agent_id="agentId",
            conversation_id="conversation_id",
        )
        assert_matches_type(ResponseRetrieveResponse, response, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Inconvo) -> None:
        http_response = client.agents.conversations.response.with_raw_response.retrieve(
            response_id="response_id",
            agent_id="agentId",
            conversation_id="conversation_id",
        )

        assert http_response.is_closed is True
        assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"
        response = http_response.parse()
        assert_matches_type(ResponseRetrieveResponse, response, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Inconvo) -> None:
        with client.agents.conversations.response.with_streaming_response.retrieve(
            response_id="response_id",
            agent_id="agentId",
            conversation_id="conversation_id",
        ) as http_response:
            assert not http_response.is_closed
            assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"

            response = http_response.parse()
            assert_matches_type(ResponseRetrieveResponse, response, path=["response"])

        assert cast(Any, http_response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Inconvo) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.conversations.response.with_raw_response.retrieve(
                response_id="response_id",
                agent_id="",
                conversation_id="conversation_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conversation_id` but received ''"):
            client.agents.conversations.response.with_raw_response.retrieve(
                response_id="response_id",
                agent_id="agentId",
                conversation_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `response_id` but received ''"):
            client.agents.conversations.response.with_raw_response.retrieve(
                response_id="",
                agent_id="agentId",
                conversation_id="conversation_id",
            )


class TestAsyncResponse:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncInconvo) -> None:
        response = await async_client.agents.conversations.response.create(
            conversation_id="conversation_id",
            agent_id="agentId",
            message="message",
        )
        assert_matches_type(ResponseCreateResponse, response, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncInconvo) -> None:
        response = await async_client.agents.conversations.response.create(
            conversation_id="conversation_id",
            agent_id="agentId",
            message="message",
            stream=True,
        )
        assert_matches_type(ResponseCreateResponse, response, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncInconvo) -> None:
        http_response = await async_client.agents.conversations.response.with_raw_response.create(
            conversation_id="conversation_id",
            agent_id="agentId",
            message="message",
        )

        assert http_response.is_closed is True
        assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"
        response = await http_response.parse()
        assert_matches_type(ResponseCreateResponse, response, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncInconvo) -> None:
        async with async_client.agents.conversations.response.with_streaming_response.create(
            conversation_id="conversation_id",
            agent_id="agentId",
            message="message",
        ) as http_response:
            assert not http_response.is_closed
            assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"

            response = await http_response.parse()
            assert_matches_type(ResponseCreateResponse, response, path=["response"])

        assert cast(Any, http_response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncInconvo) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.conversations.response.with_raw_response.create(
                conversation_id="conversation_id",
                agent_id="",
                message="message",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conversation_id` but received ''"):
            await async_client.agents.conversations.response.with_raw_response.create(
                conversation_id="",
                agent_id="agentId",
                message="message",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncInconvo) -> None:
        response = await async_client.agents.conversations.response.retrieve(
            response_id="response_id",
            agent_id="agentId",
            conversation_id="conversation_id",
        )
        assert_matches_type(ResponseRetrieveResponse, response, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncInconvo) -> None:
        http_response = await async_client.agents.conversations.response.with_raw_response.retrieve(
            response_id="response_id",
            agent_id="agentId",
            conversation_id="conversation_id",
        )

        assert http_response.is_closed is True
        assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"
        response = await http_response.parse()
        assert_matches_type(ResponseRetrieveResponse, response, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncInconvo) -> None:
        async with async_client.agents.conversations.response.with_streaming_response.retrieve(
            response_id="response_id",
            agent_id="agentId",
            conversation_id="conversation_id",
        ) as http_response:
            assert not http_response.is_closed
            assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"

            response = await http_response.parse()
            assert_matches_type(ResponseRetrieveResponse, response, path=["response"])

        assert cast(Any, http_response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncInconvo) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.conversations.response.with_raw_response.retrieve(
                response_id="response_id",
                agent_id="",
                conversation_id="conversation_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conversation_id` but received ''"):
            await async_client.agents.conversations.response.with_raw_response.retrieve(
                response_id="response_id",
                agent_id="agentId",
                conversation_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `response_id` but received ''"):
            await async_client.agents.conversations.response.with_raw_response.retrieve(
                response_id="",
                agent_id="agentId",
                conversation_id="conversation_id",
            )
