# VmwareVMCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availability_zone** | **str** | Availability zone | 
**flavor_id** | **str** | Flavor id | 
**image_id** | **str** | Id of an image used for VM creation | 
**keypair_id** | **str** | Keypair id | 
**management_enabled** | **bool** | Specifies if management of a VM in EOS is enabled | [optional] 
**management_tool_id** | **str** |  | [optional] 
**name** | **str** | VM name | 
**nics** | **list[str]** | List of network ids | [optional] 
**security_groups** | **list[str]** | List of security group ids. The list is always empty because there are no security groups in VMware. | 
**subnet_id** | **str** | Subnet id in which VM should be created | [optional] 
**tags** | [**list[VmwareTag]**](VmwareTag.md) | Tags (name and value) assigned to this VM | 
**volume_size** | **int** | Volume size in GB | 
**volume_type_id** | **str** | Volume type id that will be used for OS volume | 
**workshift** | [**VmwareOptionalWorkshift**](VmwareOptionalWorkshift.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


