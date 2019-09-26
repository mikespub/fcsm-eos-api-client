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


class VmwareUpdateVolumeParams(object):
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
        'size_in_gb': 'int'
    }

    attribute_map = {
        'size_in_gb': 'sizeInGb'
    }

    def __init__(self, size_in_gb=None):  # noqa: E501
        """VmwareUpdateVolumeParams - a model defined in OpenAPI"""  # noqa: E501

        self._size_in_gb = None
        self.discriminator = None

        if size_in_gb is not None:
            self.size_in_gb = size_in_gb

    @property
    def size_in_gb(self):
        """Gets the size_in_gb of this VmwareUpdateVolumeParams.  # noqa: E501

        New volume size in GB  # noqa: E501

        :return: The size_in_gb of this VmwareUpdateVolumeParams.  # noqa: E501
        :rtype: int
        """
        return self._size_in_gb

    @size_in_gb.setter
    def size_in_gb(self, size_in_gb):
        """Sets the size_in_gb of this VmwareUpdateVolumeParams.

        New volume size in GB  # noqa: E501

        :param size_in_gb: The size_in_gb of this VmwareUpdateVolumeParams.  # noqa: E501
        :type: int
        """

        self._size_in_gb = size_in_gb

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
        if not isinstance(other, VmwareUpdateVolumeParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
