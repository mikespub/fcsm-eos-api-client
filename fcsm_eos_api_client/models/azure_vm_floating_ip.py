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


class AzureVmFloatingIp(object):
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
        'floating_ip_address': 'str',
        'interface_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'floating_ip_address': 'floatingIpAddress',
        'interface_id': 'interfaceId'
    }

    def __init__(self, id=None, floating_ip_address=None, interface_id=None):  # noqa: E501
        """AzureVmFloatingIp - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._floating_ip_address = None
        self._interface_id = None
        self.discriminator = None

        self.id = id
        self.floating_ip_address = floating_ip_address
        self.interface_id = interface_id

    @property
    def id(self):
        """Gets the id of this AzureVmFloatingIp.  # noqa: E501


        :return: The id of this AzureVmFloatingIp.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AzureVmFloatingIp.


        :param id: The id of this AzureVmFloatingIp.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def floating_ip_address(self):
        """Gets the floating_ip_address of this AzureVmFloatingIp.  # noqa: E501


        :return: The floating_ip_address of this AzureVmFloatingIp.  # noqa: E501
        :rtype: str
        """
        return self._floating_ip_address

    @floating_ip_address.setter
    def floating_ip_address(self, floating_ip_address):
        """Sets the floating_ip_address of this AzureVmFloatingIp.


        :param floating_ip_address: The floating_ip_address of this AzureVmFloatingIp.  # noqa: E501
        :type: str
        """
        if floating_ip_address is None:
            raise ValueError("Invalid value for `floating_ip_address`, must not be `None`")  # noqa: E501

        self._floating_ip_address = floating_ip_address

    @property
    def interface_id(self):
        """Gets the interface_id of this AzureVmFloatingIp.  # noqa: E501


        :return: The interface_id of this AzureVmFloatingIp.  # noqa: E501
        :rtype: str
        """
        return self._interface_id

    @interface_id.setter
    def interface_id(self, interface_id):
        """Sets the interface_id of this AzureVmFloatingIp.


        :param interface_id: The interface_id of this AzureVmFloatingIp.  # noqa: E501
        :type: str
        """
        if interface_id is None:
            raise ValueError("Invalid value for `interface_id`, must not be `None`")  # noqa: E501

        self._interface_id = interface_id

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
        if not isinstance(other, AzureVmFloatingIp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
