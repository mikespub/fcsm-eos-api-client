# fcsm_eos_api_client.TagApi

All URIs are relative to *https://emeia-eos.fcsm.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tag**](TagApi.md#create_tag) | **POST** /api/v1/tag/tags | 
[**delete_tag**](TagApi.md#delete_tag) | **DELETE** /api/v1/tag/tags/{tagName} | 
[**get_tag**](TagApi.md#get_tag) | **GET** /api/v1/tag/tags/{tagName} | Returns the specified tag
[**get_tags**](TagApi.md#get_tags) | **GET** /api/v1/tag/tags | 
[**update_tag**](TagApi.md#update_tag) | **PUT** /api/v1/tag/tags/{tagName} | 


# **create_tag**
> TagTag create_tag(tag_tag, email=email)



Creates tag with given name and values

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.TagApi()
tag_tag = fcsm_eos_api_client.TagTag() # TagTag | The details of tag that will be created
email = 'email_example' # str |  (optional)

try:
    api_response = api_instance.create_tag(tag_tag, email=email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->create_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_tag** | [**TagTag**](TagTag.md)| The details of tag that will be created | 
 **email** | **str**|  | [optional] 

### Return type

[**TagTag**](TagTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The newly created tag |  -  |
**400** | Invalid json payload |  -  |
**403** | Insufficient access rights |  -  |
**500** | An unexpected error occurred |  -  |
**503** | Database is unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tag**
> delete_tag(tag_name, email=email)



Delete tag with given name

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.TagApi()
tag_name = 'tag_name_example' # str | 
email = 'email_example' # str |  (optional)

try:
    api_instance.delete_tag(tag_name, email=email)
except ApiException as e:
    print("Exception when calling TagApi->delete_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_name** | **str**|  | 
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
**200** | Successfully deleted tag |  -  |
**400** | Invalid role |  -  |
**403** | Insufficient access rights |  -  |
**404** | Unknown tagId |  -  |
**500** | An unexpected error occurred |  -  |
**503** | Database is unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tag**
> TagTag get_tag(tag_name)

Returns the specified tag

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.TagApi()
tag_name = 'tag_name_example' # str | 

try:
    # Returns the specified tag
    api_response = api_instance.get_tag(tag_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->get_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_name** | **str**|  | 

### Return type

[**TagTag**](TagTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The tag data for given name |  -  |
**404** | Unknown tagName |  -  |
**500** | An unexpected error occurred |  -  |
**503** | Database is unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tags**
> list[TagTag] get_tags()



Returns a list of all tags with values

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.TagApi()

try:
    api_response = api_instance.get_tags()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->get_tags: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[TagTag]**](TagTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of Tag objects |  -  |
**500** | An unexpected error occurred |  -  |
**503** | Database is unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tag**
> update_tag(tag_name, tag_tag_update, email=email)



Update some fields of a tag

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.TagApi()
tag_name = 'tag_name_example' # str | 
tag_tag_update = fcsm_eos_api_client.TagTagUpdate() # TagTagUpdate | The details of tag that will be updated
email = 'email_example' # str |  (optional)

try:
    api_instance.update_tag(tag_name, tag_tag_update, email=email)
except ApiException as e:
    print("Exception when calling TagApi->update_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_name** | **str**|  | 
 **tag_tag_update** | [**TagTagUpdate**](TagTagUpdate.md)| The details of tag that will be updated | 
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
**200** | Successfully updated tag |  -  |
**400** | Invalid role |  -  |
**403** | Insufficient access rights |  -  |
**404** | Unknown tagId |  -  |
**500** | An unexpected error occurred |  -  |
**503** | Database is unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

