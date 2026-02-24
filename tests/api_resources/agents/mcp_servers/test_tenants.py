# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from inconvo import Inconvo, AsyncInconvo
from tests.utils import assert_matches_type
from inconvo.types.agents.mcp_servers import TenantCreateResponse, TenantDeleteResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTenants:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Inconvo) -> None:
        tenant = client.agents.mcp_servers.tenants.create(
            mcpserver_id="mcpserver_id",
            agent_id="agentId",
            tenant={"fromapi@api.com": {"organisationId": "bar"}},
        )
        assert_matches_type(TenantCreateResponse, tenant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Inconvo) -> None:
        response = client.agents.mcp_servers.tenants.with_raw_response.create(
            mcpserver_id="mcpserver_id",
            agent_id="agentId",
            tenant={"fromapi@api.com": {"organisationId": "bar"}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tenant = response.parse()
        assert_matches_type(TenantCreateResponse, tenant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Inconvo) -> None:
        with client.agents.mcp_servers.tenants.with_streaming_response.create(
            mcpserver_id="mcpserver_id",
            agent_id="agentId",
            tenant={"fromapi@api.com": {"organisationId": "bar"}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tenant = response.parse()
            assert_matches_type(TenantCreateResponse, tenant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Inconvo) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.mcp_servers.tenants.with_raw_response.create(
                mcpserver_id="mcpserver_id",
                agent_id="",
                tenant={"fromapi@api.com": {"organisationId": "bar"}},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcpserver_id` but received ''"):
            client.agents.mcp_servers.tenants.with_raw_response.create(
                mcpserver_id="",
                agent_id="agentId",
                tenant={"fromapi@api.com": {"organisationId": "bar"}},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Inconvo) -> None:
        tenant = client.agents.mcp_servers.tenants.delete(
            mcpserver_id="mcpserver_id",
            agent_id="agentId",
            tenant_key="tenant_key",
        )
        assert_matches_type(TenantDeleteResponse, tenant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Inconvo) -> None:
        response = client.agents.mcp_servers.tenants.with_raw_response.delete(
            mcpserver_id="mcpserver_id",
            agent_id="agentId",
            tenant_key="tenant_key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tenant = response.parse()
        assert_matches_type(TenantDeleteResponse, tenant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Inconvo) -> None:
        with client.agents.mcp_servers.tenants.with_streaming_response.delete(
            mcpserver_id="mcpserver_id",
            agent_id="agentId",
            tenant_key="tenant_key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tenant = response.parse()
            assert_matches_type(TenantDeleteResponse, tenant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Inconvo) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.mcp_servers.tenants.with_raw_response.delete(
                mcpserver_id="mcpserver_id",
                agent_id="",
                tenant_key="tenant_key",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcpserver_id` but received ''"):
            client.agents.mcp_servers.tenants.with_raw_response.delete(
                mcpserver_id="",
                agent_id="agentId",
                tenant_key="tenant_key",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_key` but received ''"):
            client.agents.mcp_servers.tenants.with_raw_response.delete(
                mcpserver_id="mcpserver_id",
                agent_id="agentId",
                tenant_key="",
            )


class TestAsyncTenants:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncInconvo) -> None:
        tenant = await async_client.agents.mcp_servers.tenants.create(
            mcpserver_id="mcpserver_id",
            agent_id="agentId",
            tenant={"fromapi@api.com": {"organisationId": "bar"}},
        )
        assert_matches_type(TenantCreateResponse, tenant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncInconvo) -> None:
        response = await async_client.agents.mcp_servers.tenants.with_raw_response.create(
            mcpserver_id="mcpserver_id",
            agent_id="agentId",
            tenant={"fromapi@api.com": {"organisationId": "bar"}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tenant = await response.parse()
        assert_matches_type(TenantCreateResponse, tenant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncInconvo) -> None:
        async with async_client.agents.mcp_servers.tenants.with_streaming_response.create(
            mcpserver_id="mcpserver_id",
            agent_id="agentId",
            tenant={"fromapi@api.com": {"organisationId": "bar"}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tenant = await response.parse()
            assert_matches_type(TenantCreateResponse, tenant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncInconvo) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.mcp_servers.tenants.with_raw_response.create(
                mcpserver_id="mcpserver_id",
                agent_id="",
                tenant={"fromapi@api.com": {"organisationId": "bar"}},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcpserver_id` but received ''"):
            await async_client.agents.mcp_servers.tenants.with_raw_response.create(
                mcpserver_id="",
                agent_id="agentId",
                tenant={"fromapi@api.com": {"organisationId": "bar"}},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncInconvo) -> None:
        tenant = await async_client.agents.mcp_servers.tenants.delete(
            mcpserver_id="mcpserver_id",
            agent_id="agentId",
            tenant_key="tenant_key",
        )
        assert_matches_type(TenantDeleteResponse, tenant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncInconvo) -> None:
        response = await async_client.agents.mcp_servers.tenants.with_raw_response.delete(
            mcpserver_id="mcpserver_id",
            agent_id="agentId",
            tenant_key="tenant_key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tenant = await response.parse()
        assert_matches_type(TenantDeleteResponse, tenant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncInconvo) -> None:
        async with async_client.agents.mcp_servers.tenants.with_streaming_response.delete(
            mcpserver_id="mcpserver_id",
            agent_id="agentId",
            tenant_key="tenant_key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tenant = await response.parse()
            assert_matches_type(TenantDeleteResponse, tenant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncInconvo) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.mcp_servers.tenants.with_raw_response.delete(
                mcpserver_id="mcpserver_id",
                agent_id="",
                tenant_key="tenant_key",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mcpserver_id` but received ''"):
            await async_client.agents.mcp_servers.tenants.with_raw_response.delete(
                mcpserver_id="",
                agent_id="agentId",
                tenant_key="tenant_key",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_key` but received ''"):
            await async_client.agents.mcp_servers.tenants.with_raw_response.delete(
                mcpserver_id="mcpserver_id",
                agent_id="agentId",
                tenant_key="",
            )
