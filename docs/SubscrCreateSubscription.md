# SubscrCreateSubscription

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**platform_id** | **str** | Id of a platform | 
**name** | **str** | Name of a subscription. Must be 1 to 32 char long, no trailing whitespace allowed. | 
**provisioning** | **bool** | States if provisioning is enabled | [optional] 
**contract_id** | **str** | Subscription contract id for OpenStack|K5 account | [optional] 
**project_id** | **str** | Project ID for OpenStack|K5 platform | [optional] 
**username** | **str** | Subscription username for OpenStack|K5|Vmware subscription | [optional] 
**password** | **str** | Password for a subscription for Openstack|K5|VMware subscription | [optional] 
**access_key** | **str** | Access key ID for AWS subscription. Parameter for AWS subscription only | [optional] 
**secret_key** | **str** | Secret access key for AWS subscription. Parameter for AWS subscription only | [optional] 
**platform_subscription_id** | **str** | Platform subscription ID for Azure subscription. Parameter for Azure subscription | [optional] 
**tenant_id** | **str** | Tenant ID in Azure subscription. Parameter for Azure subscription | [optional] 
**authentication_url** | **str** | The URL which is used for authentication and token generation. Parameter for VMware subscription only | [optional] 
**api_url** | **str** | The URL which is used for communication with vRO API. Parameter for VMware subscription only | [optional] 
**policy** | [**SubscrPolicy**](SubscrPolicy.md) |  | 
**region_id** | **str** | Region of a subscription | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


