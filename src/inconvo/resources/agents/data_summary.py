# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.agents.data_summary_retrieve_response import DataSummaryRetrieveResponse

__all__ = ["DataSummaryResource", "AsyncDataSummaryResource"]


class DataSummaryResource(SyncAPIResource):
    """Retrieve information about agents and their data access"""

    @cached_property
    def with_raw_response(self) -> DataSummaryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/inconvoai/inconvo-python-sdk#accessing-raw-response-data-eg-headers
        """
        return DataSummaryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DataSummaryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/inconvoai/inconvo-python-sdk#with_streaming_response
        """
        return DataSummaryResourceWithStreamingResponse(self)

    def retrieve(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataSummaryRetrieveResponse:
        """
        Retrieve a summary of data available to the agent

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get(
            f"/agents/{agent_id}/data-summary",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataSummaryRetrieveResponse,
        )


class AsyncDataSummaryResource(AsyncAPIResource):
    """Retrieve information about agents and their data access"""

    @cached_property
    def with_raw_response(self) -> AsyncDataSummaryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/inconvoai/inconvo-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncDataSummaryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDataSummaryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/inconvoai/inconvo-python-sdk#with_streaming_response
        """
        return AsyncDataSummaryResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataSummaryRetrieveResponse:
        """
        Retrieve a summary of data available to the agent

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._get(
            f"/agents/{agent_id}/data-summary",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataSummaryRetrieveResponse,
        )


class DataSummaryResourceWithRawResponse:
    def __init__(self, data_summary: DataSummaryResource) -> None:
        self._data_summary = data_summary

        self.retrieve = to_raw_response_wrapper(
            data_summary.retrieve,
        )


class AsyncDataSummaryResourceWithRawResponse:
    def __init__(self, data_summary: AsyncDataSummaryResource) -> None:
        self._data_summary = data_summary

        self.retrieve = async_to_raw_response_wrapper(
            data_summary.retrieve,
        )


class DataSummaryResourceWithStreamingResponse:
    def __init__(self, data_summary: DataSummaryResource) -> None:
        self._data_summary = data_summary

        self.retrieve = to_streamed_response_wrapper(
            data_summary.retrieve,
        )


class AsyncDataSummaryResourceWithStreamingResponse:
    def __init__(self, data_summary: AsyncDataSummaryResource) -> None:
        self._data_summary = data_summary

        self.retrieve = async_to_streamed_response_wrapper(
            data_summary.retrieve,
        )
