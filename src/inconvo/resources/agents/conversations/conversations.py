# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncConversationsCursor, AsyncConversationsCursor
from ...._base_client import AsyncPaginator, make_request_options
from ....types.agents import conversation_list_params, conversation_create_params
from .response.response import (
    ResponseResource,
    AsyncResponseResource,
    ResponseResourceWithRawResponse,
    AsyncResponseResourceWithRawResponse,
    ResponseResourceWithStreamingResponse,
    AsyncResponseResourceWithStreamingResponse,
)
from ....types.agents.inconvo_conversation import InconvoConversation
from ....types.agents.conversation_list_response import ConversationListResponse
from ....types.agents.conversation_create_response import ConversationCreateResponse

__all__ = ["ConversationsResource", "AsyncConversationsResource"]


class ConversationsResource(SyncAPIResource):
    @cached_property
    def response(self) -> ResponseResource:
        return ResponseResource(self._client)

    @cached_property
    def with_raw_response(self) -> ConversationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/inconvo-python#accessing-raw-response-data-eg-headers
        """
        return ConversationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConversationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/inconvo-python#with_streaming_response
        """
        return ConversationsResourceWithStreamingResponse(self)

    def create(
        self,
        agent_id: str,
        *,
        user_identifier: str,
        user_context: Dict[str, Union[str, float, bool]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationCreateResponse:
        """
        Create conversation

        Args:
          user_identifier:
              Unique identifier for the end-user (1-256 chars). Allowed characters:
              alphanumeric, underscore, hyphen, period, at symbol.

          user_context: Optional context key-values for additional filtering/tenancy. Required when User
              Context status is ENABLED. Must be omitted when User Context status is DISABLED.
              Requests fail when User Context is UNSET.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._post(
            f"/agents/{agent_id}/conversations",
            body=maybe_transform(
                {
                    "user_identifier": user_identifier,
                    "user_context": user_context,
                },
                conversation_create_params.ConversationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationCreateResponse,
        )

    def retrieve(
        self,
        conversation_id: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InconvoConversation:
        """
        Retrieve conversation

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
        return self._get(
            f"/agents/{agent_id}/conversations/{conversation_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InconvoConversation,
        )

    def list(
        self,
        agent_id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        user_context: Dict[str, Union[str, float, bool]] | Omit = omit,
        user_identifier: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncConversationsCursor[ConversationListResponse]:
        """
        List conversations

        Args:
          user_context: Arbitrary userContext filters, encoded as a deep object. Example: GET
              /conversations?userContext[userId]=42&userContext[orgId]=12

          user_identifier: Filter by user identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get_api_list(
            f"/agents/{agent_id}/conversations",
            page=SyncConversationsCursor[ConversationListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "user_context": user_context,
                        "user_identifier": user_identifier,
                    },
                    conversation_list_params.ConversationListParams,
                ),
            ),
            model=ConversationListResponse,
        )


class AsyncConversationsResource(AsyncAPIResource):
    @cached_property
    def response(self) -> AsyncResponseResource:
        return AsyncResponseResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncConversationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/inconvo-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConversationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConversationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/inconvo-python#with_streaming_response
        """
        return AsyncConversationsResourceWithStreamingResponse(self)

    async def create(
        self,
        agent_id: str,
        *,
        user_identifier: str,
        user_context: Dict[str, Union[str, float, bool]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationCreateResponse:
        """
        Create conversation

        Args:
          user_identifier:
              Unique identifier for the end-user (1-256 chars). Allowed characters:
              alphanumeric, underscore, hyphen, period, at symbol.

          user_context: Optional context key-values for additional filtering/tenancy. Required when User
              Context status is ENABLED. Must be omitted when User Context status is DISABLED.
              Requests fail when User Context is UNSET.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._post(
            f"/agents/{agent_id}/conversations",
            body=await async_maybe_transform(
                {
                    "user_identifier": user_identifier,
                    "user_context": user_context,
                },
                conversation_create_params.ConversationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationCreateResponse,
        )

    async def retrieve(
        self,
        conversation_id: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InconvoConversation:
        """
        Retrieve conversation

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
        return await self._get(
            f"/agents/{agent_id}/conversations/{conversation_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InconvoConversation,
        )

    def list(
        self,
        agent_id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        user_context: Dict[str, Union[str, float, bool]] | Omit = omit,
        user_identifier: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ConversationListResponse, AsyncConversationsCursor[ConversationListResponse]]:
        """
        List conversations

        Args:
          user_context: Arbitrary userContext filters, encoded as a deep object. Example: GET
              /conversations?userContext[userId]=42&userContext[orgId]=12

          user_identifier: Filter by user identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get_api_list(
            f"/agents/{agent_id}/conversations",
            page=AsyncConversationsCursor[ConversationListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "user_context": user_context,
                        "user_identifier": user_identifier,
                    },
                    conversation_list_params.ConversationListParams,
                ),
            ),
            model=ConversationListResponse,
        )


class ConversationsResourceWithRawResponse:
    def __init__(self, conversations: ConversationsResource) -> None:
        self._conversations = conversations

        self.create = to_raw_response_wrapper(
            conversations.create,
        )
        self.retrieve = to_raw_response_wrapper(
            conversations.retrieve,
        )
        self.list = to_raw_response_wrapper(
            conversations.list,
        )

    @cached_property
    def response(self) -> ResponseResourceWithRawResponse:
        return ResponseResourceWithRawResponse(self._conversations.response)


class AsyncConversationsResourceWithRawResponse:
    def __init__(self, conversations: AsyncConversationsResource) -> None:
        self._conversations = conversations

        self.create = async_to_raw_response_wrapper(
            conversations.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            conversations.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            conversations.list,
        )

    @cached_property
    def response(self) -> AsyncResponseResourceWithRawResponse:
        return AsyncResponseResourceWithRawResponse(self._conversations.response)


class ConversationsResourceWithStreamingResponse:
    def __init__(self, conversations: ConversationsResource) -> None:
        self._conversations = conversations

        self.create = to_streamed_response_wrapper(
            conversations.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            conversations.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            conversations.list,
        )

    @cached_property
    def response(self) -> ResponseResourceWithStreamingResponse:
        return ResponseResourceWithStreamingResponse(self._conversations.response)


class AsyncConversationsResourceWithStreamingResponse:
    def __init__(self, conversations: AsyncConversationsResource) -> None:
        self._conversations = conversations

        self.create = async_to_streamed_response_wrapper(
            conversations.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            conversations.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            conversations.list,
        )

    @cached_property
    def response(self) -> AsyncResponseResourceWithStreamingResponse:
        return AsyncResponseResourceWithStreamingResponse(self._conversations.response)
