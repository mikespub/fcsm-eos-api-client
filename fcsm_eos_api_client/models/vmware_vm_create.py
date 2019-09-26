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


class VmwareVMCreate(object):
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
        'availability_zone': 'str',
        'flavor_id': 'str',
        'image_id': 'str',
        'keypair_id': 'str',
        'management_enabled': 'bool',
        'management_tool_id': 'str',
        'name': 'str',
        'nics': 'list[str]',
        'security_groups': 'list[str]',
        'subnet_id': 'str',
        'tags': 'list[VmwareTag]',
        'volume_size': 'int',
        'volume_type_id': 'str',
        'workshift': 'VmwareOptionalWorkshift'
    }

    attribute_map = {
        'availability_zone': 'availabilityZone',
        'flavor_id': 'flavorId',
        'image_id': 'imageId',
        'keypair_id': 'keypairId',
        'management_enabled': 'managementEnabled',
        'management_tool_id': 'managementToolId',
        'name': 'name',
        'nics': 'nics',
        'security_groups': 'securityGroups',
        'subnet_id': 'subnetId',
        'tags': 'tags',
        'volume_size': 'volumeSize',
        'volume_type_id': 'volumeTypeId',
        'workshift': 'workshift'
    }

    def __init__(self, availability_zone=None, flavor_id=None, image_id=None, keypair_id=None, management_enabled=None, management_tool_id=None, name=None, nics=None, security_groups=None, subnet_id=None, tags=None, volume_size=None, volume_type_id=None, workshift=None):  # noqa: E501
        """VmwareVMCreate - a model defined in OpenAPI"""  # noqa: E501

        self._availability_zone = None
        self._flavor_id = None
        self._image_id = None
        self._keypair_id = None
        self._management_enabled = None
        self._management_tool_id = None
        self._name = None
        self._nics = None
        self._security_groups = None
        self._subnet_id = None
        self._tags = None
        self._volume_size = None
        self._volume_type_id = None
        self._workshift = None
        self.discriminator = None

        self.availability_zone = availability_zone
        self.flavor_id = flavor_id
        self.image_id = image_id
        self.keypair_id = keypair_id
        if management_enabled is not None:
            self.management_enabled = management_enabled
        self.management_tool_id = management_tool_id
        self.name = name
        if nics is not None:
            self.nics = nics
        self.security_groups = security_groups
        if subnet_id is not None:
            self.subnet_id = subnet_id
        self.tags = tags
        self.volume_size = volume_size
        self.volume_type_id = volume_type_id
        self.workshift = workshift

    @property
    def availability_zone(self):
        """Gets the availability_zone of this VmwareVMCreate.  # noqa: E501

        Availability zone  # noqa: E501

        :return: The availability_zone of this VmwareVMCreate.  # noqa: E501
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this VmwareVMCreate.

        Availability zone  # noqa: E501

        :param availability_zone: The availability_zone of this VmwareVMCreate.  # noqa: E501
        :type: str
        """
        if availability_zone is None:
            raise ValueError("Invalid value for `availability_zone`, must not be `None`")  # noqa: E501

        self._availability_zone = availability_zone

    @property
    def flavor_id(self):
        """Gets the flavor_id of this VmwareVMCreate.  # noqa: E501

        Flavor id  # noqa: E501

        :return: The flavor_id of this VmwareVMCreate.  # noqa: E501
        :rtype: str
        """
        return self._flavor_id

    @flavor_id.setter
    def flavor_id(self, flavor_id):
        """Sets the flavor_id of this VmwareVMCreate.

        Flavor id  # noqa: E501

        :param flavor_id: The flavor_id of this VmwareVMCreate.  # noqa: E501
        :type: str
        """
        if flavor_id is None:
            raise ValueError("Invalid value for `flavor_id`, must not be `None`")  # noqa: E501

        self._flavor_id = flavor_id

    @property
    def image_id(self):
        """Gets the image_id of this VmwareVMCreate.  # noqa: E501

        Id of an image used for VM creation  # noqa: E501

        :return: The image_id of this VmwareVMCreate.  # noqa: E501
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this VmwareVMCreate.

        Id of an image used for VM creation  # noqa: E501

        :param image_id: The image_id of this VmwareVMCreate.  # noqa: E501
        :type: str
        """
        if image_id is None:
            raise ValueError("Invalid value for `image_id`, must not be `None`")  # noqa: E501

        self._image_id = image_id

    @property
    def keypair_id(self):
        """Gets the keypair_id of this VmwareVMCreate.  # noqa: E501

        Keypair id  # noqa: E501

        :return: The keypair_id of this VmwareVMCreate.  # noqa: E501
        :rtype: str
        """
        return self._keypair_id

    @keypair_id.setter
    def keypair_id(self, keypair_id):
        """Sets the keypair_id of this VmwareVMCreate.

        Keypair id  # noqa: E501

        :param keypair_id: The keypair_id of this VmwareVMCreate.  # noqa: E501
        :type: str
        """
        if keypair_id is None:
            raise ValueError("Invalid value for `keypair_id`, must not be `None`")  # noqa: E501

        self._keypair_id = keypair_id

    @property
    def management_enabled(self):
        """Gets the management_enabled of this VmwareVMCreate.  # noqa: E501

        Specifies if management of a VM in EOS is enabled  # noqa: E501

        :return: The management_enabled of this VmwareVMCreate.  # noqa: E501
        :rtype: bool
        """
        return self._management_enabled

    @management_enabled.setter
    def management_enabled(self, management_enabled):
        """Sets the management_enabled of this VmwareVMCreate.

        Specifies if management of a VM in EOS is enabled  # noqa: E501

        :param management_enabled: The management_enabled of this VmwareVMCreate.  # noqa: E501
        :type: bool
        """

        self._management_enabled = management_enabled

    @property
    def management_tool_id(self):
        """Gets the management_tool_id of this VmwareVMCreate.  # noqa: E501


        :return: The management_tool_id of this VmwareVMCreate.  # noqa: E501
        :rtype: str
        """
        return self._management_tool_id

    @management_tool_id.setter
    def management_tool_id(self, management_tool_id):
        """Sets the management_tool_id of this VmwareVMCreate.


        :param management_tool_id: The management_tool_id of this VmwareVMCreate.  # noqa: E501
        :type: str
        """

        self._management_tool_id = management_tool_id

    @property
    def name(self):
        """Gets the name of this VmwareVMCreate.  # noqa: E501

        VM name  # noqa: E501

        :return: The name of this VmwareVMCreate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VmwareVMCreate.

        VM name  # noqa: E501

        :param name: The name of this VmwareVMCreate.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def nics(self):
        """Gets the nics of this VmwareVMCreate.  # noqa: E501

        List of network ids  # noqa: E501

        :return: The nics of this VmwareVMCreate.  # noqa: E501
        :rtype: list[str]
        """
        return self._nics

    @nics.setter
    def nics(self, nics):
        """Sets the nics of this VmwareVMCreate.

        List of network ids  # noqa: E501

        :param nics: The nics of this VmwareVMCreate.  # noqa: E501
        :type: list[str]
        """

        self._nics = nics

    @property
    def security_groups(self):
        """Gets the security_groups of this VmwareVMCreate.  # noqa: E501

        List of security group ids. The list is always empty because there are no security groups in VMware.  # noqa: E501

        :return: The security_groups of this VmwareVMCreate.  # noqa: E501
        :rtype: list[str]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """Sets the security_groups of this VmwareVMCreate.

        List of security group ids. The list is always empty because there are no security groups in VMware.  # noqa: E501

        :param security_groups: The security_groups of this VmwareVMCreate.  # noqa: E501
        :type: list[str]
        """
        if security_groups is None:
            raise ValueError("Invalid value for `security_groups`, must not be `None`")  # noqa: E501

        self._security_groups = security_groups

    @property
    def subnet_id(self):
        """Gets the subnet_id of this VmwareVMCreate.  # noqa: E501

        Subnet id in which VM should be created  # noqa: E501

        :return: The subnet_id of this VmwareVMCreate.  # noqa: E501
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this VmwareVMCreate.

        Subnet id in which VM should be created  # noqa: E501

        :param subnet_id: The subnet_id of this VmwareVMCreate.  # noqa: E501
        :type: str
        """

        self._subnet_id = subnet_id

    @property
    def tags(self):
        """Gets the tags of this VmwareVMCreate.  # noqa: E501

        Tags (name and value) assigned to this VM  # noqa: E501

        :return: The tags of this VmwareVMCreate.  # noqa: E501
        :rtype: list[VmwareTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this VmwareVMCreate.

        Tags (name and value) assigned to this VM  # noqa: E501

        :param tags: The tags of this VmwareVMCreate.  # noqa: E501
        :type: list[VmwareTag]
        """
        if tags is None:
            raise ValueError("Invalid value for `tags`, must not be `None`")  # noqa: E501

        self._tags = tags

    @property
    def volume_size(self):
        """Gets the volume_size of this VmwareVMCreate.  # noqa: E501

        Volume size in GB  # noqa: E501

        :return: The volume_size of this VmwareVMCreate.  # noqa: E501
        :rtype: int
        """
        return self._volume_size

    @volume_size.setter
    def volume_size(self, volume_size):
        """Sets the volume_size of this VmwareVMCreate.

        Volume size in GB  # noqa: E501

        :param volume_size: The volume_size of this VmwareVMCreate.  # noqa: E501
        :type: int
        """
        if volume_size is None:
            raise ValueError("Invalid value for `volume_size`, must not be `None`")  # noqa: E501

        self._volume_size = volume_size

    @property
    def volume_type_id(self):
        """Gets the volume_type_id of this VmwareVMCreate.  # noqa: E501

        Volume type id that will be used for OS volume  # noqa: E501

        :return: The volume_type_id of this VmwareVMCreate.  # noqa: E501
        :rtype: str
        """
        return self._volume_type_id

    @volume_type_id.setter
    def volume_type_id(self, volume_type_id):
        """Sets the volume_type_id of this VmwareVMCreate.

        Volume type id that will be used for OS volume  # noqa: E501

        :param volume_type_id: The volume_type_id of this VmwareVMCreate.  # noqa: E501
        :type: str
        """
        if volume_type_id is None:
            raise ValueError("Invalid value for `volume_type_id`, must not be `None`")  # noqa: E501

        self._volume_type_id = volume_type_id

    @property
    def workshift(self):
        """Gets the workshift of this VmwareVMCreate.  # noqa: E501


        :return: The workshift of this VmwareVMCreate.  # noqa: E501
        :rtype: VmwareOptionalWorkshift
        """
        return self._workshift

    @workshift.setter
    def workshift(self, workshift):
        """Sets the workshift of this VmwareVMCreate.


        :param workshift: The workshift of this VmwareVMCreate.  # noqa: E501
        :type: VmwareOptionalWorkshift
        """

        self._workshift = workshift

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
        if not isinstance(other, VmwareVMCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other