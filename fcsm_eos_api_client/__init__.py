# coding: utf-8

# flake8: noqa

"""
    Combined FCSM EOS API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.2.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "1.2.1"

# import apis into sdk package
from fcsm_eos_api_client.api.analytics_api import AnalyticsApi
from fcsm_eos_api_client.api.auth_api import AuthApi
from fcsm_eos_api_client.api.aws_api import AwsApi
from fcsm_eos_api_client.api.azure_api import AzureApi
from fcsm_eos_api_client.api.config_api import ConfigApi
from fcsm_eos_api_client.api.img_whitelist_api import ImgWhitelistApi
from fcsm_eos_api_client.api.mgmt_api import MgmtApi
from fcsm_eos_api_client.api.notif_api import NotifApi
from fcsm_eos_api_client.api.subscr_api import SubscrApi
from fcsm_eos_api_client.api.tag_api import TagApi
from fcsm_eos_api_client.api.user_api import UserApi
from fcsm_eos_api_client.api.vmware_api import VmwareApi
from fcsm_eos_api_client.api.webhook_api import WebhookApi

# import ApiClient
from fcsm_eos_api_client.api_client import ApiClient
from fcsm_eos_api_client.configuration import Configuration
from fcsm_eos_api_client.exceptions import OpenApiException
from fcsm_eos_api_client.exceptions import ApiTypeError
from fcsm_eos_api_client.exceptions import ApiValueError
from fcsm_eos_api_client.exceptions import ApiKeyError
from fcsm_eos_api_client.exceptions import ApiException
# import models into sdk package
from fcsm_eos_api_client.models.analytics_bad_request import AnalyticsBadRequest
from fcsm_eos_api_client.models.analytics_error import AnalyticsError
from fcsm_eos_api_client.models.analytics_metric import AnalyticsMetric
from fcsm_eos_api_client.models.analytics_metrics import AnalyticsMetrics
from fcsm_eos_api_client.models.analytics_operating_system import AnalyticsOperatingSystem
from fcsm_eos_api_client.models.analytics_platform_metrics import AnalyticsPlatformMetrics
from fcsm_eos_api_client.models.analytics_platforms_usage import AnalyticsPlatformsUsage
from fcsm_eos_api_client.models.analytics_summary import AnalyticsSummary
from fcsm_eos_api_client.models.analytics_summary_usage import AnalyticsSummaryUsage
from fcsm_eos_api_client.models.auth_credentials import AuthCredentials
from fcsm_eos_api_client.models.auth_error import AuthError
from fcsm_eos_api_client.models.auth_forbidden import AuthForbidden
from fcsm_eos_api_client.models.auth_invalid_credentials import AuthInvalidCredentials
from fcsm_eos_api_client.models.auth_invalid_input import AuthInvalidInput
from fcsm_eos_api_client.models.auth_not_found import AuthNotFound
from fcsm_eos_api_client.models.auth_saml_config import AuthSamlConfig
from fcsm_eos_api_client.models.auth_token import AuthToken
from fcsm_eos_api_client.models.auth_unexpected_error import AuthUnexpectedError
from fcsm_eos_api_client.models.aws_availability_zone import AwsAvailabilityZone
from fcsm_eos_api_client.models.aws_create_keypair import AwsCreateKeypair
from fcsm_eos_api_client.models.aws_create_snapshot_params import AwsCreateSnapshotParams
from fcsm_eos_api_client.models.aws_create_volume_params import AwsCreateVolumeParams
from fcsm_eos_api_client.models.aws_encrypted_password import AwsEncryptedPassword
from fcsm_eos_api_client.models.aws_error import AwsError
from fcsm_eos_api_client.models.aws_flavor import AwsFlavor
from fcsm_eos_api_client.models.aws_i_pv4_address import AwsIPv4Address
from fcsm_eos_api_client.models.aws_image import AwsImage
from fcsm_eos_api_client.models.aws_import_keypair import AwsImportKeypair
from fcsm_eos_api_client.models.aws_interface import AwsInterface
from fcsm_eos_api_client.models.aws_interface_attachment import AwsInterfaceAttachment
from fcsm_eos_api_client.models.aws_keypair import AwsKeypair
from fcsm_eos_api_client.models.aws_management_status import AwsManagementStatus
from fcsm_eos_api_client.models.aws_network import AwsNetwork
from fcsm_eos_api_client.models.aws_new_volume_attachment import AwsNewVolumeAttachment
from fcsm_eos_api_client.models.aws_optional_workshift import AwsOptionalWorkshift
from fcsm_eos_api_client.models.aws_region import AwsRegion
from fcsm_eos_api_client.models.aws_security_group import AwsSecurityGroup
from fcsm_eos_api_client.models.aws_snapshot import AwsSnapshot
from fcsm_eos_api_client.models.aws_subnet import AwsSubnet
from fcsm_eos_api_client.models.aws_tag import AwsTag
from fcsm_eos_api_client.models.aws_tag_update import AwsTagUpdate
from fcsm_eos_api_client.models.aws_update_vm_params import AwsUpdateVmParams
from fcsm_eos_api_client.models.aws_update_volume_params import AwsUpdateVolumeParams
from fcsm_eos_api_client.models.aws_vm_create import AwsVMCreate
from fcsm_eos_api_client.models.aws_vm_detail import AwsVMDetail
from fcsm_eos_api_client.models.aws_vm_extended import AwsVMExtended
from fcsm_eos_api_client.models.aws_vm_extended_all_of import AwsVMExtendedAllOf
from fcsm_eos_api_client.models.aws_vm_power_action import AwsVMPowerAction
from fcsm_eos_api_client.models.aws_vm_simple import AwsVMSimple
from fcsm_eos_api_client.models.aws_validate_subscription import AwsValidateSubscription
from fcsm_eos_api_client.models.aws_volume import AwsVolume
from fcsm_eos_api_client.models.aws_volume_attachment import AwsVolumeAttachment
from fcsm_eos_api_client.models.aws_volume_status import AwsVolumeStatus
from fcsm_eos_api_client.models.aws_volume_type import AwsVolumeType
from fcsm_eos_api_client.models.aws_volume_type_id import AwsVolumeTypeId
from fcsm_eos_api_client.models.aws_workshift import AwsWorkshift
from fcsm_eos_api_client.models.aws_workshift_schedule import AwsWorkshiftSchedule
from fcsm_eos_api_client.models.azure_availability_set import AzureAvailabilitySet
from fcsm_eos_api_client.models.azure_availability_zone import AzureAvailabilityZone
from fcsm_eos_api_client.models.azure_create_resource_group import AzureCreateResourceGroup
from fcsm_eos_api_client.models.azure_create_snapshot import AzureCreateSnapshot
from fcsm_eos_api_client.models.azure_create_volume import AzureCreateVolume
from fcsm_eos_api_client.models.azure_encrypted_password import AzureEncryptedPassword
from fcsm_eos_api_client.models.azure_error import AzureError
from fcsm_eos_api_client.models.azure_flavor import AzureFlavor
from fcsm_eos_api_client.models.azure_generated_keypair import AzureGeneratedKeypair
from fcsm_eos_api_client.models.azure_generated_keypair_all_of import AzureGeneratedKeypairAllOf
from fcsm_eos_api_client.models.azure_i_pv4_address import AzureIPv4Address
from fcsm_eos_api_client.models.azure_interface import AzureInterface
from fcsm_eos_api_client.models.azure_interface_attachment import AzureInterfaceAttachment
from fcsm_eos_api_client.models.azure_keypair import AzureKeypair
from fcsm_eos_api_client.models.azure_keypair_generate import AzureKeypairGenerate
from fcsm_eos_api_client.models.azure_keypair_import import AzureKeypairImport
from fcsm_eos_api_client.models.azure_management_status import AzureManagementStatus
from fcsm_eos_api_client.models.azure_network import AzureNetwork
from fcsm_eos_api_client.models.azure_optional_workshift import AzureOptionalWorkshift
from fcsm_eos_api_client.models.azure_patch_volume import AzurePatchVolume
from fcsm_eos_api_client.models.azure_public_private_image import AzurePublicPrivateImage
from fcsm_eos_api_client.models.azure_region import AzureRegion
from fcsm_eos_api_client.models.azure_resource_group import AzureResourceGroup
from fcsm_eos_api_client.models.azure_security_group import AzureSecurityGroup
from fcsm_eos_api_client.models.azure_snapshot import AzureSnapshot
from fcsm_eos_api_client.models.azure_subnet import AzureSubnet
from fcsm_eos_api_client.models.azure_subscription import AzureSubscription
from fcsm_eos_api_client.models.azure_tag import AzureTag
from fcsm_eos_api_client.models.azure_tag_update import AzureTagUpdate
from fcsm_eos_api_client.models.azure_vm_create_data import AzureVMCreateData
from fcsm_eos_api_client.models.azure_vm_extended import AzureVMExtended
from fcsm_eos_api_client.models.azure_vm_extended_all_of import AzureVMExtendedAllOf
from fcsm_eos_api_client.models.azure_vm_patch import AzureVMPatch
from fcsm_eos_api_client.models.azure_vm_power_action import AzureVMPowerAction
from fcsm_eos_api_client.models.azure_vm_simple import AzureVMSimple
from fcsm_eos_api_client.models.azure_vm_details import AzureVmDetails
from fcsm_eos_api_client.models.azure_vm_floating_ip import AzureVmFloatingIp
from fcsm_eos_api_client.models.azure_volume import AzureVolume
from fcsm_eos_api_client.models.azure_volume_attachment import AzureVolumeAttachment
from fcsm_eos_api_client.models.azure_volume_status import AzureVolumeStatus
from fcsm_eos_api_client.models.azure_volume_type import AzureVolumeType
from fcsm_eos_api_client.models.azure_volume_type_id import AzureVolumeTypeId
from fcsm_eos_api_client.models.azure_workshift import AzureWorkshift
from fcsm_eos_api_client.models.azure_workshift_schedule import AzureWorkshiftSchedule
from fcsm_eos_api_client.models.config_configuration import ConfigConfiguration
from fcsm_eos_api_client.models.config_create_management_tool import ConfigCreateManagementTool
from fcsm_eos_api_client.models.config_mail_provider import ConfigMailProvider
from fcsm_eos_api_client.models.config_management_tool import ConfigManagementTool
from fcsm_eos_api_client.models.config_management_tool_type import ConfigManagementToolType
from fcsm_eos_api_client.models.config_platform_config import ConfigPlatformConfig
from fcsm_eos_api_client.models.config_unexpected_error import ConfigUnexpectedError
from fcsm_eos_api_client.models.config_update_management_tool import ConfigUpdateManagementTool
from fcsm_eos_api_client.models.img_whitelist_flavor import ImgWhitelistFlavor
from fcsm_eos_api_client.models.img_whitelist_http_error import ImgWhitelistHttpError
from fcsm_eos_api_client.models.img_whitelist_image import ImgWhitelistImage
from fcsm_eos_api_client.models.img_whitelist_image_add import ImgWhitelistImageAdd
from fcsm_eos_api_client.models.img_whitelist_image_update import ImgWhitelistImageUpdate
from fcsm_eos_api_client.models.img_whitelist_os_details import ImgWhitelistOSDetails
from fcsm_eos_api_client.models.img_whitelist_os_details_add_update import ImgWhitelistOSDetailsAddUpdate
from fcsm_eos_api_client.models.img_whitelist_whitelist import ImgWhitelistWhitelist
from fcsm_eos_api_client.models.inline_object import InlineObject
from fcsm_eos_api_client.models.inline_object1 import InlineObject1
from fcsm_eos_api_client.models.inline_object2 import InlineObject2
from fcsm_eos_api_client.models.inline_object3 import InlineObject3
from fcsm_eos_api_client.models.inline_response200 import InlineResponse200
from fcsm_eos_api_client.models.mgmt_app import MgmtApp
from fcsm_eos_api_client.models.mgmt_app_instance import MgmtAppInstance
from fcsm_eos_api_client.models.mgmt_application import MgmtApplication
from fcsm_eos_api_client.models.mgmt_bad_request import MgmtBadRequest
from fcsm_eos_api_client.models.mgmt_bootstrap_script import MgmtBootstrapScript
from fcsm_eos_api_client.models.mgmt_bootstrap_script_return import MgmtBootstrapScriptReturn
from fcsm_eos_api_client.models.mgmt_error import MgmtError
from fcsm_eos_api_client.models.mgmt_http_not_found_error import MgmtHttpNotFoundError
from fcsm_eos_api_client.models.mgmt_manage_vm import MgmtManageVm
from fcsm_eos_api_client.models.mgmt_managed_vms import MgmtManagedVms
from fcsm_eos_api_client.models.mgmt_register_vm import MgmtRegisterVm
from fcsm_eos_api_client.models.mgmt_replace_app import MgmtReplaceApp
from fcsm_eos_api_client.models.mgmt_subscrption import MgmtSubscrption
from fcsm_eos_api_client.models.mgmt_task import MgmtTask
from fcsm_eos_api_client.models.mgmt_tool_token import MgmtToolToken
from fcsm_eos_api_client.models.mgmt_vm_details import MgmtVmDetails
from fcsm_eos_api_client.models.mgmt_vm_details_params import MgmtVmDetailsParams
from fcsm_eos_api_client.models.notif_message import NotifMessage
from fcsm_eos_api_client.models.subscr_bad_request import SubscrBadRequest
from fcsm_eos_api_client.models.subscr_create_subscription import SubscrCreateSubscription
from fcsm_eos_api_client.models.subscr_error import SubscrError
from fcsm_eos_api_client.models.subscr_modify_subscription import SubscrModifySubscription
from fcsm_eos_api_client.models.subscr_policy import SubscrPolicy
from fcsm_eos_api_client.models.subscr_status import SubscrStatus
from fcsm_eos_api_client.models.subscr_subscription import SubscrSubscription
from fcsm_eos_api_client.models.subscr_tag import SubscrTag
from fcsm_eos_api_client.models.subscr_tag_rule import SubscrTagRule
from fcsm_eos_api_client.models.subscr_token import SubscrToken
from fcsm_eos_api_client.models.subscr_token_services import SubscrTokenServices
from fcsm_eos_api_client.models.subscr_virtual_machine import SubscrVirtualMachine
from fcsm_eos_api_client.models.subscr_virtual_machine_validation_parameters import SubscrVirtualMachineValidationParameters
from fcsm_eos_api_client.models.subscr_workshift import SubscrWorkshift
from fcsm_eos_api_client.models.subscr_workshift_rule import SubscrWorkshiftRule
from fcsm_eos_api_client.models.subscr_workshift_schedule import SubscrWorkshiftSchedule
from fcsm_eos_api_client.models.subscr_workshift_validation_parameters import SubscrWorkshiftValidationParameters
from fcsm_eos_api_client.models.tag_error import TagError
from fcsm_eos_api_client.models.tag_invalid_input import TagInvalidInput
from fcsm_eos_api_client.models.tag_service_unavailable import TagServiceUnavailable
from fcsm_eos_api_client.models.tag_tag import TagTag
from fcsm_eos_api_client.models.tag_tag_not_found import TagTagNotFound
from fcsm_eos_api_client.models.tag_tag_update import TagTagUpdate
from fcsm_eos_api_client.models.tag_tag_value import TagTagValue
from fcsm_eos_api_client.models.tag_unauthorized import TagUnauthorized
from fcsm_eos_api_client.models.tag_unexpected_error import TagUnexpectedError
from fcsm_eos_api_client.models.user_access_right import UserAccessRight
from fcsm_eos_api_client.models.user_credentials import UserCredentials
from fcsm_eos_api_client.models.user_error import UserError
from fcsm_eos_api_client.models.user_forbidden import UserForbidden
from fcsm_eos_api_client.models.user_forgotten_password import UserForgottenPassword
from fcsm_eos_api_client.models.user_invalid_credentials import UserInvalidCredentials
from fcsm_eos_api_client.models.user_invalid_input import UserInvalidInput
from fcsm_eos_api_client.models.user_not_found import UserNotFound
from fcsm_eos_api_client.models.user_password_reset import UserPasswordReset
from fcsm_eos_api_client.models.user_password_update import UserPasswordUpdate
from fcsm_eos_api_client.models.user_permissions import UserPermissions
from fcsm_eos_api_client.models.user_role_update import UserRoleUpdate
from fcsm_eos_api_client.models.user_service_unavailable import UserServiceUnavailable
from fcsm_eos_api_client.models.user_subscription_id import UserSubscriptionID
from fcsm_eos_api_client.models.user_token import UserToken
from fcsm_eos_api_client.models.user_unauthorized import UserUnauthorized
from fcsm_eos_api_client.models.user_unexpected_error import UserUnexpectedError
from fcsm_eos_api_client.models.user_update_user import UserUpdateUser
from fcsm_eos_api_client.models.user_user import UserUser
from fcsm_eos_api_client.models.vmware_action import VmwareAction
from fcsm_eos_api_client.models.vmware_availability_zone import VmwareAvailabilityZone
from fcsm_eos_api_client.models.vmware_create_snapshot import VmwareCreateSnapshot
from fcsm_eos_api_client.models.vmware_day import VmwareDay
from fcsm_eos_api_client.models.vmware_flavor import VmwareFlavor
from fcsm_eos_api_client.models.vmware_generate_keypair import VmwareGenerateKeypair
from fcsm_eos_api_client.models.vmware_i_pv4_address import VmwareIPv4Address
from fcsm_eos_api_client.models.vmware_image import VmwareImage
from fcsm_eos_api_client.models.vmware_import_keypair import VmwareImportKeypair
from fcsm_eos_api_client.models.vmware_interface import VmwareInterface
from fcsm_eos_api_client.models.vmware_interface_attachment import VmwareInterfaceAttachment
from fcsm_eos_api_client.models.vmware_keypair import VmwareKeypair
from fcsm_eos_api_client.models.vmware_management import VmwareManagement
from fcsm_eos_api_client.models.vmware_network import VmwareNetwork
from fcsm_eos_api_client.models.vmware_new_keypair import VmwareNewKeypair
from fcsm_eos_api_client.models.vmware_new_volume import VmwareNewVolume
from fcsm_eos_api_client.models.vmware_optional_workshift import VmwareOptionalWorkshift
from fcsm_eos_api_client.models.vmware_password import VmwarePassword
from fcsm_eos_api_client.models.vmware_power_state import VmwarePowerState
from fcsm_eos_api_client.models.vmware_public_private_image import VmwarePublicPrivateImage
from fcsm_eos_api_client.models.vmware_region import VmwareRegion
from fcsm_eos_api_client.models.vmware_snapshot import VmwareSnapshot
from fcsm_eos_api_client.models.vmware_status import VmwareStatus
from fcsm_eos_api_client.models.vmware_subnet import VmwareSubnet
from fcsm_eos_api_client.models.vmware_subscription import VmwareSubscription
from fcsm_eos_api_client.models.vmware_tag import VmwareTag
from fcsm_eos_api_client.models.vmware_tag_update import VmwareTagUpdate
from fcsm_eos_api_client.models.vmware_update_vm_params import VmwareUpdateVmParams
from fcsm_eos_api_client.models.vmware_update_volume_params import VmwareUpdateVolumeParams
from fcsm_eos_api_client.models.vmware_vm import VmwareVM
from fcsm_eos_api_client.models.vmware_vm_create import VmwareVMCreate
from fcsm_eos_api_client.models.vmware_v_mdetails import VmwareVMdetails
from fcsm_eos_api_client.models.vmware_vm_simple import VmwareVmSimple
from fcsm_eos_api_client.models.vmware_vmware_service_resources_status_get_response import VmwareVmwareServiceResourcesStatusGetResponse
from fcsm_eos_api_client.models.vmware_volume import VmwareVolume
from fcsm_eos_api_client.models.vmware_volume_attachment import VmwareVolumeAttachment
from fcsm_eos_api_client.models.vmware_volume_status import VmwareVolumeStatus
from fcsm_eos_api_client.models.vmware_volume_type import VmwareVolumeType
from fcsm_eos_api_client.models.vmware_workshift import VmwareWorkshift
from fcsm_eos_api_client.models.vmware_workshift_schedule import VmwareWorkshiftSchedule
from fcsm_eos_api_client.models.webhook_change_status_error import WebhookChangeStatusError
from fcsm_eos_api_client.models.webhook_error import WebhookError
from fcsm_eos_api_client.models.webhook_event_type import WebhookEventType
from fcsm_eos_api_client.models.webhook_invalid_input import WebhookInvalidInput
from fcsm_eos_api_client.models.webhook_service_unavailable import WebhookServiceUnavailable
from fcsm_eos_api_client.models.webhook_unauthorized import WebhookUnauthorized
from fcsm_eos_api_client.models.webhook_unexpected_error import WebhookUnexpectedError
from fcsm_eos_api_client.models.webhook_webhook import WebhookWebhook
from fcsm_eos_api_client.models.webhook_webhook_not_found import WebhookWebhookNotFound

