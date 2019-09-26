# AwsVMCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availability_zone** | **str** | Availability zone | [optional] 
**availability_zone_id** | **str** | Availability zone id | [optional] 
**flavor_id** | **str** | Flavor id | 
**image_id** | **str** | Image id user for VM creation | 
**keypair_id** | **str** | Keypair id | 
**management_enabled** | **bool** | Specifies if management of a VM in EOS is enabled | [optional] 
**mangement_tool_id** | **str** |  | [optional] 
**name** | **str** | VM name | 
**nics** | **list[str]** | List of network ids. Set eiher nics or subnetId. | [optional] 
**security_group_ids** | **list[str]** | List of security group ids | [optional] 
**security_groups** | **list[str]** | List of security group ids | [optional] 
**subnet_id** | **str** | Subnet id. Set either nics or subnetId. | [optional] 
**tags** | [**list[AwsTag]**](AwsTag.md) | Tags (name and value) assigned to this VM | 
**volume_size** | **int** | Volume size in GB | 
**volume_type_id** | **str** | Volume type id that will be used as OS volume | [default to 'gp2']
**workshift** | [**AwsOptionalWorkshift**](AwsOptionalWorkshift.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


