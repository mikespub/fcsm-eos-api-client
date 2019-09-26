# fcsm_eos_api_client.ImgWhitelistApi

All URIs are relative to *https://emeia-eos.fcsm.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_whitelist_image_os_get**](ImgWhitelistApi.md#api_v1_whitelist_image_os_get) | **GET** /api/v1/whitelist/imageOS | Get image type (OS) for a image
[**api_v1_whitelist_images_delete**](ImgWhitelistApi.md#api_v1_whitelist_images_delete) | **DELETE** /api/v1/whitelist/images | Delete whitelist
[**api_v1_whitelist_images_get**](ImgWhitelistApi.md#api_v1_whitelist_images_get) | **GET** /api/v1/whitelist/images | Get images from whitelist
[**api_v1_whitelist_images_image_id_delete**](ImgWhitelistApi.md#api_v1_whitelist_images_image_id_delete) | **DELETE** /api/v1/whitelist/images/{imageId} | Remove image from whitelist
[**api_v1_whitelist_images_image_id_get**](ImgWhitelistApi.md#api_v1_whitelist_images_image_id_get) | **GET** /api/v1/whitelist/images/{imageId} | Get single image
[**api_v1_whitelist_images_image_id_patch**](ImgWhitelistApi.md#api_v1_whitelist_images_image_id_patch) | **PATCH** /api/v1/whitelist/images/{imageId} | Update operating system for image
[**api_v1_whitelist_images_image_id_put**](ImgWhitelistApi.md#api_v1_whitelist_images_image_id_put) | **PUT** /api/v1/whitelist/images/{imageId} | Update operating system for image
[**api_v1_whitelist_images_post**](ImgWhitelistApi.md#api_v1_whitelist_images_post) | **POST** /api/v1/whitelist/images | Add single image to whitelist
[**api_v1_whitelist_os_list_get**](ImgWhitelistApi.md#api_v1_whitelist_os_list_get) | **GET** /api/v1/whitelist/osList | Get os types and distributions as a list


# **api_v1_whitelist_image_os_get**
> ImgWhitelistOSDetails api_v1_whitelist_image_os_get(name)

Get image type (OS) for a image

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.ImgWhitelistApi()
name = 'name_example' # str | Image name to specify OS

try:
    # Get image type (OS) for a image
    api_response = api_instance.api_v1_whitelist_image_os_get(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImgWhitelistApi->api_v1_whitelist_image_os_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Image name to specify OS | 

### Return type

[**ImgWhitelistOSDetails**](ImgWhitelistOSDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | An unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_whitelist_images_delete**
> api_v1_whitelist_images_delete(subscription_id)

Delete whitelist

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.ImgWhitelistApi()
subscription_id = 'subscription_id_example' # str | Subscription id

try:
    # Delete whitelist
    api_instance.api_v1_whitelist_images_delete(subscription_id)
except ApiException as e:
    print("Exception when calling ImgWhitelistApi->api_v1_whitelist_images_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| Subscription id | 

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
**200** | Whitelist was deleted |  -  |
**400** | Subscription for unsupported platform was passed |  -  |
**404** | Unknown subscription id was passed |  -  |
**500** | An unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_whitelist_images_get**
> ImgWhitelistWhitelist api_v1_whitelist_images_get(subscription_id, name=name, limit=limit, page=page, is_private=is_private)

Get images from whitelist

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.ImgWhitelistApi()
subscription_id = 'subscription_id_example' # str | Subscription id
name = 'name_example' # str | Image name to filter by (optional)
limit = 10 # int | Limit of images to show (optional) (default to 10)
page = 1 # int | Number of the page for pagination (optional) (default to 1)
is_private = True # bool | Parameter to filter public/ private images. If it is set to true return private images, if it is set to false return public images, if it is not passed return all images. (optional)

try:
    # Get images from whitelist
    api_response = api_instance.api_v1_whitelist_images_get(subscription_id, name=name, limit=limit, page=page, is_private=is_private)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImgWhitelistApi->api_v1_whitelist_images_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| Subscription id | 
 **name** | **str**| Image name to filter by | [optional] 
 **limit** | **int**| Limit of images to show | [optional] [default to 10]
 **page** | **int**| Number of the page for pagination | [optional] [default to 1]
 **is_private** | **bool**| Parameter to filter public/ private images. If it is set to true return private images, if it is set to false return public images, if it is not passed return all images. | [optional] 

### Return type

[**ImgWhitelistWhitelist**](ImgWhitelistWhitelist.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of the images |  -  |
**400** | Subscription for unsupported platform was passed |  -  |
**404** | Unknown subscription id was passed |  -  |
**500** | Error while retrieving flavors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_whitelist_images_image_id_delete**
> api_v1_whitelist_images_image_id_delete(subscription_id, image_id)

Remove image from whitelist

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.ImgWhitelistApi()
subscription_id = 'subscription_id_example' # str | Subscription id
image_id = 'image_id_example' # str | Image id

try:
    # Remove image from whitelist
    api_instance.api_v1_whitelist_images_image_id_delete(subscription_id, image_id)
except ApiException as e:
    print("Exception when calling ImgWhitelistApi->api_v1_whitelist_images_image_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| Subscription id | 
 **image_id** | **str**| Image id | 

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
**200** | OK |  -  |
**400** | Subscription for unsupported platform was passed |  -  |
**404** | Unknown subscription id or image id was passed |  -  |
**500** | An unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_whitelist_images_image_id_get**
> ImgWhitelistImage api_v1_whitelist_images_image_id_get(subscription_id, image_id)

Get single image

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.ImgWhitelistApi()
subscription_id = 'subscription_id_example' # str | Subscription id
image_id = 'image_id_example' # str | Image id

try:
    # Get single image
    api_response = api_instance.api_v1_whitelist_images_image_id_get(subscription_id, image_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImgWhitelistApi->api_v1_whitelist_images_image_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| Subscription id | 
 **image_id** | **str**| Image id | 

### Return type

[**ImgWhitelistImage**](ImgWhitelistImage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Subscription for unsupported platform was passed |  -  |
**404** | Unknown subscription id or image id was passed |  -  |
**500** | Error while retrieving flavors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_whitelist_images_image_id_patch**
> ImgWhitelistImage api_v1_whitelist_images_image_id_patch(subscription_id, image_id, img_whitelist_image_update)

Update operating system for image

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.ImgWhitelistApi()
subscription_id = 'subscription_id_example' # str | Subscription id
image_id = 'image_id_example' # str | Image id
img_whitelist_image_update = fcsm_eos_api_client.ImgWhitelistImageUpdate() # ImgWhitelistImageUpdate | Image details

try:
    # Update operating system for image
    api_response = api_instance.api_v1_whitelist_images_image_id_patch(subscription_id, image_id, img_whitelist_image_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImgWhitelistApi->api_v1_whitelist_images_image_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| Subscription id | 
 **image_id** | **str**| Image id | 
 **img_whitelist_image_update** | [**ImgWhitelistImageUpdate**](ImgWhitelistImageUpdate.md)| Image details | 

### Return type

[**ImgWhitelistImage**](ImgWhitelistImage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | OS should be one of values linux, windows, unknown or subscription for unsupported platform was passed |  -  |
**404** | Unknown subscription id or image id was passed |  -  |
**500** | An unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_whitelist_images_image_id_put**
> ImgWhitelistImage api_v1_whitelist_images_image_id_put(subscription_id, image_id, img_whitelist_image_update)

Update operating system for image

Please use PATCH method. This action will be removed on 14.05.2019

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.ImgWhitelistApi()
subscription_id = 'subscription_id_example' # str | Subscription id
image_id = 'image_id_example' # str | Image id
img_whitelist_image_update = fcsm_eos_api_client.ImgWhitelistImageUpdate() # ImgWhitelistImageUpdate | Image details

try:
    # Update operating system for image
    api_response = api_instance.api_v1_whitelist_images_image_id_put(subscription_id, image_id, img_whitelist_image_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImgWhitelistApi->api_v1_whitelist_images_image_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| Subscription id | 
 **image_id** | **str**| Image id | 
 **img_whitelist_image_update** | [**ImgWhitelistImageUpdate**](ImgWhitelistImageUpdate.md)| Image details | 

### Return type

[**ImgWhitelistImage**](ImgWhitelistImage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | OS should be one of values linux, windows, unknown or subscription for unsupported platform was passed |  -  |
**404** | Unknown subscription id or image id was passed |  -  |
**500** | An unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_whitelist_images_post**
> ImgWhitelistImage api_v1_whitelist_images_post(subscription_id, img_whitelist_image_add)

Add single image to whitelist

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.ImgWhitelistApi()
subscription_id = 'subscription_id_example' # str | Subscription id
img_whitelist_image_add = fcsm_eos_api_client.ImgWhitelistImageAdd() # ImgWhitelistImageAdd | Image details

try:
    # Add single image to whitelist
    api_response = api_instance.api_v1_whitelist_images_post(subscription_id, img_whitelist_image_add)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImgWhitelistApi->api_v1_whitelist_images_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)| Subscription id | 
 **img_whitelist_image_add** | [**ImgWhitelistImageAdd**](ImgWhitelistImageAdd.md)| Image details | 

### Return type

[**ImgWhitelistImage**](ImgWhitelistImage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error saving data or subscription for unsupported platform was passed |  -  |
**404** | Unknown subscription id was passed |  -  |
**500** | An unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_whitelist_os_list_get**
> list[ImgWhitelistOSDetails] api_v1_whitelist_os_list_get()

Get os types and distributions as a list

### Example

```python
from __future__ import print_function
import time
import fcsm_eos_api_client
from fcsm_eos_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = fcsm_eos_api_client.ImgWhitelistApi()

try:
    # Get os types and distributions as a list
    api_response = api_instance.api_v1_whitelist_os_list_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImgWhitelistApi->api_v1_whitelist_os_list_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ImgWhitelistOSDetails]**](ImgWhitelistOSDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | An unexpected error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

