# VmwareVM

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_power_actions** | **list[str]** | A list of power actions that are allowed in the current VM state | 
**availability_zone** | **str** |  | [optional] 
**availability_zone_id** | **str** |  | 
**created_at** | **str** |  | [optional] 
**flavor_id** | **str** |  | 
**id** | **str** |  | 
**image_id** | **str** |  | 
**interfaces** | **list[str]** | A list of VM network interface ids | 
**is_managed** | **bool** |  | 
**keypair_id** | **str** |  | 
**management_tool_id** | **str** |  | 
**name** | **str** |  | 
**power_state** | **str** |  | 
**status** | **str** |  | [optional] 
**status_message** | **str** |  | [optional] 
**tags** | [**list[VmwareTag]**](VmwareTag.md) | A list of VM tags | 
**volumes** | **list[str]** | A list of volume ids attached to the VM | 
**workshift** | [**VmwareOptionalWorkshift**](VmwareOptionalWorkshift.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


