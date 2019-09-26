# fcsm_eos_api_client.WebhookApi

All URIs are relative to *https://emeia-eos.fcsm.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_webhook**](WebhookApi.md#create_webhook) | **POST** /api/v1/webhook/webhooks | Create a new webhook
[**delete_webhook**](WebhookApi.md#delete_webhook) | **DELETE** /api/v1/webhook/webhooks/{webhook_id} | Delete specified webhook
[**disable_webhook**](WebhookApi.md#disable_webhook) | **DELETE** /api/v1/webhook/webhooks/{webhook_id}/disable | Disable specified webhook
[**enable_webhook**](WebhookApi.md#enable_webhook) | **PUT** /api/v1/webhook/webhooks/{webhook_id}/enable | Enable specified webhook
[**get_content_types**](WebhookApi.md#get_content_types) | **GET** /api/v1/webhook/contentTypes | Get available content types for webhooks
[**get_event_types**](WebhookApi.md#get_event_types) | **GET** /api/v1/webhook/eventTypes | Get available event types for webhooks
[**get_single_webhook**](WebhookApi.md#get_single_webhook) | **GET** /api/v1/webhook/webhooks/{webhook_id} | Get single webhook
[**get_webhooks**](WebhookApi.md#get_webhooks) | **GET** /api/v1/webhook/webhooks | Get list of defined webhooks
[**update_webhook**](WebhookApi.md#update_webhook) | **PUT** /api/v1/webhook/webhooks/{webhook_id} | Update specified webhook


# **create_webhook**
> create_webhook(webhook_webhook, email=email)

Create a new webhook

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.WebhookApi()
webhook_webhook = fcsm_eos_api_client.WebhookWebhook() # WebhookWebhook | The details of the new webhook
email = 'email_example' # str |  (optional)

try:
    # Create a new webhook
    api_instance.create_webhook(webhook_webhook, email=email)
except ApiException as e:
    print("Exception when calling WebhookApi->create_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_webhook** | [**WebhookWebhook**](WebhookWebhook.md)| The details of the new webhook | 
 **email** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Properly created a new webhook |  -  |
**400** | Invalid JSON payload |  -  |
**403** | Insufficient access rights |  -  |
**500** | An unexpected error occured |  -  |
**503** | Database is unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_webhook**
> delete_webhook(webhook_id, email=email)

Delete specified webhook

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.WebhookApi()
webhook_id = 'webhook_id_example' # str | 
email = 'email_example' # str |  (optional)

try:
    # Delete specified webhook
    api_instance.delete_webhook(webhook_id, email=email)
except ApiException as e:
    print("Exception when calling WebhookApi->delete_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**|  | 
 **email** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Webhook was deleted properly |  -  |
**400** | Invalid role |  -  |
**403** | Insufficient access rights |  -  |
**404** | Unknown webhook id |  -  |
**500** | An unexpected error occured |  -  |
**503** | Database is unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_webhook**
> disable_webhook(webhook_id, email=email)

Disable specified webhook

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.WebhookApi()
webhook_id = 'webhook_id_example' # str | 
email = 'email_example' # str |  (optional)

try:
    # Disable specified webhook
    api_instance.disable_webhook(webhook_id, email=email)
except ApiException as e:
    print("Exception when calling WebhookApi->disable_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**|  | 
 **email** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Webhook was disabled properly |  -  |
**400** | Invalid role |  -  |
**403** | Insufficient access rights |  -  |
**404** | Unknown webhook id |  -  |
**409** | Changing status error |  -  |
**500** | An unexpected error occured |  -  |
**503** | Database is unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_webhook**
> enable_webhook(webhook_id, email=email)

Enable specified webhook

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.WebhookApi()
webhook_id = 'webhook_id_example' # str | 
email = 'email_example' # str |  (optional)

try:
    # Enable specified webhook
    api_instance.enable_webhook(webhook_id, email=email)
except ApiException as e:
    print("Exception when calling WebhookApi->enable_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**|  | 
 **email** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Webhook was enabled properly |  -  |
**400** | Invalid role |  -  |
**403** | Insufficient access rights |  -  |
**404** | Unknown webhook id |  -  |
**409** | Changing status error |  -  |
**500** | An unexpected error occured |  -  |
**503** | Database is unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_content_types**
> list[str] get_content_types()

Get available content types for webhooks

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.WebhookApi()

try:
    # Get available content types for webhooks
    api_response = api_instance.get_content_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookApi->get_content_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of Content Types |  -  |
**500** | An unexpected error occured |  -  |
**503** | Database is unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_types**
> list[WebhookEventType] get_event_types()

Get available event types for webhooks

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.WebhookApi()

try:
    # Get available event types for webhooks
    api_response = api_instance.get_event_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookApi->get_event_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[WebhookEventType]**](WebhookEventType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of Event Types objects |  -  |
**500** | An unexpected error occured |  -  |
**503** | Database is unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_single_webhook**
> WebhookWebhook get_single_webhook(webhook_id)

Get single webhook

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.WebhookApi()
webhook_id = 'webhook_id_example' # str | 

try:
    # Get single webhook
    api_response = api_instance.get_single_webhook(webhook_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookApi->get_single_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**|  | 

### Return type

[**WebhookWebhook**](WebhookWebhook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Webhook for give id |  -  |
**404** | Unknown webhook id |  -  |
**500** | An unexpected error occured |  -  |
**503** | Database is unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhooks**
> list[WebhookWebhook] get_webhooks()

Get list of defined webhooks

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.WebhookApi()

try:
    # Get list of defined webhooks
    api_response = api_instance.get_webhooks()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookApi->get_webhooks: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[WebhookWebhook]**](WebhookWebhook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of Webhooks |  -  |
**500** | An unexpected error occured |  -  |
**503** | Database is unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_webhook**
> update_webhook(webhook_id, webhook_webhook, email=email)

Update specified webhook

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.WebhookApi()
webhook_id = 'webhook_id_example' # str | 
webhook_webhook = fcsm_eos_api_client.WebhookWebhook() # WebhookWebhook | The details of the webhook
email = 'email_example' # str |  (optional)

try:
    # Update specified webhook
    api_instance.update_webhook(webhook_id, webhook_webhook, email=email)
except ApiException as e:
    print("Exception when calling WebhookApi->update_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**|  | 
 **webhook_webhook** | [**WebhookWebhook**](WebhookWebhook.md)| The details of the webhook | 
 **email** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Webhook was updated properly |  -  |
**400** | Invalid JSON payload |  -  |
**403** | Insufficient access rights |  -  |
**404** | Unknown webhook id |  -  |
**500** | An unexpected error occured |  -  |
**503** | Database is unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

