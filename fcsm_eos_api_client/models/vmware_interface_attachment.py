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


class VmwareInterfaceAttachment(object):
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
        'subnet_id': 'str',
        'vm_id': 'str'
    }

    attribute_map = {
        'subnet_id': 'subnetId',
        'vm_id': 'vmId'
    }

    def __init__(self, subnet_id=None, vm_id=None):  # noqa: E501
        """VmwareInterfaceAttachment - a model defined in OpenAPI"""  # noqa: E501

        self._subnet_id = None
        self._vm_id = None
        self.discriminator = None

        self.subnet_id = subnet_id
        self.vm_id = vm_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this VmwareInterfaceAttachment.  # noqa: E501

        subnet id  # noqa: E501

        :return: The subnet_id of this VmwareInterfaceAttachment.  # noqa: E501
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this VmwareInterfaceAttachment.

        subnet id  # noqa: E501

        :param subnet_id: The subnet_id of this VmwareInterfaceAttachment.  # noqa: E501
        :type: str
        """
        if subnet_id is None:
            raise ValueError("Invalid value for `subnet_id`, must not be `None`")  # noqa: E501

        self._subnet_id = subnet_id

    @property
    def vm_id(self):
        """Gets the vm_id of this VmwareInterfaceAttachment.  # noqa: E501

        vm id  # noqa: E501

        :return: The vm_id of this VmwareInterfaceAttachment.  # noqa: E501
        :rtype: str
        """
        return self._vm_id

    @vm_id.setter
    def vm_id(self, vm_id):
        """Sets the vm_id of this VmwareInterfaceAttachment.

        vm id  # noqa: E501

        :param vm_id: The vm_id of this VmwareInterfaceAttachment.  # noqa: E501
        :type: str
        """
        if vm_id is None:
            raise ValueError("Invalid value for `vm_id`, must not be `None`")  # noqa: E501

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
        if not isinstance(other, VmwareInterfaceAttachment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
