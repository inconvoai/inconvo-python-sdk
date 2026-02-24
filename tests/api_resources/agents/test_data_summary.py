# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from inconvo import Inconvo, AsyncInconvo
from tests.utils import assert_matches_type
from inconvo.types.agents import DataSummaryRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDataSummary:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Inconvo) -> None:
        data_summary = client.agents.data_summary.retrieve(
            "agentId",
        )
        assert_matches_type(DataSummaryRetrieveResponse, data_summary, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Inconvo) -> None:
        response = client.agents.data_summary.with_raw_response.retrieve(
            "agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_summary = response.parse()
        assert_matches_type(DataSummaryRetrieveResponse, data_summary, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Inconvo) -> None:
        with client.agents.data_summary.with_streaming_response.retrieve(
            "agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_summary = response.parse()
            assert_matches_type(DataSummaryRetrieveResponse, data_summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Inconvo) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.data_summary.with_raw_response.retrieve(
                "",
            )


class TestAsyncDataSummary:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncInconvo) -> None:
        data_summary = await async_client.agents.data_summary.retrieve(
            "agentId",
        )
        assert_matches_type(DataSummaryRetrieveResponse, data_summary, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncInconvo) -> None:
        response = await async_client.agents.data_summary.with_raw_response.retrieve(
            "agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_summary = await response.parse()
        assert_matches_type(DataSummaryRetrieveResponse, data_summary, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncInconvo) -> None:
        async with async_client.agents.data_summary.with_streaming_response.retrieve(
            "agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_summary = await response.parse()
            assert_matches_type(DataSummaryRetrieveResponse, data_summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncInconvo) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.data_summary.with_raw_response.retrieve(
                "",
            )
