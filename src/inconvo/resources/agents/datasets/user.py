# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast

import httpx

from ...._files import deepcopy_with_paths
from ...._types import Body, Omit, Query, Headers, NotGiven, FileTypes, omit, not_given
from ...._utils import extract_files, path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.agents.datasets import user_upload_params
from ....types.agents.datasets.user_list_response import UserListResponse
from ....types.agents.datasets.user_delete_response import UserDeleteResponse
from ....types.agents.datasets.user_upload_response import UserUploadResponse

__all__ = ["UserResource", "AsyncUserResource"]


class UserResource(SyncAPIResource):
    """Manage dataset files with scoped access.

    Datasets can be scoped in two ways:
    - **User-scoped** (`/datasets/user/{userIdentifier}`): Files accessible only to a specific user
    - **Context-scoped** (`/datasets/context/{contextKey}/{contextValue}`): Files shared with all users matching a context value

    File storage paths:
    - User-scoped: `/{orgId}/{agentId}/userIdentifier/{userIdentifier}/filename.csv`
    - Context-scoped: `/{orgId}/{agentId}/userContext/{contextKey}:{contextValue}/filename.csv`
    """

    @cached_property
    def with_raw_response(self) -> UserResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/inconvoai/inconvo-python-sdk#accessing-raw-response-data-eg-headers
        """
        return UserResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UserResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/inconvoai/inconvo-python-sdk#with_streaming_response
        """
        return UserResourceWithStreamingResponse(self)

    def list(
        self,
        user_identifier: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserListResponse:
        """
        List all dataset files scoped to a specific user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not user_identifier:
            raise ValueError(f"Expected a non-empty value for `user_identifier` but received {user_identifier!r}")
        return self._get(
            path_template(
                "/agents/{agent_id}/datasets/user/{user_identifier}", agent_id=agent_id, user_identifier=user_identifier
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserListResponse,
        )

    def delete(
        self,
        filename: str,
        *,
        agent_id: str,
        user_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserDeleteResponse:
        """
        Delete a dataset file scoped to a specific user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not user_identifier:
            raise ValueError(f"Expected a non-empty value for `user_identifier` but received {user_identifier!r}")
        if not filename:
            raise ValueError(f"Expected a non-empty value for `filename` but received {filename!r}")
        return self._delete(
            path_template(
                "/agents/{agent_id}/datasets/user/{user_identifier}/{filename}",
                agent_id=agent_id,
                user_identifier=user_identifier,
                filename=filename,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserDeleteResponse,
        )

    def upload(
        self,
        user_identifier: str,
        *,
        agent_id: str,
        file: FileTypes,
        notes: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserUploadResponse:
        """
        Upload a dataset file scoped to a specific user.

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
        if not user_identifier:
            raise ValueError(f"Expected a non-empty value for `user_identifier` but received {user_identifier!r}")
        body = deepcopy_with_paths(
            {
                "file": file,
                "notes": notes,
            },
            [["file"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            path_template(
                "/agents/{agent_id}/datasets/user/{user_identifier}", agent_id=agent_id, user_identifier=user_identifier
            ),
            body=maybe_transform(body, user_upload_params.UserUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserUploadResponse,
        )


class AsyncUserResource(AsyncAPIResource):
    """Manage dataset files with scoped access.

    Datasets can be scoped in two ways:
    - **User-scoped** (`/datasets/user/{userIdentifier}`): Files accessible only to a specific user
    - **Context-scoped** (`/datasets/context/{contextKey}/{contextValue}`): Files shared with all users matching a context value

    File storage paths:
    - User-scoped: `/{orgId}/{agentId}/userIdentifier/{userIdentifier}/filename.csv`
    - Context-scoped: `/{orgId}/{agentId}/userContext/{contextKey}:{contextValue}/filename.csv`
    """

    @cached_property
    def with_raw_response(self) -> AsyncUserResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/inconvoai/inconvo-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncUserResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUserResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/inconvoai/inconvo-python-sdk#with_streaming_response
        """
        return AsyncUserResourceWithStreamingResponse(self)

    async def list(
        self,
        user_identifier: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserListResponse:
        """
        List all dataset files scoped to a specific user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not user_identifier:
            raise ValueError(f"Expected a non-empty value for `user_identifier` but received {user_identifier!r}")
        return await self._get(
            path_template(
                "/agents/{agent_id}/datasets/user/{user_identifier}", agent_id=agent_id, user_identifier=user_identifier
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserListResponse,
        )

    async def delete(
        self,
        filename: str,
        *,
        agent_id: str,
        user_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserDeleteResponse:
        """
        Delete a dataset file scoped to a specific user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not user_identifier:
            raise ValueError(f"Expected a non-empty value for `user_identifier` but received {user_identifier!r}")
        if not filename:
            raise ValueError(f"Expected a non-empty value for `filename` but received {filename!r}")
        return await self._delete(
            path_template(
                "/agents/{agent_id}/datasets/user/{user_identifier}/{filename}",
                agent_id=agent_id,
                user_identifier=user_identifier,
                filename=filename,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserDeleteResponse,
        )

    async def upload(
        self,
        user_identifier: str,
        *,
        agent_id: str,
        file: FileTypes,
        notes: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserUploadResponse:
        """
        Upload a dataset file scoped to a specific user.

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
        if not user_identifier:
            raise ValueError(f"Expected a non-empty value for `user_identifier` but received {user_identifier!r}")
        body = deepcopy_with_paths(
            {
                "file": file,
                "notes": notes,
            },
            [["file"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            path_template(
                "/agents/{agent_id}/datasets/user/{user_identifier}", agent_id=agent_id, user_identifier=user_identifier
            ),
            body=await async_maybe_transform(body, user_upload_params.UserUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserUploadResponse,
        )


class UserResourceWithRawResponse:
    def __init__(self, user: UserResource) -> None:
        self._user = user

        self.list = to_raw_response_wrapper(
            user.list,
        )
        self.delete = to_raw_response_wrapper(
            user.delete,
        )
        self.upload = to_raw_response_wrapper(
            user.upload,
        )


class AsyncUserResourceWithRawResponse:
    def __init__(self, user: AsyncUserResource) -> None:
        self._user = user

        self.list = async_to_raw_response_wrapper(
            user.list,
        )
        self.delete = async_to_raw_response_wrapper(
            user.delete,
        )
        self.upload = async_to_raw_response_wrapper(
            user.upload,
        )


class UserResourceWithStreamingResponse:
    def __init__(self, user: UserResource) -> None:
        self._user = user

        self.list = to_streamed_response_wrapper(
            user.list,
        )
        self.delete = to_streamed_response_wrapper(
            user.delete,
        )
        self.upload = to_streamed_response_wrapper(
            user.upload,
        )


class AsyncUserResourceWithStreamingResponse:
    def __init__(self, user: AsyncUserResource) -> None:
        self._user = user

        self.list = async_to_streamed_response_wrapper(
            user.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            user.delete,
        )
        self.upload = async_to_streamed_response_wrapper(
            user.upload,
        )
