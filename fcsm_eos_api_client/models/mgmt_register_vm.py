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


class MgmtRegisterVm(object):
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
        'management_tool_id': 'str',
        'subscription_id': 'str',
        'operating_system': 'str'
    }

    attribute_map = {
        'management_tool_id': 'managementToolId',
        'subscription_id': 'subscriptionId',
        'operating_system': 'operatingSystem'
    }

    def __init__(self, management_tool_id=None, subscription_id=None, operating_system=None):  # noqa: E501
        """MgmtRegisterVm - a model defined in OpenAPI"""  # noqa: E501

        self._management_tool_id = None
        self._subscription_id = None
        self._operating_system = None
        self.discriminator = None

        if management_tool_id is not None:
            self.management_tool_id = management_tool_id
        if subscription_id is not None:
            self.subscription_id = subscription_id
        if operating_system is not None:
            self.operating_system = operating_system

    @property
    def management_tool_id(self):
        """Gets the management_tool_id of this MgmtRegisterVm.  # noqa: E501

        Management tool id  # noqa: E501

        :return: The management_tool_id of this MgmtRegisterVm.  # noqa: E501
        :rtype: str
        """
        return self._management_tool_id

    @management_tool_id.setter
    def management_tool_id(self, management_tool_id):
        """Sets the management_tool_id of this MgmtRegisterVm.

        Management tool id  # noqa: E501

        :param management_tool_id: The management_tool_id of this MgmtRegisterVm.  # noqa: E501
        :type: str
        """

        self._management_tool_id = management_tool_id

    @property
    def subscription_id(self):
        """Gets the subscription_id of this MgmtRegisterVm.  # noqa: E501

        Subscription id  # noqa: E501

        :return: The subscription_id of this MgmtRegisterVm.  # noqa: E501
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this MgmtRegisterVm.

        Subscription id  # noqa: E501

        :param subscription_id: The subscription_id of this MgmtRegisterVm.  # noqa: E501
        :type: str
        """

        self._subscription_id = subscription_id

    @property
    def operating_system(self):
        """Gets the operating_system of this MgmtRegisterVm.  # noqa: E501

        Operating system  # noqa: E501

        :return: The operating_system of this MgmtRegisterVm.  # noqa: E501
        :rtype: str
        """
        return self._operating_system

    @operating_system.setter
    def operating_system(self, operating_system):
        """Sets the operating_system of this MgmtRegisterVm.

        Operating system  # noqa: E501

        :param operating_system: The operating_system of this MgmtRegisterVm.  # noqa: E501
        :type: str
        """
        allowed_values = ["linux", "windows"]  # noqa: E501
        if operating_system not in allowed_values:
            raise ValueError(
                "Invalid value for `operating_system` ({0}), must be one of {1}"  # noqa: E501
                .format(operating_system, allowed_values)
            )

        self._operating_system = operating_system

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
        if not isinstance(other, MgmtRegisterVm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other