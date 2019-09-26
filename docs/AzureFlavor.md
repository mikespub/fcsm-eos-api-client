# AzureFlavor

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**ram_in_mb** | **int** | Amount of memory supported by virtual machine with this flavor | 
**vcpus** | **int** | Amount of VCPUs supported by virtual machine with this flavor | 
**disk_in_gb** | **int** | Highest OS volume size allowed for virtual machines with this flavor | 
**ephemeral_disk_in_gb** | **int** | Highest data volume size allowed for virtual machines with this flavor | [optional] 
**compatible_volume_type_ids** | [**list[AzureVolumeTypeId]**](AzureVolumeTypeId.md) | List of volume types that can be attached to this virtual machine as data volumes | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


