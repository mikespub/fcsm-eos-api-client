# fcsm_eos_api_client.ConfigApi

All URIs are relative to *https://emeia-eos.fcsm.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_mail_provider**](ConfigApi.md#add_mail_provider) | **POST** /api/v1/configuration/mailProviders | Add provider data
[**api_v1_configuration_logo_get**](ConfigApi.md#api_v1_configuration_logo_get) | **GET** /api/v1/configuration/logo | Get logo image
[**api_v1_configuration_logo_post**](ConfigApi.md#api_v1_configuration_logo_post) | **POST** /api/v1/configuration/logo | Send logo image to be stored
[**api_v1_configuration_mail_providers_default_provider_id_delete**](ConfigApi.md#api_v1_configuration_mail_providers_default_provider_id_delete) | **DELETE** /api/v1/configuration/mailProviders/default/{provider_id} | Unset default mail provider
[**api_v1_configuration_mail_providers_default_provider_id_put**](ConfigApi.md#api_v1_configuration_mail_providers_default_provider_id_put) | **PUT** /api/v1/configuration/mailProviders/default/{provider_id} | Set default mail provider
[**api_v1_configuration_mail_providers_provider_id_delete**](ConfigApi.md#api_v1_configuration_mail_providers_provider_id_delete) | **DELETE** /api/v1/configuration/mailProviders/{provider_id} | Delete provider
[**api_v1_configuration_management_tool_types_get**](ConfigApi.md#api_v1_configuration_management_tool_types_get) | **GET** /api/v1/configuration/managementToolTypes | Get management tool types
[**api_v1_configuration_management_tools_get**](ConfigApi.md#api_v1_configuration_management_tools_get) | **GET** /api/v1/configuration/managementTools | Get all mangement tools
[**api_v1_configuration_management_tools_post**](ConfigApi.md#api_v1_configuration_management_tools_post) | **POST** /api/v1/configuration/managementTools | Create new management tool
[**api_v1_configuration_management_tools_tool_id_get**](ConfigApi.md#api_v1_configuration_management_tools_tool_id_get) | **GET** /api/v1/configuration/managementTools/{tool_id} | Get specified management tool
[**api_v1_configuration_management_tools_tool_id_put**](ConfigApi.md#api_v1_configuration_management_tools_tool_id_put) | **PUT** /api/v1/configuration/managementTools/{tool_id} | Update specified management tool
[**edit_mail_provider**](ConfigApi.md#edit_mail_provider) | **PUT** /api/v1/configuration/mailProviders/{provider_id} | Edit provider
[**edit_platform_access**](ConfigApi.md#edit_platform_access) | **PUT** /api/v1/configuration/platformAccess | Set platform access configutation
[**get_all_platform_access**](ConfigApi.md#get_all_platform_access) | **GET** /api/v1/configuration/platformAccess | Get platform access configutation
[**get_mail_provider**](ConfigApi.md#get_mail_provider) | **GET** /api/v1/configuration/mailProviders/{provider_id} | Get provider data
[**get_mail_providers**](ConfigApi.md#get_mail_providers) | **GET** /api/v1/configuration/mailProviders | Get mail providers
[**get_platform_access**](ConfigApi.md#get_platform_access) | **GET** /api/v1/configuration/platformAccess/{platform_id} | Get platform access value
[**set_default_mail_provider**](ConfigApi.md#set_default_mail_provider) | **GET** /api/v1/configuration/mailProviders/default | Get default mail provider


# **add_mail_provider**
> ConfigMailProvider add_mail_provider(config_mail_provider)

Add provider data

Add new provider data

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.ConfigApi()
config_mail_provider = fcsm_eos_api_client.ConfigMailProvider() # ConfigMailProvider | Provider data

try:
    # Add provider data
    api_response = api_instance.add_mail_provider(config_mail_provider)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->add_mail_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_mail_provider** | [**ConfigMailProvider**](ConfigMailProvider.md)| Provider data | 

### Return type

[**ConfigMailProvider**](ConfigMailProvider.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Wrong provider service or provider name already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_configuration_logo_get**
> api_v1_configuration_logo_get()

Get logo image

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.ConfigApi()

try:
    # Get logo image
    api_instance.api_v1_configuration_logo_get()
except ApiException as e:
    print("Exception when calling ConfigApi->api_v1_configuration_logo_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | There is no image stored yet |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_configuration_logo_post**
> api_v1_configuration_logo_post(logo)

Send logo image to be stored

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.ConfigApi()
logo = '/path/to/file' # file | Uploaded logo image

try:
    # Send logo image to be stored
    api_instance.api_v1_configuration_logo_post(logo)
except ApiException as e:
    print("Exception when calling ConfigApi->api_v1_configuration_logo_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logo** | **file**| Uploaded logo image | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid request headers, unsupported image extension, error saving image. |  -  |
**411** | Missing request header Content-Length |  -  |
**413** | Image is to large. Maximum image size is 0.5MB. |  -  |
**415** | Unsupported Media Type |  -  |
**500** | Error while saving logo image |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_configuration_mail_providers_default_provider_id_delete**
> api_v1_configuration_mail_providers_default_provider_id_delete(provider_id)

Unset default mail provider

Unset mail provider as default

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.ConfigApi()
provider_id = 'provider_id_example' # str | Provider id

try:
    # Unset default mail provider
    api_instance.api_v1_configuration_mail_providers_default_provider_id_delete(provider_id)
except ApiException as e:
    print("Exception when calling ConfigApi->api_v1_configuration_mail_providers_default_provider_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| Provider id | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Provider id does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_configuration_mail_providers_default_provider_id_put**
> ConfigMailProvider api_v1_configuration_mail_providers_default_provider_id_put(provider_id)

Set default mail provider

Set default mail provider

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.ConfigApi()
provider_id = 'provider_id_example' # str | Provider id

try:
    # Set default mail provider
    api_response = api_instance.api_v1_configuration_mail_providers_default_provider_id_put(provider_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->api_v1_configuration_mail_providers_default_provider_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| Provider id | 

### Return type

[**ConfigMailProvider**](ConfigMailProvider.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Provider id does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_configuration_mail_providers_provider_id_delete**
> api_v1_configuration_mail_providers_provider_id_delete(provider_id)

Delete provider

Delete provider

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.ConfigApi()
provider_id = 'provider_id_example' # str | Provider id

try:
    # Delete provider
    api_instance.api_v1_configuration_mail_providers_provider_id_delete(provider_id)
except ApiException as e:
    print("Exception when calling ConfigApi->api_v1_configuration_mail_providers_provider_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| Provider id | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | OK |  -  |
**400** | Provider is currently set as default and cannot be deleted |  -  |
**404** | Provider id does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_configuration_management_tool_types_get**
> list[ConfigManagementToolType] api_v1_configuration_management_tool_types_get()

Get management tool types

Get management tool types

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.ConfigApi()

try:
    # Get management tool types
    api_response = api_instance.api_v1_configuration_management_tool_types_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->api_v1_configuration_management_tool_types_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ConfigManagementToolType]**](ConfigManagementToolType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_configuration_management_tools_get**
> list[ConfigManagementTool] api_v1_configuration_management_tools_get()

Get all mangement tools

Get all management tools

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.ConfigApi()

try:
    # Get all mangement tools
    api_response = api_instance.api_v1_configuration_management_tools_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->api_v1_configuration_management_tools_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ConfigManagementTool]**](ConfigManagementTool.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_configuration_management_tools_post**
> ConfigManagementTool api_v1_configuration_management_tools_post(config_create_management_tool)

Create new management tool

Create new management tool

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.ConfigApi()
config_create_management_tool = fcsm_eos_api_client.ConfigCreateManagementTool() # ConfigCreateManagementTool | arguments

try:
    # Create new management tool
    api_response = api_instance.api_v1_configuration_management_tools_post(config_create_management_tool)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->api_v1_configuration_management_tools_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_create_management_tool** | [**ConfigCreateManagementTool**](ConfigCreateManagementTool.md)| arguments | 

### Return type

[**ConfigManagementTool**](ConfigManagementTool.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid management tool type or url format or error saving data in database |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_configuration_management_tools_tool_id_get**
> ConfigManagementTool api_v1_configuration_management_tools_tool_id_get(tool_id)

Get specified management tool

Get specified management tool

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.ConfigApi()
tool_id = 'tool_id_example' # str | Management tool id

try:
    # Get specified management tool
    api_response = api_instance.api_v1_configuration_management_tools_tool_id_get(tool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->api_v1_configuration_management_tools_tool_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tool_id** | **str**| Management tool id | 

### Return type

[**ConfigManagementTool**](ConfigManagementTool.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Wrong tool id format |  -  |
**404** | Unknown tool id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_configuration_management_tools_tool_id_put**
> ConfigManagementTool api_v1_configuration_management_tools_tool_id_put(tool_id, config_update_management_tool)

Update specified management tool

Update specified management tool

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.ConfigApi()
tool_id = 'tool_id_example' # str | Management tool id
config_update_management_tool = fcsm_eos_api_client.ConfigUpdateManagementTool() # ConfigUpdateManagementTool | arguments

try:
    # Update specified management tool
    api_response = api_instance.api_v1_configuration_management_tools_tool_id_put(tool_id, config_update_management_tool)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->api_v1_configuration_management_tools_tool_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tool_id** | **str**| Management tool id | 
 **config_update_management_tool** | [**ConfigUpdateManagementTool**](ConfigUpdateManagementTool.md)| arguments | 

### Return type

[**ConfigManagementTool**](ConfigManagementTool.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Wrong tool id or url format |  -  |
**404** | Unknown tool id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_mail_provider**
> ConfigMailProvider edit_mail_provider(provider_id, config_mail_provider)

Edit provider

Edit provider

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.ConfigApi()
provider_id = 'provider_id_example' # str | Provider id
config_mail_provider = fcsm_eos_api_client.ConfigMailProvider() # ConfigMailProvider | Provider data

try:
    # Edit provider
    api_response = api_instance.edit_mail_provider(provider_id, config_mail_provider)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->edit_mail_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| Provider id | 
 **config_mail_provider** | [**ConfigMailProvider**](ConfigMailProvider.md)| Provider data | 

### Return type

[**ConfigMailProvider**](ConfigMailProvider.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Provider id does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_platform_access**
> edit_platform_access(config_configuration)

Set platform access configutation

Set platform access configutation

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.ConfigApi()
config_configuration = fcsm_eos_api_client.ConfigConfiguration() # ConfigConfiguration | Configuration to set

try:
    # Set platform access configutation
    api_instance.edit_platform_access(config_configuration)
except ApiException as e:
    print("Exception when calling ConfigApi->edit_platform_access: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_configuration** | [**ConfigConfiguration**](ConfigConfiguration.md)| Configuration to set | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Empty configuration given |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_platform_access**
> list[ConfigPlatformConfig] get_all_platform_access()

Get platform access configutation

Get platform access configutation

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.ConfigApi()

try:
    # Get platform access configutation
    api_response = api_instance.get_all_platform_access()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_all_platform_access: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ConfigPlatformConfig]**](ConfigPlatformConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mail_provider**
> ConfigMailProvider get_mail_provider(provider_id)

Get provider data

Get provider data

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.ConfigApi()
provider_id = 'provider_id_example' # str | Provider id

try:
    # Get provider data
    api_response = api_instance.get_mail_provider(provider_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_mail_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| Provider id | 

### Return type

[**ConfigMailProvider**](ConfigMailProvider.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Provider id does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mail_providers**
> list[ConfigMailProvider] get_mail_providers()

Get mail providers

Get all mail providers

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.ConfigApi()

try:
    # Get mail providers
    api_response = api_instance.get_mail_providers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_mail_providers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ConfigMailProvider]**](ConfigMailProvider.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_platform_access**
> bool get_platform_access(platform_id)

Get platform access value

Get platform access value

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.ConfigApi()
platform_id = 'platform_id_example' # str | Platform id

try:
    # Get platform access value
    api_response = api_instance.get_platform_access(platform_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_platform_access: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_id** | **str**| Platform id | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_default_mail_provider**
> ConfigMailProvider set_default_mail_provider()

Get default mail provider

Get data for default mail provider

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.ConfigApi()

try:
    # Get default mail provider
    api_response = api_instance.set_default_mail_provider()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->set_default_mail_provider: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConfigMailProvider**](ConfigMailProvider.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | No default mail provider set |  -  |
**500** | More than one default provider set |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

