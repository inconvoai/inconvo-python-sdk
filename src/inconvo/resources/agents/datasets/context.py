# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, FileTypes, omit, not_given
from ...._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.agents.datasets import context_upload_params
from ....types.agents.datasets.context_list_response import ContextListResponse
from ....types.agents.datasets.context_delete_response import ContextDeleteResponse
from ....types.agents.datasets.context_upload_response import ContextUploadResponse

__all__ = ["ContextResource", "AsyncContextResource"]


class ContextResource(SyncAPIResource):
    """Manage dataset files with scoped access.

    Datasets can be scoped in two ways:
    - **User-scoped** (`/datasets/user/{userIdentifier}`): Files accessible only to a specific user
    - **Context-scoped** (`/datasets/context/{contextKey}/{contextValue}`): Files shared with all users matching a context value

    File storage paths:
    - User-scoped: `/{orgId}/{agentId}/userIdentifier/{userIdentifier}/filename.csv`
    - Context-scoped: `/{orgId}/{agentId}/userContext/{contextKey}:{contextValue}/filename.csv`
    """

    @cached_property
    def with_raw_response(self) -> ContextResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/inconvoai/inconvo-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ContextResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContextResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/inconvoai/inconvo-python-sdk#with_streaming_response
        """
        return ContextResourceWithStreamingResponse(self)

    def list(
        self,
        context_value: str,
        *,
        agent_id: str,
        context_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContextListResponse:
        """List all dataset files scoped to a context value.

        These files are shared with
        all users who have this context value. Requires User Context to be enabled.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not context_key:
            raise ValueError(f"Expected a non-empty value for `context_key` but received {context_key!r}")
        if not context_value:
            raise ValueError(f"Expected a non-empty value for `context_value` but received {context_value!r}")
        return self._get(
            f"/agents/{agent_id}/datasets/context/{context_key}/{context_value}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContextListResponse,
        )

    def delete(
        self,
        filename: str,
        *,
        agent_id: str,
        context_key: str,
        context_value: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContextDeleteResponse:
        """Delete a dataset file scoped to a context value.

        Requires User Context to be
        enabled.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not context_key:
            raise ValueError(f"Expected a non-empty value for `context_key` but received {context_key!r}")
        if not context_value:
            raise ValueError(f"Expected a non-empty value for `context_value` but received {context_value!r}")
        if not filename:
            raise ValueError(f"Expected a non-empty value for `filename` but received {filename!r}")
        return self._delete(
            f"/agents/{agent_id}/datasets/context/{context_key}/{context_value}/{filename}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContextDeleteResponse,
        )

    def upload(
        self,
        context_value: str,
        *,
        agent_id: str,
        context_key: str,
        file: FileTypes,
        notes: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContextUploadResponse:
        """Upload a dataset file scoped to a context value.

        This file will be shared with
        all users who have this context value. Requires User Context to be enabled and
        contextKey to be defined in the schema.

        Args:
          file: The file to upload (CSV or JSON, max 10MB)

          notes: Optional notes or description for the dataset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not context_key:
            raise ValueError(f"Expected a non-empty value for `context_key` but received {context_key!r}")
        if not context_value:
            raise ValueError(f"Expected a non-empty value for `context_value` but received {context_value!r}")
        body = deepcopy_minimal(
            {
                "file": file,
                "notes": notes,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            f"/agents/{agent_id}/datasets/context/{context_key}/{context_value}",
            body=maybe_transform(body, context_upload_params.ContextUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContextUploadResponse,
        )


class AsyncContextResource(AsyncAPIResource):
    """Manage dataset files with scoped access.

    Datasets can be scoped in two ways:
    - **User-scoped** (`/datasets/user/{userIdentifier}`): Files accessible only to a specific user
    - **Context-scoped** (`/datasets/context/{contextKey}/{contextValue}`): Files shared with all users matching a context value

    File storage paths:
    - User-scoped: `/{orgId}/{agentId}/userIdentifier/{userIdentifier}/filename.csv`
    - Context-scoped: `/{orgId}/{agentId}/userContext/{contextKey}:{contextValue}/filename.csv`
    """

    @cached_property
    def with_raw_response(self) -> AsyncContextResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/inconvoai/inconvo-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncContextResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContextResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/inconvoai/inconvo-python-sdk#with_streaming_response
        """
        return AsyncContextResourceWithStreamingResponse(self)

    async def list(
        self,
        context_value: str,
        *,
        agent_id: str,
        context_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContextListResponse:
        """List all dataset files scoped to a context value.

        These files are shared with
        all users who have this context value. Requires User Context to be enabled.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not context_key:
            raise ValueError(f"Expected a non-empty value for `context_key` but received {context_key!r}")
        if not context_value:
            raise ValueError(f"Expected a non-empty value for `context_value` but received {context_value!r}")
        return await self._get(
            f"/agents/{agent_id}/datasets/context/{context_key}/{context_value}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContextListResponse,
        )

    async def delete(
        self,
        filename: str,
        *,
        agent_id: str,
        context_key: str,
        context_value: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContextDeleteResponse:
        """Delete a dataset file scoped to a context value.

        Requires User Context to be
        enabled.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not context_key:
            raise ValueError(f"Expected a non-empty value for `context_key` but received {context_key!r}")
        if not context_value:
            raise ValueError(f"Expected a non-empty value for `context_value` but received {context_value!r}")
        if not filename:
            raise ValueError(f"Expected a non-empty value for `filename` but received {filename!r}")
        return await self._delete(
            f"/agents/{agent_id}/datasets/context/{context_key}/{context_value}/{filename}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContextDeleteResponse,
        )

    async def upload(
        self,
        context_value: str,
        *,
        agent_id: str,
        context_key: str,
        file: FileTypes,
        notes: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContextUploadResponse:
        """Upload a dataset file scoped to a context value.

        This file will be shared with
        all users who have this context value. Requires User Context to be enabled and
        contextKey to be defined in the schema.

        Args:
          file: The file to upload (CSV or JSON, max 10MB)

          notes: Optional notes or description for the dataset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not context_key:
            raise ValueError(f"Expected a non-empty value for `context_key` but received {context_key!r}")
        if not context_value:
            raise ValueError(f"Expected a non-empty value for `context_value` but received {context_value!r}")
        body = deepcopy_minimal(
            {
                "file": file,
                "notes": notes,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            f"/agents/{agent_id}/datasets/context/{context_key}/{context_value}",
            body=await async_maybe_transform(body, context_upload_params.ContextUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContextUploadResponse,
        )


class ContextResourceWithRawResponse:
    def __init__(self, context: ContextResource) -> None:
        self._context = context

        self.list = to_raw_response_wrapper(
            context.list,
        )
        self.delete = to_raw_response_wrapper(
            context.delete,
        )
        self.upload = to_raw_response_wrapper(
            context.upload,
        )


class AsyncContextResourceWithRawResponse:
    def __init__(self, context: AsyncContextResource) -> None:
        self._context = context

        self.list = async_to_raw_response_wrapper(
            context.list,
        )
        self.delete = async_to_raw_response_wrapper(
            context.delete,
        )
        self.upload = async_to_raw_response_wrapper(
            context.upload,
        )


class ContextResourceWithStreamingResponse:
    def __init__(self, context: ContextResource) -> None:
        self._context = context

        self.list = to_streamed_response_wrapper(
            context.list,
        )
        self.delete = to_streamed_response_wrapper(
            context.delete,
        )
        self.upload = to_streamed_response_wrapper(
            context.upload,
        )


class AsyncContextResourceWithStreamingResponse:
    def __init__(self, context: AsyncContextResource) -> None:
        self._context = context

        self.list = async_to_streamed_response_wrapper(
            context.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            context.delete,
        )
        self.upload = async_to_streamed_response_wrapper(
            context.upload,
        )
