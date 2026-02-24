# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .data_summary import (
    DataSummaryResource,
    AsyncDataSummaryResource,
    DataSummaryResourceWithRawResponse,
    AsyncDataSummaryResourceWithRawResponse,
    DataSummaryResourceWithStreamingResponse,
    AsyncDataSummaryResourceWithStreamingResponse,
)
from .datasets.datasets import (
    DatasetsResource,
    AsyncDatasetsResource,
    DatasetsResourceWithRawResponse,
    AsyncDatasetsResourceWithRawResponse,
    DatasetsResourceWithStreamingResponse,
    AsyncDatasetsResourceWithStreamingResponse,
)
from .mcp_servers.mcp_servers import (
    McpServersResource,
    AsyncMcpServersResource,
    McpServersResourceWithRawResponse,
    AsyncMcpServersResourceWithRawResponse,
    McpServersResourceWithStreamingResponse,
    AsyncMcpServersResourceWithStreamingResponse,
)
from .conversations.conversations import (
    ConversationsResource,
    AsyncConversationsResource,
    ConversationsResourceWithRawResponse,
    AsyncConversationsResourceWithRawResponse,
    ConversationsResourceWithStreamingResponse,
    AsyncConversationsResourceWithStreamingResponse,
)

__all__ = ["AgentsResource", "AsyncAgentsResource"]


class AgentsResource(SyncAPIResource):
    @cached_property
    def data_summary(self) -> DataSummaryResource:
        return DataSummaryResource(self._client)

    @cached_property
    def conversations(self) -> ConversationsResource:
        return ConversationsResource(self._client)

    @cached_property
    def datasets(self) -> DatasetsResource:
        return DatasetsResource(self._client)

    @cached_property
    def mcp_servers(self) -> McpServersResource:
        return McpServersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/inconvo-python#accessing-raw-response-data-eg-headers
        """
        return AgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/inconvo-python#with_streaming_response
        """
        return AgentsResourceWithStreamingResponse(self)


class AsyncAgentsResource(AsyncAPIResource):
    @cached_property
    def data_summary(self) -> AsyncDataSummaryResource:
        return AsyncDataSummaryResource(self._client)

    @cached_property
    def conversations(self) -> AsyncConversationsResource:
        return AsyncConversationsResource(self._client)

    @cached_property
    def datasets(self) -> AsyncDatasetsResource:
        return AsyncDatasetsResource(self._client)

    @cached_property
    def mcp_servers(self) -> AsyncMcpServersResource:
        return AsyncMcpServersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/inconvo-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/inconvo-python#with_streaming_response
        """
        return AsyncAgentsResourceWithStreamingResponse(self)


class AgentsResourceWithRawResponse:
    def __init__(self, agents: AgentsResource) -> None:
        self._agents = agents

    @cached_property
    def data_summary(self) -> DataSummaryResourceWithRawResponse:
        return DataSummaryResourceWithRawResponse(self._agents.data_summary)

    @cached_property
    def conversations(self) -> ConversationsResourceWithRawResponse:
        return ConversationsResourceWithRawResponse(self._agents.conversations)

    @cached_property
    def datasets(self) -> DatasetsResourceWithRawResponse:
        return DatasetsResourceWithRawResponse(self._agents.datasets)

    @cached_property
    def mcp_servers(self) -> McpServersResourceWithRawResponse:
        return McpServersResourceWithRawResponse(self._agents.mcp_servers)


class AsyncAgentsResourceWithRawResponse:
    def __init__(self, agents: AsyncAgentsResource) -> None:
        self._agents = agents

    @cached_property
    def data_summary(self) -> AsyncDataSummaryResourceWithRawResponse:
        return AsyncDataSummaryResourceWithRawResponse(self._agents.data_summary)

    @cached_property
    def conversations(self) -> AsyncConversationsResourceWithRawResponse:
        return AsyncConversationsResourceWithRawResponse(self._agents.conversations)

    @cached_property
    def datasets(self) -> AsyncDatasetsResourceWithRawResponse:
        return AsyncDatasetsResourceWithRawResponse(self._agents.datasets)

    @cached_property
    def mcp_servers(self) -> AsyncMcpServersResourceWithRawResponse:
        return AsyncMcpServersResourceWithRawResponse(self._agents.mcp_servers)


class AgentsResourceWithStreamingResponse:
    def __init__(self, agents: AgentsResource) -> None:
        self._agents = agents

    @cached_property
    def data_summary(self) -> DataSummaryResourceWithStreamingResponse:
        return DataSummaryResourceWithStreamingResponse(self._agents.data_summary)

    @cached_property
    def conversations(self) -> ConversationsResourceWithStreamingResponse:
        return ConversationsResourceWithStreamingResponse(self._agents.conversations)

    @cached_property
    def datasets(self) -> DatasetsResourceWithStreamingResponse:
        return DatasetsResourceWithStreamingResponse(self._agents.datasets)

    @cached_property
    def mcp_servers(self) -> McpServersResourceWithStreamingResponse:
        return McpServersResourceWithStreamingResponse(self._agents.mcp_servers)


class AsyncAgentsResourceWithStreamingResponse:
    def __init__(self, agents: AsyncAgentsResource) -> None:
        self._agents = agents

    @cached_property
    def data_summary(self) -> AsyncDataSummaryResourceWithStreamingResponse:
        return AsyncDataSummaryResourceWithStreamingResponse(self._agents.data_summary)

    @cached_property
    def conversations(self) -> AsyncConversationsResourceWithStreamingResponse:
        return AsyncConversationsResourceWithStreamingResponse(self._agents.conversations)

    @cached_property
    def datasets(self) -> AsyncDatasetsResourceWithStreamingResponse:
        return AsyncDatasetsResourceWithStreamingResponse(self._agents.datasets)

    @cached_property
    def mcp_servers(self) -> AsyncMcpServersResourceWithStreamingResponse:
        return AsyncMcpServersResourceWithStreamingResponse(self._agents.mcp_servers)
