# fcsm_eos_api_client.AnalyticsApi

All URIs are relative to *https://emeia-eos.fcsm.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_metrics**](AnalyticsApi.md#get_metrics) | **GET** /api/v1/analytics/metrics | 
[**get_operating_systems**](AnalyticsApi.md#get_operating_systems) | **GET** /api/v1/analytics/operatingSystems | 
[**get_platform_metrics**](AnalyticsApi.md#get_platform_metrics) | **GET** /api/v1/analytics/platforms/{platformId} | 
[**get_platforms_usage**](AnalyticsApi.md#get_platforms_usage) | **GET** /api/v1/analytics/platformsUsage | 
[**get_summary**](AnalyticsApi.md#get_summary) | **GET** /api/v1/analytics/summary | 
[**get_summary_usage**](AnalyticsApi.md#get_summary_usage) | **GET** /api/v1/analytics/summaryUsage | 


# **get_metrics**
> AnalyticsMetrics get_metrics(start_date=start_date, end_date=end_date)



Retrieve all metrics

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
api_instance = fcsm_eos_api_client.AnalyticsApi(fcsm_eos_api_client.ApiClient(configuration))
start_date = '2013-10-20' # date | Start date for showing metrics (YYYY-MM-DD) (optional)
end_date = '2013-10-20' # date | End date for showing metrics (YYYY-MM-DD) (optional)

try:
    api_response = api_instance.get_metrics(start_date=start_date, end_date=end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **date**| Start date for showing metrics (YYYY-MM-DD) | [optional] 
 **end_date** | **date**| End date for showing metrics (YYYY-MM-DD) | [optional] 

### Return type

[**AnalyticsMetrics**](AnalyticsMetrics.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of all metrics |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_operating_systems**
> list[AnalyticsOperatingSystem] get_operating_systems()



Retrieve information about operating systems in use

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
api_instance = fcsm_eos_api_client.AnalyticsApi(fcsm_eos_api_client.ApiClient(configuration))

try:
    api_response = api_instance.get_operating_systems()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_operating_systems: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[AnalyticsOperatingSystem]**](AnalyticsOperatingSystem.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response may be empty list if all platforms are disabled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_platform_metrics**
> AnalyticsPlatformMetrics get_platform_metrics(platform_id)



Retrieve metrics for specific platform

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
api_instance = fcsm_eos_api_client.AnalyticsApi(fcsm_eos_api_client.ApiClient(configuration))
platform_id = 'platform_id_example' # str | ID of platform

try:
    api_response = api_instance.get_platform_metrics(platform_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_platform_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_id** | **str**| ID of platform | 

### Return type

[**AnalyticsPlatformMetrics**](AnalyticsPlatformMetrics.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metrics for one platform |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_platforms_usage**
> AnalyticsPlatformsUsage get_platforms_usage()



Retrieve percentage platforms usage

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
api_instance = fcsm_eos_api_client.AnalyticsApi(fcsm_eos_api_client.ApiClient(configuration))

try:
    api_response = api_instance.get_platforms_usage()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_platforms_usage: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AnalyticsPlatformsUsage**](AnalyticsPlatformsUsage.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response may be empty object if all platforms are disabled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_summary**
> AnalyticsSummary get_summary()



Retrieve usage summary

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
api_instance = fcsm_eos_api_client.AnalyticsApi(fcsm_eos_api_client.ApiClient(configuration))

try:
    api_response = api_instance.get_summary()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_summary: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AnalyticsSummary**](AnalyticsSummary.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Summary response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_summary_usage**
> AnalyticsSummaryUsage get_summary_usage()



Retrieve usage summary for all platforms

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
api_instance = fcsm_eos_api_client.AnalyticsApi(fcsm_eos_api_client.ApiClient(configuration))

try:
    api_response = api_instance.get_summary_usage()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_summary_usage: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AnalyticsSummaryUsage**](AnalyticsSummaryUsage.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Summarized usage of resources |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

