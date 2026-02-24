# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from inconvo import Inconvo, AsyncInconvo
from tests.utils import assert_matches_type
from inconvo.types.agents.conversations.response import Feedback

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFeedback:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Inconvo) -> None:
        feedback = client.agents.conversations.response.feedback.create(
            response_id="response_id",
            agent_id="agentId",
            conversation_id="conversation_id",
            rating="positive",
        )
        assert_matches_type(Feedback, feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Inconvo) -> None:
        feedback = client.agents.conversations.response.feedback.create(
            response_id="response_id",
            agent_id="agentId",
            conversation_id="conversation_id",
            rating="positive",
            comment="comment",
        )
        assert_matches_type(Feedback, feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Inconvo) -> None:
        response = client.agents.conversations.response.feedback.with_raw_response.create(
            response_id="response_id",
            agent_id="agentId",
            conversation_id="conversation_id",
            rating="positive",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback = response.parse()
        assert_matches_type(Feedback, feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Inconvo) -> None:
        with client.agents.conversations.response.feedback.with_streaming_response.create(
            response_id="response_id",
            agent_id="agentId",
            conversation_id="conversation_id",
            rating="positive",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feedback = response.parse()
            assert_matches_type(Feedback, feedback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Inconvo) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.conversations.response.feedback.with_raw_response.create(
                response_id="response_id",
                agent_id="",
                conversation_id="conversation_id",
                rating="positive",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conversation_id` but received ''"):
            client.agents.conversations.response.feedback.with_raw_response.create(
                response_id="response_id",
                agent_id="agentId",
                conversation_id="",
                rating="positive",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `response_id` but received ''"):
            client.agents.conversations.response.feedback.with_raw_response.create(
                response_id="",
                agent_id="agentId",
                conversation_id="conversation_id",
                rating="positive",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Inconvo) -> None:
        feedback = client.agents.conversations.response.feedback.update(
            feedback_id="feedback_id",
            agent_id="agentId",
            conversation_id="conversation_id",
            response_id="response_id",
        )
        assert_matches_type(Feedback, feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Inconvo) -> None:
        feedback = client.agents.conversations.response.feedback.update(
            feedback_id="feedback_id",
            agent_id="agentId",
            conversation_id="conversation_id",
            response_id="response_id",
            comment="comment",
            rating="positive",
        )
        assert_matches_type(Feedback, feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Inconvo) -> None:
        response = client.agents.conversations.response.feedback.with_raw_response.update(
            feedback_id="feedback_id",
            agent_id="agentId",
            conversation_id="conversation_id",
            response_id="response_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback = response.parse()
        assert_matches_type(Feedback, feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Inconvo) -> None:
        with client.agents.conversations.response.feedback.with_streaming_response.update(
            feedback_id="feedback_id",
            agent_id="agentId",
            conversation_id="conversation_id",
            response_id="response_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feedback = response.parse()
            assert_matches_type(Feedback, feedback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Inconvo) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.conversations.response.feedback.with_raw_response.update(
                feedback_id="feedback_id",
                agent_id="",
                conversation_id="conversation_id",
                response_id="response_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conversation_id` but received ''"):
            client.agents.conversations.response.feedback.with_raw_response.update(
                feedback_id="feedback_id",
                agent_id="agentId",
                conversation_id="",
                response_id="response_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `response_id` but received ''"):
            client.agents.conversations.response.feedback.with_raw_response.update(
                feedback_id="feedback_id",
                agent_id="agentId",
                conversation_id="conversation_id",
                response_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `feedback_id` but received ''"):
            client.agents.conversations.response.feedback.with_raw_response.update(
                feedback_id="",
                agent_id="agentId",
                conversation_id="conversation_id",
                response_id="response_id",
            )


class TestAsyncFeedback:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncInconvo) -> None:
        feedback = await async_client.agents.conversations.response.feedback.create(
            response_id="response_id",
            agent_id="agentId",
            conversation_id="conversation_id",
            rating="positive",
        )
        assert_matches_type(Feedback, feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncInconvo) -> None:
        feedback = await async_client.agents.conversations.response.feedback.create(
            response_id="response_id",
            agent_id="agentId",
            conversation_id="conversation_id",
            rating="positive",
            comment="comment",
        )
        assert_matches_type(Feedback, feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncInconvo) -> None:
        response = await async_client.agents.conversations.response.feedback.with_raw_response.create(
            response_id="response_id",
            agent_id="agentId",
            conversation_id="conversation_id",
            rating="positive",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback = await response.parse()
        assert_matches_type(Feedback, feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncInconvo) -> None:
        async with async_client.agents.conversations.response.feedback.with_streaming_response.create(
            response_id="response_id",
            agent_id="agentId",
            conversation_id="conversation_id",
            rating="positive",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feedback = await response.parse()
            assert_matches_type(Feedback, feedback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncInconvo) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.conversations.response.feedback.with_raw_response.create(
                response_id="response_id",
                agent_id="",
                conversation_id="conversation_id",
                rating="positive",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conversation_id` but received ''"):
            await async_client.agents.conversations.response.feedback.with_raw_response.create(
                response_id="response_id",
                agent_id="agentId",
                conversation_id="",
                rating="positive",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `response_id` but received ''"):
            await async_client.agents.conversations.response.feedback.with_raw_response.create(
                response_id="",
                agent_id="agentId",
                conversation_id="conversation_id",
                rating="positive",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncInconvo) -> None:
        feedback = await async_client.agents.conversations.response.feedback.update(
            feedback_id="feedback_id",
            agent_id="agentId",
            conversation_id="conversation_id",
            response_id="response_id",
        )
        assert_matches_type(Feedback, feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncInconvo) -> None:
        feedback = await async_client.agents.conversations.response.feedback.update(
            feedback_id="feedback_id",
            agent_id="agentId",
            conversation_id="conversation_id",
            response_id="response_id",
            comment="comment",
            rating="positive",
        )
        assert_matches_type(Feedback, feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncInconvo) -> None:
        response = await async_client.agents.conversations.response.feedback.with_raw_response.update(
            feedback_id="feedback_id",
            agent_id="agentId",
            conversation_id="conversation_id",
            response_id="response_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback = await response.parse()
        assert_matches_type(Feedback, feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncInconvo) -> None:
        async with async_client.agents.conversations.response.feedback.with_streaming_response.update(
            feedback_id="feedback_id",
            agent_id="agentId",
            conversation_id="conversation_id",
            response_id="response_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feedback = await response.parse()
            assert_matches_type(Feedback, feedback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncInconvo) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.conversations.response.feedback.with_raw_response.update(
                feedback_id="feedback_id",
                agent_id="",
                conversation_id="conversation_id",
                response_id="response_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conversation_id` but received ''"):
            await async_client.agents.conversations.response.feedback.with_raw_response.update(
                feedback_id="feedback_id",
                agent_id="agentId",
                conversation_id="",
                response_id="response_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `response_id` but received ''"):
            await async_client.agents.conversations.response.feedback.with_raw_response.update(
                feedback_id="feedback_id",
                agent_id="agentId",
                conversation_id="conversation_id",
                response_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `feedback_id` but received ''"):
            await async_client.agents.conversations.response.feedback.with_raw_response.update(
                feedback_id="",
                agent_id="agentId",
                conversation_id="conversation_id",
                response_id="response_id",
            )
