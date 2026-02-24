# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Dict, Iterator, AsyncIterator, cast
from typing_extensions import Literal, overload, override

import httpx

from .feedback import (
    FeedbackResource,
    AsyncFeedbackResource,
    FeedbackResourceWithRawResponse,
    AsyncFeedbackResourceWithRawResponse,
    FeedbackResourceWithStreamingResponse,
    AsyncFeedbackResourceWithStreamingResponse,
)
from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._streaming import Stream, AsyncStream
from ....._base_client import make_request_options
from .....types.agents.conversations import response_create_params
from .....types.agents.conversations.response_create_response import ResponseCreateResponse
from .....types.agents.conversations.response_retrieve_response import ResponseRetrieveResponse

__all__ = ["ResponseResource", "AsyncResponseResource"]


ResponseStreamEvent = Dict[str, Any]


def _with_sse_accept_header(extra_headers: Headers | None) -> Headers:
    return {**(extra_headers or {}), "Accept": "text/event-stream"}


class ResponseCreateEventStream(Stream[ResponseStreamEvent]):
    @override
    def __stream__(self) -> Iterator[ResponseStreamEvent]:
        cast_to = cast(Any, self._cast_to)
        response = self.response
        process_data = self._client._process_response_data
        iterator = self._iter_events()

        try:
            for sse in iterator:
                if sse.data == "[DONE]":
                    continue

                try:
                    data = sse.json()
                except Exception:
                    continue

                yield process_data(data=data, cast_to=cast_to, response=response)
        finally:
            response.close()


class AsyncResponseCreateEventStream(AsyncStream[ResponseStreamEvent]):
    @override
    async def __stream__(self) -> AsyncIterator[ResponseStreamEvent]:
        cast_to = cast(Any, self._cast_to)
        response = self.response
        process_data = self._client._process_response_data
        iterator = self._iter_events()

        try:
            async for sse in iterator:
                if sse.data == "[DONE]":
                    continue

                try:
                    data = sse.json()
                except Exception:
                    continue

                yield process_data(data=data, cast_to=cast_to, response=response)
        finally:
            await response.aclose()


