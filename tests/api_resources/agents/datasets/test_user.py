# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from inconvo import Inconvo, AsyncInconvo
from tests.utils import assert_matches_type
from inconvo.types.agents.datasets import UserListResponse, UserDeleteResponse, UserUploadResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUser:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Inconvo) -> None:
        user = client.agents.datasets.user.list(
            user_identifier="user_123",
            agent_id="agentId",
        )
        assert_matches_type(UserListResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Inconvo) -> None:
        response = client.agents.datasets.user.with_raw_response.list(
            user_identifier="user_123",
            agent_id="agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserListResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Inconvo) -> None:
        with client.agents.datasets.user.with_streaming_response.list(
            user_identifier="user_123",
            agent_id="agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserListResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Inconvo) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.datasets.user.with_raw_response.list(
                user_identifier="user_123",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_identifier` but received ''"):
            client.agents.datasets.user.with_raw_response.list(
                user_identifier="",
                agent_id="agentId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Inconvo) -> None:
        user = client.agents.datasets.user.delete(
            filename="data.csv",
            agent_id="agentId",
            user_identifier="user_123",
        )
        assert_matches_type(UserDeleteResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Inconvo) -> None:
        response = client.agents.datasets.user.with_raw_response.delete(
            filename="data.csv",
            agent_id="agentId",
            user_identifier="user_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserDeleteResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Inconvo) -> None:
        with client.agents.datasets.user.with_streaming_response.delete(
            filename="data.csv",
            agent_id="agentId",
            user_identifier="user_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserDeleteResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Inconvo) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.datasets.user.with_raw_response.delete(
                filename="data.csv",
                agent_id="",
                user_identifier="user_123",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_identifier` but received ''"):
            client.agents.datasets.user.with_raw_response.delete(
                filename="data.csv",
                agent_id="agentId",
                user_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `filename` but received ''"):
            client.agents.datasets.user.with_raw_response.delete(
                filename="",
                agent_id="agentId",
                user_identifier="user_123",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upload(self, client: Inconvo) -> None:
        user = client.agents.datasets.user.upload(
            user_identifier="user_123",
            agent_id="agentId",
            file=b"Example data",
        )
        assert_matches_type(UserUploadResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upload_with_all_params(self, client: Inconvo) -> None:
        user = client.agents.datasets.user.upload(
            user_identifier="user_123",
            agent_id="agentId",
            file=b"Example data",
            notes="notes",
        )
        assert_matches_type(UserUploadResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_upload(self, client: Inconvo) -> None:
        response = client.agents.datasets.user.with_raw_response.upload(
            user_identifier="user_123",
            agent_id="agentId",
            file=b"Example data",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserUploadResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_upload(self, client: Inconvo) -> None:
        with client.agents.datasets.user.with_streaming_response.upload(
            user_identifier="user_123",
            agent_id="agentId",
            file=b"Example data",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserUploadResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_upload(self, client: Inconvo) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.datasets.user.with_raw_response.upload(
                user_identifier="user_123",
                agent_id="",
                file=b"Example data",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_identifier` but received ''"):
            client.agents.datasets.user.with_raw_response.upload(
                user_identifier="",
                agent_id="agentId",
                file=b"Example data",
            )


class TestAsyncUser:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncInconvo) -> None:
        user = await async_client.agents.datasets.user.list(
            user_identifier="user_123",
            agent_id="agentId",
        )
        assert_matches_type(UserListResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncInconvo) -> None:
        response = await async_client.agents.datasets.user.with_raw_response.list(
            user_identifier="user_123",
            agent_id="agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserListResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncInconvo) -> None:
        async with async_client.agents.datasets.user.with_streaming_response.list(
            user_identifier="user_123",
            agent_id="agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserListResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncInconvo) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.datasets.user.with_raw_response.list(
                user_identifier="user_123",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_identifier` but received ''"):
            await async_client.agents.datasets.user.with_raw_response.list(
                user_identifier="",
                agent_id="agentId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncInconvo) -> None:
        user = await async_client.agents.datasets.user.delete(
            filename="data.csv",
            agent_id="agentId",
            user_identifier="user_123",
        )
        assert_matches_type(UserDeleteResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncInconvo) -> None:
        response = await async_client.agents.datasets.user.with_raw_response.delete(
            filename="data.csv",
            agent_id="agentId",
            user_identifier="user_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserDeleteResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncInconvo) -> None:
        async with async_client.agents.datasets.user.with_streaming_response.delete(
            filename="data.csv",
            agent_id="agentId",
            user_identifier="user_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserDeleteResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncInconvo) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.datasets.user.with_raw_response.delete(
                filename="data.csv",
                agent_id="",
                user_identifier="user_123",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_identifier` but received ''"):
            await async_client.agents.datasets.user.with_raw_response.delete(
                filename="data.csv",
                agent_id="agentId",
                user_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `filename` but received ''"):
            await async_client.agents.datasets.user.with_raw_response.delete(
                filename="",
                agent_id="agentId",
                user_identifier="user_123",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upload(self, async_client: AsyncInconvo) -> None:
        user = await async_client.agents.datasets.user.upload(
            user_identifier="user_123",
            agent_id="agentId",
            file=b"Example data",
        )
        assert_matches_type(UserUploadResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upload_with_all_params(self, async_client: AsyncInconvo) -> None:
        user = await async_client.agents.datasets.user.upload(
            user_identifier="user_123",
            agent_id="agentId",
            file=b"Example data",
            notes="notes",
        )
        assert_matches_type(UserUploadResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncInconvo) -> None:
        response = await async_client.agents.datasets.user.with_raw_response.upload(
            user_identifier="user_123",
            agent_id="agentId",
            file=b"Example data",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserUploadResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncInconvo) -> None:
        async with async_client.agents.datasets.user.with_streaming_response.upload(
            user_identifier="user_123",
            agent_id="agentId",
            file=b"Example data",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserUploadResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_upload(self, async_client: AsyncInconvo) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.datasets.user.with_raw_response.upload(
                user_identifier="user_123",
                agent_id="",
                file=b"Example data",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_identifier` but received ''"):
            await async_client.agents.datasets.user.with_raw_response.upload(
                user_identifier="",
                agent_id="agentId",
                file=b"Example data",
            )
