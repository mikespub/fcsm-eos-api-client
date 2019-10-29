# fcsm_eos_api_client.NotifApi

All URIs are relative to *https://emeia-eos.fcsm.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**send_email**](NotifApi.md#send_email) | **POST** /api/v1/notification/email | Send email


# **send_email**
> send_email(notif_message)

Send email

Send email

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
api_instance = fcsm_eos_api_client.NotifApi(fcsm_eos_api_client.ApiClient(configuration))
notif_message = fcsm_eos_api_client.NotifMessage() # NotifMessage | Message data

try:
    # Send email
    api_instance.send_email(notif_message)
except ApiException as e:
    print("Exception when calling NotifApi->send_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notif_message** | [**NotifMessage**](NotifMessage.md)| Message data | 

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
**200** | OK |  -  |
**400** | unsupported mail provider |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

