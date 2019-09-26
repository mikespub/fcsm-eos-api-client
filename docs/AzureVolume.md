# AzureVolume

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**created_at** | **str** |  | 
**size_in_gb** | **int** |  | 
**status** | [**AzureVolumeStatus**](AzureVolumeStatus.md) |  | 
**type_id** | [**AzureVolumeTypeId**](AzureVolumeTypeId.md) |  | 
**is_os_disk** | **bool** |  | 
**tags** | [**list[AzureTag]**](AzureTag.md) | Tags (name and value) assigned to this Volume | 
**availability_zone_id** | **str** |  | [default to 'default']
**attachment** | [**AzureVolumeAttachment**](AzureVolumeAttachment.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


