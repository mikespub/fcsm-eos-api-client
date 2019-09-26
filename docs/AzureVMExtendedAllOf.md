# AzureVMExtendedAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interface_ids** | **list[str]** |  | 
**interfaces** | **list[str]** | Deprecated after 3 months. Please use &#x60;interfaceIds&#x60; | [optional] 
**volume_ids** | **list[str]** | List will contain at least one item which will be an ID of the OS volume virtual machine boots from  | 
**volumes** | **list[str]** | Deprecated after 3 months. Please use &#x60;volumeIds&#x60; | [optional] 
**allowed_power_actions** | [**list[AzureVMPowerAction]**](AzureVMPowerAction.md) |  | 
**status** | **str** |  | 
**status_message** | **str** |  | [optional] 
**workshift** | [**AzureOptionalWorkshift**](AzureOptionalWorkshift.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