class ResponseResource(SyncAPIResource):
    @cached_property
    def feedback(self) -> FeedbackResource:
        return FeedbackResource(self._client)

    @cached_property
    def with_raw_response(self) -> ResponseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/inconvoai/inconvo-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ResponseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResponseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/inconvoai/inconvo-python-sdk#with_streaming_response
        """
        return ResponseResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        conversation_id: str,
        *,
        agent_id: str,
        message: str,
        stream: Literal[True],
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResponseCreateEventStream: ...

    @overload
    def create(
        self,
        conversation_id: str,
        *,
        agent_id: str,
        message: str,
        stream: Literal[False] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResponseCreateResponse: ...

    @overload
    def create(
        self,
        conversation_id: str,
        *,
        agent_id: str,
        message: str,
        stream: bool | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResponseCreateResponse | ResponseCreateEventStream: ...

    def create(
        self,
        conversation_id: str,
        *,
        agent_id: str,
        message: str,
        stream: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResponseCreateResponse | ResponseCreateEventStream:
        """
        Create response (sync or streamed)

        Args:
          stream: If true and the client sets `Accept: text/event-stream`, the API returns an SSE
              stream instead of a single JSON body.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        extra_headers = _with_sse_accept_header(extra_headers) if stream is True else extra_headers
        return self._post(
            f"/agents/{agent_id}/conversations/{conversation_id}/response",
            body=maybe_transform(
                {
                    "message": message,
                    "stream": stream,
                },
                response_create_params.ResponseCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResponseCreateResponse,
            stream=stream is True,
            stream_cls=ResponseCreateEventStream if stream is True else None,
        )

    def retrieve(
        self,
        response_id: str,
        *,
        agent_id: str,
        conversation_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResponseRetrieveResponse:
        """
        Get a response

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        if not response_id:
            raise ValueError(f"Expected a non-empty value for `response_id` but received {response_id!r}")
        return self._get(
            f"/agents/{agent_id}/conversations/{conversation_id}/response/{response_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResponseRetrieveResponse,
        )


class AsyncResponseResource(AsyncAPIResource):
    @cached_property
    def feedback(self) -> AsyncFeedbackResource:
        return AsyncFeedbackResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncResponseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/inconvoai/inconvo-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncResponseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResponseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/inconvoai/inconvo-python-sdk#with_streaming_response
        """
        return AsyncResponseResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        conversation_id: str,
        *,
        agent_id: str,
        message: str,
        stream: Literal[True],
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncResponseCreateEventStream: ...

    @overload
    async def create(
        self,
        conversation_id: str,
        *,
        agent_id: str,
        message: str,
        stream: Literal[False] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResponseCreateResponse: ...

    @overload
    async def create(
        self,
        conversation_id: str,
        *,
        agent_id: str,
        message: str,
        stream: bool | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResponseCreateResponse | AsyncResponseCreateEventStream: ...

    async def create(
        self,
        conversation_id: str,
        *,
        agent_id: str,
        message: str,
        stream: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResponseCreateResponse | AsyncResponseCreateEventStream:
        """
        Create response (sync or streamed)

        Args:
          stream: If true and the client sets `Accept: text/event-stream`, the API returns an SSE
              stream instead of a single JSON body.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        extra_headers = _with_sse_accept_header(extra_headers) if stream is True else extra_headers
        return await self._post(
            f"/agents/{agent_id}/conversations/{conversation_id}/response",
            body=await async_maybe_transform(
                {
                    "message": message,
                    "stream": stream,
                },
                response_create_params.ResponseCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResponseCreateResponse,
            stream=stream is True,
            stream_cls=AsyncResponseCreateEventStream if stream is True else None,
        )

    async def retrieve(
        self,
        response_id: str,
        *,
        agent_id: str,
        conversation_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResponseRetrieveResponse:
        """
        Get a response

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        if not response_id:
            raise ValueError(f"Expected a non-empty value for `response_id` but received {response_id!r}")
        return await self._get(
            f"/agents/{agent_id}/conversations/{conversation_id}/response/{response_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResponseRetrieveResponse,
        )


class ResponseResourceWithRawResponse:
    def __init__(self, response: ResponseResource) -> None:
        self._response = response

        self.create = to_raw_response_wrapper(
            response.create,
        )
        self.retrieve = to_raw_response_wrapper(
            response.retrieve,
        )

    @cached_property
    def feedback(self) -> FeedbackResourceWithRawResponse:
        return FeedbackResourceWithRawResponse(self._response.feedback)


class AsyncResponseResourceWithRawResponse:
    def __init__(self, response: AsyncResponseResource) -> None:
        self._response = response

        self.create = async_to_raw_response_wrapper(
            response.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            response.retrieve,
        )

    @cached_property
    def feedback(self) -> AsyncFeedbackResourceWithRawResponse:
        return AsyncFeedbackResourceWithRawResponse(self._response.feedback)


class ResponseResourceWithStreamingResponse:
    def __init__(self, response: ResponseResource) -> None:
        self._response = response

        self.create = to_streamed_response_wrapper(
            response.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            response.retrieve,
        )

    @cached_property
    def feedback(self) -> FeedbackResourceWithStreamingResponse:
        return FeedbackResourceWithStreamingResponse(self._response.feedback)


class AsyncResponseResourceWithStreamingResponse:
    def __init__(self, response: AsyncResponseResource) -> None:
        self._response = response

        self.create = async_to_streamed_response_wrapper(
            response.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            response.retrieve,
        )

    @cached_property
    def feedback(self) -> AsyncFeedbackResourceWithStreamingResponse:
        return AsyncFeedbackResourceWithStreamingResponse(self._response.feedback)
