# SubscrSubscription

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of a subscription | 
**platform_id** | **str** | Id of a platform | 
**name** | **str** | Name of a subscription | 
**region_id** | **str** | Region of a subscription | 
**owner_id** | **str** | Id of a subscription owner | 
**provisioning** | **bool** | States if provisioning is enabled | [optional] 
**created_at** | **str** | Date when subscription was created | [optional] 
**updated_at** | **str** | Date of last subscription update | [optional] 
**contract_id** | **str** | Subscription contract id for OpenStack|K5 account | [optional] 
**project_id** | **str** | Project ID for OpenStack|K5 | [optional] 
**username** | **str** | Subscription username for OpenStack|K5|VMware subscription | [optional] 
**password** | **str** | Password for a subscription for OpenStack|K5|VMware subscription | [optional] 
**access_key** | **str** | Access key ID for AWS/Azure subscriptions. Parameter for AWS/Azure subscriptions only | [optional] 
**secret_key** | **str** | Secret access key for AWS/Azure subscriptions. Parameter for AWS/Azure subscriptions only | [optional] 
**tenant_id** | **str** | Tenant ID for Azure. | [optional] 
**platform_subscription_id** | **str** | Subscription ID for Azure. | [optional] 
**authentication_url** | **str** | The URL which is used for authentication and token generation. Parameter for VMware subscription only | [optional] 
**api_url** | **str** | The URL which is used for communication with vRO API. Parameter for VMware subscription only | [optional] 
**policy** | [**SubscrPolicy**](SubscrPolicy.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


