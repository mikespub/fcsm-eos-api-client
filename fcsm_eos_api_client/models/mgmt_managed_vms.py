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


class MgmtManagedVms(object):
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
        'vm_id': 'str',
        'management_tool_id': 'str'
    }

    attribute_map = {
        'vm_id': 'vmId',
        'management_tool_id': 'managementToolId'
    }

    def __init__(self, vm_id=None, management_tool_id=None):  # noqa: E501
        """MgmtManagedVms - a model defined in OpenAPI"""  # noqa: E501

        self._vm_id = None
        self._management_tool_id = None
        self.discriminator = None

        if vm_id is not None:
            self.vm_id = vm_id
        if management_tool_id is not None:
            self.management_tool_id = management_tool_id

    @property
    def vm_id(self):
        """Gets the vm_id of this MgmtManagedVms.  # noqa: E501

        VM id  # noqa: E501

        :return: The vm_id of this MgmtManagedVms.  # noqa: E501
        :rtype: str
        """
        return self._vm_id

    @vm_id.setter
    def vm_id(self, vm_id):
        """Sets the vm_id of this MgmtManagedVms.

        VM id  # noqa: E501

        :param vm_id: The vm_id of this MgmtManagedVms.  # noqa: E501
        :type: str
        """

        self._vm_id = vm_id

    @property
    def management_tool_id(self):
        """Gets the management_tool_id of this MgmtManagedVms.  # noqa: E501

        Management tool id  # noqa: E501

        :return: The management_tool_id of this MgmtManagedVms.  # noqa: E501
        :rtype: str
        """
        return self._management_tool_id

    @management_tool_id.setter
    def management_tool_id(self, management_tool_id):
        """Sets the management_tool_id of this MgmtManagedVms.

        Management tool id  # noqa: E501

        :param management_tool_id: The management_tool_id of this MgmtManagedVms.  # noqa: E501
        :type: str
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
        if not isinstance(other, MgmtManagedVms):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
