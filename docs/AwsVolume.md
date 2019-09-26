# AwsVolume

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachment** | [**AwsVolumeAttachment**](AwsVolumeAttachment.md) |  | 
**availability_zone** | **str** | Availability Zone | [optional] 
**availability_zone_id** | **str** | Availability Zone | 
**created_at** | **str** | Disk creation date | 
**id** | **str** | Volume id | 
**is_os_disk** | **bool** | If set to true volume is an OS disk, otherwise it is a data disk | 
**name** | **str** | Disk name | 
**size_in_gb** | **int** | Disk size in GB | 
**status** | **str** | Disk state, e.g. in-use | 
**tags** | [**list[AwsTag]**](AwsTag.md) | Tags (name and value) assigned to this Volume | 
**type_id** | [**AwsVolumeTypeId**](AwsVolumeTypeId.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


