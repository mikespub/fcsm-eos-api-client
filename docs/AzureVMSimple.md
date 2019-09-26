# AzureVMSimple

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**is_managed** | **bool** |  | 
**management_tool_id** | [**AnyOfUUIDobject**](AnyOfUUIDobject.md) |  | 
**flavor_id** | **str** |  | 
**image_id** | [**AnyOfstringobject**](AnyOfstringobject.md) |  | 
**power_state** | **str** |  | 
**created_at** | **str** |  | [optional] 
**availability_zone_id** | **str** |  | [default to 'default']
**availability_zone** | **str** | Deprecated after 3 months. Please use &#x60;availabilityZoneId&#x60; | 
**availability_set_id** | [**AnyOfstringobject**](AnyOfstringobject.md) |  | [optional] 
**tags** | [**list[AzureTag]**](AzureTag.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


