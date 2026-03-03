# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .user import (
    UserResource,
    AsyncUserResource,
    UserResourceWithRawResponse,
    AsyncUserResourceWithRawResponse,
    UserResourceWithStreamingResponse,
    AsyncUserResourceWithStreamingResponse,
)
from .context import (
    ContextResource,
    AsyncContextResource,
    ContextResourceWithRawResponse,
    AsyncContextResourceWithRawResponse,
    ContextResourceWithStreamingResponse,
    AsyncContextResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["DatasetsResource", "AsyncDatasetsResource"]


class DatasetsResource(SyncAPIResource):
    @cached_property
    def user(self) -> UserResource:
        """Manage dataset files with scoped access.

        Datasets can be scoped in two ways:
        - **User-scoped** (`/datasets/user/{userIdentifier}`): Files accessible only to a specific user
        - **Context-scoped** (`/datasets/context/{contextKey}/{contextValue}`): Files shared with all users matching a context value

        File storage paths:
        - User-scoped: `/{orgId}/{agentId}/userIdentifier/{userIdentifier}/filename.csv`
        - Context-scoped: `/{orgId}/{agentId}/userContext/{contextKey}:{contextValue}/filename.csv`
        """
        return UserResource(self._client)

    @cached_property
    def context(self) -> ContextResource:
        """Manage dataset files with scoped access.

        Datasets can be scoped in two ways:
        - **User-scoped** (`/datasets/user/{userIdentifier}`): Files accessible only to a specific user
        - **Context-scoped** (`/datasets/context/{contextKey}/{contextValue}`): Files shared with all users matching a context value

        File storage paths:
        - User-scoped: `/{orgId}/{agentId}/userIdentifier/{userIdentifier}/filename.csv`
        - Context-scoped: `/{orgId}/{agentId}/userContext/{contextKey}:{contextValue}/filename.csv`
        """
        return ContextResource(self._client)

    @cached_property
    def with_raw_response(self) -> DatasetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/inconvoai/inconvo-python-sdk#accessing-raw-response-data-eg-headers
        """
        return DatasetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DatasetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/inconvoai/inconvo-python-sdk#with_streaming_response
        """
        return DatasetsResourceWithStreamingResponse(self)


class AsyncDatasetsResource(AsyncAPIResource):
    @cached_property
    def user(self) -> AsyncUserResource:
        """Manage dataset files with scoped access.

        Datasets can be scoped in two ways:
        - **User-scoped** (`/datasets/user/{userIdentifier}`): Files accessible only to a specific user
        - **Context-scoped** (`/datasets/context/{contextKey}/{contextValue}`): Files shared with all users matching a context value

        File storage paths:
        - User-scoped: `/{orgId}/{agentId}/userIdentifier/{userIdentifier}/filename.csv`
        - Context-scoped: `/{orgId}/{agentId}/userContext/{contextKey}:{contextValue}/filename.csv`
        """
        return AsyncUserResource(self._client)

    @cached_property
    def context(self) -> AsyncContextResource:
        """Manage dataset files with scoped access.

        Datasets can be scoped in two ways:
        - **User-scoped** (`/datasets/user/{userIdentifier}`): Files accessible only to a specific user
        - **Context-scoped** (`/datasets/context/{contextKey}/{contextValue}`): Files shared with all users matching a context value

        File storage paths:
        - User-scoped: `/{orgId}/{agentId}/userIdentifier/{userIdentifier}/filename.csv`
        - Context-scoped: `/{orgId}/{agentId}/userContext/{contextKey}:{contextValue}/filename.csv`
        """
        return AsyncContextResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDatasetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/inconvoai/inconvo-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncDatasetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDatasetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/inconvoai/inconvo-python-sdk#with_streaming_response
        """
        return AsyncDatasetsResourceWithStreamingResponse(self)


class DatasetsResourceWithRawResponse:
    def __init__(self, datasets: DatasetsResource) -> None:
        self._datasets = datasets

    @cached_property
    def user(self) -> UserResourceWithRawResponse:
        """Manage dataset files with scoped access.

        Datasets can be scoped in two ways:
        - **User-scoped** (`/datasets/user/{userIdentifier}`): Files accessible only to a specific user
        - **Context-scoped** (`/datasets/context/{contextKey}/{contextValue}`): Files shared with all users matching a context value

        File storage paths:
        - User-scoped: `/{orgId}/{agentId}/userIdentifier/{userIdentifier}/filename.csv`
        - Context-scoped: `/{orgId}/{agentId}/userContext/{contextKey}:{contextValue}/filename.csv`
        """
        return UserResourceWithRawResponse(self._datasets.user)

    @cached_property
    def context(self) -> ContextResourceWithRawResponse:
        """Manage dataset files with scoped access.

        Datasets can be scoped in two ways:
        - **User-scoped** (`/datasets/user/{userIdentifier}`): Files accessible only to a specific user
        - **Context-scoped** (`/datasets/context/{contextKey}/{contextValue}`): Files shared with all users matching a context value

        File storage paths:
        - User-scoped: `/{orgId}/{agentId}/userIdentifier/{userIdentifier}/filename.csv`
        - Context-scoped: `/{orgId}/{agentId}/userContext/{contextKey}:{contextValue}/filename.csv`
        """
        return ContextResourceWithRawResponse(self._datasets.context)


class AsyncDatasetsResourceWithRawResponse:
    def __init__(self, datasets: AsyncDatasetsResource) -> None:
        self._datasets = datasets

    @cached_property
    def user(self) -> AsyncUserResourceWithRawResponse:
        """Manage dataset files with scoped access.

        Datasets can be scoped in two ways:
        - **User-scoped** (`/datasets/user/{userIdentifier}`): Files accessible only to a specific user
        - **Context-scoped** (`/datasets/context/{contextKey}/{contextValue}`): Files shared with all users matching a context value

        File storage paths:
        - User-scoped: `/{orgId}/{agentId}/userIdentifier/{userIdentifier}/filename.csv`
        - Context-scoped: `/{orgId}/{agentId}/userContext/{contextKey}:{contextValue}/filename.csv`
        """
        return AsyncUserResourceWithRawResponse(self._datasets.user)

    @cached_property
    def context(self) -> AsyncContextResourceWithRawResponse:
        """Manage dataset files with scoped access.

        Datasets can be scoped in two ways:
        - **User-scoped** (`/datasets/user/{userIdentifier}`): Files accessible only to a specific user
        - **Context-scoped** (`/datasets/context/{contextKey}/{contextValue}`): Files shared with all users matching a context value

        File storage paths:
        - User-scoped: `/{orgId}/{agentId}/userIdentifier/{userIdentifier}/filename.csv`
        - Context-scoped: `/{orgId}/{agentId}/userContext/{contextKey}:{contextValue}/filename.csv`
        """
        return AsyncContextResourceWithRawResponse(self._datasets.context)


class DatasetsResourceWithStreamingResponse:
    def __init__(self, datasets: DatasetsResource) -> None:
        self._datasets = datasets

    @cached_property
    def user(self) -> UserResourceWithStreamingResponse:
        """Manage dataset files with scoped access.

        Datasets can be scoped in two ways:
        - **User-scoped** (`/datasets/user/{userIdentifier}`): Files accessible only to a specific user
        - **Context-scoped** (`/datasets/context/{contextKey}/{contextValue}`): Files shared with all users matching a context value

        File storage paths:
        - User-scoped: `/{orgId}/{agentId}/userIdentifier/{userIdentifier}/filename.csv`
        - Context-scoped: `/{orgId}/{agentId}/userContext/{contextKey}:{contextValue}/filename.csv`
        """
        return UserResourceWithStreamingResponse(self._datasets.user)

    @cached_property
    def context(self) -> ContextResourceWithStreamingResponse:
        """Manage dataset files with scoped access.

        Datasets can be scoped in two ways:
        - **User-scoped** (`/datasets/user/{userIdentifier}`): Files accessible only to a specific user
        - **Context-scoped** (`/datasets/context/{contextKey}/{contextValue}`): Files shared with all users matching a context value

        File storage paths:
        - User-scoped: `/{orgId}/{agentId}/userIdentifier/{userIdentifier}/filename.csv`
        - Context-scoped: `/{orgId}/{agentId}/userContext/{contextKey}:{contextValue}/filename.csv`
        """
        return ContextResourceWithStreamingResponse(self._datasets.context)


class AsyncDatasetsResourceWithStreamingResponse:
    def __init__(self, datasets: AsyncDatasetsResource) -> None:
        self._datasets = datasets

    @cached_property
    def user(self) -> AsyncUserResourceWithStreamingResponse:
        """Manage dataset files with scoped access.

        Datasets can be scoped in two ways:
        - **User-scoped** (`/datasets/user/{userIdentifier}`): Files accessible only to a specific user
        - **Context-scoped** (`/datasets/context/{contextKey}/{contextValue}`): Files shared with all users matching a context value

        File storage paths:
        - User-scoped: `/{orgId}/{agentId}/userIdentifier/{userIdentifier}/filename.csv`
        - Context-scoped: `/{orgId}/{agentId}/userContext/{contextKey}:{contextValue}/filename.csv`
        """
        return AsyncUserResourceWithStreamingResponse(self._datasets.user)

    @cached_property
    def context(self) -> AsyncContextResourceWithStreamingResponse:
        """Manage dataset files with scoped access.

        Datasets can be scoped in two ways:
        - **User-scoped** (`/datasets/user/{userIdentifier}`): Files accessible only to a specific user
        - **Context-scoped** (`/datasets/context/{contextKey}/{contextValue}`): Files shared with all users matching a context value

        File storage paths:
        - User-scoped: `/{orgId}/{agentId}/userIdentifier/{userIdentifier}/filename.csv`
        - Context-scoped: `/{orgId}/{agentId}/userContext/{contextKey}:{contextValue}/filename.csv`
        """
        return AsyncContextResourceWithStreamingResponse(self._datasets.context)
