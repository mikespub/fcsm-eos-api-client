# fcsm_eos_api_client.AzureApi

All URIs are relative to *https://emeia-eos.fcsm.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**azure_service_api_availability_set_get**](AzureApi.md#azure_service_api_availability_set_get) | **GET** /api/v1/azure/compute/availabilitySets/{availability_set_id} | Gets availability set by id
[**azure_service_api_availability_sets_get**](AzureApi.md#azure_service_api_availability_sets_get) | **GET** /api/v1/azure/compute/availabilitySets | Lists availability sets for specified subscription and resource group
[**azure_service_api_availability_zone_get**](AzureApi.md#azure_service_api_availability_zone_get) | **GET** /api/v1/azure/compute/availabilityZones | Lists availability zones for specified subscription
[**azure_service_api_flavor_get**](AzureApi.md#azure_service_api_flavor_get) | **GET** /api/v1/azure/compute/flavors/{flavor_id} | Gets a single flavor by ID
[**azure_service_api_flavors_get**](AzureApi.md#azure_service_api_flavors_get) | **GET** /api/v1/azure/compute/flavors | Lists flavors for specified subscription
[**azure_service_api_image_get**](AzureApi.md#azure_service_api_image_get) | **GET** /api/v1/azure/compute/images/{image_id} | Gets a single image by id
[**azure_service_api_interfaces_get**](AzureApi.md#azure_service_api_interfaces_get) | **GET** /api/v1/azure/compute/interfaces | Lists interfaces for specified subscription
[**azure_service_api_keypair_delete**](AzureApi.md#azure_service_api_keypair_delete) | **DELETE** /api/v1/azure/compute/keypairs/{keypair_id} | Delets a single keypair
[**azure_service_api_keypair_generate_post**](AzureApi.md#azure_service_api_keypair_generate_post) | **POST** /api/v1/azure/compute/keypairs/generate | Generate a new keypair
[**azure_service_api_keypair_get**](AzureApi.md#azure_service_api_keypair_get) | **GET** /api/v1/azure/compute/keypairs/{keypair_id} | Gets a single keypair
[**azure_service_api_keypair_import_post**](AzureApi.md#azure_service_api_keypair_import_post) | **POST** /api/v1/azure/compute/keypairs/import | Import a public key
[**azure_service_api_keypairs_get**](AzureApi.md#azure_service_api_keypairs_get) | **GET** /api/v1/azure/compute/keypairs | Lists keypairs
[**azure_service_api_network_subnets_get**](AzureApi.md#azure_service_api_network_subnets_get) | **GET** /api/v1/azure/compute/networks/{network_id}/subnets | Lists subnets for specified network and subscription
[**azure_service_api_networks_get**](AzureApi.md#azure_service_api_networks_get) | **GET** /api/v1/azure/compute/networks | List networks for specified subscription
[**azure_service_api_private_image_get**](AzureApi.md#azure_service_api_private_image_get) | **GET** /api/v1/azure/compute/privateImages/{image_id} | Gets a single private image by id
[**azure_service_api_private_images_get**](AzureApi.md#azure_service_api_private_images_get) | **GET** /api/v1/azure/compute/privateImages | Lists private images for specified subscription
[**azure_service_api_public_image_get**](AzureApi.md#azure_service_api_public_image_get) | **GET** /api/v1/azure/compute/publicImages/{image_id} | Gets a single public image by id
[**azure_service_api_public_images_get**](AzureApi.md#azure_service_api_public_images_get) | **GET** /api/v1/azure/compute/publicImages | Lists all public images for specified subscription
[**azure_service_api_regions_get**](AzureApi.md#azure_service_api_regions_get) | **GET** /api/v1/azure/compute/regions | Lists regions
[**azure_service_api_resource_groups_get**](AzureApi.md#azure_service_api_resource_groups_get) | **GET** /api/v1/azure/compute/resourceGroups | Lists resource groups
[**azure_service_api_resource_groups_post**](AzureApi.md#azure_service_api_resource_groups_post) | **POST** /api/v1/azure/compute/resourceGroups | Creates new resource group
[**azure_service_api_security_groups_get**](AzureApi.md#azure_service_api_security_groups_get) | **GET** /api/v1/azure/compute/securityGroups | Lists security groups for specified subscription
[**azure_service_api_snapshot_delete**](AzureApi.md#azure_service_api_snapshot_delete) | **DELETE** /api/v1/azure/compute/snapshots/{snapshot_id} | Delete snapshot
[**azure_service_api_snapshots_get**](AzureApi.md#azure_service_api_snapshots_get) | **GET** /api/v1/azure/compute/snapshots | Get list of all snapshots
[**azure_service_api_snapshots_post**](AzureApi.md#azure_service_api_snapshots_post) | **POST** /api/v1/azure/compute/snapshots | Create a new snapshot
[**azure_service_api_validate_subscription_post**](AzureApi.md#azure_service_api_validate_subscription_post) | **POST** /api/v1/azure/compute/validateSubscription | Validate subscription credentials
[**azure_service_api_vm_command_put**](AzureApi.md#azure_service_api_vm_command_put) | **PUT** /api/v1/azure/compute/vms/{vm_id}/command/{action} | Executes power action on a VM
[**azure_service_api_vm_delete**](AzureApi.md#azure_service_api_vm_delete) | **DELETE** /api/v1/azure/compute/vms/{vm_id} | Deletes a single virtual machine by ID
[**azure_service_api_vm_details_get**](AzureApi.md#azure_service_api_vm_details_get) | **GET** /api/v1/azure/compute/vms/{vm_id}/details | Gets specified virtual machine details
[**azure_service_api_vm_floating_ip_delete**](AzureApi.md#azure_service_api_vm_floating_ip_delete) | **DELETE** /api/v1/azure/compute/vms/{vm_id}/unassignFloatingIp | Unassigns floating public IP from specified VM
[**azure_service_api_vm_floating_ip_put**](AzureApi.md#azure_service_api_vm_floating_ip_put) | **PUT** /api/v1/azure/compute/vms/{vm_id}/assignFloatingIp | Assigns a floating public IP v4 to specified VM
[**azure_service_api_vm_get**](AzureApi.md#azure_service_api_vm_get) | **GET** /api/v1/azure/compute/vms/{vm_id} | Gets a single virtual machine by ID
[**azure_service_api_vm_management_get**](AzureApi.md#azure_service_api_vm_management_get) | **GET** /api/v1/azure/compute/vms/{vm_id}/management | Gets specified virtual machine management status
[**azure_service_api_vm_password_get**](AzureApi.md#azure_service_api_vm_password_get) | **GET** /api/v1/azure/compute/vms/{vm_id}/password | Gets specified virtual machine encrypted password
[**azure_service_api_vm_patch**](AzureApi.md#azure_service_api_vm_patch) | **PATCH** /api/v1/azure/compute/vms/{vm_id} | Modifies specified virtual machine
[**azure_service_api_vm_security_groups_delete**](AzureApi.md#azure_service_api_vm_security_groups_delete) | **DELETE** /api/v1/azure/compute/vms/{vm_id}/securityGroups/{security_group_id} | Unassigns specified security group from specified VM
[**azure_service_api_vm_security_groups_put**](AzureApi.md#azure_service_api_vm_security_groups_put) | **PUT** /api/v1/azure/compute/vms/{vm_id}/securityGroups/{security_group_id} | Assigns a new network security group and unassigns old one
[**azure_service_api_vm_tag_put**](AzureApi.md#azure_service_api_vm_tag_put) | **PUT** /api/v1/azure/compute/vms/{vm_id}/setTag | Sets/unsets tag in virtual machine
[**azure_service_api_vm_workshift_delete**](AzureApi.md#azure_service_api_vm_workshift_delete) | **DELETE** /api/v1/azure/compute/vms/{vm_id}/workshift | Delete VM Workshift
[**azure_service_api_vm_workshift_post**](AzureApi.md#azure_service_api_vm_workshift_post) | **POST** /api/v1/azure/compute/vms/{vm_id}/workshift | Add a workshift to the VM
[**azure_service_api_vm_workshift_put**](AzureApi.md#azure_service_api_vm_workshift_put) | **PUT** /api/v1/azure/compute/vms/{vm_id}/workshift | Update VM Workshift
[**azure_service_api_vms_get**](AzureApi.md#azure_service_api_vms_get) | **GET** /api/v1/azure/compute/vms | Lists virtual machines for specified subscription
[**azure_service_api_vms_post**](AzureApi.md#azure_service_api_vms_post) | **POST** /api/v1/azure/compute/vms | Provisions virtual machine according to specified parameters
[**azure_service_api_volume_attachment_delete**](AzureApi.md#azure_service_api_volume_attachment_delete) | **DELETE** /api/v1/azure/compute/volumes/{volume_id}/detach | Dettaches volume
[**azure_service_api_volume_attachment_put**](AzureApi.md#azure_service_api_volume_attachment_put) | **PUT** /api/v1/azure/compute/volumes/{volume_id}/attach | Attaches volume
[**azure_service_api_volume_delete**](AzureApi.md#azure_service_api_volume_delete) | **DELETE** /api/v1/azure/compute/volumes/{volume_id} | Removes volume
[**azure_service_api_volume_get**](AzureApi.md#azure_service_api_volume_get) | **GET** /api/v1/azure/compute/volumes/{volume_id} | Gets a single volume by ID
[**azure_service_api_volume_patch**](AzureApi.md#azure_service_api_volume_patch) | **PATCH** /api/v1/azure/compute/volumes/{volume_id} | Modify volume properties
[**azure_service_api_volume_types_get**](AzureApi.md#azure_service_api_volume_types_get) | **GET** /api/v1/azure/compute/volumeTypes | Lists volume types
[**azure_service_api_volumes_get**](AzureApi.md#azure_service_api_volumes_get) | **GET** /api/v1/azure/compute/volumes | Lists volumes for specified subscription
[**azure_service_api_volumes_post**](AzureApi.md#azure_service_api_volumes_post) | **POST** /api/v1/azure/compute/volumes | Creates new volume


# **azure_service_api_availability_set_get**
> AzureAvailabilitySet azure_service_api_availability_set_get(subscription_id, availability_set_id)

Gets availability set by id

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
api_instance = fcsm_eos_api_client.AzureApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | ID of subscription
availability_set_id = 'availability_set_id_example' # str | Availability Set ID

try:
    # Gets availability set by id
    api_response = api_instance.azure_service_api_availability_set_get(subscription_id, availability_set_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureApi->azure_service_api_availability_set_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| ID of subscription | 
 **availability_set_id** | **str**| Availability Set ID | 

### Return type

[**AzureAvailabilitySet**](AzureAvailabilitySet.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Availability set identified by ID |  -  |
**404** | Object was not found |  -  |
**408** | There was a timeout when processing the request |  -  |
**0** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azure_service_api_availability_sets_get**
> list[AzureAvailabilitySet] azure_service_api_availability_sets_get(subscription_id)

Lists availability sets for specified subscription and resource group

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
api_instance = fcsm_eos_api_client.AzureApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | ID of subscription

try:
    # Lists availability sets for specified subscription and resource group
    api_response = api_instance.azure_service_api_availability_sets_get(subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureApi->azure_service_api_availability_sets_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| ID of subscription | 

### Return type

[**list[AzureAvailabilitySet]**](AzureAvailabilitySet.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of availability sets |  -  |
**404** | Object was not found |  -  |
**408** | There was a timeout when processing the request |  -  |
**0** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azure_service_api_availability_zone_get**
> list[AzureAvailabilityZone] azure_service_api_availability_zone_get(subscription_id)

Lists availability zones for specified subscription

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
api_instance = fcsm_eos_api_client.AzureApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | ID of subscription

try:
    # Lists availability zones for specified subscription
    api_response = api_instance.azure_service_api_availability_zone_get(subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureApi->azure_service_api_availability_zone_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| ID of subscription | 

### Return type

[**list[AzureAvailabilityZone]**](AzureAvailabilityZone.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of availability zones |  -  |
**408** | There was a timeout when processing the request |  -  |
**0** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azure_service_api_flavor_get**
> AzureFlavor azure_service_api_flavor_get(subscription_id, flavor_id)

Gets a single flavor by ID

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
api_instance = fcsm_eos_api_client.AzureApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | ID of subscription
flavor_id = 'flavor_id_example' # str | ID of Flavor

try:
    # Gets a single flavor by ID
    api_response = api_instance.azure_service_api_flavor_get(subscription_id, flavor_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureApi->azure_service_api_flavor_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| ID of subscription | 
 **flavor_id** | **str**| ID of Flavor | 

### Return type

[**AzureFlavor**](AzureFlavor.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Single flavor identified by ID |  -  |
**404** | Object was not found |  -  |
**408** | There was a timeout when processing the request |  -  |
**0** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azure_service_api_flavors_get**
> list[AzureFlavor] azure_service_api_flavors_get(subscription_id)

Lists flavors for specified subscription

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
api_instance = fcsm_eos_api_client.AzureApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | ID of subscription

try:
    # Lists flavors for specified subscription
    api_response = api_instance.azure_service_api_flavors_get(subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureApi->azure_service_api_flavors_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| ID of subscription | 

### Return type

[**list[AzureFlavor]**](AzureFlavor.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of flavors |  -  |
**408** | There was a timeout when processing the request |  -  |
**0** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azure_service_api_image_get**
> AzurePublicPrivateImage azure_service_api_image_get(subscription_id, image_id)

Gets a single image by id

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
api_instance = fcsm_eos_api_client.AzureApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | ID of subscription
image_id = 'image_id_example' # str | Image id

try:
    # Gets a single image by id
    api_response = api_instance.azure_service_api_image_get(subscription_id, image_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureApi->azure_service_api_image_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| ID of subscription | 
 **image_id** | **str**| Image id | 

### Return type

[**AzurePublicPrivateImage**](AzurePublicPrivateImage.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Single image |  -  |
**404** | Object was not found |  -  |
**408** | There was a timeout when processing the request |  -  |
**422** | Server was able to read the request but the instructions are not correct |  -  |
**503** | Service is unavailable |  -  |
**0** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azure_service_api_interfaces_get**
> list[AzureInterface] azure_service_api_interfaces_get(subscription_id, vm_id=vm_id, network_id=network_id, subnet_id=subnet_id)

Lists interfaces for specified subscription

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
api_instance = fcsm_eos_api_client.AzureApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | ID of subscription
vm_id = 'vm_id_example' # str | Vm id to filter by (optional)
network_id = 'network_id_example' # str | Network id to filter by (optional)
subnet_id = 'subnet_id_example' # str | Subnet id to filter by (optional)

try:
    # Lists interfaces for specified subscription
    api_response = api_instance.azure_service_api_interfaces_get(subscription_id, vm_id=vm_id, network_id=network_id, subnet_id=subnet_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureApi->azure_service_api_interfaces_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| ID of subscription | 
 **vm_id** | **str**| Vm id to filter by | [optional] 
 **network_id** | **str**| Network id to filter by | [optional] 
 **subnet_id** | **str**| Subnet id to filter by | [optional] 

### Return type

[**list[AzureInterface]**](AzureInterface.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of interfaces |  -  |
**408** | There was a timeout when processing the request |  -  |
**422** | Server was able to read the request but the instructions are not correct |  -  |
**503** | Service is unavailable |  -  |
**0** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azure_service_api_keypair_delete**
> azure_service_api_keypair_delete(subscription_id, keypair_id)

Delets a single keypair

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
api_instance = fcsm_eos_api_client.AzureApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | ID of subscription
keypair_id = 'keypair_id_example' # str | Id of the keypair

try:
    # Delets a single keypair
    api_instance.azure_service_api_keypair_delete(subscription_id, keypair_id)
except ApiException as e:
    print("Exception when calling AzureApi->azure_service_api_keypair_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| ID of subscription | 
 **keypair_id** | **str**| Id of the keypair | 

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
**204** | Keypair was deleted |  -  |
**404** | Object was not found |  -  |
**408** | There was a timeout when processing the request |  -  |
**422** | Server was able to read the request but the instructions are not correct |  -  |
**503** | Service is unavailable |  -  |
**0** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azure_service_api_keypair_generate_post**
> AzureGeneratedKeypair azure_service_api_keypair_generate_post(subscription_id, azure_keypair_generate)

Generate a new keypair

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
api_instance = fcsm_eos_api_client.AzureApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | ID of subscription
azure_keypair_generate = fcsm_eos_api_client.AzureKeypairGenerate() # AzureKeypairGenerate | 

try:
    # Generate a new keypair
    api_response = api_instance.azure_service_api_keypair_generate_post(subscription_id, azure_keypair_generate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureApi->azure_service_api_keypair_generate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| ID of subscription | 
 **azure_keypair_generate** | [**AzureKeypairGenerate**](AzureKeypairGenerate.md)|  | 

### Return type

[**AzureGeneratedKeypair**](AzureGeneratedKeypair.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Generated keypair |  -  |
**400** | Bad request |  -  |
**408** | There was a timeout when processing the request |  -  |
**422** | Server was able to read the request but the instructions are not correct |  -  |
**503** | Service is unavailable |  -  |
**0** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azure_service_api_keypair_get**
> AzureKeypair azure_service_api_keypair_get(subscription_id, keypair_id)

Gets a single keypair

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
api_instance = fcsm_eos_api_client.AzureApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | ID of subscription
keypair_id = 'keypair_id_example' # str | Id of the keypair

try:
    # Gets a single keypair
    api_response = api_instance.azure_service_api_keypair_get(subscription_id, keypair_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureApi->azure_service_api_keypair_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| ID of subscription | 
 **keypair_id** | **str**| Id of the keypair | 

### Return type

[**AzureKeypair**](AzureKeypair.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Single keypair |  -  |
**404** | Object was not found |  -  |
**408** | There was a timeout when processing the request |  -  |
**422** | Server was able to read the request but the instructions are not correct |  -  |
**503** | Service is unavailable |  -  |
**0** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azure_service_api_keypair_import_post**
> AzureKeypair azure_service_api_keypair_import_post(subscription_id, azure_keypair_import)

Import a public key

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
api_instance = fcsm_eos_api_client.AzureApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | ID of subscription
azure_keypair_import = fcsm_eos_api_client.AzureKeypairImport() # AzureKeypairImport | 

try:
    # Import a public key
    api_response = api_instance.azure_service_api_keypair_import_post(subscription_id, azure_keypair_import)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureApi->azure_service_api_keypair_import_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| ID of subscription | 
 **azure_keypair_import** | [**AzureKeypairImport**](AzureKeypairImport.md)|  | 

### Return type

[**AzureKeypair**](AzureKeypair.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Generated keypair |  -  |
**400** | Bad request |  -  |
**408** | There was a timeout when processing the request |  -  |
**422** | Server was able to read the request but the instructions are not correct |  -  |
**503** | Service is unavailable |  -  |
**0** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azure_service_api_keypairs_get**
> list[AzureKeypair] azure_service_api_keypairs_get(subscription_id, availability_zone=availability_zone)

Lists keypairs

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
api_instance = fcsm_eos_api_client.AzureApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | ID of subscription
availability_zone = 'default' # str | Availibility zone to filter by (optional) (default to 'default')

try:
    # Lists keypairs
    api_response = api_instance.azure_service_api_keypairs_get(subscription_id, availability_zone=availability_zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureApi->azure_service_api_keypairs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| ID of subscription | 
 **availability_zone** | **str**| Availibility zone to filter by | [optional] [default to &#39;default&#39;]

### Return type

[**list[AzureKeypair]**](AzureKeypair.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of keypairs |  -  |
**408** | There was a timeout when processing the request |  -  |
**422** | Server was able to read the request but the instructions are not correct |  -  |
**503** | Service is unavailable |  -  |
**0** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azure_service_api_network_subnets_get**
> list[AzureSubnet] azure_service_api_network_subnets_get(subscription_id, network_id, availability_zone=availability_zone)

Lists subnets for specified network and subscription

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
api_instance = fcsm_eos_api_client.AzureApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | ID of subscription
network_id = 'network_id_example' # str | ID of network
availability_zone = 'default' # str | Availibility zone to filter by (optional) (default to 'default')

try:
    # Lists subnets for specified network and subscription
    api_response = api_instance.azure_service_api_network_subnets_get(subscription_id, network_id, availability_zone=availability_zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureApi->azure_service_api_network_subnets_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| ID of subscription | 
 **network_id** | **str**| ID of network | 
 **availability_zone** | **str**| Availibility zone to filter by | [optional] [default to &#39;default&#39;]

### Return type

[**list[AzureSubnet]**](AzureSubnet.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of subnets for specified network |  -  |
**404** | Object was not found |  -  |
**408** | There was a timeout when processing the request |  -  |
**422** | Server was able to read the request but the instructions are not correct |  -  |
**503** | Service is unavailable |  -  |
**0** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azure_service_api_networks_get**
> list[AzureNetwork] azure_service_api_networks_get(subscription_id, availability_zone=availability_zone)

List networks for specified subscription

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
api_instance = fcsm_eos_api_client.AzureApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | ID of subscription
availability_zone = 'default' # str | Availibility zone to filter by (optional) (default to 'default')

try:
    # List networks for specified subscription
    api_response = api_instance.azure_service_api_networks_get(subscription_id, availability_zone=availability_zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureApi->azure_service_api_networks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| ID of subscription | 
 **availability_zone** | **str**| Availibility zone to filter by | [optional] [default to &#39;default&#39;]

### Return type

[**list[AzureNetwork]**](AzureNetwork.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of networks |  -  |
**408** | There was a timeout when processing the request |  -  |
**422** | Server was able to read the request but the instructions are not correct |  -  |
**503** | Service is unavailable |  -  |
**0** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azure_service_api_private_image_get**
> azure_service_api_private_image_get(subscription_id, image_id)

Gets a single private image by id

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
api_instance = fcsm_eos_api_client.AzureApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | ID of subscription
image_id = 'image_id_example' # str | Image id

try:
    # Gets a single private image by id
    api_instance.azure_service_api_private_image_get(subscription_id, image_id)
except ApiException as e:
    print("Exception when calling AzureApi->azure_service_api_private_image_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| ID of subscription | 
 **image_id** | **str**| Image id | 

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
**404** | Object was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azure_service_api_private_images_get**
> list[AzurePublicPrivateImage] azure_service_api_private_images_get(subscription_id, name=name)

Lists private images for specified subscription

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
api_instance = fcsm_eos_api_client.AzureApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | ID of subscription
name = 'name_example' # str | Full/partial name of an image to look for (optional)

try:
    # Lists private images for specified subscription
    api_response = api_instance.azure_service_api_private_images_get(subscription_id, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureApi->azure_service_api_private_images_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| ID of subscription | 
 **name** | **str**| Full/partial name of an image to look for | [optional] 

### Return type

[**list[AzurePublicPrivateImage]**](AzurePublicPrivateImage.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Since there are no private images in Azure returned list is always empty. |  -  |
**0** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azure_service_api_public_image_get**
> AzurePublicPrivateImage azure_service_api_public_image_get(subscription_id, image_id)

Gets a single public image by id

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
api_instance = fcsm_eos_api_client.AzureApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | ID of subscription
image_id = 'image_id_example' # str | Image id

try:
    # Gets a single public image by id
    api_response = api_instance.azure_service_api_public_image_get(subscription_id, image_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureApi->azure_service_api_public_image_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| ID of subscription | 
 **image_id** | **str**| Image id | 

### Return type

[**AzurePublicPrivateImage**](AzurePublicPrivateImage.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Single public image |  -  |
**404** | Object was not found |  -  |
**408** | There was a timeout when processing the request |  -  |
**422** | Server was able to read the request but the instructions are not correct |  -  |
**503** | Service is unavailable |  -  |
**0** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azure_service_api_public_images_get**
> list[AzurePublicPrivateImage] azure_service_api_public_images_get(subscription_id, name=name)

Lists all public images for specified subscription

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
api_instance = fcsm_eos_api_client.AzureApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | ID of subscription
name = 'name_example' # str | Full/partial name of an image to look for (optional)

try:
    # Lists all public images for specified subscription
    api_response = api_instance.azure_service_api_public_images_get(subscription_id, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureApi->azure_service_api_public_images_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| ID of subscription | 
 **name** | **str**| Full/partial name of an image to look for | [optional] 

### Return type

[**list[AzurePublicPrivateImage]**](AzurePublicPrivateImage.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of public images |  -  |
**0** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azure_service_api_regions_get**
> list[AzureRegion] azure_service_api_regions_get(subscription_id=subscription_id)

Lists regions

If subscriptionId is not passed as query parameters endpoint returns list of regions not scoped to any subscription. Otherwise it returns regions for specified subscription. 

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
api_instance = fcsm_eos_api_client.AzureApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Optional ID of subscription (optional)

try:
    # Lists regions
    api_response = api_instance.azure_service_api_regions_get(subscription_id=subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureApi->azure_service_api_regions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| Optional ID of subscription | [optional] 

### Return type

[**list[AzureRegion]**](AzureRegion.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of regions |  -  |
**0** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azure_service_api_resource_groups_get**
> list[AzureResourceGroup] azure_service_api_resource_groups_get(subscription_id)

Lists resource groups

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
api_instance = fcsm_eos_api_client.AzureApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | ID of subscription

try:
    # Lists resource groups
    api_response = api_instance.azure_service_api_resource_groups_get(subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureApi->azure_service_api_resource_groups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| ID of subscription | 

### Return type

[**list[AzureResourceGroup]**](AzureResourceGroup.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of resource groups |  -  |
**408** | There was a timeout when processing the request |  -  |
**0** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azure_service_api_resource_groups_post**
> AzureResourceGroup azure_service_api_resource_groups_post(subscription_id, azure_create_resource_group)

Creates new resource group

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
api_instance = fcsm_eos_api_client.AzureApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | ID of subscription
azure_create_resource_group = fcsm_eos_api_client.AzureCreateResourceGroup() # AzureCreateResourceGroup | 

try:
    # Creates new resource group
    api_response = api_instance.azure_service_api_resource_groups_post(subscription_id, azure_create_resource_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureApi->azure_service_api_resource_groups_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| ID of subscription | 
 **azure_create_resource_group** | [**AzureCreateResourceGroup**](AzureCreateResourceGroup.md)|  | 

### Return type

[**AzureResourceGroup**](AzureResourceGroup.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New resource group |  -  |
**400** | Bad request |  -  |
**408** | There was a timeout when processing the request |  -  |
**422** | Server was able to read the request but the instructions are not correct |  -  |
**503** | Service is unavailable |  -  |
**0** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azure_service_api_security_groups_get**
> list[AzureSecurityGroup] azure_service_api_security_groups_get(subscription_id, vm_id=vm_id)

Lists security groups for specified subscription

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
api_instance = fcsm_eos_api_client.AzureApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | ID of subscription
vm_id = 'vm_id_example' # str | Vm id to filter by (optional)

try:
    # Lists security groups for specified subscription
    api_response = api_instance.azure_service_api_security_groups_get(subscription_id, vm_id=vm_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureApi->azure_service_api_security_groups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| ID of subscription | 
 **vm_id** | **str**| Vm id to filter by | [optional] 

### Return type

[**list[AzureSecurityGroup]**](AzureSecurityGroup.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of security groups |  -  |
**408** | There was a timeout when processing the request |  -  |
**422** | Server was able to read the request but the instructions are not correct |  -  |
**503** | Service is unavailable |  -  |
**0** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azure_service_api_snapshot_delete**
> azure_service_api_snapshot_delete(subscription_id, snapshot_id)

Delete snapshot

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
api_instance = fcsm_eos_api_client.AzureApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | ID of subscription
snapshot_id = 'snapshot_id_example' # str | snapshot ID

try:
    # Delete snapshot
    api_instance.azure_service_api_snapshot_delete(subscription_id, snapshot_id)
except ApiException as e:
    print("Exception when calling AzureApi->azure_service_api_snapshot_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| ID of subscription | 
 **snapshot_id** | **str**| snapshot ID | 

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
**204** | Snapshot deleted successfully |  -  |
**404** | Object was not found |  -  |
**408** | There was a timeout when processing the request |  -  |
**503** | Service is unavailable |  -  |
**0** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azure_service_api_snapshots_get**
> list[AzureSnapshot] azure_service_api_snapshots_get(subscription_id, vm_id=vm_id)

Get list of all snapshots

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
api_instance = fcsm_eos_api_client.AzureApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | ID of subscription
vm_id = 'vm_id_example' # str | Vm id to filter by (optional)

try:
    # Get list of all snapshots
    api_response = api_instance.azure_service_api_snapshots_get(subscription_id, vm_id=vm_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureApi->azure_service_api_snapshots_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| ID of subscription | 
 **vm_id** | **str**| Vm id to filter by | [optional] 

### Return type

[**list[AzureSnapshot]**](AzureSnapshot.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of Snapshots |  -  |
**408** | There was a timeout when processing the request |  -  |
**422** | Server was able to read the request but the instructions are not correct |  -  |
**503** | Service is unavailable |  -  |
**0** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azure_service_api_snapshots_post**
> AzureSnapshot azure_service_api_snapshots_post(subscription_id, azure_create_snapshot)

Create a new snapshot

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
api_instance = fcsm_eos_api_client.AzureApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | ID of subscription
azure_create_snapshot = fcsm_eos_api_client.AzureCreateSnapshot() # AzureCreateSnapshot | A create snapshot object

try:
    # Create a new snapshot
    api_response = api_instance.azure_service_api_snapshots_post(subscription_id, azure_create_snapshot)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureApi->azure_service_api_snapshots_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| ID of subscription | 
 **azure_create_snapshot** | [**AzureCreateSnapshot**](AzureCreateSnapshot.md)| A create snapshot object | 

### Return type

[**AzureSnapshot**](AzureSnapshot.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Snapshot created |  -  |
**400** | Bad request |  -  |
**408** | There was a timeout when processing the request |  -  |
**422** | Server was able to read the request but the instructions are not correct |  -  |
**503** | Service is unavailable |  -  |
**0** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azure_service_api_validate_subscription_post**
> azure_service_api_validate_subscription_post(azure_subscription)

Validate subscription credentials

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
api_instance = fcsm_eos_api_client.AzureApi(fcsm_eos_api_client.ApiClient(configuration))
azure_subscription = fcsm_eos_api_client.AzureSubscription() # AzureSubscription | 

try:
    # Validate subscription credentials
    api_instance.azure_service_api_validate_subscription_post(azure_subscription)
except ApiException as e:
    print("Exception when calling AzureApi->azure_service_api_validate_subscription_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **azure_subscription** | [**AzureSubscription**](AzureSubscription.md)|  | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Properly validated subscription |  -  |
**400** | Bad request |  -  |
**404** | Object was not found |  -  |
**408** | There was a timeout when processing the request |  -  |
**422** | Server was able to read the request but the instructions are not correct |  -  |
**503** | Service is unavailable |  -  |
**0** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azure_service_api_vm_command_put**
> azure_service_api_vm_command_put(subscription_id, vm_id, action)

Executes power action on a VM

Executes power action on a VM. Only specified VMPowerAction are allowed.

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
api_instance = fcsm_eos_api_client.AzureApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | ID of subscription
vm_id = 'vm_id_example' # str | ID of VM
action = fcsm_eos_api_client.AzureVMPowerAction() # AzureVMPowerAction | Commands for the VM

try:
    # Executes power action on a VM
    api_instance.azure_service_api_vm_command_put(subscription_id, vm_id, action)
except ApiException as e:
    print("Exception when calling AzureApi->azure_service_api_vm_command_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| ID of subscription | 
 **vm_id** | **str**| ID of VM | 
 **action** | [**AzureVMPowerAction**](.md)| Commands for the VM | 

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
**202** | Volume was updated successfully |  -  |
**400** | Bad request |  -  |
**404** | Object was not found |  -  |
**408** | There was a timeout when processing the request |  -  |
**409** | Resource is not in desired state |  -  |
**422** | Server was able to read the request but the instructions are not correct |  -  |
**503** | Service is unavailable |  -  |
**0** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azure_service_api_vm_delete**
> azure_service_api_vm_delete(subscription_id, vm_id)

Deletes a single virtual machine by ID

Endpoint takes care of deleting the virtual machine from the platform. It also removes:  - OS volume - all network interfaces - management if VM was managed by management tool - workshift if VM had one - initial password if VM was provisioned with one 

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
api_instance = fcsm_eos_api_client.AzureApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | ID of subscription
vm_id = 'vm_id_example' # str | ID of VM

try:
    # Deletes a single virtual machine by ID
    api_instance.azure_service_api_vm_delete(subscription_id, vm_id)
except ApiException as e:
    print("Exception when calling AzureApi->azure_service_api_vm_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| ID of subscription | 
 **vm_id** | **str**| ID of VM | 

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
**204** | VM deleted |  -  |
**404** | Object was not found |  -  |
**408** | There was a timeout when processing the request |  -  |
**503** | Service is unavailable |  -  |
**0** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azure_service_api_vm_details_get**
> list[AzureVmDetails] azure_service_api_vm_details_get(subscription_id, vm_id)

Gets specified virtual machine details

If specified virtual machine is provision with enabled management details will contain information gathered by management tool. Aither way it will contains basic information 

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
api_instance = fcsm_eos_api_client.AzureApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | ID of subscription
vm_id = 'vm_id_example' # str | ID of VM

try:
    # Gets specified virtual machine details
    api_response = api_instance.azure_service_api_vm_details_get(subscription_id, vm_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureApi->azure_service_api_vm_details_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| ID of subscription | 
 **vm_id** | **str**| ID of VM | 

### Return type

[**list[AzureVmDetails]**](AzureVmDetails.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Virtual machine details |  -  |
**400** | Bad request |  -  |
**404** | Object was not found |  -  |
**408** | There was a timeout when processing the request |  -  |
**409** | Resource is not in desired state |  -  |
**422** | Server was able to read the request but the instructions are not correct |  -  |
**503** | Service is unavailable |  -  |
**0** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azure_service_api_vm_floating_ip_delete**
> azure_service_api_vm_floating_ip_delete(subscription_id, vm_id)

Unassigns floating public IP from specified VM

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
api_instance = fcsm_eos_api_client.AzureApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | ID of subscription
vm_id = 'vm_id_example' # str | ID of VM

try:
    # Unassigns floating public IP from specified VM
    api_instance.azure_service_api_vm_floating_ip_delete(subscription_id, vm_id)
except ApiException as e:
    print("Exception when calling AzureApi->azure_service_api_vm_floating_ip_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| ID of subscription | 
 **vm_id** | **str**| ID of VM | 

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
**204** | Unassigned floating IP from VM |  -  |
**404** | Object was not found |  -  |
**408** | There was a timeout when processing the request |  -  |
**422** | Server was able to read the request but the instructions are not correct |  -  |
**503** | Service is unavailable |  -  |
**0** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azure_service_api_vm_floating_ip_put**
> AzureVmFloatingIp azure_service_api_vm_floating_ip_put(subscription_id, vm_id)

Assigns a floating public IP v4 to specified VM

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
api_instance = fcsm_eos_api_client.AzureApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | ID of subscription
vm_id = 'vm_id_example' # str | ID of VM

try:
    # Assigns a floating public IP v4 to specified VM
    api_response = api_instance.azure_service_api_vm_floating_ip_put(subscription_id, vm_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureApi->azure_service_api_vm_floating_ip_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| ID of subscription | 
 **vm_id** | **str**| ID of VM | 

### Return type

[**AzureVmFloatingIp**](AzureVmFloatingIp.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Assigned floating IP to a VM |  -  |
**404** | Object was not found |  -  |
**408** | There was a timeout when processing the request |  -  |
**422** | Server was able to read the request but the instructions are not correct |  -  |
**503** | Service is unavailable |  -  |
**0** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azure_service_api_vm_get**
> AzureVMExtended azure_service_api_vm_get(subscription_id, vm_id)

Gets a single virtual machine by ID

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
api_instance = fcsm_eos_api_client.AzureApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | ID of subscription
vm_id = 'vm_id_example' # str | ID of VM

try:
    # Gets a single virtual machine by ID
    api_response = api_instance.azure_service_api_vm_get(subscription_id, vm_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureApi->azure_service_api_vm_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| ID of subscription | 
 **vm_id** | **str**| ID of VM | 

### Return type

[**AzureVMExtended**](AzureVMExtended.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Single virtual machine identified by ID |  -  |
**404** | Object was not found |  -  |
**408** | There was a timeout when processing the request |  -  |
**422** | Server was able to read the request but the instructions are not correct |  -  |
**503** | Service is unavailable |  -  |
**0** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azure_service_api_vm_management_get**
> AzureManagementStatus azure_service_api_vm_management_get(subscription_id, vm_id)

Gets specified virtual machine management status

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
api_instance = fcsm_eos_api_client.AzureApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | ID of subscription
vm_id = 'vm_id_example' # str | ID of VM

try:
    # Gets specified virtual machine management status
    api_response = api_instance.azure_service_api_vm_management_get(subscription_id, vm_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureApi->azure_service_api_vm_management_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| ID of subscription | 
 **vm_id** | **str**| ID of VM | 

### Return type

[**AzureManagementStatus**](AzureManagementStatus.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Single virtual machine identified by ID |  -  |
**408** | There was a timeout when processing the request |  -  |
**422** | Server was able to read the request but the instructions are not correct |  -  |
**503** | Service is unavailable |  -  |
**0** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azure_service_api_vm_password_get**
> AzureEncryptedPassword azure_service_api_vm_password_get(subscription_id, vm_id)

Gets specified virtual machine encrypted password

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
api_instance = fcsm_eos_api_client.AzureApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | ID of subscription
vm_id = 'vm_id_example' # str | ID of VM

try:
    # Gets specified virtual machine encrypted password
    api_response = api_instance.azure_service_api_vm_password_get(subscription_id, vm_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureApi->azure_service_api_vm_password_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| ID of subscription | 
 **vm_id** | **str**| ID of VM | 

### Return type

[**AzureEncryptedPassword**](AzureEncryptedPassword.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Virtual machine encrypted password |  -  |
**404** | Object was not found |  -  |
**408** | There was a timeout when processing the request |  -  |
**422** | Server was able to read the request but the instructions are not correct |  -  |
**503** | Service is unavailable |  -  |
**0** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azure_service_api_vm_patch**
> azure_service_api_vm_patch(subscription_id, vm_id, azure_vm_patch=azure_vm_patch)

Modifies specified virtual machine

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
api_instance = fcsm_eos_api_client.AzureApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | ID of subscription
vm_id = 'vm_id_example' # str | ID of VM
azure_vm_patch = fcsm_eos_api_client.AzureVMPatch() # AzureVMPatch | Virtual machine object to modify (optional)

try:
    # Modifies specified virtual machine
    api_instance.azure_service_api_vm_patch(subscription_id, vm_id, azure_vm_patch=azure_vm_patch)
except ApiException as e:
    print("Exception when calling AzureApi->azure_service_api_vm_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| ID of subscription | 
 **vm_id** | **str**| ID of VM | 
 **azure_vm_patch** | [**AzureVMPatch**](AzureVMPatch.md)| Virtual machine object to modify | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Modified virtual machine |  -  |
**404** | Object was not found |  -  |
**408** | There was a timeout when processing the request |  -  |
**422** | Server was able to read the request but the instructions are not correct |  -  |
**503** | Service is unavailable |  -  |
**0** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azure_service_api_vm_security_groups_delete**
> azure_service_api_vm_security_groups_delete(subscription_id, vm_id, security_group_id)

Unassigns specified security group from specified VM

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
api_instance = fcsm_eos_api_client.AzureApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | ID of subscription
vm_id = 'vm_id_example' # str | ID of VM
security_group_id = 'security_group_id_example' # str | Security group id

try:
    # Unassigns specified security group from specified VM
    api_instance.azure_service_api_vm_security_groups_delete(subscription_id, vm_id, security_group_id)
except ApiException as e:
    print("Exception when calling AzureApi->azure_service_api_vm_security_groups_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| ID of subscription | 
 **vm_id** | **str**| ID of VM | 
 **security_group_id** | **str**| Security group id | 

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
**200** | Security group is not assign to this VM |  -  |
**204** | Unassigned security group from a VM |  -  |
**404** | Object was not found |  -  |
**408** | There was a timeout when processing the request |  -  |
**422** | Server was able to read the request but the instructions are not correct |  -  |
**503** | Service is unavailable |  -  |
**0** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azure_service_api_vm_security_groups_put**
> azure_service_api_vm_security_groups_put(subscription_id, vm_id, security_group_id)

Assigns a new network security group and unassigns old one

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
api_instance = fcsm_eos_api_client.AzureApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | ID of subscription
vm_id = 'vm_id_example' # str | ID of VM
security_group_id = 'security_group_id_example' # str | Security group id

try:
    # Assigns a new network security group and unassigns old one
    api_instance.azure_service_api_vm_security_groups_put(subscription_id, vm_id, security_group_id)
except ApiException as e:
    print("Exception when calling AzureApi->azure_service_api_vm_security_groups_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| ID of subscription | 
 **vm_id** | **str**| ID of VM | 
 **security_group_id** | **str**| Security group id | 

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
**200** | Security group is already assigned to VM |  -  |
**201** | Assigned security group to a VM and unasigned old one |  -  |
**404** | Object was not found |  -  |
**408** | There was a timeout when processing the request |  -  |
**422** | Server was able to read the request but the instructions are not correct |  -  |
**503** | Service is unavailable |  -  |
**0** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azure_service_api_vm_tag_put**
> azure_service_api_vm_tag_put(subscription_id, vm_id, azure_tag_update)

Sets/unsets tag in virtual machine

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
api_instance = fcsm_eos_api_client.AzureApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | ID of subscription
vm_id = 'vm_id_example' # str | ID of VM
azure_tag_update = fcsm_eos_api_client.AzureTagUpdate() # AzureTagUpdate | 

try:
    # Sets/unsets tag in virtual machine
    api_instance.azure_service_api_vm_tag_put(subscription_id, vm_id, azure_tag_update)
except ApiException as e:
    print("Exception when calling AzureApi->azure_service_api_vm_tag_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| ID of subscription | 
 **vm_id** | **str**| ID of VM | 
 **azure_tag_update** | [**AzureTagUpdate**](AzureTagUpdate.md)|  | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Tag successfully set/unset in VM |  -  |
**404** | Object was not found |  -  |
**408** | There was a timeout when processing the request |  -  |
**422** | Server was able to read the request but the instructions are not correct |  -  |
**503** | Service is unavailable |  -  |
**0** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azure_service_api_vm_workshift_delete**
> azure_service_api_vm_workshift_delete(subscription_id, vm_id)

Delete VM Workshift

Delete VM Workshift

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
api_instance = fcsm_eos_api_client.AzureApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | ID of subscription
vm_id = 'vm_id_example' # str | ID of VM

try:
    # Delete VM Workshift
    api_instance.azure_service_api_vm_workshift_delete(subscription_id, vm_id)
except ApiException as e:
    print("Exception when calling AzureApi->azure_service_api_vm_workshift_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| ID of subscription | 
 **vm_id** | **str**| ID of VM | 

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
**204** | Workshift deleted |  -  |
**400** | Bad request |  -  |
**404** | Object was not found |  -  |
**0** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azure_service_api_vm_workshift_post**
> AzureWorkshift azure_service_api_vm_workshift_post(subscription_id, vm_id, azure_workshift)

Add a workshift to the VM

Create a VM Workshift

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
api_instance = fcsm_eos_api_client.AzureApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | ID of subscription
vm_id = 'vm_id_example' # str | ID of VM
azure_workshift = fcsm_eos_api_client.AzureWorkshift() # AzureWorkshift | Workshift object

try:
    # Add a workshift to the VM
    api_response = api_instance.azure_service_api_vm_workshift_post(subscription_id, vm_id, azure_workshift)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureApi->azure_service_api_vm_workshift_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| ID of subscription | 
 **vm_id** | **str**| ID of VM | 
 **azure_workshift** | [**AzureWorkshift**](AzureWorkshift.md)| Workshift object | 

### Return type

[**AzureWorkshift**](AzureWorkshift.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Workshift created successfully |  -  |
**400** | Bad request |  -  |
**404** | Object was not found |  -  |
**0** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azure_service_api_vm_workshift_put**
> AzureWorkshift azure_service_api_vm_workshift_put(subscription_id, vm_id, azure_workshift)

Update VM Workshift

Update a VM Workshift

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
api_instance = fcsm_eos_api_client.AzureApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | ID of subscription
vm_id = 'vm_id_example' # str | ID of VM
azure_workshift = fcsm_eos_api_client.AzureWorkshift() # AzureWorkshift | Workshift object

try:
    # Update VM Workshift
    api_response = api_instance.azure_service_api_vm_workshift_put(subscription_id, vm_id, azure_workshift)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureApi->azure_service_api_vm_workshift_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| ID of subscription | 
 **vm_id** | **str**| ID of VM | 
 **azure_workshift** | [**AzureWorkshift**](AzureWorkshift.md)| Workshift object | 

### Return type

[**AzureWorkshift**](AzureWorkshift.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Workshift created successfully |  -  |
**400** | Bad request |  -  |
**404** | Object was not found |  -  |
**0** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azure_service_api_vms_get**
> list[AzureVMSimple] azure_service_api_vms_get(subscription_id, availability_set_id=availability_set_id, availability_zone_id=availability_zone_id)

Lists virtual machines for specified subscription

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
api_instance = fcsm_eos_api_client.AzureApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | ID of subscription
availability_set_id = 'availability_set_id_example' # str | Availability Set ID (optional)
availability_zone_id = 'default' # str | Availibility zone id to filter by (optional) (default to 'default')

try:
    # Lists virtual machines for specified subscription
    api_response = api_instance.azure_service_api_vms_get(subscription_id, availability_set_id=availability_set_id, availability_zone_id=availability_zone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureApi->azure_service_api_vms_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| ID of subscription | 
 **availability_set_id** | **str**| Availability Set ID | [optional] 
 **availability_zone_id** | **str**| Availibility zone id to filter by | [optional] [default to &#39;default&#39;]

### Return type

[**list[AzureVMSimple]**](AzureVMSimple.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of virtual machines |  -  |
**404** | Object was not found |  -  |
**408** | There was a timeout when processing the request |  -  |
**422** | Server was able to read the request but the instructions are not correct |  -  |
**503** | Service is unavailable |  -  |
**0** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azure_service_api_vms_post**
> AzureVMExtended azure_service_api_vms_post(subscription_id, azure_vm_create_data=azure_vm_create_data)

Provisions virtual machine according to specified parameters

May provision managed or unmanaged virtual machine in accordance to the `managementToolId` property. If such is set and points to valid `management tool`, virtual machine will have aformentioned tool deployed and it will be possible to install the application on it. 

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
api_instance = fcsm_eos_api_client.AzureApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | ID of subscription
azure_vm_create_data = fcsm_eos_api_client.AzureVMCreateData() # AzureVMCreateData | Parameters for the new virtual machine (optional)

try:
    # Provisions virtual machine according to specified parameters
    api_response = api_instance.azure_service_api_vms_post(subscription_id, azure_vm_create_data=azure_vm_create_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureApi->azure_service_api_vms_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| ID of subscription | 
 **azure_vm_create_data** | [**AzureVMCreateData**](AzureVMCreateData.md)| Parameters for the new virtual machine | [optional] 

### Return type

[**AzureVMExtended**](AzureVMExtended.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Single virtual machine identified by ID |  -  |
**400** | Bad request |  -  |
**404** | Object was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azure_service_api_volume_attachment_delete**
> azure_service_api_volume_attachment_delete(subscription_id, volume_id, vm_id)

Dettaches volume

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
api_instance = fcsm_eos_api_client.AzureApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | ID of subscription
volume_id = 'volume_id_example' # str | ID of Volume
vm_id = 'vm_id_example' # str | ID of VM in query string

try:
    # Dettaches volume
    api_instance.azure_service_api_volume_attachment_delete(subscription_id, volume_id, vm_id)
except ApiException as e:
    print("Exception when calling AzureApi->azure_service_api_volume_attachment_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| ID of subscription | 
 **volume_id** | **str**| ID of Volume | 
 **vm_id** | **str**| ID of VM in query string | 

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
**204** | Volume detached from the VM successfully |  -  |
**400** | Bad request |  -  |
**404** | Object was not found |  -  |
**408** | There was a timeout when processing the request |  -  |
**422** | Server was able to read the request but the instructions are not correct |  -  |
**503** | Service is unavailable |  -  |
**0** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azure_service_api_volume_attachment_put**
> AzureVolumeAttachment azure_service_api_volume_attachment_put(subscription_id, volume_id, vm_id)

Attaches volume

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
api_instance = fcsm_eos_api_client.AzureApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | ID of subscription
volume_id = 'volume_id_example' # str | ID of Volume
vm_id = 'vm_id_example' # str | ID of VM in query string

try:
    # Attaches volume
    api_response = api_instance.azure_service_api_volume_attachment_put(subscription_id, volume_id, vm_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureApi->azure_service_api_volume_attachment_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| ID of subscription | 
 **volume_id** | **str**| ID of Volume | 
 **vm_id** | **str**| ID of VM in query string | 

### Return type

[**AzureVolumeAttachment**](AzureVolumeAttachment.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Volume attached to the VM successfully |  -  |
**400** | Bad request |  -  |
**404** | Object was not found |  -  |
**408** | There was a timeout when processing the request |  -  |
**422** | Server was able to read the request but the instructions are not correct |  -  |
**503** | Service is unavailable |  -  |
**0** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azure_service_api_volume_delete**
> azure_service_api_volume_delete(subscription_id, volume_id)

Removes volume

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
api_instance = fcsm_eos_api_client.AzureApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | ID of subscription
volume_id = 'volume_id_example' # str | ID of Volume

try:
    # Removes volume
    api_instance.azure_service_api_volume_delete(subscription_id, volume_id)
except ApiException as e:
    print("Exception when calling AzureApi->azure_service_api_volume_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| ID of subscription | 
 **volume_id** | **str**| ID of Volume | 

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
**204** | Volume was removed successfully |  -  |
**400** | Bad request |  -  |
**404** | Object was not found |  -  |
**408** | There was a timeout when processing the request |  -  |
**409** | Resource is not in desired state |  -  |
**422** | Server was able to read the request but the instructions are not correct |  -  |
**503** | Service is unavailable |  -  |
**0** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azure_service_api_volume_get**
> AzureVolume azure_service_api_volume_get(subscription_id, volume_id)

Gets a single volume by ID

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
api_instance = fcsm_eos_api_client.AzureApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | ID of subscription
volume_id = 'volume_id_example' # str | ID of Volume

try:
    # Gets a single volume by ID
    api_response = api_instance.azure_service_api_volume_get(subscription_id, volume_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureApi->azure_service_api_volume_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| ID of subscription | 
 **volume_id** | **str**| ID of Volume | 

### Return type

[**AzureVolume**](AzureVolume.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Single volume identified by ID |  -  |
**404** | Object was not found |  -  |
**408** | There was a timeout when processing the request |  -  |
**422** | Server was able to read the request but the instructions are not correct |  -  |
**503** | Service is unavailable |  -  |
**0** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azure_service_api_volume_patch**
> azure_service_api_volume_patch(subscription_id, volume_id, azure_patch_volume)

Modify volume properties

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
api_instance = fcsm_eos_api_client.AzureApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | ID of subscription
volume_id = 'volume_id_example' # str | ID of Volume
azure_patch_volume = fcsm_eos_api_client.AzurePatchVolume() # AzurePatchVolume | 

try:
    # Modify volume properties
    api_instance.azure_service_api_volume_patch(subscription_id, volume_id, azure_patch_volume)
except ApiException as e:
    print("Exception when calling AzureApi->azure_service_api_volume_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| ID of subscription | 
 **volume_id** | **str**| ID of Volume | 
 **azure_patch_volume** | [**AzurePatchVolume**](AzurePatchVolume.md)|  | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Volume was updated successfully |  -  |
**400** | Bad request |  -  |
**404** | Object was not found |  -  |
**408** | There was a timeout when processing the request |  -  |
**409** | Resource is not in desired state |  -  |
**422** | Server was able to read the request but the instructions are not correct |  -  |
**503** | Service is unavailable |  -  |
**0** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azure_service_api_volume_types_get**
> list[AzureVolumeType] azure_service_api_volume_types_get(subscription_id, is_os_compatible=is_os_compatible, availability_zone_id=availability_zone_id)

Lists volume types

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
api_instance = fcsm_eos_api_client.AzureApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | ID of subscription
is_os_compatible = True # bool | Filter volumes by OS compatibility (optional)
availability_zone_id = 'default' # str | Availibility zone id to filter by (optional) (default to 'default')

try:
    # Lists volume types
    api_response = api_instance.azure_service_api_volume_types_get(subscription_id, is_os_compatible=is_os_compatible, availability_zone_id=availability_zone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureApi->azure_service_api_volume_types_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| ID of subscription | 
 **is_os_compatible** | **bool**| Filter volumes by OS compatibility | [optional] 
 **availability_zone_id** | **str**| Availibility zone id to filter by | [optional] [default to &#39;default&#39;]

### Return type

[**list[AzureVolumeType]**](AzureVolumeType.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of volume types |  -  |
**408** | There was a timeout when processing the request |  -  |
**422** | Server was able to read the request but the instructions are not correct |  -  |
**503** | Service is unavailable |  -  |
**0** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azure_service_api_volumes_get**
> list[AzureVolume] azure_service_api_volumes_get(subscription_id, status=status, is_os_disk=is_os_disk, availability_zone=availability_zone)

Lists volumes for specified subscription

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
api_instance = fcsm_eos_api_client.AzureApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | ID of subscription
status = fcsm_eos_api_client.AzureVolumeStatus() # AzureVolumeStatus | Volume status to filter by (optional)
is_os_disk = True # bool | Filter volumes by IsOsDisk value (optional)
availability_zone = 'default' # str | Availibility zone to filter by (optional) (default to 'default')

try:
    # Lists volumes for specified subscription
    api_response = api_instance.azure_service_api_volumes_get(subscription_id, status=status, is_os_disk=is_os_disk, availability_zone=availability_zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureApi->azure_service_api_volumes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| ID of subscription | 
 **status** | [**AzureVolumeStatus**](.md)| Volume status to filter by | [optional] 
 **is_os_disk** | **bool**| Filter volumes by IsOsDisk value | [optional] 
 **availability_zone** | **str**| Availibility zone to filter by | [optional] [default to &#39;default&#39;]

### Return type

[**list[AzureVolume]**](AzureVolume.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of volumes |  -  |
**408** | There was a timeout when processing the request |  -  |
**422** | Server was able to read the request but the instructions are not correct |  -  |
**503** | Service is unavailable |  -  |
**0** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azure_service_api_volumes_post**
> AzureVolume azure_service_api_volumes_post(subscription_id, azure_create_volume)

Creates new volume

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
api_instance = fcsm_eos_api_client.AzureApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | ID of subscription
azure_create_volume = fcsm_eos_api_client.AzureCreateVolume() # AzureCreateVolume | 

try:
    # Creates new volume
    api_response = api_instance.azure_service_api_volumes_post(subscription_id, azure_create_volume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureApi->azure_service_api_volumes_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| ID of subscription | 
 **azure_create_volume** | [**AzureCreateVolume**](AzureCreateVolume.md)|  | 

### Return type

[**AzureVolume**](AzureVolume.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New volume |  -  |
**408** | There was a timeout when processing the request |  -  |
**404** | Object was not found |  -  |
**422** | Server was able to read the request but the instructions are not correct |  -  |
**503** | Service is unavailable |  -  |
**0** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

