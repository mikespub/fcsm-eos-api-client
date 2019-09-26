# fcsm_eos_api_client.MgmtApi

All URIs are relative to *https://emeia-eos.fcsm.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_management_app_instances_app_instance_id_delete**](MgmtApi.md#api_v1_management_app_instances_app_instance_id_delete) | **DELETE** /api/v1/management/appInstances/{app_instance_id} | Delete an app instance
[**api_v1_management_app_instances_app_instance_id_get**](MgmtApi.md#api_v1_management_app_instances_app_instance_id_get) | **GET** /api/v1/management/appInstances/{app_instance_id} | Get an app instance
[**api_v1_management_app_instances_app_instance_id_uninstall_put**](MgmtApi.md#api_v1_management_app_instances_app_instance_id_uninstall_put) | **PUT** /api/v1/management/appInstances/{app_instance_id}/uninstall | 
[**api_v1_management_app_instances_get**](MgmtApi.md#api_v1_management_app_instances_get) | **GET** /api/v1/management/appInstances | List apps instances
[**api_v1_management_app_instances_post**](MgmtApi.md#api_v1_management_app_instances_post) | **POST** /api/v1/management/appInstances | Create an app instance
[**api_v1_management_apps_app_id_get**](MgmtApi.md#api_v1_management_apps_app_id_get) | **GET** /api/v1/management/apps/{app_id} | Get app by id
[**api_v1_management_apps_get**](MgmtApi.md#api_v1_management_apps_get) | **GET** /api/v1/management/apps | List apps
[**api_v1_management_details_get**](MgmtApi.md#api_v1_management_details_get) | **GET** /api/v1/management/details | Get vm details
[**api_v1_management_get_bootstrap_script_get**](MgmtApi.md#api_v1_management_get_bootstrap_script_get) | **GET** /api/v1/management/getBootstrapScript | Get bootstrap script
[**api_v1_management_install_app_post**](MgmtApi.md#api_v1_management_install_app_post) | **POST** /api/v1/management/installApp | Install application
[**api_v1_management_is_managed_get**](MgmtApi.md#api_v1_management_is_managed_get) | **GET** /api/v1/management/isManaged | Check if a vm is managed
[**api_v1_management_managed_vms_get**](MgmtApi.md#api_v1_management_managed_vms_get) | **GET** /api/v1/management/managedVms | Return list of managed VM ids
[**api_v1_management_register_vm_post**](MgmtApi.md#api_v1_management_register_vm_post) | **POST** /api/v1/management/registerVm | 
[**api_v1_management_replace_apps_post**](MgmtApi.md#api_v1_management_replace_apps_post) | **POST** /api/v1/management/replaceApps | Upload apps metadata
[**api_v1_management_test_connectivity_post**](MgmtApi.md#api_v1_management_test_connectivity_post) | **POST** /api/v1/management/testConnectivity | Check connection with Vm
[**api_v1_management_tools_tool_id_apps_app_name_get**](MgmtApi.md#api_v1_management_tools_tool_id_apps_app_name_get) | **GET** /api/v1/management/tools/{tool_id}/apps/{app_name} | Get app by name
[**api_v1_management_tools_tool_id_tokens_post**](MgmtApi.md#api_v1_management_tools_tool_id_tokens_post) | **POST** /api/v1/management/tools/{tool_id}/tokens | Generate a new token for the given tool
[**api_v1_management_tools_tool_id_tokens_token_value_delete**](MgmtApi.md#api_v1_management_tools_tool_id_tokens_token_value_delete) | **DELETE** /api/v1/management/tools/{tool_id}/tokens/{token_value} | Delete the token
[**api_v1_management_uninstall_app_delete**](MgmtApi.md#api_v1_management_uninstall_app_delete) | **DELETE** /api/v1/management/uninstallApp | Uninstall application
[**api_v1_management_unregister_subscription_vms_delete**](MgmtApi.md#api_v1_management_unregister_subscription_vms_delete) | **DELETE** /api/v1/management/unregisterSubscriptionVms | Unregister vms from subscription
[**api_v1_management_unregister_vm_delete**](MgmtApi.md#api_v1_management_unregister_vm_delete) | **DELETE** /api/v1/management/unregisterVm | Unregister Vm from management tool


# **api_v1_management_app_instances_app_instance_id_delete**
> api_v1_management_app_instances_app_instance_id_delete(subscription_id, app_instance_id, force_delete=force_delete)

Delete an app instance

It is allowed to delete app instances that are in one of the following states: INITIAL, INSTALL_FAILED, UNINSTALL_SUCCEEDED, UNINSTALL_FAILED. 

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.MgmtApi()
subscription_id = 'subscription_id_example' # str | subscription id
app_instance_id = 'app_instance_id_example' # str | 
force_delete = True # bool | Forcely delete app_instance not checking the state. This option is only available for administrators  (optional)

try:
    # Delete an app instance
    api_instance.api_v1_management_app_instances_app_instance_id_delete(subscription_id, app_instance_id, force_delete=force_delete)
except ApiException as e:
    print("Exception when calling MgmtApi->api_v1_management_app_instances_app_instance_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| subscription id | 
 **app_instance_id** | [**str**](.md)|  | 
 **force_delete** | **bool**| Forcely delete app_instance not checking the state. This option is only available for administrators  | [optional] 

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
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | App instance not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_management_app_instances_app_instance_id_get**
> MgmtAppInstance api_v1_management_app_instances_app_instance_id_get(subscription_id, app_instance_id)

Get an app instance

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.MgmtApi()
subscription_id = 'subscription_id_example' # str | subscription id
app_instance_id = 'app_instance_id_example' # str | 

try:
    # Get an app instance
    api_response = api_instance.api_v1_management_app_instances_app_instance_id_get(subscription_id, app_instance_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MgmtApi->api_v1_management_app_instances_app_instance_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| subscription id | 
 **app_instance_id** | [**str**](.md)|  | 

### Return type

[**MgmtAppInstance**](MgmtAppInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_management_app_instances_app_instance_id_uninstall_put**
> MgmtAppInstance api_v1_management_app_instances_app_instance_id_uninstall_put(subscription_id, app_instance_id)



### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.MgmtApi()
subscription_id = 'subscription_id_example' # str | subscription id
app_instance_id = 'app_instance_id_example' # str | 

try:
    api_response = api_instance.api_v1_management_app_instances_app_instance_id_uninstall_put(subscription_id, app_instance_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MgmtApi->api_v1_management_app_instances_app_instance_id_uninstall_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| subscription id | 
 **app_instance_id** | [**str**](.md)|  | 

### Return type

[**MgmtAppInstance**](MgmtAppInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_management_app_instances_get**
> list[MgmtAppInstance] api_v1_management_app_instances_get(subscription_id, tool_id=tool_id, vm_id=vm_id, state=state)

List apps instances

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.MgmtApi()
subscription_id = 'subscription_id_example' # str | subscription id
tool_id = 'tool_id_example' # str | Optional filter (optional)
vm_id = 'vm_id_example' # str | Optional filter. (optional)
state = 'state_example' # str | Optional filter. (optional)

try:
    # List apps instances
    api_response = api_instance.api_v1_management_app_instances_get(subscription_id, tool_id=tool_id, vm_id=vm_id, state=state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MgmtApi->api_v1_management_app_instances_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| subscription id | 
 **tool_id** | [**str**](.md)| Optional filter | [optional] 
 **vm_id** | **str**| Optional filter. | [optional] 
 **state** | **str**| Optional filter. | [optional] 

### Return type

[**list[MgmtAppInstance]**](MgmtAppInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_management_app_instances_post**
> MgmtAppInstance api_v1_management_app_instances_post(subscription_id, inline_object2)

Create an app instance

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.MgmtApi()
subscription_id = 'subscription_id_example' # str | subscription id
inline_object2 = fcsm_eos_api_client.InlineObject2() # InlineObject2 | 

try:
    # Create an app instance
    api_response = api_instance.api_v1_management_app_instances_post(subscription_id, inline_object2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MgmtApi->api_v1_management_app_instances_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| subscription id | 
 **inline_object2** | [**InlineObject2**](InlineObject2.md)|  | 

### Return type

[**MgmtAppInstance**](MgmtAppInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_management_apps_app_id_get**
> MgmtApp api_v1_management_apps_app_id_get(app_id)

Get app by id

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.MgmtApi()
app_id = 'app_id_example' # str | 

try:
    # Get app by id
    api_response = api_instance.api_v1_management_apps_app_id_get(app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MgmtApi->api_v1_management_apps_app_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 

### Return type

[**MgmtApp**](MgmtApp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_management_apps_get**
> list[MgmtApp] api_v1_management_apps_get(tool_id=tool_id)

List apps

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.MgmtApi()
tool_id = 'tool_id_example' # str |  (optional)

try:
    # List apps
    api_response = api_instance.api_v1_management_apps_get(tool_id=tool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MgmtApi->api_v1_management_apps_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tool_id** | [**str**](.md)|  | [optional] 

### Return type

[**list[MgmtApp]**](MgmtApp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_management_details_get**
> MgmtVmDetails api_v1_management_details_get(mgmt_vm_details_params)

Get vm details

Get vm details

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.MgmtApi()
mgmt_vm_details_params = fcsm_eos_api_client.MgmtVmDetailsParams() # MgmtVmDetailsParams | Operating system and Vm information

try:
    # Get vm details
    api_response = api_instance.api_v1_management_details_get(mgmt_vm_details_params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MgmtApi->api_v1_management_details_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mgmt_vm_details_params** | [**MgmtVmDetailsParams**](MgmtVmDetailsParams.md)| Operating system and Vm information | 

### Return type

[**MgmtVmDetails**](MgmtVmDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Given vm was not found |  -  |
**504** | Timeout error communicating with management tool |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_management_get_bootstrap_script_get**
> MgmtBootstrapScriptReturn api_v1_management_get_bootstrap_script_get(mgmt_bootstrap_script)

Get bootstrap script

Get bootstrap script

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.MgmtApi()
mgmt_bootstrap_script = fcsm_eos_api_client.MgmtBootstrapScript() # MgmtBootstrapScript | Platform and Vm information

try:
    # Get bootstrap script
    api_response = api_instance.api_v1_management_get_bootstrap_script_get(mgmt_bootstrap_script)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MgmtApi->api_v1_management_get_bootstrap_script_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mgmt_bootstrap_script** | [**MgmtBootstrapScript**](MgmtBootstrapScript.md)| Platform and Vm information | 

### Return type

[**MgmtBootstrapScriptReturn**](MgmtBootstrapScriptReturn.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error while processing input information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_management_install_app_post**
> bool api_v1_management_install_app_post(mgmt_application)

Install application

Install application

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.MgmtApi()
mgmt_application = fcsm_eos_api_client.MgmtApplication() # MgmtApplication | Application and VM information

try:
    # Install application
    api_response = api_instance.api_v1_management_install_app_post(mgmt_application)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MgmtApi->api_v1_management_install_app_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mgmt_application** | [**MgmtApplication**](MgmtApplication.md)| Application and VM information | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Given vm was not found |  -  |
**504** | Timeout error communicating with management tool |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_management_is_managed_get**
> bool api_v1_management_is_managed_get(mgmt_manage_vm)

Check if a vm is managed

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.MgmtApi()
mgmt_manage_vm = fcsm_eos_api_client.MgmtManageVm() # MgmtManageVm | Vm information

try:
    # Check if a vm is managed
    api_response = api_instance.api_v1_management_is_managed_get(mgmt_manage_vm)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MgmtApi->api_v1_management_is_managed_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mgmt_manage_vm** | [**MgmtManageVm**](MgmtManageVm.md)| Vm information | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | No management information for given VM exists |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_management_managed_vms_get**
> list[MgmtManagedVms] api_v1_management_managed_vms_get(subscription_id, vm_id=vm_id)

Return list of managed VM ids

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.MgmtApi()
subscription_id = 'subscription_id_example' # str | 
vm_id = 'vm_id_example' # str |  (optional)

try:
    # Return list of managed VM ids
    api_response = api_instance.api_v1_management_managed_vms_get(subscription_id, vm_id=vm_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MgmtApi->api_v1_management_managed_vms_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **vm_id** | **str**|  | [optional] 

### Return type

[**list[MgmtManagedVms]**](MgmtManagedVms.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_management_register_vm_post**
> api_v1_management_register_vm_post(mgmt_register_vm)



Register Vm in management tool

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.MgmtApi()
mgmt_register_vm = fcsm_eos_api_client.MgmtRegisterVm() # MgmtRegisterVm | Vm and management tool information

try:
    api_instance.api_v1_management_register_vm_post(mgmt_register_vm)
except ApiException as e:
    print("Exception when calling MgmtApi->api_v1_management_register_vm_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mgmt_register_vm** | [**MgmtRegisterVm**](MgmtRegisterVm.md)| Vm and management tool information | 

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
**204** | OK |  -  |
**504** | Timeout error communicating with management tool |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_management_replace_apps_post**
> api_v1_management_replace_apps_post(x_tool_token, inline_object1)

Upload apps metadata

Upload apps metadata

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.MgmtApi()
x_tool_token = 'x_tool_token_example' # str | A token that gives permission to upload apps for specific tool.
inline_object1 = fcsm_eos_api_client.InlineObject1() # InlineObject1 | 

try:
    # Upload apps metadata
    api_instance.api_v1_management_replace_apps_post(x_tool_token, inline_object1)
except ApiException as e:
    print("Exception when calling MgmtApi->api_v1_management_replace_apps_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tool_token** | **str**| A token that gives permission to upload apps for specific tool. | 
 **inline_object1** | [**InlineObject1**](InlineObject1.md)|  | 

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
**204** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_management_test_connectivity_post**
> bool api_v1_management_test_connectivity_post(mgmt_manage_vm)

Check connection with Vm

Check connection with Vm

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.MgmtApi()
mgmt_manage_vm = fcsm_eos_api_client.MgmtManageVm() # MgmtManageVm | Vm information

try:
    # Check connection with Vm
    api_response = api_instance.api_v1_management_test_connectivity_post(mgmt_manage_vm)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MgmtApi->api_v1_management_test_connectivity_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mgmt_manage_vm** | [**MgmtManageVm**](MgmtManageVm.md)| Vm information | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Given vm was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_management_tools_tool_id_apps_app_name_get**
> MgmtApp api_v1_management_tools_tool_id_apps_app_name_get(tool_id, app_name)

Get app by name

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.MgmtApi()
tool_id = 'tool_id_example' # str | 
app_name = 'app_name_example' # str | 

try:
    # Get app by name
    api_response = api_instance.api_v1_management_tools_tool_id_apps_app_name_get(tool_id, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MgmtApi->api_v1_management_tools_tool_id_apps_app_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tool_id** | [**str**](.md)|  | 
 **app_name** | **str**|  | 

### Return type

[**MgmtApp**](MgmtApp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_management_tools_tool_id_tokens_post**
> MgmtToolToken api_v1_management_tools_tool_id_tokens_post(tool_id, inline_object3)

Generate a new token for the given tool

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.MgmtApi()
tool_id = 'tool_id_example' # str | 
inline_object3 = fcsm_eos_api_client.InlineObject3() # InlineObject3 | 

try:
    # Generate a new token for the given tool
    api_response = api_instance.api_v1_management_tools_tool_id_tokens_post(tool_id, inline_object3)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MgmtApi->api_v1_management_tools_tool_id_tokens_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tool_id** | [**str**](.md)|  | 
 **inline_object3** | [**InlineObject3**](InlineObject3.md)|  | 

### Return type

[**MgmtToolToken**](MgmtToolToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_management_tools_tool_id_tokens_token_value_delete**
> api_v1_management_tools_tool_id_tokens_token_value_delete(tool_id, token_value)

Delete the token

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.MgmtApi()
tool_id = 'tool_id_example' # str | 
token_value = 'token_value_example' # str | 

try:
    # Delete the token
    api_instance.api_v1_management_tools_tool_id_tokens_token_value_delete(tool_id, token_value)
except ApiException as e:
    print("Exception when calling MgmtApi->api_v1_management_tools_tool_id_tokens_token_value_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tool_id** | [**str**](.md)|  | 
 **token_value** | **str**|  | 

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
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_management_uninstall_app_delete**
> bool api_v1_management_uninstall_app_delete(mgmt_application)

Uninstall application

Uninstall application

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.MgmtApi()
mgmt_application = fcsm_eos_api_client.MgmtApplication() # MgmtApplication | Application and Vm information

try:
    # Uninstall application
    api_response = api_instance.api_v1_management_uninstall_app_delete(mgmt_application)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MgmtApi->api_v1_management_uninstall_app_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mgmt_application** | [**MgmtApplication**](MgmtApplication.md)| Application and Vm information | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Given vm was not found |  -  |
**504** | Timeout error communicating with management tool |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_management_unregister_subscription_vms_delete**
> api_v1_management_unregister_subscription_vms_delete(body)

Unregister vms from subscription

Unregister vms from subscription

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.MgmtApi()
body = 'body_example' # str | Subscription id

try:
    # Unregister vms from subscription
    api_instance.api_v1_management_unregister_subscription_vms_delete(body)
except ApiException as e:
    print("Exception when calling MgmtApi->api_v1_management_unregister_subscription_vms_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| Subscription id | 

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
**204** | OK |  -  |
**400** | Error while processing input information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_management_unregister_vm_delete**
> api_v1_management_unregister_vm_delete(mgmt_manage_vm)

Unregister Vm from management tool

Unregister Vm from management tool

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.MgmtApi()
mgmt_manage_vm = fcsm_eos_api_client.MgmtManageVm() # MgmtManageVm | Vm information

try:
    # Unregister Vm from management tool
    api_instance.api_v1_management_unregister_vm_delete(mgmt_manage_vm)
except ApiException as e:
    print("Exception when calling MgmtApi->api_v1_management_unregister_vm_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mgmt_manage_vm** | [**MgmtManageVm**](MgmtManageVm.md)| Vm information | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | OK |  -  |
**404** | Given vm was not found |  -  |
**504** | Timeout error communicating with management tool |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

