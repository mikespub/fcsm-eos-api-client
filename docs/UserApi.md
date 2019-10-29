# fcsm_eos_api_client.UserApi

All URIs are relative to *https://emeia-eos.fcsm.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_credentials**](UserApi.md#check_credentials) | **POST** /api/v1/user/checkCredentials | 
[**create_user**](UserApi.md#create_user) | **POST** /api/v1/user/users | 
[**delete_user**](UserApi.md#delete_user) | **DELETE** /api/v1/user/users/{user_id} | 
[**forgot_password**](UserApi.md#forgot_password) | **POST** /api/v1/user/forgotPassword | 
[**get_me**](UserApi.md#get_me) | **GET** /api/v1/user/me | 
[**get_user**](UserApi.md#get_user) | **GET** /api/v1/user/users/{user_id} | 
[**get_users**](UserApi.md#get_users) | **GET** /api/v1/user/users | 
[**remove_subscription**](UserApi.md#remove_subscription) | **DELETE** /api/v1/user/removeSubscription | 
[**reset_password**](UserApi.md#reset_password) | **POST** /api/v1/user/resetPassword | 
[**set_access_rights**](UserApi.md#set_access_rights) | **PUT** /api/v1/user/users/{user_id}/setAccessRights | 
[**set_password**](UserApi.md#set_password) | **PUT** /api/v1/user/users/{user_id}/setPassword | 
[**set_role**](UserApi.md#set_role) | **PUT** /api/v1/user/users/{user_id}/setRole | 
[**update_user**](UserApi.md#update_user) | **PUT** /api/v1/user/users/{user_id} | 
[**validate_token**](UserApi.md#validate_token) | **POST** /api/v1/user/validateToken | 


# **check_credentials**
> UserUser check_credentials(user_credentials)



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
api_instance = fcsm_eos_api_client.UserApi(fcsm_eos_api_client.ApiClient(configuration))
user_credentials = fcsm_eos_api_client.UserCredentials() # UserCredentials | 

try:
    api_response = api_instance.check_credentials(user_credentials)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->check_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_credentials** | [**UserCredentials**](UserCredentials.md)|  | 

### Return type

[**UserUser**](UserUser.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The user with those credentials |  -  |
**400** | Input data is invalid |  -  |
**403** | Invalid credentials |  -  |
**500** | An unexpected error occurred |  -  |
**503** | Database unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user**
> UserUser create_user(email, user_user)



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
api_instance = fcsm_eos_api_client.UserApi(fcsm_eos_api_client.ApiClient(configuration))
email = 'email_example' # str | 
user_user = fcsm_eos_api_client.UserUser() # UserUser | 

try:
    api_response = api_instance.create_user(email, user_user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 
 **user_user** | [**UserUser**](UserUser.md)|  | 

### Return type

[**UserUser**](UserUser.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The newly created user |  -  |
**400** | Input data is invalid |  -  |
**403** | Admin rights are required |  -  |
**500** | An unexpected error occurred |  -  |
**503** | Cannot send the password reset email or database unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> delete_user(user_id, user_id2)



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
api_instance = fcsm_eos_api_client.UserApi(fcsm_eos_api_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 
user_id2 = 'user_id_example' # str | 

try:
    api_instance.delete_user(user_id, user_id2)
except ApiException as e:
    print("Exception when calling UserApi->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **user_id2** | **str**|  | 

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
**200** | Successfully deleted the user |  -  |
**400** | Input data is invalid |  -  |
**403** | Admin rights are required and admins cannot delete themselves |  -  |
**404** | Unknown user id |  -  |
**500** | An unexpected error occurred |  -  |
**503** | Database unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forgot_password**
> forgot_password(user_forgotten_password)



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
api_instance = fcsm_eos_api_client.UserApi(fcsm_eos_api_client.ApiClient(configuration))
user_forgotten_password = fcsm_eos_api_client.UserForgottenPassword() # UserForgottenPassword | 

try:
    api_instance.forgot_password(user_forgotten_password)
except ApiException as e:
    print("Exception when calling UserApi->forgot_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_forgotten_password** | [**UserForgottenPassword**](UserForgottenPassword.md)|  | 

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
**200** | Password reset request successfully received |  -  |
**400** | Input data is invalid |  -  |
**500** | An unexpected error occurred |  -  |
**503** | Cannot send the password reset email or database unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_me**
> UserUser get_me(user_id)



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
api_instance = fcsm_eos_api_client.UserApi(fcsm_eos_api_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.get_me(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_me: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**UserUser**](UserUser.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The current user |  -  |
**401** | User is not logged in |  -  |
**500** | An unexpected error occurred |  -  |
**503** | Database unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> UserUser get_user(user_id)



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
api_instance = fcsm_eos_api_client.UserApi(fcsm_eos_api_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.get_user(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**UserUser**](UserUser.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The user with the given user id |  -  |
**400** | Input data is invalid |  -  |
**403** | Admin rights are required |  -  |
**404** | Unknown user id |  -  |
**500** | An unexpected error occurred |  -  |
**503** | Database unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users**
> list[UserUser] get_users(email=email)



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
api_instance = fcsm_eos_api_client.UserApi(fcsm_eos_api_client.ApiClient(configuration))
email = 'email_example' # str |  (optional)

try:
    api_response = api_instance.get_users(email=email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | [optional] 

### Return type

[**list[UserUser]**](UserUser.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All users in the database |  -  |
**400** | Input data is invalid |  -  |
**403** | Admin rights are required |  -  |
**500** | An unexpected error occurred |  -  |
**503** | Database unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_subscription**
> remove_subscription(external, user_subscription_id)



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
api_instance = fcsm_eos_api_client.UserApi(fcsm_eos_api_client.ApiClient(configuration))
external = 'external_example' # str | 
user_subscription_id = fcsm_eos_api_client.UserSubscriptionID() # UserSubscriptionID | 

try:
    api_instance.remove_subscription(external, user_subscription_id)
except ApiException as e:
    print("Exception when calling UserApi->remove_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external** | **str**|  | 
 **user_subscription_id** | [**UserSubscriptionID**](UserSubscriptionID.md)|  | 

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
**200** | Successfully deleted subscription |  -  |
**400** | Input data is invalid |  -  |
**403** | Admin rights are required |  -  |
**404** | Unknown subscription id |  -  |
**500** | An unexpected error occurred |  -  |
**503** | Database unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_password**
> reset_password(user_password_reset)



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
api_instance = fcsm_eos_api_client.UserApi(fcsm_eos_api_client.ApiClient(configuration))
user_password_reset = fcsm_eos_api_client.UserPasswordReset() # UserPasswordReset | 

try:
    api_instance.reset_password(user_password_reset)
except ApiException as e:
    print("Exception when calling UserApi->reset_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_password_reset** | [**UserPasswordReset**](UserPasswordReset.md)|  | 

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
**200** | Password successfully reset |  -  |
**400** | Input data is invalid |  -  |
**403** | Invalid token |  -  |
**500** | An unexpected error occurred |  -  |
**503** | Database unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_access_rights**
> set_access_rights(user_id, email, user_id2, user_access_right)



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
api_instance = fcsm_eos_api_client.UserApi(fcsm_eos_api_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 
email = 'email_example' # str | 
user_id2 = 'user_id_example' # str | 
user_access_right = [fcsm_eos_api_client.UserAccessRight()] # list[UserAccessRight] | 

try:
    api_instance.set_access_rights(user_id, email, user_id2, user_access_right)
except ApiException as e:
    print("Exception when calling UserApi->set_access_rights: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **email** | **str**|  | 
 **user_id2** | **str**|  | 
 **user_access_right** | [**list[UserAccessRight]**](UserAccessRight.md)|  | 

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
**200** | Successfully updated access rights |  -  |
**400** | Input data is invalid |  -  |
**403** | Admin rights are required and admins cannot change their own permissions |  -  |
**404** | Unknown user id |  -  |
**500** | An unexpected error occurred |  -  |
**503** | Database unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_password**
> set_password(user_id, user_id2, user_password_update)



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
api_instance = fcsm_eos_api_client.UserApi(fcsm_eos_api_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 
user_id2 = 'user_id_example' # str | 
user_password_update = fcsm_eos_api_client.UserPasswordUpdate() # UserPasswordUpdate | 

try:
    api_instance.set_password(user_id, user_id2, user_password_update)
except ApiException as e:
    print("Exception when calling UserApi->set_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **user_id2** | **str**|  | 
 **user_password_update** | [**UserPasswordUpdate**](UserPasswordUpdate.md)|  | 

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
**200** | Successfully updated the password |  -  |
**400** | Input data is invalid |  -  |
**403** | Cannot change another user&#39;s password and the old password must be correct |  -  |
**404** | Unknown user id |  -  |
**500** | An unexpected error occurred |  -  |
**503** | Database unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_role**
> set_role(user_id, email, user_id2, user_role_update)



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
api_instance = fcsm_eos_api_client.UserApi(fcsm_eos_api_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 
email = 'email_example' # str | 
user_id2 = 'user_id_example' # str | 
user_role_update = fcsm_eos_api_client.UserRoleUpdate() # UserRoleUpdate | 

try:
    api_instance.set_role(user_id, email, user_id2, user_role_update)
except ApiException as e:
    print("Exception when calling UserApi->set_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **email** | **str**|  | 
 **user_id2** | **str**|  | 
 **user_role_update** | [**UserRoleUpdate**](UserRoleUpdate.md)|  | 

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
**200** | Successfully updated role |  -  |
**400** | Input data is invalid |  -  |
**403** | Admin rights are required and admins cannot change their own role |  -  |
**404** | Unknown user id |  -  |
**500** | An unexpected error occurred |  -  |
**503** | Database unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> update_user(user_id, user_id2, email, user_update_user)



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
api_instance = fcsm_eos_api_client.UserApi(fcsm_eos_api_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 
user_id2 = 'user_id_example' # str | 
email = 'email_example' # str | 
user_update_user = fcsm_eos_api_client.UserUpdateUser() # UserUpdateUser | 

try:
    api_instance.update_user(user_id, user_id2, email, user_update_user)
except ApiException as e:
    print("Exception when calling UserApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **user_id2** | **str**|  | 
 **email** | **str**|  | 
 **user_update_user** | [**UserUpdateUser**](UserUpdateUser.md)|  | 

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
**200** | Successfully updated the user |  -  |
**400** | Input data is invalid |  -  |
**403** | Users can only update their own data |  -  |
**404** | Unknown user id |  -  |
**500** | An unexpected error occurred |  -  |
**503** | Database unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_token**
> validate_token(user_token)



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
api_instance = fcsm_eos_api_client.UserApi(fcsm_eos_api_client.ApiClient(configuration))
user_token = fcsm_eos_api_client.UserToken() # UserToken | 

try:
    api_instance.validate_token(user_token)
except ApiException as e:
    print("Exception when calling UserApi->validate_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | [**UserToken**](UserToken.md)|  | 

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
**200** | Valid token |  -  |
**400** | Input data is invalid |  -  |
**403** | Invalid or unknown token |  -  |
**404** | No user for this token found |  -  |
**500** | An unexpected error occurred |  -  |
**503** | Database unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

