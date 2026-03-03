# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .tenants import (
    TenantsResource,
    AsyncTenantsResource,
    TenantsResourceWithRawResponse,
    AsyncTenantsResourceWithRawResponse,
    TenantsResourceWithStreamingResponse,
    AsyncTenantsResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["McpServersResource", "AsyncMcpServersResource"]


class McpServersResource(SyncAPIResource):
    @cached_property
    def tenants(self) -> TenantsResource:
        """Manage MCP servers and their tenant mappings"""
        return TenantsResource(self._client)

    @cached_property
    def with_raw_response(self) -> McpServersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/inconvoai/inconvo-python-sdk#accessing-raw-response-data-eg-headers
        """
        return McpServersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> McpServersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/inconvoai/inconvo-python-sdk#with_streaming_response
        """
        return McpServersResourceWithStreamingResponse(self)


class AsyncMcpServersResource(AsyncAPIResource):
    @cached_property
    def tenants(self) -> AsyncTenantsResource:
        """Manage MCP servers and their tenant mappings"""
        return AsyncTenantsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMcpServersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/inconvoai/inconvo-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncMcpServersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMcpServersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/inconvoai/inconvo-python-sdk#with_streaming_response
        """
        return AsyncMcpServersResourceWithStreamingResponse(self)


class McpServersResourceWithRawResponse:
    def __init__(self, mcp_servers: McpServersResource) -> None:
        self._mcp_servers = mcp_servers

    @cached_property
    def tenants(self) -> TenantsResourceWithRawResponse:
        """Manage MCP servers and their tenant mappings"""
        return TenantsResourceWithRawResponse(self._mcp_servers.tenants)


class AsyncMcpServersResourceWithRawResponse:
    def __init__(self, mcp_servers: AsyncMcpServersResource) -> None:
        self._mcp_servers = mcp_servers

    @cached_property
    def tenants(self) -> AsyncTenantsResourceWithRawResponse:
        """Manage MCP servers and their tenant mappings"""
        return AsyncTenantsResourceWithRawResponse(self._mcp_servers.tenants)


class McpServersResourceWithStreamingResponse:
    def __init__(self, mcp_servers: McpServersResource) -> None:
        self._mcp_servers = mcp_servers

    @cached_property
    def tenants(self) -> TenantsResourceWithStreamingResponse:
        """Manage MCP servers and their tenant mappings"""
        return TenantsResourceWithStreamingResponse(self._mcp_servers.tenants)


class AsyncMcpServersResourceWithStreamingResponse:
    def __init__(self, mcp_servers: AsyncMcpServersResource) -> None:
        self._mcp_servers = mcp_servers

    @cached_property
    def tenants(self) -> AsyncTenantsResourceWithStreamingResponse:
        """Manage MCP servers and their tenant mappings"""
        return AsyncTenantsResourceWithStreamingResponse(self._mcp_servers.tenants)
