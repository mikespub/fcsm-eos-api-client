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


class VmwareUpdateVmParams(object):
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
        'flavor_id': 'str'
    }

    attribute_map = {
        'flavor_id': 'flavorId'
    }

    def __init__(self, flavor_id=None):  # noqa: E501
        """VmwareUpdateVmParams - a model defined in OpenAPI"""  # noqa: E501

        self._flavor_id = None
        self.discriminator = None

        if flavor_id is not None:
            self.flavor_id = flavor_id

    @property
    def flavor_id(self):
        """Gets the flavor_id of this VmwareUpdateVmParams.  # noqa: E501

        Id of VM flavor  # noqa: E501

        :return: The flavor_id of this VmwareUpdateVmParams.  # noqa: E501
        :rtype: str
        """
        return self._flavor_id

    @flavor_id.setter
    def flavor_id(self, flavor_id):
        """Sets the flavor_id of this VmwareUpdateVmParams.

        Id of VM flavor  # noqa: E501

        :param flavor_id: The flavor_id of this VmwareUpdateVmParams.  # noqa: E501
        :type: str
        """

        self._flavor_id = flavor_id

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
        if not isinstance(other, VmwareUpdateVmParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
