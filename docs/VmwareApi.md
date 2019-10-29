# fcsm_eos_api_client.VmwareApi

All URIs are relative to *https://emeia-eos.fcsm.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vmware_service_resources_availability_zones_get**](VmwareApi.md#vmware_service_resources_availability_zones_get) | **GET** /api/v1/vmware/compute/availabilityZones | List availability zones
[**vmware_service_resources_flavor_get**](VmwareApi.md#vmware_service_resources_flavor_get) | **GET** /api/v1/vmware/compute/flavors/{flavorId} | Get flavor by id
[**vmware_service_resources_flavors_get**](VmwareApi.md#vmware_service_resources_flavors_get) | **GET** /api/v1/vmware/compute/flavors | List flavors
[**vmware_service_resources_image_get**](VmwareApi.md#vmware_service_resources_image_get) | **GET** /api/v1/vmware/compute/images/{imageId} | Get image by id
[**vmware_service_resources_image_get_private**](VmwareApi.md#vmware_service_resources_image_get_private) | **GET** /api/v1/vmware/compute/privateImages/{imageId} | Get private image by id
[**vmware_service_resources_image_get_public**](VmwareApi.md#vmware_service_resources_image_get_public) | **GET** /api/v1/vmware/compute/publicImages/{imageId} | Get public image by id
[**vmware_service_resources_images_get**](VmwareApi.md#vmware_service_resources_images_get) | **GET** /api/v1/vmware/compute/images | Get images
[**vmware_service_resources_images_get_private**](VmwareApi.md#vmware_service_resources_images_get_private) | **GET** /api/v1/vmware/compute/privateImages | Get private images
[**vmware_service_resources_images_get_public**](VmwareApi.md#vmware_service_resources_images_get_public) | **GET** /api/v1/vmware/compute/publicImages | Get public images
[**vmware_service_resources_interfaces_get**](VmwareApi.md#vmware_service_resources_interfaces_get) | **GET** /api/v1/vmware/compute/interfaces | List network interfaces
[**vmware_service_resources_keypair_delete**](VmwareApi.md#vmware_service_resources_keypair_delete) | **DELETE** /api/v1/vmware/compute/keypairs/{keypairId} | Delete a keypair
[**vmware_service_resources_keypairs_get**](VmwareApi.md#vmware_service_resources_keypairs_get) | **GET** /api/v1/vmware/compute/keypairs | List keypairs
[**vmware_service_resources_keypairs_post**](VmwareApi.md#vmware_service_resources_keypairs_post) | **POST** /api/v1/vmware/compute/keypairs/generate | Create a new keypair
[**vmware_service_resources_keypairs_upload**](VmwareApi.md#vmware_service_resources_keypairs_upload) | **POST** /api/v1/vmware/compute/keypairs/import | Import a keypair
[**vmware_service_resources_management_get**](VmwareApi.md#vmware_service_resources_management_get) | **GET** /api/v1/vmware/compute/vms/{vmId}/management | Get VM management status
[**vmware_service_resources_networks_get**](VmwareApi.md#vmware_service_resources_networks_get) | **GET** /api/v1/vmware/compute/networks | List networks
[**vmware_service_resources_regions_get**](VmwareApi.md#vmware_service_resources_regions_get) | **GET** /api/v1/vmware/compute/regions | List regions
[**vmware_service_resources_security_groups_get**](VmwareApi.md#vmware_service_resources_security_groups_get) | **GET** /api/v1/vmware/compute/securityGroups | List security groups
[**vmware_service_resources_snapshot_delete**](VmwareApi.md#vmware_service_resources_snapshot_delete) | **DELETE** /api/v1/vmware/compute/snapshots/{snapshotId} | Delete snapshot
[**vmware_service_resources_snapshots_get**](VmwareApi.md#vmware_service_resources_snapshots_get) | **GET** /api/v1/vmware/compute/snapshots | List snapshots
[**vmware_service_resources_snapshots_post**](VmwareApi.md#vmware_service_resources_snapshots_post) | **POST** /api/v1/vmware/compute/snapshots | Create a new snapshot
[**vmware_service_resources_subnets_get**](VmwareApi.md#vmware_service_resources_subnets_get) | **GET** /api/v1/vmware/compute/networks/{networkId}/subnets | List network subnets
[**vmware_service_resources_validate_subscription_post**](VmwareApi.md#vmware_service_resources_validate_subscription_post) | **POST** /api/v1/vmware/compute/validateSubscription | Validate subscription
[**vmware_service_resources_vm_command_put**](VmwareApi.md#vmware_service_resources_vm_command_put) | **PUT** /api/v1/vmware/compute/vms/{vmId}/command/{action} | Execute a power action on a VM
[**vmware_service_resources_vm_delete**](VmwareApi.md#vmware_service_resources_vm_delete) | **DELETE** /api/v1/vmware/compute/vms/{vmId} | Delete a VM
[**vmware_service_resources_vm_details_get**](VmwareApi.md#vmware_service_resources_vm_details_get) | **GET** /api/v1/vmware/compute/vms/{vmId}/details | Get VM details
[**vmware_service_resources_vm_get**](VmwareApi.md#vmware_service_resources_vm_get) | **GET** /api/v1/vmware/compute/vms/{vmId} | Get VM by id
[**vmware_service_resources_vm_password_get**](VmwareApi.md#vmware_service_resources_vm_password_get) | **GET** /api/v1/vmware/compute/vms/{vmId}/password | Get the VM password
[**vmware_service_resources_vm_patch**](VmwareApi.md#vmware_service_resources_vm_patch) | **PATCH** /api/v1/vmware/compute/vms/{vmId} | Update VM
[**vmware_service_resources_vm_tag_put**](VmwareApi.md#vmware_service_resources_vm_tag_put) | **PUT** /api/v1/vmware/compute/vms/{vmId}/setTag | Tag VM
[**vmware_service_resources_vm_workshift_delete**](VmwareApi.md#vmware_service_resources_vm_workshift_delete) | **DELETE** /api/v1/vmware/compute/vms/{vmId}/workshift | Delete the VM Workshift
[**vmware_service_resources_vm_workshift_put**](VmwareApi.md#vmware_service_resources_vm_workshift_put) | **PUT** /api/v1/vmware/compute/vms/{vmId}/workshift | Update the VM workshift
[**vmware_service_resources_vm_workshifts_post**](VmwareApi.md#vmware_service_resources_vm_workshifts_post) | **POST** /api/v1/vmware/compute/vms/{vmId}/workshift | Add a workshift to the VM
[**vmware_service_resources_vms_get**](VmwareApi.md#vmware_service_resources_vms_get) | **GET** /api/v1/vmware/compute/vms | List VMs
[**vmware_service_resources_vms_post**](VmwareApi.md#vmware_service_resources_vms_post) | **POST** /api/v1/vmware/compute/vms | Create a VM
[**vmware_service_resources_volume_attachment_delete**](VmwareApi.md#vmware_service_resources_volume_attachment_delete) | **DELETE** /api/v1/vmware/compute/volumes/{volume_id}/detach | Dettaches and deletes a volume
[**vmware_service_resources_volume_patch**](VmwareApi.md#vmware_service_resources_volume_patch) | **PATCH** /api/v1/vmware/compute/volumes/{volume_id} | Update a volume
[**vmware_service_resources_volume_types_get**](VmwareApi.md#vmware_service_resources_volume_types_get) | **GET** /api/v1/vmware/compute/volumeTypes | List volume types
[**vmware_service_resources_volumes_get**](VmwareApi.md#vmware_service_resources_volumes_get) | **GET** /api/v1/vmware/compute/volumes | List volumes
[**vmware_service_resources_volumes_post**](VmwareApi.md#vmware_service_resources_volumes_post) | **POST** /api/v1/vmware/compute/volumes | Create a new volume


# **vmware_service_resources_availability_zones_get**
> list[VmwareAvailabilityZone] vmware_service_resources_availability_zones_get(subscription_id)

List availability zones

List all Availability Zones

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
api_instance = fcsm_eos_api_client.VmwareApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of subscription

try:
    # List availability zones
    api_response = api_instance.vmware_service_resources_availability_zones_get(subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VmwareApi->vmware_service_resources_availability_zones_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Id of subscription | 

### Return type

[**list[VmwareAvailabilityZone]**](VmwareAvailabilityZone.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of availability zones |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vmware_service_resources_flavor_get**
> VmwareFlavor vmware_service_resources_flavor_get(subscription_id, flavor_id)

Get flavor by id

Get specific flavor by id

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
api_instance = fcsm_eos_api_client.VmwareApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of subscription
flavor_id = 'flavor_id_example' # str | Flavor id

try:
    # Get flavor by id
    api_response = api_instance.vmware_service_resources_flavor_get(subscription_id, flavor_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VmwareApi->vmware_service_resources_flavor_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Id of subscription | 
 **flavor_id** | **str**| Flavor id | 

### Return type

[**VmwareFlavor**](VmwareFlavor.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vmware_service_resources_flavors_get**
> list[VmwareFlavor] vmware_service_resources_flavors_get(subscription_id)

List flavors

Get the list of all flavors

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
api_instance = fcsm_eos_api_client.VmwareApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of subscription

try:
    # List flavors
    api_response = api_instance.vmware_service_resources_flavors_get(subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VmwareApi->vmware_service_resources_flavors_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Id of subscription | 

### Return type

[**list[VmwareFlavor]**](VmwareFlavor.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vmware_service_resources_image_get**
> VmwareImage vmware_service_resources_image_get(subscription_id, image_id)

Get image by id

Get specific images by id

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
api_instance = fcsm_eos_api_client.VmwareApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of subscription
image_id = 'image_id_example' # str | Image id

try:
    # Get image by id
    api_response = api_instance.vmware_service_resources_image_get(subscription_id, image_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VmwareApi->vmware_service_resources_image_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Id of subscription | 
 **image_id** | **str**| Image id | 

### Return type

[**VmwareImage**](VmwareImage.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vmware_service_resources_image_get_private**
> vmware_service_resources_image_get_private(subscription_id, image_id)

Get private image by id

Get specific private image by id

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
api_instance = fcsm_eos_api_client.VmwareApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of subscription
image_id = 'image_id_example' # str | Image id

try:
    # Get private image by id
    api_instance.vmware_service_resources_image_get_private(subscription_id, image_id)
except ApiException as e:
    print("Exception when calling VmwareApi->vmware_service_resources_image_get_private: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Id of subscription | 
 **image_id** | **str**| Image id | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Image does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vmware_service_resources_image_get_public**
> VmwareImage vmware_service_resources_image_get_public(subscription_id, image_id)

Get public image by id

Get specific public image by id

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
api_instance = fcsm_eos_api_client.VmwareApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of subscription
image_id = 'image_id_example' # str | Image id

try:
    # Get public image by id
    api_response = api_instance.vmware_service_resources_image_get_public(subscription_id, image_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VmwareApi->vmware_service_resources_image_get_public: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Id of subscription | 
 **image_id** | **str**| Image id | 

### Return type

[**VmwareImage**](VmwareImage.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Image does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vmware_service_resources_images_get**
> list[VmwarePublicPrivateImage] vmware_service_resources_images_get(subscription_id, name=name)

Get images

The endpoint is used only by the analytics service and should be deprecated in favor of whitelist/images.

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
api_instance = fcsm_eos_api_client.VmwareApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of subscription
name = 'name_example' # str | Name of the image to filter (optional)

try:
    # Get images
    api_response = api_instance.vmware_service_resources_images_get(subscription_id, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VmwareApi->vmware_service_resources_images_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Id of subscription | 
 **name** | **str**| Name of the image to filter | [optional] 

### Return type

[**list[VmwarePublicPrivateImage]**](VmwarePublicPrivateImage.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vmware_service_resources_images_get_private**
> list[VmwarePublicPrivateImage] vmware_service_resources_images_get_private(subscription_id, name=name, id=id)

Get private images

Get private images

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
api_instance = fcsm_eos_api_client.VmwareApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of subscription
name = 'name_example' # str | Name of the image to filter (optional)
id = 'id_example' # str | Image id to filter by (optional)

try:
    # Get private images
    api_response = api_instance.vmware_service_resources_images_get_private(subscription_id, name=name, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VmwareApi->vmware_service_resources_images_get_private: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Id of subscription | 
 **name** | **str**| Name of the image to filter | [optional] 
 **id** | **str**| Image id to filter by | [optional] 

### Return type

[**list[VmwarePublicPrivateImage]**](VmwarePublicPrivateImage.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Too many filtration params were specified. Choose either name or id. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vmware_service_resources_images_get_public**
> list[VmwarePublicPrivateImage] vmware_service_resources_images_get_public(subscription_id, name=name, id=id)

Get public images

Get public images

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
api_instance = fcsm_eos_api_client.VmwareApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of subscription
name = 'name_example' # str | Name of the image to filter (optional)
id = 'id_example' # str | Image id to filter by (optional)

try:
    # Get public images
    api_response = api_instance.vmware_service_resources_images_get_public(subscription_id, name=name, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VmwareApi->vmware_service_resources_images_get_public: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Id of subscription | 
 **name** | **str**| Name of the image to filter | [optional] 
 **id** | **str**| Image id to filter by | [optional] 

### Return type

[**list[VmwarePublicPrivateImage]**](VmwarePublicPrivateImage.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Too many filtration params were specified. Choose either name or id. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vmware_service_resources_interfaces_get**
> list[VmwareInterface] vmware_service_resources_interfaces_get(subscription_id, vm_id=vm_id)

List network interfaces

List of network interfaces

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
api_instance = fcsm_eos_api_client.VmwareApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of subscription
vm_id = 'vm_id_example' # str | Filter interfaces for VM id (optional)

try:
    # List network interfaces
    api_response = api_instance.vmware_service_resources_interfaces_get(subscription_id, vm_id=vm_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VmwareApi->vmware_service_resources_interfaces_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Id of subscription | 
 **vm_id** | **str**| Filter interfaces for VM id | [optional] 

### Return type

[**list[VmwareInterface]**](VmwareInterface.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vmware_service_resources_keypair_delete**
> vmware_service_resources_keypair_delete(subscription_id, keypair_id)

Delete a keypair

Delete a specific keypair

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
api_instance = fcsm_eos_api_client.VmwareApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of subscription
keypair_id = 'keypair_id_example' # str | Keypair id

try:
    # Delete a keypair
    api_instance.vmware_service_resources_keypair_delete(subscription_id, keypair_id)
except ApiException as e:
    print("Exception when calling VmwareApi->vmware_service_resources_keypair_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Id of subscription | 
 **keypair_id** | **str**| Keypair id | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Keypair deleted successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vmware_service_resources_keypairs_get**
> list[VmwareKeypair] vmware_service_resources_keypairs_get(subscription_id)

List keypairs

List all keypairs

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
api_instance = fcsm_eos_api_client.VmwareApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of subscription

try:
    # List keypairs
    api_response = api_instance.vmware_service_resources_keypairs_get(subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VmwareApi->vmware_service_resources_keypairs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Id of subscription | 

### Return type

[**list[VmwareKeypair]**](VmwareKeypair.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of keypairs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vmware_service_resources_keypairs_post**
> VmwareNewKeypair vmware_service_resources_keypairs_post(subscription_id, vmware_generate_keypair)

Create a new keypair

Create a new keypair

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
api_instance = fcsm_eos_api_client.VmwareApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of subscription
vmware_generate_keypair = fcsm_eos_api_client.VmwareGenerateKeypair() # VmwareGenerateKeypair | Keypair data

try:
    # Create a new keypair
    api_response = api_instance.vmware_service_resources_keypairs_post(subscription_id, vmware_generate_keypair)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VmwareApi->vmware_service_resources_keypairs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Id of subscription | 
 **vmware_generate_keypair** | [**VmwareGenerateKeypair**](VmwareGenerateKeypair.md)| Keypair data | 

### Return type

[**VmwareNewKeypair**](VmwareNewKeypair.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Keypair created successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vmware_service_resources_keypairs_upload**
> VmwareKeypair vmware_service_resources_keypairs_upload(subscription_id, vmware_import_keypair)

Import a keypair

Import a new public keypair

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
api_instance = fcsm_eos_api_client.VmwareApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of subscription
vmware_import_keypair = fcsm_eos_api_client.VmwareImportKeypair() # VmwareImportKeypair | Public keypair to import

try:
    # Import a keypair
    api_response = api_instance.vmware_service_resources_keypairs_upload(subscription_id, vmware_import_keypair)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VmwareApi->vmware_service_resources_keypairs_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Id of subscription | 
 **vmware_import_keypair** | [**VmwareImportKeypair**](VmwareImportKeypair.md)| Public keypair to import | 

### Return type

[**VmwareKeypair**](VmwareKeypair.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Keypair imported successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vmware_service_resources_management_get**
> VmwareManagement vmware_service_resources_management_get(subscription_id, vm_id)

Get VM management status

Check if management service for the VM is available

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
api_instance = fcsm_eos_api_client.VmwareApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of subscription
vm_id = 'vm_id_example' # str | Id of VM

try:
    # Get VM management status
    api_response = api_instance.vmware_service_resources_management_get(subscription_id, vm_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VmwareApi->vmware_service_resources_management_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Id of subscription | 
 **vm_id** | **str**| Id of VM | 

### Return type

[**VmwareManagement**](VmwareManagement.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | VM management status |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vmware_service_resources_networks_get**
> list[VmwareNetwork] vmware_service_resources_networks_get(subscription_id, availability_zone=availability_zone)

List networks

List all networks

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
api_instance = fcsm_eos_api_client.VmwareApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of subscription
availability_zone = 'availability_zone_example' # str | Availability zone to filter by (optional)

try:
    # List networks
    api_response = api_instance.vmware_service_resources_networks_get(subscription_id, availability_zone=availability_zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VmwareApi->vmware_service_resources_networks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Id of subscription | 
 **availability_zone** | **str**| Availability zone to filter by | [optional] 

### Return type

[**list[VmwareNetwork]**](VmwareNetwork.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of networks |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vmware_service_resources_regions_get**
> list[VmwareRegion] vmware_service_resources_regions_get()

List regions

List all regions

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
api_instance = fcsm_eos_api_client.VmwareApi(fcsm_eos_api_client.ApiClient(configuration))

try:
    # List regions
    api_response = api_instance.vmware_service_resources_regions_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VmwareApi->vmware_service_resources_regions_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[VmwareRegion]**](VmwareRegion.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of regions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vmware_service_resources_security_groups_get**
> list[object] vmware_service_resources_security_groups_get(subscription_id, vm_id=vm_id)

List security groups

List of security groups. The result is always an empty list. There are no security groups in VMWare.

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
api_instance = fcsm_eos_api_client.VmwareApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of subscription
vm_id = 'vm_id_example' # str | VM id (optional)

try:
    # List security groups
    api_response = api_instance.vmware_service_resources_security_groups_get(subscription_id, vm_id=vm_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VmwareApi->vmware_service_resources_security_groups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Id of subscription | 
 **vm_id** | **str**| VM id | [optional] 

### Return type

**list[object]**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Empty list. There are no security groups in VMWare. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vmware_service_resources_snapshot_delete**
> vmware_service_resources_snapshot_delete(subscription_id, snapshot_id)

Delete snapshot

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
api_instance = fcsm_eos_api_client.VmwareApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of subscription
snapshot_id = 'snapshot_id_example' # str | snapshot id

try:
    # Delete snapshot
    api_instance.vmware_service_resources_snapshot_delete(subscription_id, snapshot_id)
except ApiException as e:
    print("Exception when calling VmwareApi->vmware_service_resources_snapshot_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Id of subscription | 
 **snapshot_id** | **str**| snapshot id | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**501** | Not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vmware_service_resources_snapshots_get**
> vmware_service_resources_snapshots_get(subscription_id, vm_id=vm_id)

List snapshots

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
api_instance = fcsm_eos_api_client.VmwareApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of subscription
vm_id = 'vm_id_example' # str | Id of VM in query (optional)

try:
    # List snapshots
    api_instance.vmware_service_resources_snapshots_get(subscription_id, vm_id=vm_id)
except ApiException as e:
    print("Exception when calling VmwareApi->vmware_service_resources_snapshots_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Id of subscription | 
 **vm_id** | **str**| Id of VM in query | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**501** | Not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vmware_service_resources_snapshots_post**
> vmware_service_resources_snapshots_post(subscription_id, vmware_create_snapshot)

Create a new snapshot

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
api_instance = fcsm_eos_api_client.VmwareApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of subscription
vmware_create_snapshot = fcsm_eos_api_client.VmwareCreateSnapshot() # VmwareCreateSnapshot | A create snapshot object

try:
    # Create a new snapshot
    api_instance.vmware_service_resources_snapshots_post(subscription_id, vmware_create_snapshot)
except ApiException as e:
    print("Exception when calling VmwareApi->vmware_service_resources_snapshots_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Id of subscription | 
 **vmware_create_snapshot** | [**VmwareCreateSnapshot**](VmwareCreateSnapshot.md)| A create snapshot object | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**501** | Not implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vmware_service_resources_subnets_get**
> list[VmwareSubnet] vmware_service_resources_subnets_get(subscription_id, network_id, availability_zone=availability_zone)

List network subnets

List all subnets which belong to the given network

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
api_instance = fcsm_eos_api_client.VmwareApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of subscription
network_id = 'network_id_example' # str | Network id
availability_zone = 'availability_zone_example' # str | Availability zone to filter by (optional)

try:
    # List network subnets
    api_response = api_instance.vmware_service_resources_subnets_get(subscription_id, network_id, availability_zone=availability_zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VmwareApi->vmware_service_resources_subnets_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Id of subscription | 
 **network_id** | **str**| Network id | 
 **availability_zone** | **str**| Availability zone to filter by | [optional] 

### Return type

[**list[VmwareSubnet]**](VmwareSubnet.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of subnets |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vmware_service_resources_validate_subscription_post**
> vmware_service_resources_validate_subscription_post(vmware_subscription=vmware_subscription)

Validate subscription

Validate subscription before adding it

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
api_instance = fcsm_eos_api_client.VmwareApi(fcsm_eos_api_client.ApiClient(configuration))
vmware_subscription = fcsm_eos_api_client.VmwareSubscription() # VmwareSubscription | Validate subscription data (optional)

try:
    # Validate subscription
    api_instance.vmware_service_resources_validate_subscription_post(vmware_subscription=vmware_subscription)
except ApiException as e:
    print("Exception when calling VmwareApi->vmware_service_resources_validate_subscription_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vmware_subscription** | [**VmwareSubscription**](VmwareSubscription.md)| Validate subscription data | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Subscription successfully validated |  -  |
**400** | Invalid subscription |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vmware_service_resources_vm_command_put**
> vmware_service_resources_vm_command_put(subscription_id, vm_id, action)

Execute a power action on a VM

Execute action on a VM. Actions are start, poweroff, softReboot, hardReboot.

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
api_instance = fcsm_eos_api_client.VmwareApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of subscription
vm_id = 'vm_id_example' # str | Id of VM
action = fcsm_eos_api_client.VmwareAction() # VmwareAction | Power action to be invoked on the VM

try:
    # Execute a power action on a VM
    api_instance.vmware_service_resources_vm_command_put(subscription_id, vm_id, action)
except ApiException as e:
    print("Exception when calling VmwareApi->vmware_service_resources_vm_command_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Id of subscription | 
 **vm_id** | **str**| Id of VM | 
 **action** | [**VmwareAction**](.md)| Power action to be invoked on the VM | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vmware_service_resources_vm_delete**
> vmware_service_resources_vm_delete(subscription_id, vm_id)

Delete a VM

Delete a VM

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
api_instance = fcsm_eos_api_client.VmwareApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of subscription
vm_id = 'vm_id_example' # str | Id of VM

try:
    # Delete a VM
    api_instance.vmware_service_resources_vm_delete(subscription_id, vm_id)
except ApiException as e:
    print("Exception when calling VmwareApi->vmware_service_resources_vm_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Id of subscription | 
 **vm_id** | **str**| Id of VM | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | VM is deleted and marked as unmanaged |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vmware_service_resources_vm_details_get**
> list[VmwareVMdetails] vmware_service_resources_vm_details_get(subscription_id, vm_id)

Get VM details

Get VM details

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
api_instance = fcsm_eos_api_client.VmwareApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of subscription
vm_id = 'vm_id_example' # str | Id of VM

try:
    # Get VM details
    api_response = api_instance.vmware_service_resources_vm_details_get(subscription_id, vm_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VmwareApi->vmware_service_resources_vm_details_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Id of subscription | 
 **vm_id** | **str**| Id of VM | 

### Return type

[**list[VmwareVMdetails]**](VmwareVMdetails.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vmware_service_resources_vm_get**
> VmwareVM vmware_service_resources_vm_get(subscription_id, vm_id)

Get VM by id

Get virtual machine by id

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
api_instance = fcsm_eos_api_client.VmwareApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of subscription
vm_id = 'vm_id_example' # str | Id of VM

try:
    # Get VM by id
    api_response = api_instance.vmware_service_resources_vm_get(subscription_id, vm_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VmwareApi->vmware_service_resources_vm_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Id of subscription | 
 **vm_id** | **str**| Id of VM | 

### Return type

[**VmwareVM**](VmwareVM.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A VM object |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vmware_service_resources_vm_password_get**
> VmwarePassword vmware_service_resources_vm_password_get(subscription_id, vm_id)

Get the VM password

Get the password in an encrypted form for the virtual machine

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
api_instance = fcsm_eos_api_client.VmwareApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of subscription
vm_id = 'vm_id_example' # str | Id of VM

try:
    # Get the VM password
    api_response = api_instance.vmware_service_resources_vm_password_get(subscription_id, vm_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VmwareApi->vmware_service_resources_vm_password_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Id of subscription | 
 **vm_id** | **str**| Id of VM | 

### Return type

[**VmwarePassword**](VmwarePassword.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Encrypted VM password |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vmware_service_resources_vm_patch**
> vmware_service_resources_vm_patch(subscription_id, vm_id, vmware_update_vm_params)

Update VM

Modify VM properties. Currently it is possible to modify the VM flavor.

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
api_instance = fcsm_eos_api_client.VmwareApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of subscription
vm_id = 'vm_id_example' # str | Id of VM
vmware_update_vm_params = fcsm_eos_api_client.VmwareUpdateVmParams() # VmwareUpdateVmParams | VM properties

try:
    # Update VM
    api_instance.vmware_service_resources_vm_patch(subscription_id, vm_id, vmware_update_vm_params)
except ApiException as e:
    print("Exception when calling VmwareApi->vmware_service_resources_vm_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Id of subscription | 
 **vm_id** | **str**| Id of VM | 
 **vmware_update_vm_params** | [**VmwareUpdateVmParams**](VmwareUpdateVmParams.md)| VM properties | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response body is empty |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vmware_service_resources_vm_tag_put**
> vmware_service_resources_vm_tag_put(subscription_id, vm_id, vmware_tag_update)

Tag VM

Set a tag value for a VM

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
api_instance = fcsm_eos_api_client.VmwareApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of subscription
vm_id = 'vm_id_example' # str | Id of VM
vmware_tag_update = fcsm_eos_api_client.VmwareTagUpdate() # VmwareTagUpdate | Tag object to be updated

try:
    # Tag VM
    api_instance.vmware_service_resources_vm_tag_put(subscription_id, vm_id, vmware_tag_update)
except ApiException as e:
    print("Exception when calling VmwareApi->vmware_service_resources_vm_tag_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Id of subscription | 
 **vm_id** | **str**| Id of VM | 
 **vmware_tag_update** | [**VmwareTagUpdate**](VmwareTagUpdate.md)| Tag object to be updated | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vmware_service_resources_vm_workshift_delete**
> vmware_service_resources_vm_workshift_delete(vm_id, subscription_id)

Delete the VM Workshift

Delete the VM Workshift

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
api_instance = fcsm_eos_api_client.VmwareApi(fcsm_eos_api_client.ApiClient(configuration))
vm_id = 'vm_id_example' # str | Id of VM
subscription_id = 'subscription_id_example' # str | Id of subscription

try:
    # Delete the VM Workshift
    api_instance.vmware_service_resources_vm_workshift_delete(vm_id, subscription_id)
except ApiException as e:
    print("Exception when calling VmwareApi->vmware_service_resources_vm_workshift_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vm_id** | **str**| Id of VM | 
 **subscription_id** | **str**| Id of subscription | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Workshift deleted successfully |  -  |
**400** | Bad request |  -  |
**404** | Workshift does not exist |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vmware_service_resources_vm_workshift_put**
> VmwareWorkshift vmware_service_resources_vm_workshift_put(subscription_id, vm_id, vmware_workshift)

Update the VM workshift

Update the VM Workshift

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
api_instance = fcsm_eos_api_client.VmwareApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of subscription
vm_id = 'vm_id_example' # str | Id of VM
vmware_workshift = fcsm_eos_api_client.VmwareWorkshift() # VmwareWorkshift | Workshift object

try:
    # Update the VM workshift
    api_response = api_instance.vmware_service_resources_vm_workshift_put(subscription_id, vm_id, vmware_workshift)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VmwareApi->vmware_service_resources_vm_workshift_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Id of subscription | 
 **vm_id** | **str**| Id of VM | 
 **vmware_workshift** | [**VmwareWorkshift**](VmwareWorkshift.md)| Workshift object | 

### Return type

[**VmwareWorkshift**](VmwareWorkshift.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Workshift updated successfully |  -  |
**400** | Bad request |  -  |
**404** | Workshift does not exist |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vmware_service_resources_vm_workshifts_post**
> VmwareWorkshift vmware_service_resources_vm_workshifts_post(subscription_id, vm_id, vmware_workshift)

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
api_instance = fcsm_eos_api_client.VmwareApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of subscription
vm_id = 'vm_id_example' # str | Id of VM
vmware_workshift = fcsm_eos_api_client.VmwareWorkshift() # VmwareWorkshift | Workshift object

try:
    # Add a workshift to the VM
    api_response = api_instance.vmware_service_resources_vm_workshifts_post(subscription_id, vm_id, vmware_workshift)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VmwareApi->vmware_service_resources_vm_workshifts_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Id of subscription | 
 **vm_id** | **str**| Id of VM | 
 **vmware_workshift** | [**VmwareWorkshift**](VmwareWorkshift.md)| Workshift object | 

### Return type

[**VmwareWorkshift**](VmwareWorkshift.md)

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
**404** | Workshift does not exist |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vmware_service_resources_vms_get**
> list[VmwareVmSimple] vmware_service_resources_vms_get(subscription_id, availability_zone_id=availability_zone_id)

List VMs

List all virtual machines

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
api_instance = fcsm_eos_api_client.VmwareApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of subscription
availability_zone_id = 'availability_zone_id_example' # str | Availability zone to filter by (optional)

try:
    # List VMs
    api_response = api_instance.vmware_service_resources_vms_get(subscription_id, availability_zone_id=availability_zone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VmwareApi->vmware_service_resources_vms_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Id of subscription | 
 **availability_zone_id** | **str**| Availability zone to filter by | [optional] 

### Return type

[**list[VmwareVmSimple]**](VmwareVmSimple.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of VMs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vmware_service_resources_vms_post**
> VmwareVM vmware_service_resources_vms_post(subscription_id, vmware_vm_create)

Create a VM

Create a new VM

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
api_instance = fcsm_eos_api_client.VmwareApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of subscription
vmware_vm_create = fcsm_eos_api_client.VmwareVMCreate() # VmwareVMCreate | VM creation data

try:
    # Create a VM
    api_response = api_instance.vmware_service_resources_vms_post(subscription_id, vmware_vm_create)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VmwareApi->vmware_service_resources_vms_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Id of subscription | 
 **vmware_vm_create** | [**VmwareVMCreate**](VmwareVMCreate.md)| VM creation data | 

### Return type

[**VmwareVM**](VmwareVM.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A VM object |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vmware_service_resources_volume_attachment_delete**
> vmware_service_resources_volume_attachment_delete(subscription_id, volume_id, vm_id=vm_id)

Dettaches and deletes a volume

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
api_instance = fcsm_eos_api_client.VmwareApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of subscription
volume_id = 'volume_id_example' # str | ID of Volume
vm_id = 'vm_id_example' # str | Id of VM in query (optional)

try:
    # Dettaches and deletes a volume
    api_instance.vmware_service_resources_volume_attachment_delete(subscription_id, volume_id, vm_id=vm_id)
except ApiException as e:
    print("Exception when calling VmwareApi->vmware_service_resources_volume_attachment_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Id of subscription | 
 **volume_id** | **str**| ID of Volume | 
 **vm_id** | **str**| Id of VM in query | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Volume detached from the VM successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vmware_service_resources_volume_patch**
> vmware_service_resources_volume_patch(subscription_id, volume_id, vmware_update_volume_params)

Update a volume

Modify volume properties. Currently it is possible to change to volume size.

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
api_instance = fcsm_eos_api_client.VmwareApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of subscription
volume_id = 'volume_id_example' # str | ID of Volume
vmware_update_volume_params = fcsm_eos_api_client.VmwareUpdateVolumeParams() # VmwareUpdateVolumeParams | Volume properties

try:
    # Update a volume
    api_instance.vmware_service_resources_volume_patch(subscription_id, volume_id, vmware_update_volume_params)
except ApiException as e:
    print("Exception when calling VmwareApi->vmware_service_resources_volume_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Id of subscription | 
 **volume_id** | **str**| ID of Volume | 
 **vmware_update_volume_params** | [**VmwareUpdateVolumeParams**](VmwareUpdateVolumeParams.md)| Volume properties | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Volume was updated successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vmware_service_resources_volume_types_get**
> list[VmwareVolumeType] vmware_service_resources_volume_types_get(subscription_id, availability_zone_id=availability_zone_id, is_os_compatible=is_os_compatible)

List volume types

Get a list of all volume types user can create volume with

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
api_instance = fcsm_eos_api_client.VmwareApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of subscription
availability_zone_id = 'availability_zone_id_example' # str | Availability zone to filter by (optional)
is_os_compatible = True # bool | If true, show only volumes on which OS can be installed (optional)

try:
    # List volume types
    api_response = api_instance.vmware_service_resources_volume_types_get(subscription_id, availability_zone_id=availability_zone_id, is_os_compatible=is_os_compatible)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VmwareApi->vmware_service_resources_volume_types_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Id of subscription | 
 **availability_zone_id** | **str**| Availability zone to filter by | [optional] 
 **is_os_compatible** | **bool**| If true, show only volumes on which OS can be installed | [optional] 

### Return type

[**list[VmwareVolumeType]**](VmwareVolumeType.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of objects |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vmware_service_resources_volumes_get**
> list[VmwareVolume] vmware_service_resources_volumes_get(subscription_id, status=status, availability_zone=availability_zone, is_os_disk=is_os_disk)

List volumes

Get list of all volumes

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
api_instance = fcsm_eos_api_client.VmwareApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of subscription
status = fcsm_eos_api_client.VmwareVolumeStatus() # VmwareVolumeStatus | Volume status to filter by (optional)
availability_zone = 'availability_zone_example' # str | Availability zone to filter by (optional)
is_os_disk = True # bool | Filter volumes by isOsDisk value (optional)

try:
    # List volumes
    api_response = api_instance.vmware_service_resources_volumes_get(subscription_id, status=status, availability_zone=availability_zone, is_os_disk=is_os_disk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VmwareApi->vmware_service_resources_volumes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Id of subscription | 
 **status** | [**VmwareVolumeStatus**](.md)| Volume status to filter by | [optional] 
 **availability_zone** | **str**| Availability zone to filter by | [optional] 
 **is_os_disk** | **bool**| Filter volumes by isOsDisk value | [optional] 

### Return type

[**list[VmwareVolume]**](VmwareVolume.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of volumes |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vmware_service_resources_volumes_post**
> VmwareVolume vmware_service_resources_volumes_post(subscription_id, vmware_new_volume)

Create a new volume

Create a new volume

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
api_instance = fcsm_eos_api_client.VmwareApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of subscription
vmware_new_volume = fcsm_eos_api_client.VmwareNewVolume() # VmwareNewVolume | A volume object

try:
    # Create a new volume
    api_response = api_instance.vmware_service_resources_volumes_post(subscription_id, vmware_new_volume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VmwareApi->vmware_service_resources_volumes_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Id of subscription | 
 **vmware_new_volume** | [**VmwareNewVolume**](VmwareNewVolume.md)| A volume object | 

### Return type

[**VmwareVolume**](VmwareVolume.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

