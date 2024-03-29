# coding: utf-8

"""
    Combined FCSM EOS API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.2.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import fcsm_eos_api_client
from fcsm_eos_api_client.api.vmware_api import VmwareApi  # noqa: E501
from fcsm_eos_api_client.rest import ApiException


class TestVmwareApi(unittest.TestCase):
    """VmwareApi unit test stubs"""

    def setUp(self):
        self.api = fcsm_eos_api_client.api.vmware_api.VmwareApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_vmware_service_resources_availability_zones_get(self):
        """Test case for vmware_service_resources_availability_zones_get

        List availability zones  # noqa: E501
        """
        pass

    def test_vmware_service_resources_flavor_get(self):
        """Test case for vmware_service_resources_flavor_get

        Get flavor by id  # noqa: E501
        """
        pass

    def test_vmware_service_resources_flavors_get(self):
        """Test case for vmware_service_resources_flavors_get

        List flavors  # noqa: E501
        """
        pass

    def test_vmware_service_resources_image_get(self):
        """Test case for vmware_service_resources_image_get

        Get image by id  # noqa: E501
        """
        pass

    def test_vmware_service_resources_image_get_private(self):
        """Test case for vmware_service_resources_image_get_private

        Get private image by id  # noqa: E501
        """
        pass

    def test_vmware_service_resources_image_get_public(self):
        """Test case for vmware_service_resources_image_get_public

        Get public image by id  # noqa: E501
        """
        pass

    def test_vmware_service_resources_images_get(self):
        """Test case for vmware_service_resources_images_get

        Get images  # noqa: E501
        """
        pass

    def test_vmware_service_resources_images_get_private(self):
        """Test case for vmware_service_resources_images_get_private

        Get private images  # noqa: E501
        """
        pass

    def test_vmware_service_resources_images_get_public(self):
        """Test case for vmware_service_resources_images_get_public

        Get public images  # noqa: E501
        """
        pass

    def test_vmware_service_resources_interfaces_get(self):
        """Test case for vmware_service_resources_interfaces_get

        List network interfaces  # noqa: E501
        """
        pass

    def test_vmware_service_resources_keypair_delete(self):
        """Test case for vmware_service_resources_keypair_delete

        Delete a keypair  # noqa: E501
        """
        pass

    def test_vmware_service_resources_keypairs_get(self):
        """Test case for vmware_service_resources_keypairs_get

        List keypairs  # noqa: E501
        """
        pass

    def test_vmware_service_resources_keypairs_post(self):
        """Test case for vmware_service_resources_keypairs_post

        Create a new keypair  # noqa: E501
        """
        pass

    def test_vmware_service_resources_keypairs_upload(self):
        """Test case for vmware_service_resources_keypairs_upload

        Import a keypair  # noqa: E501
        """
        pass

    def test_vmware_service_resources_management_get(self):
        """Test case for vmware_service_resources_management_get

        Get VM management status  # noqa: E501
        """
        pass

    def test_vmware_service_resources_networks_get(self):
        """Test case for vmware_service_resources_networks_get

        List networks  # noqa: E501
        """
        pass

    def test_vmware_service_resources_regions_get(self):
        """Test case for vmware_service_resources_regions_get

        List regions  # noqa: E501
        """
        pass

    def test_vmware_service_resources_security_groups_get(self):
        """Test case for vmware_service_resources_security_groups_get

        List security groups  # noqa: E501
        """
        pass

    def test_vmware_service_resources_snapshot_delete(self):
        """Test case for vmware_service_resources_snapshot_delete

        Delete snapshot  # noqa: E501
        """
        pass

    def test_vmware_service_resources_snapshots_get(self):
        """Test case for vmware_service_resources_snapshots_get

        List snapshots  # noqa: E501
        """
        pass

    def test_vmware_service_resources_snapshots_post(self):
        """Test case for vmware_service_resources_snapshots_post

        Create a new snapshot  # noqa: E501
        """
        pass

    def test_vmware_service_resources_subnets_get(self):
        """Test case for vmware_service_resources_subnets_get

        List network subnets  # noqa: E501
        """
        pass

    def test_vmware_service_resources_validate_subscription_post(self):
        """Test case for vmware_service_resources_validate_subscription_post

        Validate subscription  # noqa: E501
        """
        pass

    def test_vmware_service_resources_vm_command_put(self):
        """Test case for vmware_service_resources_vm_command_put

        Execute a power action on a VM  # noqa: E501
        """
        pass

    def test_vmware_service_resources_vm_delete(self):
        """Test case for vmware_service_resources_vm_delete

        Delete a VM  # noqa: E501
        """
        pass

    def test_vmware_service_resources_vm_details_get(self):
        """Test case for vmware_service_resources_vm_details_get

        Get VM details  # noqa: E501
        """
        pass

    def test_vmware_service_resources_vm_get(self):
        """Test case for vmware_service_resources_vm_get

        Get VM by id  # noqa: E501
        """
        pass

    def test_vmware_service_resources_vm_password_get(self):
        """Test case for vmware_service_resources_vm_password_get

        Get the VM password  # noqa: E501
        """
        pass

    def test_vmware_service_resources_vm_patch(self):
        """Test case for vmware_service_resources_vm_patch

        Update VM  # noqa: E501
        """
        pass

    def test_vmware_service_resources_vm_tag_put(self):
        """Test case for vmware_service_resources_vm_tag_put

        Tag VM  # noqa: E501
        """
        pass

    def test_vmware_service_resources_vm_workshift_delete(self):
        """Test case for vmware_service_resources_vm_workshift_delete

        Delete the VM Workshift  # noqa: E501
        """
        pass

    def test_vmware_service_resources_vm_workshift_put(self):
        """Test case for vmware_service_resources_vm_workshift_put

        Update the VM workshift  # noqa: E501
        """
        pass

    def test_vmware_service_resources_vm_workshifts_post(self):
        """Test case for vmware_service_resources_vm_workshifts_post

        Add a workshift to the VM  # noqa: E501
        """
        pass

    def test_vmware_service_resources_vms_get(self):
        """Test case for vmware_service_resources_vms_get

        List VMs  # noqa: E501
        """
        pass

    def test_vmware_service_resources_vms_post(self):
        """Test case for vmware_service_resources_vms_post

        Create a VM  # noqa: E501
        """
        pass

    def test_vmware_service_resources_volume_attachment_delete(self):
        """Test case for vmware_service_resources_volume_attachment_delete

        Dettaches and deletes a volume  # noqa: E501
        """
        pass

    def test_vmware_service_resources_volume_patch(self):
        """Test case for vmware_service_resources_volume_patch

        Update a volume  # noqa: E501
        """
        pass

    def test_vmware_service_resources_volume_types_get(self):
        """Test case for vmware_service_resources_volume_types_get

        List volume types  # noqa: E501
        """
        pass

    def test_vmware_service_resources_volumes_get(self):
        """Test case for vmware_service_resources_volumes_get

        List volumes  # noqa: E501
        """
        pass

    def test_vmware_service_resources_volumes_post(self):
        """Test case for vmware_service_resources_volumes_post

        Create a new volume  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
