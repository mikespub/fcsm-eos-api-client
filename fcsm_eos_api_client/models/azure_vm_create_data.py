# coding: utf-8

"""
    Combined FCSM EOS API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.2.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class AzureVMCreateData(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'name': 'str',
        'resource_group_id': 'str',
        'flavor_id': 'str',
        'image_id': 'str',
        'keypair_id': 'str',
        'volume_size': 'int',
        'volume_type_id': 'AzureVolumeTypeId',
        'tags': 'list[AzureTag]',
        'workshift': 'AzureOptionalWorkshift',
        'security_groups': 'list[str]',
        'security_group_ids': 'list[str]',
        'avalability_zone': 'str',
        'availability_zone_id': 'str',
        'availability_set_id': 'str',
        'nics': 'list[str]',
        'subnet_id': 'str',
        'management_enabled': 'bool',
        'management_tool_id': 'AnyOfUUIDobject'
    }

    attribute_map = {
        'name': 'name',
        'resource_group_id': 'resourceGroupId',
        'flavor_id': 'flavorId',
        'image_id': 'imageId',
        'keypair_id': 'keypairId',
        'volume_size': 'volumeSize',
        'volume_type_id': 'volumeTypeId',
        'tags': 'tags',
        'workshift': 'workshift',
        'security_groups': 'securityGroups',
        'security_group_ids': 'securityGroupIds',
        'avalability_zone': 'avalabilityZone',
        'availability_zone_id': 'availabilityZoneId',
        'availability_set_id': 'availabilitySetId',
        'nics': 'nics',
        'subnet_id': 'subnetId',
        'management_enabled': 'managementEnabled',
        'management_tool_id': 'managementToolId'
    }

    def __init__(self, name=None, resource_group_id=None, flavor_id=None, image_id=None, keypair_id=None, volume_size=None, volume_type_id=None, tags=None, workshift=None, security_groups=None, security_group_ids=None, avalability_zone=None, availability_zone_id='default', availability_set_id=None, nics=None, subnet_id=None, management_enabled=None, management_tool_id=None):  # noqa: E501
        """AzureVMCreateData - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._resource_group_id = None
        self._flavor_id = None
        self._image_id = None
        self._keypair_id = None
        self._volume_size = None
        self._volume_type_id = None
        self._tags = None
        self._workshift = None
        self._security_groups = None
        self._security_group_ids = None
        self._avalability_zone = None
        self._availability_zone_id = None
        self._availability_set_id = None
        self._nics = None
        self._subnet_id = None
        self._management_enabled = None
        self._management_tool_id = None
        self.discriminator = None

        self.name = name
        self.resource_group_id = resource_group_id
        self.flavor_id = flavor_id
        self.image_id = image_id
        self.keypair_id = keypair_id
        self.volume_size = volume_size
        self.volume_type_id = volume_type_id
        self.tags = tags
        if workshift is not None:
            self.workshift = workshift
        if security_groups is not None:
            self.security_groups = security_groups
        if security_group_ids is not None:
            self.security_group_ids = security_group_ids
        if avalability_zone is not None:
            self.avalability_zone = avalability_zone
        if availability_zone_id is not None:
            self.availability_zone_id = availability_zone_id
        if availability_set_id is not None:
            self.availability_set_id = availability_set_id
        if nics is not None:
            self.nics = nics
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if management_enabled is not None:
            self.management_enabled = management_enabled
        if management_tool_id is not None:
            self.management_tool_id = management_tool_id

    @property
    def name(self):
        """Gets the name of this AzureVMCreateData.  # noqa: E501


        :return: The name of this AzureVMCreateData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AzureVMCreateData.


        :param name: The name of this AzureVMCreateData.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and not re.search(r'^(?!-)[A-Za-z0-9-_]{1,63}(?<!-)$', name):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^(?!-)[A-Za-z0-9-_]{1,63}(?<!-)$/`")  # noqa: E501

        self._name = name

    @property
    def resource_group_id(self):
        """Gets the resource_group_id of this AzureVMCreateData.  # noqa: E501


        :return: The resource_group_id of this AzureVMCreateData.  # noqa: E501
        :rtype: str
        """
        return self._resource_group_id

    @resource_group_id.setter
    def resource_group_id(self, resource_group_id):
        """Sets the resource_group_id of this AzureVMCreateData.


        :param resource_group_id: The resource_group_id of this AzureVMCreateData.  # noqa: E501
        :type: str
        """
        if resource_group_id is None:
            raise ValueError("Invalid value for `resource_group_id`, must not be `None`")  # noqa: E501

        self._resource_group_id = resource_group_id

    @property
    def flavor_id(self):
        """Gets the flavor_id of this AzureVMCreateData.  # noqa: E501


        :return: The flavor_id of this AzureVMCreateData.  # noqa: E501
        :rtype: str
        """
        return self._flavor_id

    @flavor_id.setter
    def flavor_id(self, flavor_id):
        """Sets the flavor_id of this AzureVMCreateData.


        :param flavor_id: The flavor_id of this AzureVMCreateData.  # noqa: E501
        :type: str
        """
        if flavor_id is None:
            raise ValueError("Invalid value for `flavor_id`, must not be `None`")  # noqa: E501

        self._flavor_id = flavor_id

    @property
    def image_id(self):
        """Gets the image_id of this AzureVMCreateData.  # noqa: E501


        :return: The image_id of this AzureVMCreateData.  # noqa: E501
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this AzureVMCreateData.


        :param image_id: The image_id of this AzureVMCreateData.  # noqa: E501
        :type: str
        """
        if image_id is None:
            raise ValueError("Invalid value for `image_id`, must not be `None`")  # noqa: E501
        if image_id is not None and len(image_id) < 1:
            raise ValueError("Invalid value for `image_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._image_id = image_id

    @property
    def keypair_id(self):
        """Gets the keypair_id of this AzureVMCreateData.  # noqa: E501


        :return: The keypair_id of this AzureVMCreateData.  # noqa: E501
        :rtype: str
        """
        return self._keypair_id

    @keypair_id.setter
    def keypair_id(self, keypair_id):
        """Sets the keypair_id of this AzureVMCreateData.


        :param keypair_id: The keypair_id of this AzureVMCreateData.  # noqa: E501
        :type: str
        """
        if keypair_id is None:
            raise ValueError("Invalid value for `keypair_id`, must not be `None`")  # noqa: E501
        if keypair_id is not None and len(keypair_id) > 60:
            raise ValueError("Invalid value for `keypair_id`, length must be less than or equal to `60`")  # noqa: E501
        if keypair_id is not None and len(keypair_id) < 1:
            raise ValueError("Invalid value for `keypair_id`, length must be greater than or equal to `1`")  # noqa: E501
        if keypair_id is not None and not re.search(r'^[a-zA-Z0-9_-]+$', keypair_id):  # noqa: E501
            raise ValueError(r"Invalid value for `keypair_id`, must be a follow pattern or equal to `/^[a-zA-Z0-9_-]+$/`")  # noqa: E501

        self._keypair_id = keypair_id

    @property
    def volume_size(self):
        """Gets the volume_size of this AzureVMCreateData.  # noqa: E501


        :return: The volume_size of this AzureVMCreateData.  # noqa: E501
        :rtype: int
        """
        return self._volume_size

    @volume_size.setter
    def volume_size(self, volume_size):
        """Sets the volume_size of this AzureVMCreateData.


        :param volume_size: The volume_size of this AzureVMCreateData.  # noqa: E501
        :type: int
        """
        if volume_size is None:
            raise ValueError("Invalid value for `volume_size`, must not be `None`")  # noqa: E501
        if volume_size is not None and volume_size > 1000:  # noqa: E501
            raise ValueError("Invalid value for `volume_size`, must be a value less than or equal to `1000`")  # noqa: E501

        self._volume_size = volume_size

    @property
    def volume_type_id(self):
        """Gets the volume_type_id of this AzureVMCreateData.  # noqa: E501


        :return: The volume_type_id of this AzureVMCreateData.  # noqa: E501
        :rtype: AzureVolumeTypeId
        """
        return self._volume_type_id

    @volume_type_id.setter
    def volume_type_id(self, volume_type_id):
        """Sets the volume_type_id of this AzureVMCreateData.


        :param volume_type_id: The volume_type_id of this AzureVMCreateData.  # noqa: E501
        :type: AzureVolumeTypeId
        """
        if volume_type_id is None:
            raise ValueError("Invalid value for `volume_type_id`, must not be `None`")  # noqa: E501

        self._volume_type_id = volume_type_id

    @property
    def tags(self):
        """Gets the tags of this AzureVMCreateData.  # noqa: E501


        :return: The tags of this AzureVMCreateData.  # noqa: E501
        :rtype: list[AzureTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this AzureVMCreateData.


        :param tags: The tags of this AzureVMCreateData.  # noqa: E501
        :type: list[AzureTag]
        """
        if tags is None:
            raise ValueError("Invalid value for `tags`, must not be `None`")  # noqa: E501

        self._tags = tags

    @property
    def workshift(self):
        """Gets the workshift of this AzureVMCreateData.  # noqa: E501


        :return: The workshift of this AzureVMCreateData.  # noqa: E501
        :rtype: AzureOptionalWorkshift
        """
        return self._workshift

    @workshift.setter
    def workshift(self, workshift):
        """Sets the workshift of this AzureVMCreateData.


        :param workshift: The workshift of this AzureVMCreateData.  # noqa: E501
        :type: AzureOptionalWorkshift
        """

        self._workshift = workshift

    @property
    def security_groups(self):
        """Gets the security_groups of this AzureVMCreateData.  # noqa: E501

        \"securityGroups\" is deprecated in favor of \"securityGroupIds\" and will be removed in 3 months.  # noqa: E501

        :return: The security_groups of this AzureVMCreateData.  # noqa: E501
        :rtype: list[str]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """Sets the security_groups of this AzureVMCreateData.

        \"securityGroups\" is deprecated in favor of \"securityGroupIds\" and will be removed in 3 months.  # noqa: E501

        :param security_groups: The security_groups of this AzureVMCreateData.  # noqa: E501
        :type: list[str]
        """

        self._security_groups = security_groups

    @property
    def security_group_ids(self):
        """Gets the security_group_ids of this AzureVMCreateData.  # noqa: E501


        :return: The security_group_ids of this AzureVMCreateData.  # noqa: E501
        :rtype: list[str]
        """
        return self._security_group_ids

    @security_group_ids.setter
    def security_group_ids(self, security_group_ids):
        """Sets the security_group_ids of this AzureVMCreateData.


        :param security_group_ids: The security_group_ids of this AzureVMCreateData.  # noqa: E501
        :type: list[str]
        """

        self._security_group_ids = security_group_ids

    @property
    def avalability_zone(self):
        """Gets the avalability_zone of this AzureVMCreateData.  # noqa: E501


        :return: The avalability_zone of this AzureVMCreateData.  # noqa: E501
        :rtype: str
        """
        return self._avalability_zone

    @avalability_zone.setter
    def avalability_zone(self, avalability_zone):
        """Sets the avalability_zone of this AzureVMCreateData.


        :param avalability_zone: The avalability_zone of this AzureVMCreateData.  # noqa: E501
        :type: str
        """

        self._avalability_zone = avalability_zone

    @property
    def availability_zone_id(self):
        """Gets the availability_zone_id of this AzureVMCreateData.  # noqa: E501


        :return: The availability_zone_id of this AzureVMCreateData.  # noqa: E501
        :rtype: str
        """
        return self._availability_zone_id

    @availability_zone_id.setter
    def availability_zone_id(self, availability_zone_id):
        """Sets the availability_zone_id of this AzureVMCreateData.


        :param availability_zone_id: The availability_zone_id of this AzureVMCreateData.  # noqa: E501
        :type: str
        """

        self._availability_zone_id = availability_zone_id

    @property
    def availability_set_id(self):
        """Gets the availability_set_id of this AzureVMCreateData.  # noqa: E501


        :return: The availability_set_id of this AzureVMCreateData.  # noqa: E501
        :rtype: str
        """
        return self._availability_set_id

    @availability_set_id.setter
    def availability_set_id(self, availability_set_id):
        """Sets the availability_set_id of this AzureVMCreateData.


        :param availability_set_id: The availability_set_id of this AzureVMCreateData.  # noqa: E501
        :type: str
        """

        self._availability_set_id = availability_set_id

    @property
    def nics(self):
        """Gets the nics of this AzureVMCreateData.  # noqa: E501

        \"nics\" is deprecated in favor of \"subnetId\" and will be removed in 3 months.  # noqa: E501

        :return: The nics of this AzureVMCreateData.  # noqa: E501
        :rtype: list[str]
        """
        return self._nics

    @nics.setter
    def nics(self, nics):
        """Sets the nics of this AzureVMCreateData.

        \"nics\" is deprecated in favor of \"subnetId\" and will be removed in 3 months.  # noqa: E501

        :param nics: The nics of this AzureVMCreateData.  # noqa: E501
        :type: list[str]
        """

        self._nics = nics

    @property
    def subnet_id(self):
        """Gets the subnet_id of this AzureVMCreateData.  # noqa: E501


        :return: The subnet_id of this AzureVMCreateData.  # noqa: E501
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this AzureVMCreateData.


        :param subnet_id: The subnet_id of this AzureVMCreateData.  # noqa: E501
        :type: str
        """

        self._subnet_id = subnet_id

    @property
    def management_enabled(self):
        """Gets the management_enabled of this AzureVMCreateData.  # noqa: E501

        \"managementEnabled\" is deprecated in favor of \"managementToolId\" and will be removed in 3 months.  # noqa: E501

        :return: The management_enabled of this AzureVMCreateData.  # noqa: E501
        :rtype: bool
        """
        return self._management_enabled

    @management_enabled.setter
    def management_enabled(self, management_enabled):
        """Sets the management_enabled of this AzureVMCreateData.

        \"managementEnabled\" is deprecated in favor of \"managementToolId\" and will be removed in 3 months.  # noqa: E501

        :param management_enabled: The management_enabled of this AzureVMCreateData.  # noqa: E501
        :type: bool
        """

        self._management_enabled = management_enabled

    @property
    def management_tool_id(self):
        """Gets the management_tool_id of this AzureVMCreateData.  # noqa: E501


        :return: The management_tool_id of this AzureVMCreateData.  # noqa: E501
        :rtype: AnyOfUUIDobject
        """
        return self._management_tool_id

    @management_tool_id.setter
    def management_tool_id(self, management_tool_id):
        """Sets the management_tool_id of this AzureVMCreateData.


        :param management_tool_id: The management_tool_id of this AzureVMCreateData.  # noqa: E501
        :type: AnyOfUUIDobject
        """

        self._management_tool_id = management_tool_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AzureVMCreateData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
