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


class AzureCreateVolume(object):
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
        'size': 'int',
        'type_id': 'AzureVolumeTypeId',
        'resource_group_id': 'str',
        'availability_zone_id': 'str',
        'availability_zone': 'str',
        'vm_id': 'AnyOfstringobject'
    }

    attribute_map = {
        'name': 'name',
        'size': 'size',
        'type_id': 'typeId',
        'resource_group_id': 'resourceGroupId',
        'availability_zone_id': 'availabilityZoneId',
        'availability_zone': 'availabilityZone',
        'vm_id': 'vmId'
    }

    def __init__(self, name=None, size=None, type_id=None, resource_group_id=None, availability_zone_id='default', availability_zone=None, vm_id=None):  # noqa: E501
        """AzureCreateVolume - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._size = None
        self._type_id = None
        self._resource_group_id = None
        self._availability_zone_id = None
        self._availability_zone = None
        self._vm_id = None
        self.discriminator = None

        self.name = name
        self.size = size
        self.type_id = type_id
        self.resource_group_id = resource_group_id
        if availability_zone_id is not None:
            self.availability_zone_id = availability_zone_id
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if vm_id is not None:
            self.vm_id = vm_id

    @property
    def name(self):
        """Gets the name of this AzureCreateVolume.  # noqa: E501


        :return: The name of this AzureCreateVolume.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AzureCreateVolume.


        :param name: The name of this AzureCreateVolume.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 60:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `60`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501
        if name is not None and not re.search(r'^[a-zA-Z0-9]+[a-zA-Z0-9_.-]*\w$', name):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^[a-zA-Z0-9]+[a-zA-Z0-9_.-]*\w$/`")  # noqa: E501

        self._name = name

    @property
    def size(self):
        """Gets the size of this AzureCreateVolume.  # noqa: E501


        :return: The size of this AzureCreateVolume.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this AzureCreateVolume.


        :param size: The size of this AzureCreateVolume.  # noqa: E501
        :type: int
        """
        if size is None:
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

    @property
    def type_id(self):
        """Gets the type_id of this AzureCreateVolume.  # noqa: E501


        :return: The type_id of this AzureCreateVolume.  # noqa: E501
        :rtype: AzureVolumeTypeId
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this AzureCreateVolume.


        :param type_id: The type_id of this AzureCreateVolume.  # noqa: E501
        :type: AzureVolumeTypeId
        """
        if type_id is None:
            raise ValueError("Invalid value for `type_id`, must not be `None`")  # noqa: E501

        self._type_id = type_id

    @property
    def resource_group_id(self):
        """Gets the resource_group_id of this AzureCreateVolume.  # noqa: E501


        :return: The resource_group_id of this AzureCreateVolume.  # noqa: E501
        :rtype: str
        """
        return self._resource_group_id

    @resource_group_id.setter
    def resource_group_id(self, resource_group_id):
        """Sets the resource_group_id of this AzureCreateVolume.


        :param resource_group_id: The resource_group_id of this AzureCreateVolume.  # noqa: E501
        :type: str
        """
        if resource_group_id is None:
            raise ValueError("Invalid value for `resource_group_id`, must not be `None`")  # noqa: E501

        self._resource_group_id = resource_group_id

    @property
    def availability_zone_id(self):
        """Gets the availability_zone_id of this AzureCreateVolume.  # noqa: E501


        :return: The availability_zone_id of this AzureCreateVolume.  # noqa: E501
        :rtype: str
        """
        return self._availability_zone_id

    @availability_zone_id.setter
    def availability_zone_id(self, availability_zone_id):
        """Sets the availability_zone_id of this AzureCreateVolume.


        :param availability_zone_id: The availability_zone_id of this AzureCreateVolume.  # noqa: E501
        :type: str
        """

        self._availability_zone_id = availability_zone_id

    @property
    def availability_zone(self):
        """Gets the availability_zone of this AzureCreateVolume.  # noqa: E501

        Deprecated after 3 months. Please use `availabilityZoneId`  # noqa: E501

        :return: The availability_zone of this AzureCreateVolume.  # noqa: E501
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this AzureCreateVolume.

        Deprecated after 3 months. Please use `availabilityZoneId`  # noqa: E501

        :param availability_zone: The availability_zone of this AzureCreateVolume.  # noqa: E501
        :type: str
        """

        self._availability_zone = availability_zone

    @property
    def vm_id(self):
        """Gets the vm_id of this AzureCreateVolume.  # noqa: E501


        :return: The vm_id of this AzureCreateVolume.  # noqa: E501
        :rtype: AnyOfstringobject
        """
        return self._vm_id

    @vm_id.setter
    def vm_id(self, vm_id):
        """Sets the vm_id of this AzureCreateVolume.


        :param vm_id: The vm_id of this AzureCreateVolume.  # noqa: E501
        :type: AnyOfstringobject
        """

        self._vm_id = vm_id

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
        if not isinstance(other, AzureCreateVolume):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
