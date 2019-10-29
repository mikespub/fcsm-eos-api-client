# fcsm_eos_api_client.AuthApi

All URIs are relative to *https://emeia-eos.fcsm.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_external_provider**](AuthApi.md#add_external_provider) | **POST** /api/v1/auth/externalProviders | 
[**delete_external_provider**](AuthApi.md#delete_external_provider) | **DELETE** /api/v1/auth/externalProviders/{providerId} | 
[**get_external_provider**](AuthApi.md#get_external_provider) | **GET** /api/v1/auth/externalProviders/{providerId} | 
[**get_external_providers**](AuthApi.md#get_external_providers) | **GET** /api/v1/auth/externalProviders | 
[**login**](AuthApi.md#login) | **POST** /api/v1/auth/login | 


# **add_external_provider**
> AuthSamlConfig add_external_provider(auth_saml_config)



Adds new external identity provider for saml

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint
configuration = fcsm_eos_api_client.Configuration()
# Configure Bearer authorization (JWT): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://emeia-eos.fcsm.io
configuration.host = "https://emeia-eos.fcsm.io"
# Create an instance of the API class
api_instance = fcsm_eos_api_client.AuthApi(fcsm_eos_api_client.ApiClient(configuration))
auth_saml_config = fcsm_eos_api_client.AuthSamlConfig() # AuthSamlConfig | 

try:
    api_response = api_instance.add_external_provider(auth_saml_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->add_external_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_saml_config** | [**AuthSamlConfig**](AuthSamlConfig.md)|  | 

### Return type

[**AuthSamlConfig**](AuthSamlConfig.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Saml IdP provider added successfully |  -  |
**400** | Input data is invalid |  -  |
**403** | Admin rights are required |  -  |
**500** | An unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_external_provider**
> delete_external_provider(provider_id)



Delete external identity provider

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint
configuration = fcsm_eos_api_client.Configuration()
# Configure Bearer authorization (JWT): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://emeia-eos.fcsm.io
configuration.host = "https://emeia-eos.fcsm.io"
# Create an instance of the API class
api_instance = fcsm_eos_api_client.AuthApi(fcsm_eos_api_client.ApiClient(configuration))
provider_id = 'provider_id_example' # str | 

try:
    api_instance.delete_external_provider(provider_id)
except ApiException as e:
    print("Exception when calling AuthApi->delete_external_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Provider deleted successfully |  -  |
**400** | Input data is invalid |  -  |
**403** | Admin rights are required |  -  |
**500** | An unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_external_provider**
> AuthSamlConfig get_external_provider(provider_id)



Configured external identity provider by id

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint
configuration = fcsm_eos_api_client.Configuration()
# Configure Bearer authorization (JWT): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://emeia-eos.fcsm.io
configuration.host = "https://emeia-eos.fcsm.io"
# Create an instance of the API class
api_instance = fcsm_eos_api_client.AuthApi(fcsm_eos_api_client.ApiClient(configuration))
provider_id = 'provider_id_example' # str | 

try:
    api_response = api_instance.get_external_provider(provider_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->get_external_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**|  | 

### Return type

[**AuthSamlConfig**](AuthSamlConfig.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Providers configuration |  -  |
**400** | Input data is invalid |  -  |
**403** | Admin rights are required |  -  |
**404** | Provider with this id does not exist |  -  |
**500** | An unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_external_providers**
> list[AuthSamlConfig] get_external_providers()



List of configured external identity providers

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint
configuration = fcsm_eos_api_client.Configuration()
# Configure Bearer authorization (JWT): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://emeia-eos.fcsm.io
configuration.host = "https://emeia-eos.fcsm.io"
# Create an instance of the API class
api_instance = fcsm_eos_api_client.AuthApi(fcsm_eos_api_client.ApiClient(configuration))

try:
    api_response = api_instance.get_external_providers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->get_external_providers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[AuthSamlConfig]**](AuthSamlConfig.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of providers |  -  |
**400** | Input data is invalid |  -  |
**403** | Admin rights are required |  -  |
**500** | An unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login**
> AuthToken login(auth_credentials)



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint
configuration = fcsm_eos_api_client.Configuration()
# Configure Bearer authorization (JWT): bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://emeia-eos.fcsm.io
configuration.host = "https://emeia-eos.fcsm.io"
# Create an instance of the API class
api_instance = fcsm_eos_api_client.AuthApi(fcsm_eos_api_client.ApiClient(configuration))
auth_credentials = fcsm_eos_api_client.AuthCredentials() # AuthCredentials | 

try:
    api_response = api_instance.login(auth_credentials)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_credentials** | [**AuthCredentials**](AuthCredentials.md)|  | 

### Return type

[**AuthToken**](AuthToken.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Token created successfully |  -  |
**400** | Input data is invalid |  -  |
**403** | Incorrect credentials |  -  |
**500** | An unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

