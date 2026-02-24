# Agents

## DataSummary

Types:

```python
from inconvo.types.agents import DataSummaryRetrieveResponse
```

Methods:

- <code title="get /agents/{agentId}/data-summary">client.agents.data_summary.<a href="./src/inconvo/resources/agents/data_summary.py">retrieve</a>(agent_id) -> <a href="./src/inconvo/types/agents/data_summary_retrieve_response.py">DataSummaryRetrieveResponse</a></code>

## Conversations

Types:

```python
from inconvo.types.agents import (
    InconvoConversation,
    ConversationCreateResponse,
    ConversationListResponse,
)
```

Methods:

- <code title="post /agents/{agentId}/conversations">client.agents.conversations.<a href="./src/inconvo/resources/agents/conversations/conversations.py">create</a>(agent_id, \*\*<a href="src/inconvo/types/agents/conversation_create_params.py">params</a>) -> <a href="./src/inconvo/types/agents/conversation_create_response.py">ConversationCreateResponse</a></code>
- <code title="get /agents/{agentId}/conversations/{conversation_id}">client.agents.conversations.<a href="./src/inconvo/resources/agents/conversations/conversations.py">retrieve</a>(conversation_id, \*, agent_id) -> <a href="./src/inconvo/types/agents/inconvo_conversation.py">InconvoConversation</a></code>
- <code title="get /agents/{agentId}/conversations">client.agents.conversations.<a href="./src/inconvo/resources/agents/conversations/conversations.py">list</a>(agent_id, \*\*<a href="src/inconvo/types/agents/conversation_list_params.py">params</a>) -> <a href="./src/inconvo/types/agents/conversation_list_response.py">SyncConversationsCursor[ConversationListResponse]</a></code>

### Response

Types:

```python
from inconvo.types.agents.conversations import (
    Chart,
    Table,
    ResponseCreateResponse,
    ResponseRetrieveResponse,
)
```

Methods:

- <code title="post /agents/{agentId}/conversations/{conversation_id}/response">client.agents.conversations.response.<a href="./src/inconvo/resources/agents/conversations/response/response.py">create</a>(conversation_id, \*, agent_id, \*\*<a href="src/inconvo/types/agents/conversations/response_create_params.py">params</a>) -> <a href="./src/inconvo/types/agents/conversations/response_create_response.py">ResponseCreateResponse</a></code>
- <code title="get /agents/{agentId}/conversations/{conversation_id}/response/{response_id}">client.agents.conversations.response.<a href="./src/inconvo/resources/agents/conversations/response/response.py">retrieve</a>(response_id, \*, agent_id, conversation_id) -> <a href="./src/inconvo/types/agents/conversations/response_retrieve_response.py">ResponseRetrieveResponse</a></code>

#### Feedback

Types:

```python
from inconvo.types.agents.conversations.response import Feedback
```

Methods:

- <code title="post /agents/{agentId}/conversations/{conversation_id}/response/{response_id}/feedback">client.agents.conversations.response.feedback.<a href="./src/inconvo/resources/agents/conversations/response/feedback.py">create</a>(response_id, \*, agent_id, conversation_id, \*\*<a href="src/inconvo/types/agents/conversations/response/feedback_create_params.py">params</a>) -> <a href="./src/inconvo/types/agents/conversations/response/feedback.py">Feedback</a></code>
- <code title="patch /agents/{agentId}/conversations/{conversation_id}/response/{response_id}/feedback/{feedback_id}">client.agents.conversations.response.feedback.<a href="./src/inconvo/resources/agents/conversations/response/feedback.py">update</a>(feedback_id, \*, agent_id, conversation_id, response_id, \*\*<a href="src/inconvo/types/agents/conversations/response/feedback_update_params.py">params</a>) -> <a href="./src/inconvo/types/agents/conversations/response/feedback.py">Feedback</a></code>

## Datasets

### User

Types:

```python
from inconvo.types.agents.datasets import UserListResponse, UserDeleteResponse, UserUploadResponse
```

Methods:

- <code title="get /agents/{agentId}/datasets/user/{userIdentifier}">client.agents.datasets.user.<a href="./src/inconvo/resources/agents/datasets/user.py">list</a>(user_identifier, \*, agent_id) -> <a href="./src/inconvo/types/agents/datasets/user_list_response.py">UserListResponse</a></code>
- <code title="delete /agents/{agentId}/datasets/user/{userIdentifier}/{filename}">client.agents.datasets.user.<a href="./src/inconvo/resources/agents/datasets/user.py">delete</a>(filename, \*, agent_id, user_identifier) -> <a href="./src/inconvo/types/agents/datasets/user_delete_response.py">UserDeleteResponse</a></code>
- <code title="post /agents/{agentId}/datasets/user/{userIdentifier}">client.agents.datasets.user.<a href="./src/inconvo/resources/agents/datasets/user.py">upload</a>(user_identifier, \*, agent_id, \*\*<a href="src/inconvo/types/agents/datasets/user_upload_params.py">params</a>) -> <a href="./src/inconvo/types/agents/datasets/user_upload_response.py">UserUploadResponse</a></code>

### Context

Types:

```python
from inconvo.types.agents.datasets import (
    ContextListResponse,
    ContextDeleteResponse,
    ContextUploadResponse,
)
```

Methods:

- <code title="get /agents/{agentId}/datasets/context/{contextKey}/{contextValue}">client.agents.datasets.context.<a href="./src/inconvo/resources/agents/datasets/context.py">list</a>(context_value, \*, agent_id, context_key) -> <a href="./src/inconvo/types/agents/datasets/context_list_response.py">ContextListResponse</a></code>
- <code title="delete /agents/{agentId}/datasets/context/{contextKey}/{contextValue}/{filename}">client.agents.datasets.context.<a href="./src/inconvo/resources/agents/datasets/context.py">delete</a>(filename, \*, agent_id, context_key, context_value) -> <a href="./src/inconvo/types/agents/datasets/context_delete_response.py">ContextDeleteResponse</a></code>
- <code title="post /agents/{agentId}/datasets/context/{contextKey}/{contextValue}">client.agents.datasets.context.<a href="./src/inconvo/resources/agents/datasets/context.py">upload</a>(context_value, \*, agent_id, context_key, \*\*<a href="src/inconvo/types/agents/datasets/context_upload_params.py">params</a>) -> <a href="./src/inconvo/types/agents/datasets/context_upload_response.py">ContextUploadResponse</a></code>

## McpServers

### Tenants

Types:

```python
from inconvo.types.agents.mcp_servers import TenantCreateResponse, TenantDeleteResponse
```

Methods:

- <code title="post /agents/{agentId}/mcpservers/{mcpserver_id}/tenants">client.agents.mcp_servers.tenants.<a href="./src/inconvo/resources/agents/mcp_servers/tenants.py">create</a>(mcpserver_id, \*, agent_id, \*\*<a href="src/inconvo/types/agents/mcp_servers/tenant_create_params.py">params</a>) -> <a href="./src/inconvo/types/agents/mcp_servers/tenant_create_response.py">TenantCreateResponse</a></code>
- <code title="delete /agents/{agentId}/mcpservers/{mcpserver_id}/tenants/{tenant_key}">client.agents.mcp_servers.tenants.<a href="./src/inconvo/resources/agents/mcp_servers/tenants.py">delete</a>(mcpserver_id, \*, agent_id, tenant_key) -> <a href="./src/inconvo/types/agents/mcp_servers/tenant_delete_response.py">TenantDeleteResponse</a></code>
