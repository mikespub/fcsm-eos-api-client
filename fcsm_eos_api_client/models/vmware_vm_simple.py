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


class VmwareVmSimple(object):
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
        'availability_zone_id': 'str',
        'created_at': 'str',
        'flavor_id': 'str',
        'id': 'str',
        'image_id': 'str',
        'is_managed': 'bool',
        'management_tool_id': 'str',
        'name': 'str',
        'power_state': 'VmwarePowerState',
        'tags': 'list[VmwareTag]'
    }

    attribute_map = {
        'availability_zone': 'availabilityZone',
        'availability_zone_id': 'availabilityZoneId',
        'created_at': 'createdAt',
        'flavor_id': 'flavorId',
        'id': 'id',
        'image_id': 'imageId',
        'is_managed': 'isManaged',
        'management_tool_id': 'managementToolId',
        'name': 'name',
        'power_state': 'powerState',
        'tags': 'tags'
    }

    def __init__(self, availability_zone=None, availability_zone_id=None, created_at=None, flavor_id=None, id=None, image_id=None, is_managed=None, management_tool_id=None, name=None, power_state=None, tags=None):  # noqa: E501
        """VmwareVmSimple - a model defined in OpenAPI"""  # noqa: E501

        self._availability_zone = None
        self._availability_zone_id = None
        self._created_at = None
        self._flavor_id = None
        self._id = None
        self._image_id = None
        self._is_managed = None
        self._management_tool_id = None
        self._name = None
        self._power_state = None
        self._tags = None
        self.discriminator = None

        if availability_zone is not None:
            self.availability_zone = availability_zone
        self.availability_zone_id = availability_zone_id
        if created_at is not None:
            self.created_at = created_at
        self.flavor_id = flavor_id
        self.id = id
        self.image_id = image_id
        self.is_managed = is_managed
        self.management_tool_id = management_tool_id
        self.name = name
        self.power_state = power_state
        self.tags = tags

    @property
    def availability_zone(self):
        """Gets the availability_zone of this VmwareVmSimple.  # noqa: E501


        :return: The availability_zone of this VmwareVmSimple.  # noqa: E501
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this VmwareVmSimple.


        :param availability_zone: The availability_zone of this VmwareVmSimple.  # noqa: E501
        :type: str
        """

        self._availability_zone = availability_zone

    @property
    def availability_zone_id(self):
        """Gets the availability_zone_id of this VmwareVmSimple.  # noqa: E501


        :return: The availability_zone_id of this VmwareVmSimple.  # noqa: E501
        :rtype: str
        """
        return self._availability_zone_id

    @availability_zone_id.setter
    def availability_zone_id(self, availability_zone_id):
        """Sets the availability_zone_id of this VmwareVmSimple.


        :param availability_zone_id: The availability_zone_id of this VmwareVmSimple.  # noqa: E501
        :type: str
        """
        if availability_zone_id is None:
            raise ValueError("Invalid value for `availability_zone_id`, must not be `None`")  # noqa: E501

        self._availability_zone_id = availability_zone_id

    @property
    def created_at(self):
        """Gets the created_at of this VmwareVmSimple.  # noqa: E501


        :return: The created_at of this VmwareVmSimple.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this VmwareVmSimple.


        :param created_at: The created_at of this VmwareVmSimple.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def flavor_id(self):
        """Gets the flavor_id of this VmwareVmSimple.  # noqa: E501


        :return: The flavor_id of this VmwareVmSimple.  # noqa: E501
        :rtype: str
        """
        return self._flavor_id

    @flavor_id.setter
    def flavor_id(self, flavor_id):
        """Sets the flavor_id of this VmwareVmSimple.


        :param flavor_id: The flavor_id of this VmwareVmSimple.  # noqa: E501
        :type: str
        """
        if flavor_id is None:
            raise ValueError("Invalid value for `flavor_id`, must not be `None`")  # noqa: E501

        self._flavor_id = flavor_id

    @property
    def id(self):
        """Gets the id of this VmwareVmSimple.  # noqa: E501


        :return: The id of this VmwareVmSimple.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VmwareVmSimple.


        :param id: The id of this VmwareVmSimple.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def image_id(self):
        """Gets the image_id of this VmwareVmSimple.  # noqa: E501


        :return: The image_id of this VmwareVmSimple.  # noqa: E501
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this VmwareVmSimple.


        :param image_id: The image_id of this VmwareVmSimple.  # noqa: E501
        :type: str
        """
        if image_id is None:
            raise ValueError("Invalid value for `image_id`, must not be `None`")  # noqa: E501

        self._image_id = image_id

    @property
    def is_managed(self):
        """Gets the is_managed of this VmwareVmSimple.  # noqa: E501


        :return: The is_managed of this VmwareVmSimple.  # noqa: E501
        :rtype: bool
        """
        return self._is_managed

    @is_managed.setter
    def is_managed(self, is_managed):
        """Sets the is_managed of this VmwareVmSimple.


        :param is_managed: The is_managed of this VmwareVmSimple.  # noqa: E501
        :type: bool
        """
        if is_managed is None:
            raise ValueError("Invalid value for `is_managed`, must not be `None`")  # noqa: E501

        self._is_managed = is_managed

    @property
    def management_tool_id(self):
        """Gets the management_tool_id of this VmwareVmSimple.  # noqa: E501


        :return: The management_tool_id of this VmwareVmSimple.  # noqa: E501
        :rtype: str
        """
        return self._management_tool_id

    @management_tool_id.setter
    def management_tool_id(self, management_tool_id):
        """Sets the management_tool_id of this VmwareVmSimple.


        :param management_tool_id: The management_tool_id of this VmwareVmSimple.  # noqa: E501
        :type: str
        """

        self._management_tool_id = management_tool_id

    @property
    def name(self):
        """Gets the name of this VmwareVmSimple.  # noqa: E501


        :return: The name of this VmwareVmSimple.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VmwareVmSimple.


        :param name: The name of this VmwareVmSimple.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def power_state(self):
        """Gets the power_state of this VmwareVmSimple.  # noqa: E501


        :return: The power_state of this VmwareVmSimple.  # noqa: E501
        :rtype: VmwarePowerState
        """
        return self._power_state

    @power_state.setter
    def power_state(self, power_state):
        """Sets the power_state of this VmwareVmSimple.


        :param power_state: The power_state of this VmwareVmSimple.  # noqa: E501
        :type: VmwarePowerState
        """
        if power_state is None:
            raise ValueError("Invalid value for `power_state`, must not be `None`")  # noqa: E501

        self._power_state = power_state

    @property
    def tags(self):
        """Gets the tags of this VmwareVmSimple.  # noqa: E501

        A list of VM tags  # noqa: E501

        :return: The tags of this VmwareVmSimple.  # noqa: E501
        :rtype: list[VmwareTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this VmwareVmSimple.

        A list of VM tags  # noqa: E501

        :param tags: The tags of this VmwareVmSimple.  # noqa: E501
        :type: list[VmwareTag]
        """
        if tags is None:
            raise ValueError("Invalid value for `tags`, must not be `None`")  # noqa: E501

        self._tags = tags

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
        if not isinstance(other, VmwareVmSimple):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
