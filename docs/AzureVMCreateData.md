# AzureVMCreateData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**resource_group_id** | **str** |  | 
**flavor_id** | **str** |  | 
**image_id** | **str** |  | 
**keypair_id** | **str** |  | 
**volume_size** | **int** |  | 
**volume_type_id** | [**AzureVolumeTypeId**](AzureVolumeTypeId.md) |  | 
**tags** | [**list[AzureTag]**](AzureTag.md) |  | 
**workshift** | [**AzureOptionalWorkshift**](AzureOptionalWorkshift.md) |  | [optional] 
**security_groups** | **list[str]** | \&quot;securityGroups\&quot; is deprecated in favor of \&quot;securityGroupIds\&quot; and will be removed in 3 months. | [optional] 
**security_group_ids** | **list[str]** |  | [optional] 
**avalability_zone** | **str** |  | [optional] 
**availability_zone_id** | **str** |  | [optional] [default to 'default']
**availability_set_id** | **str** |  | [optional] 
**nics** | **list[str]** | \&quot;nics\&quot; is deprecated in favor of \&quot;subnetId\&quot; and will be removed in 3 months. | [optional] 
**subnet_id** | **str** |  | [optional] 
**management_enabled** | **bool** | \&quot;managementEnabled\&quot; is deprecated in favor of \&quot;managementToolId\&quot; and will be removed in 3 months. | [optional] 
**management_tool_id** | [**AnyOfUUIDobject**](AnyOfUUIDobject.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


