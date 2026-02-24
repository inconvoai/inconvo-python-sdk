# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from inconvo import Inconvo, AsyncInconvo
from tests.utils import assert_matches_type
from inconvo.types.agents.datasets import (
    ContextListResponse,
    ContextDeleteResponse,
    ContextUploadResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContext:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Inconvo) -> None:
        context = client.agents.datasets.context.list(
            context_value="org_456",
            agent_id="agentId",
            context_key="orgId",
        )
        assert_matches_type(ContextListResponse, context, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Inconvo) -> None:
        response = client.agents.datasets.context.with_raw_response.list(
            context_value="org_456",
            agent_id="agentId",
            context_key="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        context = response.parse()
        assert_matches_type(ContextListResponse, context, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Inconvo) -> None:
        with client.agents.datasets.context.with_streaming_response.list(
            context_value="org_456",
            agent_id="agentId",
            context_key="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            context = response.parse()
            assert_matches_type(ContextListResponse, context, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Inconvo) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.datasets.context.with_raw_response.list(
                context_value="org_456",
                agent_id="",
                context_key="orgId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `context_key` but received ''"):
            client.agents.datasets.context.with_raw_response.list(
                context_value="org_456",
                agent_id="agentId",
                context_key="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `context_value` but received ''"):
            client.agents.datasets.context.with_raw_response.list(
                context_value="",
                agent_id="agentId",
                context_key="orgId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Inconvo) -> None:
        context = client.agents.datasets.context.delete(
            filename="shared_data.csv",
            agent_id="agentId",
            context_key="orgId",
            context_value="org_456",
        )
        assert_matches_type(ContextDeleteResponse, context, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Inconvo) -> None:
        response = client.agents.datasets.context.with_raw_response.delete(
            filename="shared_data.csv",
            agent_id="agentId",
            context_key="orgId",
            context_value="org_456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        context = response.parse()
        assert_matches_type(ContextDeleteResponse, context, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Inconvo) -> None:
        with client.agents.datasets.context.with_streaming_response.delete(
            filename="shared_data.csv",
            agent_id="agentId",
            context_key="orgId",
            context_value="org_456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            context = response.parse()
            assert_matches_type(ContextDeleteResponse, context, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Inconvo) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.datasets.context.with_raw_response.delete(
                filename="shared_data.csv",
                agent_id="",
                context_key="orgId",
                context_value="org_456",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `context_key` but received ''"):
            client.agents.datasets.context.with_raw_response.delete(
                filename="shared_data.csv",
                agent_id="agentId",
                context_key="",
                context_value="org_456",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `context_value` but received ''"):
            client.agents.datasets.context.with_raw_response.delete(
                filename="shared_data.csv",
                agent_id="agentId",
                context_key="orgId",
                context_value="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `filename` but received ''"):
            client.agents.datasets.context.with_raw_response.delete(
                filename="",
                agent_id="agentId",
                context_key="orgId",
                context_value="org_456",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upload(self, client: Inconvo) -> None:
        context = client.agents.datasets.context.upload(
            context_value="org_456",
            agent_id="agentId",
            context_key="orgId",
            file=b"raw file contents",
        )
        assert_matches_type(ContextUploadResponse, context, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upload_with_all_params(self, client: Inconvo) -> None:
        context = client.agents.datasets.context.upload(
            context_value="org_456",
            agent_id="agentId",
            context_key="orgId",
            file=b"raw file contents",
            notes="notes",
        )
        assert_matches_type(ContextUploadResponse, context, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_upload(self, client: Inconvo) -> None:
        response = client.agents.datasets.context.with_raw_response.upload(
            context_value="org_456",
            agent_id="agentId",
            context_key="orgId",
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        context = response.parse()
        assert_matches_type(ContextUploadResponse, context, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_upload(self, client: Inconvo) -> None:
        with client.agents.datasets.context.with_streaming_response.upload(
            context_value="org_456",
            agent_id="agentId",
            context_key="orgId",
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            context = response.parse()
            assert_matches_type(ContextUploadResponse, context, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_upload(self, client: Inconvo) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.datasets.context.with_raw_response.upload(
                context_value="org_456",
                agent_id="",
                context_key="orgId",
                file=b"raw file contents",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `context_key` but received ''"):
            client.agents.datasets.context.with_raw_response.upload(
                context_value="org_456",
                agent_id="agentId",
                context_key="",
                file=b"raw file contents",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `context_value` but received ''"):
            client.agents.datasets.context.with_raw_response.upload(
                context_value="",
                agent_id="agentId",
                context_key="orgId",
                file=b"raw file contents",
            )


class TestAsyncContext:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncInconvo) -> None:
        context = await async_client.agents.datasets.context.list(
            context_value="org_456",
            agent_id="agentId",
            context_key="orgId",
        )
        assert_matches_type(ContextListResponse, context, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncInconvo) -> None:
        response = await async_client.agents.datasets.context.with_raw_response.list(
            context_value="org_456",
            agent_id="agentId",
            context_key="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        context = await response.parse()
        assert_matches_type(ContextListResponse, context, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncInconvo) -> None:
        async with async_client.agents.datasets.context.with_streaming_response.list(
            context_value="org_456",
            agent_id="agentId",
            context_key="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            context = await response.parse()
            assert_matches_type(ContextListResponse, context, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncInconvo) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.datasets.context.with_raw_response.list(
                context_value="org_456",
                agent_id="",
                context_key="orgId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `context_key` but received ''"):
            await async_client.agents.datasets.context.with_raw_response.list(
                context_value="org_456",
                agent_id="agentId",
                context_key="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `context_value` but received ''"):
            await async_client.agents.datasets.context.with_raw_response.list(
                context_value="",
                agent_id="agentId",
                context_key="orgId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncInconvo) -> None:
        context = await async_client.agents.datasets.context.delete(
            filename="shared_data.csv",
            agent_id="agentId",
            context_key="orgId",
            context_value="org_456",
        )
        assert_matches_type(ContextDeleteResponse, context, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncInconvo) -> None:
        response = await async_client.agents.datasets.context.with_raw_response.delete(
            filename="shared_data.csv",
            agent_id="agentId",
            context_key="orgId",
            context_value="org_456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        context = await response.parse()
        assert_matches_type(ContextDeleteResponse, context, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncInconvo) -> None:
        async with async_client.agents.datasets.context.with_streaming_response.delete(
            filename="shared_data.csv",
            agent_id="agentId",
            context_key="orgId",
            context_value="org_456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            context = await response.parse()
            assert_matches_type(ContextDeleteResponse, context, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncInconvo) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.datasets.context.with_raw_response.delete(
                filename="shared_data.csv",
                agent_id="",
                context_key="orgId",
                context_value="org_456",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `context_key` but received ''"):
            await async_client.agents.datasets.context.with_raw_response.delete(
                filename="shared_data.csv",
                agent_id="agentId",
                context_key="",
                context_value="org_456",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `context_value` but received ''"):
            await async_client.agents.datasets.context.with_raw_response.delete(
                filename="shared_data.csv",
                agent_id="agentId",
                context_key="orgId",
                context_value="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `filename` but received ''"):
            await async_client.agents.datasets.context.with_raw_response.delete(
                filename="",
                agent_id="agentId",
                context_key="orgId",
                context_value="org_456",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upload(self, async_client: AsyncInconvo) -> None:
        context = await async_client.agents.datasets.context.upload(
            context_value="org_456",
            agent_id="agentId",
            context_key="orgId",
            file=b"raw file contents",
        )
        assert_matches_type(ContextUploadResponse, context, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upload_with_all_params(self, async_client: AsyncInconvo) -> None:
        context = await async_client.agents.datasets.context.upload(
            context_value="org_456",
            agent_id="agentId",
            context_key="orgId",
            file=b"raw file contents",
            notes="notes",
        )
        assert_matches_type(ContextUploadResponse, context, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncInconvo) -> None:
        response = await async_client.agents.datasets.context.with_raw_response.upload(
            context_value="org_456",
            agent_id="agentId",
            context_key="orgId",
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        context = await response.parse()
        assert_matches_type(ContextUploadResponse, context, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncInconvo) -> None:
        async with async_client.agents.datasets.context.with_streaming_response.upload(
            context_value="org_456",
            agent_id="agentId",
            context_key="orgId",
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            context = await response.parse()
            assert_matches_type(ContextUploadResponse, context, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_upload(self, async_client: AsyncInconvo) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.datasets.context.with_raw_response.upload(
                context_value="org_456",
                agent_id="",
                context_key="orgId",
                file=b"raw file contents",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `context_key` but received ''"):
            await async_client.agents.datasets.context.with_raw_response.upload(
                context_value="org_456",
                agent_id="agentId",
                context_key="",
                file=b"raw file contents",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `context_value` but received ''"):
            await async_client.agents.datasets.context.with_raw_response.upload(
                context_value="",
                agent_id="agentId",
                context_key="orgId",
                file=b"raw file contents",
            )
