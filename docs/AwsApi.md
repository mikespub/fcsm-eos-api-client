# fcsm_eos_api_client.AwsApi

All URIs are relative to *https://emeia-eos.fcsm.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aws_service_api_availability_zones_get**](AwsApi.md#aws_service_api_availability_zones_get) | **GET** /api/v1/aws/compute/availabilityZones | 
[**aws_service_api_flavor_get**](AwsApi.md#aws_service_api_flavor_get) | **GET** /api/v1/aws/compute/flavors/{flavor_id} | Get flavor by id
[**aws_service_api_flavors_get**](AwsApi.md#aws_service_api_flavors_get) | **GET** /api/v1/aws/compute/flavors | Lists flavors
[**aws_service_api_image_get**](AwsApi.md#aws_service_api_image_get) | **GET** /api/v1/aws/compute/images/{image_id} | Gets image by id
[**aws_service_api_interfaces_get**](AwsApi.md#aws_service_api_interfaces_get) | **GET** /api/v1/aws/compute/interfaces | Gets interfaces for specified subscription
[**aws_service_api_keypair_delete**](AwsApi.md#aws_service_api_keypair_delete) | **DELETE** /api/v1/aws/compute/keypairs/{keypair_id} | Delete keypair by id
[**aws_service_api_keypair_generate_post**](AwsApi.md#aws_service_api_keypair_generate_post) | **POST** /api/v1/aws/compute/keypairs/generate | Create a new keypair
[**aws_service_api_keypair_get**](AwsApi.md#aws_service_api_keypair_get) | **GET** /api/v1/aws/compute/keypairs/{keypair_id} | Get keypair by id
[**aws_service_api_keypair_import_post**](AwsApi.md#aws_service_api_keypair_import_post) | **POST** /api/v1/aws/compute/keypairs/import | Import a new public key
[**aws_service_api_keypairs_get**](AwsApi.md#aws_service_api_keypairs_get) | **GET** /api/v1/aws/compute/keypairs | Lists keypairs
[**aws_service_api_network_subnets_get**](AwsApi.md#aws_service_api_network_subnets_get) | **GET** /api/v1/aws/compute/networks/{network_id}/subnets | Lists subnets of specified network and subscription
[**aws_service_api_networks_get**](AwsApi.md#aws_service_api_networks_get) | **GET** /api/v1/aws/compute/networks | Gets list of all networks
[**aws_service_api_private_image_get**](AwsApi.md#aws_service_api_private_image_get) | **GET** /api/v1/aws/compute/privateImages/{image_id} | Gets private image by id
[**aws_service_api_private_images_get**](AwsApi.md#aws_service_api_private_images_get) | **GET** /api/v1/aws/compute/privateImages | Lists private images
[**aws_service_api_public_image_get**](AwsApi.md#aws_service_api_public_image_get) | **GET** /api/v1/aws/compute/publicImages/{image_id} | Gets public image by id
[**aws_service_api_public_images_get**](AwsApi.md#aws_service_api_public_images_get) | **GET** /api/v1/aws/compute/publicImages | Lists public images
[**aws_service_api_regions_get**](AwsApi.md#aws_service_api_regions_get) | **GET** /api/v1/aws/compute/regions | 
[**aws_service_api_security_groups_get**](AwsApi.md#aws_service_api_security_groups_get) | **GET** /api/v1/aws/compute/securityGroups | Lists security groups for specified subscription
[**aws_service_api_snapshot_delete**](AwsApi.md#aws_service_api_snapshot_delete) | **DELETE** /api/v1/aws/compute/snapshots/{snapshot_id} | Deletes snapshots
[**aws_service_api_snapshots_get**](AwsApi.md#aws_service_api_snapshots_get) | **GET** /api/v1/aws/compute/snapshots | Lists snapshots
[**aws_service_api_snapshots_post**](AwsApi.md#aws_service_api_snapshots_post) | **POST** /api/v1/aws/compute/snapshots | Creates a new snapshot
[**aws_service_api_validate_subscription_post**](AwsApi.md#aws_service_api_validate_subscription_post) | **POST** /api/v1/aws/compute/validateSubscription | 
[**aws_service_api_vm_command_put**](AwsApi.md#aws_service_api_vm_command_put) | **PUT** /api/v1/aws/compute/vms/{vm_id}/command/{action} | Excecutes power action on a VM
[**aws_service_api_vm_delete**](AwsApi.md#aws_service_api_vm_delete) | **DELETE** /api/v1/aws/compute/vms/{vm_id} | Deletes VM by id
[**aws_service_api_vm_details_get**](AwsApi.md#aws_service_api_vm_details_get) | **GET** /api/v1/aws/compute/vms/{vm_id}/details | Gets VM details
[**aws_service_api_vm_get**](AwsApi.md#aws_service_api_vm_get) | **GET** /api/v1/aws/compute/vms/{vm_id} | Gets vm by id
[**aws_service_api_vm_management_get**](AwsApi.md#aws_service_api_vm_management_get) | **GET** /api/v1/aws/compute/vms/{vm_id}/management | Gets management status for a VM
[**aws_service_api_vm_password_get**](AwsApi.md#aws_service_api_vm_password_get) | **GET** /api/v1/aws/compute/vms/{vm_id}/password | 
[**aws_service_api_vm_patch**](AwsApi.md#aws_service_api_vm_patch) | **PATCH** /api/v1/aws/compute/vms/{vm_id} | Modify VM properties
[**aws_service_api_vm_security_group_delete**](AwsApi.md#aws_service_api_vm_security_group_delete) | **DELETE** /api/v1/aws/compute/vms/{vm_id}/securityGroups/{security_group_id} | Removes Security Group from a specified VM
[**aws_service_api_vm_security_group_put**](AwsApi.md#aws_service_api_vm_security_group_put) | **PUT** /api/v1/aws/compute/vms/{vm_id}/securityGroups/{security_group_id} | Assign Security Group to a specified VM
[**aws_service_api_vm_tag_put**](AwsApi.md#aws_service_api_vm_tag_put) | **PUT** /api/v1/aws/compute/vms/{vm_id}/setTag | Set tag value for VM
[**aws_service_api_vm_workshift_delete**](AwsApi.md#aws_service_api_vm_workshift_delete) | **DELETE** /api/v1/aws/compute/vms/{vm_id}/workshift | Delete VM Workshift
[**aws_service_api_vm_workshift_post**](AwsApi.md#aws_service_api_vm_workshift_post) | **POST** /api/v1/aws/compute/vms/{vm_id}/workshift | Add a workshift to the VM
[**aws_service_api_vm_workshift_put**](AwsApi.md#aws_service_api_vm_workshift_put) | **PUT** /api/v1/aws/compute/vms/{vm_id}/workshift | Update VM Workshift
[**aws_service_api_vms_get**](AwsApi.md#aws_service_api_vms_get) | **GET** /api/v1/aws/compute/vms | Gets list of all vms
[**aws_service_api_vms_post**](AwsApi.md#aws_service_api_vms_post) | **POST** /api/v1/aws/compute/vms | 
[**aws_service_api_volume_attachment_delete**](AwsApi.md#aws_service_api_volume_attachment_delete) | **DELETE** /api/v1/aws/compute/volumes/{volume_id}/detach | 
[**aws_service_api_volume_attachment_put**](AwsApi.md#aws_service_api_volume_attachment_put) | **PUT** /api/v1/aws/compute/volumes/{volume_id}/attach | 
[**aws_service_api_volume_delete**](AwsApi.md#aws_service_api_volume_delete) | **DELETE** /api/v1/aws/compute/volumes/{volume_id} | Deletes volume by id
[**aws_service_api_volume_get**](AwsApi.md#aws_service_api_volume_get) | **GET** /api/v1/aws/compute/volumes/{volume_id} | Gets volume by id
[**aws_service_api_volume_patch**](AwsApi.md#aws_service_api_volume_patch) | **PATCH** /api/v1/aws/compute/volumes/{volume_id} | Modify volume properties
[**aws_service_api_volume_types_get**](AwsApi.md#aws_service_api_volume_types_get) | **GET** /api/v1/aws/compute/volumeTypes | Gets a list of all volume types user can create volume with
[**aws_service_api_volumes_get**](AwsApi.md#aws_service_api_volumes_get) | **GET** /api/v1/aws/compute/volumes | Gets list of all volumes
[**aws_service_api_volumes_post**](AwsApi.md#aws_service_api_volumes_post) | **POST** /api/v1/aws/compute/volumes | Creates a new EBS volume


# **aws_service_api_availability_zones_get**
> list[AwsAvailabilityZone] aws_service_api_availability_zones_get(subscription_id)



List all availability zones

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
api_instance = fcsm_eos_api_client.AwsApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of a subscription

try:
    api_response = api_instance.aws_service_api_availability_zones_get(subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwsApi->aws_service_api_availability_zones_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| Id of a subscription | 

### Return type

[**list[AwsAvailabilityZone]**](AwsAvailabilityZone.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of availability zones |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_service_api_flavor_get**
> AwsFlavor aws_service_api_flavor_get(subscription_id, flavor_id)

Get flavor by id

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
api_instance = fcsm_eos_api_client.AwsApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of a subscription
flavor_id = 'flavor_id_example' # str | Flavor id

try:
    # Get flavor by id
    api_response = api_instance.aws_service_api_flavor_get(subscription_id, flavor_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwsApi->aws_service_api_flavor_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| Id of a subscription | 
 **flavor_id** | **str**| Flavor id | 

### Return type

[**AwsFlavor**](AwsFlavor.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Object was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_service_api_flavors_get**
> list[AwsFlavor] aws_service_api_flavors_get(subscription_id)

Lists flavors

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
api_instance = fcsm_eos_api_client.AwsApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of a subscription

try:
    # Lists flavors
    api_response = api_instance.aws_service_api_flavors_get(subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwsApi->aws_service_api_flavors_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| Id of a subscription | 

### Return type

[**list[AwsFlavor]**](AwsFlavor.md)

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

# **aws_service_api_image_get**
> AwsImage aws_service_api_image_get(subscription_id, image_id)

Gets image by id

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
api_instance = fcsm_eos_api_client.AwsApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of a subscription
image_id = 'image_id_example' # str | Image id

try:
    # Gets image by id
    api_response = api_instance.aws_service_api_image_get(subscription_id, image_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwsApi->aws_service_api_image_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| Id of a subscription | 
 **image_id** | **str**| Image id | 

### Return type

[**AwsImage**](AwsImage.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Object was not found |  -  |
**500** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_service_api_interfaces_get**
> list[AwsInterface] aws_service_api_interfaces_get(subscription_id, vm_id=vm_id, network_id=network_id, subnet_id=subnet_id)

Gets interfaces for specified subscription

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
api_instance = fcsm_eos_api_client.AwsApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of a subscription
vm_id = 'vm_id_example' # str | Vm id to filter by (optional)
network_id = 'network_id_example' # str | Network id to filter by (optional)
subnet_id = 'subnet_id_example' # str | Subnet id to filter by (optional)

try:
    # Gets interfaces for specified subscription
    api_response = api_instance.aws_service_api_interfaces_get(subscription_id, vm_id=vm_id, network_id=network_id, subnet_id=subnet_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwsApi->aws_service_api_interfaces_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| Id of a subscription | 
 **vm_id** | **str**| Vm id to filter by | [optional] 
 **network_id** | **str**| Network id to filter by | [optional] 
 **subnet_id** | **str**| Subnet id to filter by | [optional] 

### Return type

[**list[AwsInterface]**](AwsInterface.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of interfaces |  -  |
**500** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_service_api_keypair_delete**
> aws_service_api_keypair_delete(subscription_id, keypair_id)

Delete keypair by id

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
api_instance = fcsm_eos_api_client.AwsApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of a subscription
keypair_id = 'keypair_id_example' # str | Keypair id

try:
    # Delete keypair by id
    api_instance.aws_service_api_keypair_delete(subscription_id, keypair_id)
except ApiException as e:
    print("Exception when calling AwsApi->aws_service_api_keypair_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| Id of a subscription | 
 **keypair_id** | **str**| Keypair id | 

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
**204** | OK |  -  |
**404** | Object was not found |  -  |
**500** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_service_api_keypair_generate_post**
> AwsKeypair aws_service_api_keypair_generate_post(subscription_id, aws_create_keypair)

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
api_instance = fcsm_eos_api_client.AwsApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of a subscription
aws_create_keypair = fcsm_eos_api_client.AwsCreateKeypair() # AwsCreateKeypair | 

try:
    # Create a new keypair
    api_response = api_instance.aws_service_api_keypair_generate_post(subscription_id, aws_create_keypair)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwsApi->aws_service_api_keypair_generate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| Id of a subscription | 
 **aws_create_keypair** | [**AwsCreateKeypair**](AwsCreateKeypair.md)|  | 

### Return type

[**AwsKeypair**](AwsKeypair.md)

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
**500** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_service_api_keypair_get**
> AwsKeypair aws_service_api_keypair_get(subscription_id, keypair_id)

Get keypair by id

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
api_instance = fcsm_eos_api_client.AwsApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of a subscription
keypair_id = 'keypair_id_example' # str | Keypair id

try:
    # Get keypair by id
    api_response = api_instance.aws_service_api_keypair_get(subscription_id, keypair_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwsApi->aws_service_api_keypair_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| Id of a subscription | 
 **keypair_id** | **str**| Keypair id | 

### Return type

[**AwsKeypair**](AwsKeypair.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Object was not found |  -  |
**500** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_service_api_keypair_import_post**
> AwsKeypair aws_service_api_keypair_import_post(subscription_id, aws_import_keypair)

Import a new public key

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
api_instance = fcsm_eos_api_client.AwsApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of a subscription
aws_import_keypair = fcsm_eos_api_client.AwsImportKeypair() # AwsImportKeypair | 

try:
    # Import a new public key
    api_response = api_instance.aws_service_api_keypair_import_post(subscription_id, aws_import_keypair)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwsApi->aws_service_api_keypair_import_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| Id of a subscription | 
 **aws_import_keypair** | [**AwsImportKeypair**](AwsImportKeypair.md)|  | 

### Return type

[**AwsKeypair**](AwsKeypair.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: applicaiton/json, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**500** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_service_api_keypairs_get**
> list[AwsKeypair] aws_service_api_keypairs_get(subscription_id, availability_zone=availability_zone, availability_zone_id=availability_zone_id)

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
api_instance = fcsm_eos_api_client.AwsApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of a subscription
availability_zone = 'availability_zone_example' # str | Availability zone to filter by (optional)
availability_zone_id = 'availability_zone_id_example' # str | Availability zone to filter by (optional)

try:
    # Lists keypairs
    api_response = api_instance.aws_service_api_keypairs_get(subscription_id, availability_zone=availability_zone, availability_zone_id=availability_zone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwsApi->aws_service_api_keypairs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| Id of a subscription | 
 **availability_zone** | **str**| Availability zone to filter by | [optional] 
 **availability_zone_id** | **str**| Availability zone to filter by | [optional] 

### Return type

[**list[AwsKeypair]**](AwsKeypair.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_service_api_network_subnets_get**
> list[AwsSubnet] aws_service_api_network_subnets_get(subscription_id, network_id, availability_zone_id=availability_zone_id, availability_zone=availability_zone)

Lists subnets of specified network and subscription

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
api_instance = fcsm_eos_api_client.AwsApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of a subscription
network_id = 'network_id_example' # str | ID of network
availability_zone_id = 'availability_zone_id_example' # str | Availability zone to filter by (optional)
availability_zone = 'availability_zone_example' # str | Availability zone to filter by (optional)

try:
    # Lists subnets of specified network and subscription
    api_response = api_instance.aws_service_api_network_subnets_get(subscription_id, network_id, availability_zone_id=availability_zone_id, availability_zone=availability_zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwsApi->aws_service_api_network_subnets_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| Id of a subscription | 
 **network_id** | **str**| ID of network | 
 **availability_zone_id** | **str**| Availability zone to filter by | [optional] 
 **availability_zone** | **str**| Availability zone to filter by | [optional] 

### Return type

[**list[AwsSubnet]**](AwsSubnet.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Object was not found |  -  |
**500** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_service_api_networks_get**
> list[AwsNetwork] aws_service_api_networks_get(subscription_id, availability_zone=availability_zone, availability_zone_id=availability_zone_id)

Gets list of all networks

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
api_instance = fcsm_eos_api_client.AwsApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of a subscription
availability_zone = 'availability_zone_example' # str | Availability zone to filter by (optional)
availability_zone_id = 'availability_zone_id_example' # str | Availability zone to filter by (optional)

try:
    # Gets list of all networks
    api_response = api_instance.aws_service_api_networks_get(subscription_id, availability_zone=availability_zone, availability_zone_id=availability_zone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwsApi->aws_service_api_networks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| Id of a subscription | 
 **availability_zone** | **str**| Availability zone to filter by | [optional] 
 **availability_zone_id** | **str**| Availability zone to filter by | [optional] 

### Return type

[**list[AwsNetwork]**](AwsNetwork.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_service_api_private_image_get**
> AwsImage aws_service_api_private_image_get(subscription_id, image_id)

Gets private image by id

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
api_instance = fcsm_eos_api_client.AwsApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of a subscription
image_id = 'image_id_example' # str | Image id

try:
    # Gets private image by id
    api_response = api_instance.aws_service_api_private_image_get(subscription_id, image_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwsApi->aws_service_api_private_image_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| Id of a subscription | 
 **image_id** | **str**| Image id | 

### Return type

[**AwsImage**](AwsImage.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Object was not found |  -  |
**500** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_service_api_private_images_get**
> list[AwsImage] aws_service_api_private_images_get(subscription_id, name=name)

Lists private images

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
api_instance = fcsm_eos_api_client.AwsApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of a subscription
name = 'name_example' # str | Image name to filter by. Specify name or id (optional)

try:
    # Lists private images
    api_response = api_instance.aws_service_api_private_images_get(subscription_id, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwsApi->aws_service_api_private_images_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| Id of a subscription | 
 **name** | **str**| Image name to filter by. Specify name or id | [optional] 

### Return type

[**list[AwsImage]**](AwsImage.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**500** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_service_api_public_image_get**
> AwsImage aws_service_api_public_image_get(subscription_id, image_id)

Gets public image by id

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
api_instance = fcsm_eos_api_client.AwsApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of a subscription
image_id = 'image_id_example' # str | Image id

try:
    # Gets public image by id
    api_response = api_instance.aws_service_api_public_image_get(subscription_id, image_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwsApi->aws_service_api_public_image_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| Id of a subscription | 
 **image_id** | **str**| Image id | 

### Return type

[**AwsImage**](AwsImage.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Object was not found |  -  |
**500** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_service_api_public_images_get**
> list[AwsImage] aws_service_api_public_images_get(subscription_id, name=name)

Lists public images

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
api_instance = fcsm_eos_api_client.AwsApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of a subscription
name = 'name_example' # str | Image name to filter by. Specify name or id (optional)

try:
    # Lists public images
    api_response = api_instance.aws_service_api_public_images_get(subscription_id, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwsApi->aws_service_api_public_images_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| Id of a subscription | 
 **name** | **str**| Image name to filter by. Specify name or id | [optional] 

### Return type

[**list[AwsImage]**](AwsImage.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**500** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_service_api_regions_get**
> list[AwsRegion] aws_service_api_regions_get(subscription_id=subscription_id)



Lists regions

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
api_instance = fcsm_eos_api_client.AwsApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of subscription (optional)

try:
    api_response = api_instance.aws_service_api_regions_get(subscription_id=subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwsApi->aws_service_api_regions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| Id of subscription | [optional] 

### Return type

[**list[AwsRegion]**](AwsRegion.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of regions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_service_api_security_groups_get**
> list[AwsSecurityGroup] aws_service_api_security_groups_get(subscription_id, vm_id=vm_id)

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
api_instance = fcsm_eos_api_client.AwsApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of a subscription
vm_id = 'vm_id_example' # str | Vm id to filter by (optional)

try:
    # Lists security groups for specified subscription
    api_response = api_instance.aws_service_api_security_groups_get(subscription_id, vm_id=vm_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwsApi->aws_service_api_security_groups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| Id of a subscription | 
 **vm_id** | **str**| Vm id to filter by | [optional] 

### Return type

[**list[AwsSecurityGroup]**](AwsSecurityGroup.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of security groups |  -  |
**404** | Object was not found |  -  |
**500** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_service_api_snapshot_delete**
> aws_service_api_snapshot_delete(subscription_id, snapshot_id)

Deletes snapshots

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
api_instance = fcsm_eos_api_client.AwsApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of a subscription
snapshot_id = 'snapshot_id_example' # str | Snapshot id

try:
    # Deletes snapshots
    api_instance.aws_service_api_snapshot_delete(subscription_id, snapshot_id)
except ApiException as e:
    print("Exception when calling AwsApi->aws_service_api_snapshot_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| Id of a subscription | 
 **snapshot_id** | **str**| Snapshot id | 

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
**204** | OK |  -  |
**400** | Bad request |  -  |
**404** | Object was not found |  -  |
**500** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_service_api_snapshots_get**
> list[AwsSnapshot] aws_service_api_snapshots_get(subscription_id, vm_id=vm_id)

Lists snapshots

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
api_instance = fcsm_eos_api_client.AwsApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of a subscription
vm_id = 'vm_id_example' # str | Vm id to filter by (optional)

try:
    # Lists snapshots
    api_response = api_instance.aws_service_api_snapshots_get(subscription_id, vm_id=vm_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwsApi->aws_service_api_snapshots_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| Id of a subscription | 
 **vm_id** | **str**| Vm id to filter by | [optional] 

### Return type

[**list[AwsSnapshot]**](AwsSnapshot.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of snapshots |  -  |
**400** | Bad request |  -  |
**500** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_service_api_snapshots_post**
> AwsSnapshot aws_service_api_snapshots_post(subscription_id, aws_create_snapshot_params)

Creates a new snapshot

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
api_instance = fcsm_eos_api_client.AwsApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of a subscription
aws_create_snapshot_params = fcsm_eos_api_client.AwsCreateSnapshotParams() # AwsCreateSnapshotParams | 

try:
    # Creates a new snapshot
    api_response = api_instance.aws_service_api_snapshots_post(subscription_id, aws_create_snapshot_params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwsApi->aws_service_api_snapshots_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| Id of a subscription | 
 **aws_create_snapshot_params** | [**AwsCreateSnapshotParams**](AwsCreateSnapshotParams.md)|  | 

### Return type

[**AwsSnapshot**](AwsSnapshot.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created snapshot |  -  |
**400** | Bad request |  -  |
**404** | Object was not found |  -  |
**500** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_service_api_validate_subscription_post**
> aws_service_api_validate_subscription_post(aws_validate_subscription)



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
api_instance = fcsm_eos_api_client.AwsApi(fcsm_eos_api_client.ApiClient(configuration))
aws_validate_subscription = fcsm_eos_api_client.AwsValidateSubscription() # AwsValidateSubscription | 

try:
    api_instance.aws_service_api_validate_subscription_post(aws_validate_subscription)
except ApiException as e:
    print("Exception when calling AwsApi->aws_service_api_validate_subscription_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aws_validate_subscription** | [**AwsValidateSubscription**](AwsValidateSubscription.md)|  | 

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
**204** | OK |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_service_api_vm_command_put**
> aws_service_api_vm_command_put(subscription_id, vm_id, action)

Excecutes power action on a VM

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
api_instance = fcsm_eos_api_client.AwsApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of a subscription
vm_id = 'vm_id_example' # str | Virtual Machine id
action = 'action_example' # str | 

try:
    # Excecutes power action on a VM
    api_instance.aws_service_api_vm_command_put(subscription_id, vm_id, action)
except ApiException as e:
    print("Exception when calling AwsApi->aws_service_api_vm_command_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| Id of a subscription | 
 **vm_id** | **str**| Virtual Machine id | 
 **action** | **str**|  | 

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
**202** | OK |  -  |
**400** | Bad request |  -  |
**404** | Object was not found |  -  |
**409** | Object is in conflict state |  -  |
**500** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_service_api_vm_delete**
> aws_service_api_vm_delete(subscription_id, vm_id)

Deletes VM by id

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
api_instance = fcsm_eos_api_client.AwsApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of a subscription
vm_id = 'vm_id_example' # str | Virtual Machine id

try:
    # Deletes VM by id
    api_instance.aws_service_api_vm_delete(subscription_id, vm_id)
except ApiException as e:
    print("Exception when calling AwsApi->aws_service_api_vm_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| Id of a subscription | 
 **vm_id** | **str**| Virtual Machine id | 

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
**204** | OK |  -  |
**400** | Bad request |  -  |
**404** | Object was not found |  -  |
**500** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_service_api_vm_details_get**
> list[AwsVMDetail] aws_service_api_vm_details_get(subscription_id, vm_id)

Gets VM details

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
api_instance = fcsm_eos_api_client.AwsApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of a subscription
vm_id = 'vm_id_example' # str | Virtual Machine id

try:
    # Gets VM details
    api_response = api_instance.aws_service_api_vm_details_get(subscription_id, vm_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwsApi->aws_service_api_vm_details_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| Id of a subscription | 
 **vm_id** | **str**| Virtual Machine id | 

### Return type

[**list[AwsVMDetail]**](AwsVMDetail.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of VM details |  -  |
**404** | Object was not found |  -  |
**500** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_service_api_vm_get**
> AwsVMExtended aws_service_api_vm_get(subscription_id, vm_id)

Gets vm by id

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
api_instance = fcsm_eos_api_client.AwsApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of a subscription
vm_id = 'vm_id_example' # str | Virtual Machine id

try:
    # Gets vm by id
    api_response = api_instance.aws_service_api_vm_get(subscription_id, vm_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwsApi->aws_service_api_vm_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| Id of a subscription | 
 **vm_id** | **str**| Virtual Machine id | 

### Return type

[**AwsVMExtended**](AwsVMExtended.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Object was not found |  -  |
**500** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_service_api_vm_management_get**
> AwsManagementStatus aws_service_api_vm_management_get(subscription_id, vm_id)

Gets management status for a VM

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
api_instance = fcsm_eos_api_client.AwsApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of a subscription
vm_id = 'vm_id_example' # str | Virtual Machine id

try:
    # Gets management status for a VM
    api_response = api_instance.aws_service_api_vm_management_get(subscription_id, vm_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwsApi->aws_service_api_vm_management_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| Id of a subscription | 
 **vm_id** | **str**| Virtual Machine id | 

### Return type

[**AwsManagementStatus**](AwsManagementStatus.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Object was not found |  -  |
**500** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_service_api_vm_password_get**
> AwsEncryptedPassword aws_service_api_vm_password_get(subscription_id, vm_id)



Get encrypted password for a VM

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
api_instance = fcsm_eos_api_client.AwsApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of a subscription
vm_id = 'vm_id_example' # str | Virtual Machine id

try:
    api_response = api_instance.aws_service_api_vm_password_get(subscription_id, vm_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwsApi->aws_service_api_vm_password_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| Id of a subscription | 
 **vm_id** | **str**| Virtual Machine id | 

### Return type

[**AwsEncryptedPassword**](AwsEncryptedPassword.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Object with encrypted password |  -  |
**404** | Object was not found |  -  |
**500** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_service_api_vm_patch**
> aws_service_api_vm_patch(subscription_id, vm_id, aws_update_vm_params)

Modify VM properties

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
api_instance = fcsm_eos_api_client.AwsApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of a subscription
vm_id = 'vm_id_example' # str | Virtual Machine id
aws_update_vm_params = fcsm_eos_api_client.AwsUpdateVmParams() # AwsUpdateVmParams | 

try:
    # Modify VM properties
    api_instance.aws_service_api_vm_patch(subscription_id, vm_id, aws_update_vm_params)
except ApiException as e:
    print("Exception when calling AwsApi->aws_service_api_vm_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| Id of a subscription | 
 **vm_id** | **str**| Virtual Machine id | 
 **aws_update_vm_params** | [**AwsUpdateVmParams**](AwsUpdateVmParams.md)|  | 

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
**204** | OK |  -  |
**400** | Bad request |  -  |
**404** | Object was not found |  -  |
**409** | Object is in conflict state |  -  |
**500** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_service_api_vm_security_group_delete**
> aws_service_api_vm_security_group_delete(subscription_id, vm_id, security_group_id)

Removes Security Group from a specified VM

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
api_instance = fcsm_eos_api_client.AwsApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of a subscription
vm_id = 'vm_id_example' # str | Virtual Machine id
security_group_id = 'security_group_id_example' # str | Security Group Id

try:
    # Removes Security Group from a specified VM
    api_instance.aws_service_api_vm_security_group_delete(subscription_id, vm_id, security_group_id)
except ApiException as e:
    print("Exception when calling AwsApi->aws_service_api_vm_security_group_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| Id of a subscription | 
 **vm_id** | **str**| Virtual Machine id | 
 **security_group_id** | **str**| Security Group Id | 

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
**200** | Security group was not assigned assigned to VM |  -  |
**201** | Security group was removed from VM |  -  |
**400** | Bad request |  -  |
**404** | Object was not found |  -  |
**500** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_service_api_vm_security_group_put**
> aws_service_api_vm_security_group_put(subscription_id, vm_id, security_group_id)

Assign Security Group to a specified VM

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
api_instance = fcsm_eos_api_client.AwsApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of a subscription
vm_id = 'vm_id_example' # str | Virtual Machine id
security_group_id = 'security_group_id_example' # str | Security Group Id

try:
    # Assign Security Group to a specified VM
    api_instance.aws_service_api_vm_security_group_put(subscription_id, vm_id, security_group_id)
except ApiException as e:
    print("Exception when calling AwsApi->aws_service_api_vm_security_group_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| Id of a subscription | 
 **vm_id** | **str**| Virtual Machine id | 
 **security_group_id** | **str**| Security Group Id | 

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
**201** | Security group was assigned to VM |  -  |
**400** | Bad request |  -  |
**404** | Object was not found |  -  |
**500** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_service_api_vm_tag_put**
> aws_service_api_vm_tag_put(subscription_id, vm_id, aws_tag_update)

Set tag value for VM

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
api_instance = fcsm_eos_api_client.AwsApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of a subscription
vm_id = 'vm_id_example' # str | Virtual Machine id
aws_tag_update = fcsm_eos_api_client.AwsTagUpdate() # AwsTagUpdate | 

try:
    # Set tag value for VM
    api_instance.aws_service_api_vm_tag_put(subscription_id, vm_id, aws_tag_update)
except ApiException as e:
    print("Exception when calling AwsApi->aws_service_api_vm_tag_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| Id of a subscription | 
 **vm_id** | **str**| Virtual Machine id | 
 **aws_tag_update** | [**AwsTagUpdate**](AwsTagUpdate.md)|  | 

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
**204** | OK |  -  |
**400** | Bad request |  -  |
**404** | Object was not found |  -  |
**500** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_service_api_vm_workshift_delete**
> aws_service_api_vm_workshift_delete(subscription_id, vm_id)

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
api_instance = fcsm_eos_api_client.AwsApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of a subscription
vm_id = 'vm_id_example' # str | Virtual Machine id

try:
    # Delete VM Workshift
    api_instance.aws_service_api_vm_workshift_delete(subscription_id, vm_id)
except ApiException as e:
    print("Exception when calling AwsApi->aws_service_api_vm_workshift_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| Id of a subscription | 
 **vm_id** | **str**| Virtual Machine id | 

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
**500** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_service_api_vm_workshift_post**
> AwsWorkshift aws_service_api_vm_workshift_post(subscription_id, vm_id, aws_workshift)

Add a workshift to the VM

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
api_instance = fcsm_eos_api_client.AwsApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of a subscription
vm_id = 'vm_id_example' # str | Virtual Machine id
aws_workshift = fcsm_eos_api_client.AwsWorkshift() # AwsWorkshift | Workshift object

try:
    # Add a workshift to the VM
    api_response = api_instance.aws_service_api_vm_workshift_post(subscription_id, vm_id, aws_workshift)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwsApi->aws_service_api_vm_workshift_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| Id of a subscription | 
 **vm_id** | **str**| Virtual Machine id | 
 **aws_workshift** | [**AwsWorkshift**](AwsWorkshift.md)| Workshift object | 

### Return type

[**AwsWorkshift**](AwsWorkshift.md)

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
**500** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_service_api_vm_workshift_put**
> AwsWorkshift aws_service_api_vm_workshift_put(subscription_id, vm_id, aws_workshift)

Update VM Workshift

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
api_instance = fcsm_eos_api_client.AwsApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of a subscription
vm_id = 'vm_id_example' # str | Virtual Machine id
aws_workshift = fcsm_eos_api_client.AwsWorkshift() # AwsWorkshift | Workshift object

try:
    # Update VM Workshift
    api_response = api_instance.aws_service_api_vm_workshift_put(subscription_id, vm_id, aws_workshift)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwsApi->aws_service_api_vm_workshift_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| Id of a subscription | 
 **vm_id** | **str**| Virtual Machine id | 
 **aws_workshift** | [**AwsWorkshift**](AwsWorkshift.md)| Workshift object | 

### Return type

[**AwsWorkshift**](AwsWorkshift.md)

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
**404** | Object was not found |  -  |
**500** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_service_api_vms_get**
> list[AwsVMSimple] aws_service_api_vms_get(subscription_id, availability_zone_id=availability_zone_id, availability_zone=availability_zone)

Gets list of all vms

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
api_instance = fcsm_eos_api_client.AwsApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of a subscription
availability_zone_id = 'availability_zone_id_example' # str | Availability zone to filter by (optional)
availability_zone = 'availability_zone_example' # str | Availability zone to filter by (optional)

try:
    # Gets list of all vms
    api_response = api_instance.aws_service_api_vms_get(subscription_id, availability_zone_id=availability_zone_id, availability_zone=availability_zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwsApi->aws_service_api_vms_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| Id of a subscription | 
 **availability_zone_id** | **str**| Availability zone to filter by | [optional] 
 **availability_zone** | **str**| Availability zone to filter by | [optional] 

### Return type

[**list[AwsVMSimple]**](AwsVMSimple.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_service_api_vms_post**
> AwsVMExtended aws_service_api_vms_post(subscription_id, aws_vm_create)



Create a new virtual machine

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
api_instance = fcsm_eos_api_client.AwsApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of a subscription
aws_vm_create = fcsm_eos_api_client.AwsVMCreate() # AwsVMCreate | 

try:
    api_response = api_instance.aws_service_api_vms_post(subscription_id, aws_vm_create)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwsApi->aws_service_api_vms_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| Id of a subscription | 
 **aws_vm_create** | [**AwsVMCreate**](AwsVMCreate.md)|  | 

### Return type

[**AwsVMExtended**](AwsVMExtended.md)

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
**500** | Service encountered an error it does not know how to handle |  -  |
**504** | There was a timeout inside of cluster |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_service_api_volume_attachment_delete**
> aws_service_api_volume_attachment_delete(subscription_id, volume_id, vm_id)



Detach volume from a specified vm

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
api_instance = fcsm_eos_api_client.AwsApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of a subscription
volume_id = 'volume_id_example' # str | Volume id
vm_id = 'vm_id_example' # str | VM id to attach volume

try:
    api_instance.aws_service_api_volume_attachment_delete(subscription_id, volume_id, vm_id)
except ApiException as e:
    print("Exception when calling AwsApi->aws_service_api_volume_attachment_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| Id of a subscription | 
 **volume_id** | **str**| Volume id | 
 **vm_id** | **str**| VM id to attach volume | 

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
**204** | OK |  -  |
**400** | Bad request |  -  |
**403** | Operation is forbidden |  -  |
**404** | Object was not found |  -  |
**500** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_service_api_volume_attachment_put**
> AwsNewVolumeAttachment aws_service_api_volume_attachment_put(subscription_id, volume_id, vm_id)



Attach volume to specified VM

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
api_instance = fcsm_eos_api_client.AwsApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of a subscription
volume_id = 'volume_id_example' # str | Volume id
vm_id = 'vm_id_example' # str | VM id to attach volume

try:
    api_response = api_instance.aws_service_api_volume_attachment_put(subscription_id, volume_id, vm_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwsApi->aws_service_api_volume_attachment_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| Id of a subscription | 
 **volume_id** | **str**| Volume id | 
 **vm_id** | **str**| VM id to attach volume | 

### Return type

[**AwsNewVolumeAttachment**](AwsNewVolumeAttachment.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**404** | Object was not found |  -  |
**409** | Object is in conflict state |  -  |
**500** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_service_api_volume_delete**
> aws_service_api_volume_delete(subscription_id, volume_id)

Deletes volume by id

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
api_instance = fcsm_eos_api_client.AwsApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of a subscription
volume_id = 'volume_id_example' # str | Volume id

try:
    # Deletes volume by id
    api_instance.aws_service_api_volume_delete(subscription_id, volume_id)
except ApiException as e:
    print("Exception when calling AwsApi->aws_service_api_volume_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| Id of a subscription | 
 **volume_id** | **str**| Volume id | 

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
**204** | OK |  -  |
**400** | Bad request |  -  |
**404** | Object was not found |  -  |
**500** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_service_api_volume_get**
> AwsVolume aws_service_api_volume_get(subscription_id, volume_id)

Gets volume by id

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
api_instance = fcsm_eos_api_client.AwsApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of a subscription
volume_id = 'volume_id_example' # str | Volume id

try:
    # Gets volume by id
    api_response = api_instance.aws_service_api_volume_get(subscription_id, volume_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwsApi->aws_service_api_volume_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| Id of a subscription | 
 **volume_id** | **str**| Volume id | 

### Return type

[**AwsVolume**](AwsVolume.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Object was not found |  -  |
**500** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_service_api_volume_patch**
> aws_service_api_volume_patch(subscription_id, volume_id, aws_update_volume_params)

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
api_instance = fcsm_eos_api_client.AwsApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of a subscription
volume_id = 'volume_id_example' # str | Volume id
aws_update_volume_params = fcsm_eos_api_client.AwsUpdateVolumeParams() # AwsUpdateVolumeParams | 

try:
    # Modify volume properties
    api_instance.aws_service_api_volume_patch(subscription_id, volume_id, aws_update_volume_params)
except ApiException as e:
    print("Exception when calling AwsApi->aws_service_api_volume_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| Id of a subscription | 
 **volume_id** | **str**| Volume id | 
 **aws_update_volume_params** | [**AwsUpdateVolumeParams**](AwsUpdateVolumeParams.md)|  | 

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
**409** | Object is in conflict state |  -  |
**500** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_service_api_volume_types_get**
> list[AwsVolumeType] aws_service_api_volume_types_get(subscription_id, is_os_compatible=is_os_compatible, availability_zone_id=availability_zone_id)

Gets a list of all volume types user can create volume with

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
api_instance = fcsm_eos_api_client.AwsApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of a subscription
is_os_compatible = True # bool |  (optional)
availability_zone_id = 'availability_zone_id_example' # str | Availability zone to filter by (optional)

try:
    # Gets a list of all volume types user can create volume with
    api_response = api_instance.aws_service_api_volume_types_get(subscription_id, is_os_compatible=is_os_compatible, availability_zone_id=availability_zone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwsApi->aws_service_api_volume_types_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| Id of a subscription | 
 **is_os_compatible** | **bool**|  | [optional] 
 **availability_zone_id** | **str**| Availability zone to filter by | [optional] 

### Return type

[**list[AwsVolumeType]**](AwsVolumeType.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_service_api_volumes_get**
> list[AwsVolume] aws_service_api_volumes_get(subscription_id, availability_zone_id=availability_zone_id, availability_zone=availability_zone, status=status, is_os_disk=is_os_disk)

Gets list of all volumes

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
api_instance = fcsm_eos_api_client.AwsApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of a subscription
availability_zone_id = 'availability_zone_id_example' # str | Availability zone to filter by (optional)
availability_zone = 'availability_zone_example' # str | Availability zone to filter by (optional)
status = fcsm_eos_api_client.AwsVolumeStatus() # AwsVolumeStatus | Volume status to filter by (optional)
is_os_disk = True # bool | Filter volumes by isOsDisk value (optional)

try:
    # Gets list of all volumes
    api_response = api_instance.aws_service_api_volumes_get(subscription_id, availability_zone_id=availability_zone_id, availability_zone=availability_zone, status=status, is_os_disk=is_os_disk)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwsApi->aws_service_api_volumes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| Id of a subscription | 
 **availability_zone_id** | **str**| Availability zone to filter by | [optional] 
 **availability_zone** | **str**| Availability zone to filter by | [optional] 
 **status** | [**AwsVolumeStatus**](.md)| Volume status to filter by | [optional] 
 **is_os_disk** | **bool**| Filter volumes by isOsDisk value | [optional] 

### Return type

[**list[AwsVolume]**](AwsVolume.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aws_service_api_volumes_post**
> AwsVolume aws_service_api_volumes_post(subscription_id, aws_create_volume_params)

Creates a new EBS volume

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
api_instance = fcsm_eos_api_client.AwsApi(fcsm_eos_api_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | Id of a subscription
aws_create_volume_params = fcsm_eos_api_client.AwsCreateVolumeParams() # AwsCreateVolumeParams | 

try:
    # Creates a new EBS volume
    api_response = api_instance.aws_service_api_volumes_post(subscription_id, aws_create_volume_params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwsApi->aws_service_api_volumes_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| Id of a subscription | 
 **aws_create_volume_params** | [**AwsCreateVolumeParams**](AwsCreateVolumeParams.md)|  | 

### Return type

[**AwsVolume**](AwsVolume.md)

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
**500** | Service encountered an error it does not know how to handle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

