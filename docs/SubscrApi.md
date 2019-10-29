# fcsm_eos_api_client.SubscrApi

All URIs are relative to *https://emeia-eos.fcsm.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_subscription_validate_vm_put**](SubscrApi.md#api_v1_subscription_validate_vm_put) | **PUT** /api/v1/subscription/validateVm | 
[**api_v1_subscription_validate_workshift_put**](SubscrApi.md#api_v1_subscription_validate_workshift_put) | **PUT** /api/v1/subscription/validateWorkshift | 
[**create_subscription**](SubscrApi.md#create_subscription) | **POST** /api/v1/subscription/subscriptions | Create subscription
[**delete_subscription**](SubscrApi.md#delete_subscription) | **DELETE** /api/v1/subscription/subscriptions/{subscription_id} | Delete subscription
[**get_subscription**](SubscrApi.md#get_subscription) | **GET** /api/v1/subscription/subscriptions/{subscription_id} | Get subscription
[**get_subscriptions**](SubscrApi.md#get_subscriptions) | **GET** /api/v1/subscription/subscriptions | Get subscriptions
[**get_token**](SubscrApi.md#get_token) | **GET** /api/v1/subscription/subscriptions/{subscription_id}/tokens | Get token
[**update_subscription**](SubscrApi.md#update_subscription) | **PUT** /api/v1/subscription/subscriptions/{subscription_id} | Modify subscription


# **api_v1_subscription_validate_vm_put**
> InlineResponse200 api_v1_subscription_validate_vm_put(subscr_virtual_machine_validation_parameters)



Validate a VM against a policy.

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
api_instance = fcsm_eos_api_client.SubscrApi(fcsm_eos_api_client.ApiClient(configuration))
subscr_virtual_machine_validation_parameters = fcsm_eos_api_client.SubscrVirtualMachineValidationParameters() # SubscrVirtualMachineValidationParameters | 

try:
    api_response = api_instance.api_v1_subscription_validate_vm_put(subscr_virtual_machine_validation_parameters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscrApi->api_v1_subscription_validate_vm_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscr_virtual_machine_validation_parameters** | [**SubscrVirtualMachineValidationParameters**](SubscrVirtualMachineValidationParameters.md)|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Validation completed. Response will contain &#x60;message&#x60; property describing the reason for the failure, &#x60;isCompliant&#x60; will be set to &#x60;false&#x60; in this case. Response will be &#x60;{isCompliant: true}&#x60; in case of successfull validation. |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_subscription_validate_workshift_put**
> InlineResponse200 api_v1_subscription_validate_workshift_put(subscr_workshift_validation_parameters)



Validate a workshift against a policy.

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
api_instance = fcsm_eos_api_client.SubscrApi(fcsm_eos_api_client.ApiClient(configuration))
subscr_workshift_validation_parameters = fcsm_eos_api_client.SubscrWorkshiftValidationParameters() # SubscrWorkshiftValidationParameters | 

try:
    api_response = api_instance.api_v1_subscription_validate_workshift_put(subscr_workshift_validation_parameters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscrApi->api_v1_subscription_validate_workshift_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscr_workshift_validation_parameters** | [**SubscrWorkshiftValidationParameters**](SubscrWorkshiftValidationParameters.md)|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Validation completed. Response will contain &#x60;message&#x60; property describing the reason for the failure, &#x60;isCompliant&#x60; will be set to &#x60;false&#x60; in this case. Response will be &#x60;{isCompliant: true}&#x60; in case of successful validation. |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_subscription**
> SubscrSubscription create_subscription(userid, subscr_create_subscription)

Create subscription

Create new subscription. Provided credentials are validated against target platform

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
api_instance = fcsm_eos_api_client.SubscrApi(fcsm_eos_api_client.ApiClient(configuration))
userid = 'userid_example' # str | User ID
subscr_create_subscription = fcsm_eos_api_client.SubscrCreateSubscription() # SubscrCreateSubscription | Details of the subscription that will be created

try:
    # Create subscription
    api_response = api_instance.create_subscription(userid, subscr_create_subscription)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscrApi->create_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**| User ID | 
 **subscr_create_subscription** | [**SubscrCreateSubscription**](SubscrCreateSubscription.md)| Details of the subscription that will be created | 

### Return type

[**SubscrSubscription**](SubscrSubscription.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid parameters or credentials validation failure |  -  |
**500** | Subscription validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_subscription**
> delete_subscription(subscription_id)

Delete subscription

Delete subscription for given id

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
api_instance = fcsm_eos_api_client.SubscrApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of a subscription

try:
    # Delete subscription
    api_instance.delete_subscription(subscription_id)
except ApiException as e:
    print("Exception when calling SubscrApi->delete_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Id of a subscription | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | OK |  -  |
**404** | No subscription for given id |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription**
> SubscrSubscription get_subscription(subscription_id)

Get subscription

Get single subscription for specified subscription_id

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
api_instance = fcsm_eos_api_client.SubscrApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of a subscription

try:
    # Get subscription
    api_response = api_instance.get_subscription(subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscrApi->get_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Id of a subscription | 

### Return type

[**SubscrSubscription**](SubscrSubscription.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | No subscription for given id |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscriptions**
> list[SubscrSubscription] get_subscriptions(subscriptions=subscriptions, username=username, platform_id=platform_id)

Get subscriptions

Retrieve list of all subscriptions

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
api_instance = fcsm_eos_api_client.SubscrApi(fcsm_eos_api_client.ApiClient(configuration))
subscriptions = 'subscriptions_example' # str |  (optional)
username = 'username_example' # str | Return only subscriptions to which given user has an access to (optional)
platform_id = 'platform_id_example' # str | Filter subscription by given platform id (openStack , aws, k5, ...). (optional)

try:
    # Get subscriptions
    api_response = api_instance.get_subscriptions(subscriptions=subscriptions, username=username, platform_id=platform_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscrApi->get_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptions** | **str**|  | [optional] 
 **username** | **str**| Return only subscriptions to which given user has an access to | [optional] 
 **platform_id** | **str**| Filter subscription by given platform id (openStack , aws, k5, ...). | [optional] 

### Return type

[**list[SubscrSubscription]**](SubscrSubscription.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of subscriptions |  -  |
**400** | Bad request parameters/data |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_token**
> SubscrToken get_token(subscription_id)

Get token

Get token for a subscription

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
api_instance = fcsm_eos_api_client.SubscrApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of a subscription

try:
    # Get token
    api_response = api_instance.get_token(subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscrApi->get_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Id of a subscription | 

### Return type

[**SubscrToken**](SubscrToken.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Platform not supported |  -  |
**500** | Error during fetching token from platform |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_subscription**
> SubscrSubscription update_subscription(subscription_id, subscr_modify_subscription)

Modify subscription

Modify subscription for given id

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
api_instance = fcsm_eos_api_client.SubscrApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of a subscription
subscr_modify_subscription = fcsm_eos_api_client.SubscrModifySubscription() # SubscrModifySubscription | Details of the subscription that will be created

try:
    # Modify subscription
    api_response = api_instance.update_subscription(subscription_id, subscr_modify_subscription)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscrApi->update_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Id of a subscription | 
 **subscr_modify_subscription** | [**SubscrModifySubscription**](SubscrModifySubscription.md)| Details of the subscription that will be created | 

### Return type

[**SubscrSubscription**](SubscrSubscription.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**204** | No parameter to modify given |  -  |
**400** | Parameter that cannot be modified given or invalid credentials |  -  |
**404** | No subscription for given id |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

