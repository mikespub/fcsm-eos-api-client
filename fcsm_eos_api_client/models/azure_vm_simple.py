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


class AzureVMSimple(object):
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
        'id': 'str',
        'name': 'str',
        'is_managed': 'bool',
        'management_tool_id': 'AnyOfUUIDobject',
        'flavor_id': 'str',
        'image_id': 'AnyOfstringobject',
        'power_state': 'str',
        'created_at': 'str',
        'availability_zone_id': 'str',
        'availability_zone': 'str',
        'availability_set_id': 'AnyOfstringobject',
        'tags': 'list[AzureTag]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'is_managed': 'isManaged',
        'management_tool_id': 'managementToolId',
        'flavor_id': 'flavorId',
        'image_id': 'imageId',
        'power_state': 'powerState',
        'created_at': 'createdAt',
        'availability_zone_id': 'availabilityZoneId',
        'availability_zone': 'availabilityZone',
        'availability_set_id': 'availabilitySetId',
        'tags': 'tags'
    }

    def __init__(self, id=None, name=None, is_managed=None, management_tool_id=None, flavor_id=None, image_id=None, power_state=None, created_at=None, availability_zone_id='default', availability_zone=None, availability_set_id=None, tags=None):  # noqa: E501
        """AzureVMSimple - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._name = None
        self._is_managed = None
        self._management_tool_id = None
        self._flavor_id = None
        self._image_id = None
        self._power_state = None
        self._created_at = None
        self._availability_zone_id = None
        self._availability_zone = None
        self._availability_set_id = None
        self._tags = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.is_managed = is_managed
        self.management_tool_id = management_tool_id
        self.flavor_id = flavor_id
        self.image_id = image_id
        self.power_state = power_state
        self.created_at = created_at
        self.availability_zone_id = availability_zone_id
        self.availability_zone = availability_zone
        if availability_set_id is not None:
            self.availability_set_id = availability_set_id
        self.tags = tags

    @property
    def id(self):
        """Gets the id of this AzureVMSimple.  # noqa: E501


        :return: The id of this AzureVMSimple.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AzureVMSimple.


        :param id: The id of this AzureVMSimple.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this AzureVMSimple.  # noqa: E501


        :return: The name of this AzureVMSimple.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AzureVMSimple.


        :param name: The name of this AzureVMSimple.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def is_managed(self):
        """Gets the is_managed of this AzureVMSimple.  # noqa: E501


        :return: The is_managed of this AzureVMSimple.  # noqa: E501
        :rtype: bool
        """
        return self._is_managed

    @is_managed.setter
    def is_managed(self, is_managed):
        """Sets the is_managed of this AzureVMSimple.


        :param is_managed: The is_managed of this AzureVMSimple.  # noqa: E501
        :type: bool
        """
        if is_managed is None:
            raise ValueError("Invalid value for `is_managed`, must not be `None`")  # noqa: E501

        self._is_managed = is_managed

    @property
    def management_tool_id(self):
        """Gets the management_tool_id of this AzureVMSimple.  # noqa: E501


        :return: The management_tool_id of this AzureVMSimple.  # noqa: E501
        :rtype: AnyOfUUIDobject
        """
        return self._management_tool_id

    @management_tool_id.setter
    def management_tool_id(self, management_tool_id):
        """Sets the management_tool_id of this AzureVMSimple.


        :param management_tool_id: The management_tool_id of this AzureVMSimple.  # noqa: E501
        :type: AnyOfUUIDobject
        """
        if management_tool_id is None:
            raise ValueError("Invalid value for `management_tool_id`, must not be `None`")  # noqa: E501

        self._management_tool_id = management_tool_id

    @property
    def flavor_id(self):
        """Gets the flavor_id of this AzureVMSimple.  # noqa: E501


        :return: The flavor_id of this AzureVMSimple.  # noqa: E501
        :rtype: str
        """
        return self._flavor_id

    @flavor_id.setter
    def flavor_id(self, flavor_id):
        """Sets the flavor_id of this AzureVMSimple.


        :param flavor_id: The flavor_id of this AzureVMSimple.  # noqa: E501
        :type: str
        """
        if flavor_id is None:
            raise ValueError("Invalid value for `flavor_id`, must not be `None`")  # noqa: E501

        self._flavor_id = flavor_id

    @property
    def image_id(self):
        """Gets the image_id of this AzureVMSimple.  # noqa: E501


        :return: The image_id of this AzureVMSimple.  # noqa: E501
        :rtype: AnyOfstringobject
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this AzureVMSimple.


        :param image_id: The image_id of this AzureVMSimple.  # noqa: E501
        :type: AnyOfstringobject
        """
        if image_id is None:
            raise ValueError("Invalid value for `image_id`, must not be `None`")  # noqa: E501

        self._image_id = image_id

    @property
    def power_state(self):
        """Gets the power_state of this AzureVMSimple.  # noqa: E501


        :return: The power_state of this AzureVMSimple.  # noqa: E501
        :rtype: str
        """
        return self._power_state

    @power_state.setter
    def power_state(self, power_state):
        """Sets the power_state of this AzureVMSimple.


        :param power_state: The power_state of this AzureVMSimple.  # noqa: E501
        :type: str
        """
        if power_state is None:
            raise ValueError("Invalid value for `power_state`, must not be `None`")  # noqa: E501
        allowed_values = ["unknown", "running", "stopped", "pending"]  # noqa: E501
        if power_state not in allowed_values:
            raise ValueError(
                "Invalid value for `power_state` ({0}), must be one of {1}"  # noqa: E501
                .format(power_state, allowed_values)
            )

        self._power_state = power_state

    @property
    def created_at(self):
        """Gets the created_at of this AzureVMSimple.  # noqa: E501


        :return: The created_at of this AzureVMSimple.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this AzureVMSimple.


        :param created_at: The created_at of this AzureVMSimple.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def availability_zone_id(self):
        """Gets the availability_zone_id of this AzureVMSimple.  # noqa: E501


        :return: The availability_zone_id of this AzureVMSimple.  # noqa: E501
        :rtype: str
        """
        return self._availability_zone_id

    @availability_zone_id.setter
    def availability_zone_id(self, availability_zone_id):
        """Sets the availability_zone_id of this AzureVMSimple.


        :param availability_zone_id: The availability_zone_id of this AzureVMSimple.  # noqa: E501
        :type: str
        """
        if availability_zone_id is None:
            raise ValueError("Invalid value for `availability_zone_id`, must not be `None`")  # noqa: E501

        self._availability_zone_id = availability_zone_id

    @property
    def availability_zone(self):
        """Gets the availability_zone of this AzureVMSimple.  # noqa: E501

        Deprecated after 3 months. Please use `availabilityZoneId`  # noqa: E501

        :return: The availability_zone of this AzureVMSimple.  # noqa: E501
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this AzureVMSimple.

        Deprecated after 3 months. Please use `availabilityZoneId`  # noqa: E501

        :param availability_zone: The availability_zone of this AzureVMSimple.  # noqa: E501
        :type: str
        """
        if availability_zone is None:
            raise ValueError("Invalid value for `availability_zone`, must not be `None`")  # noqa: E501

        self._availability_zone = availability_zone

    @property
    def availability_set_id(self):
        """Gets the availability_set_id of this AzureVMSimple.  # noqa: E501


        :return: The availability_set_id of this AzureVMSimple.  # noqa: E501
        :rtype: AnyOfstringobject
        """
        return self._availability_set_id

    @availability_set_id.setter
    def availability_set_id(self, availability_set_id):
        """Sets the availability_set_id of this AzureVMSimple.


        :param availability_set_id: The availability_set_id of this AzureVMSimple.  # noqa: E501
        :type: AnyOfstringobject
        """

        self._availability_set_id = availability_set_id

    @property
    def tags(self):
        """Gets the tags of this AzureVMSimple.  # noqa: E501


        :return: The tags of this AzureVMSimple.  # noqa: E501
        :rtype: list[AzureTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this AzureVMSimple.


        :param tags: The tags of this AzureVMSimple.  # noqa: E501
        :type: list[AzureTag]
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
        if not isinstance(other, AzureVMSimple):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
