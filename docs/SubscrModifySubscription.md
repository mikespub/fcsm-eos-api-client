# SubscrModifySubscription

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of a subscription. Must be 1 to 32 char long, no trailing whitespace allowed. | 
**username** | **str** | Subscription username for OpenStack|K5|VMware subscription | [optional] 
**password** | **str** | Password for a subscription for Openstack|K5|VMware subscription | [optional] 
**provisioning** | **bool** | States if provisioning is enabled | [optional] 
**contract_id** | **str** | Subscription contract id for OpenStack|K5 account | [optional] 
**access_key** | **str** | Access key ID for AWS subscription. Parameter for AWS subscription only | [optional] 
**secret_key** | **str** | Secret access key for AWS subscription. Parameter for AWS subscription only | [optional] 
**platform_subscription_id** | **str** | Platform subscription ID for Azure subscription. Parameter for Azure subscription | [optional] 
**tenant_id** | **str** | Tenant ID in Azure subscription. Parameter for Azure subscription | [optional] 
**policy** | [**SubscrPolicy**](SubscrPolicy.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


