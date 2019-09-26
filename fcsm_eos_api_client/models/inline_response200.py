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


class InlineResponse200(object):
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
        'is_compliant': 'bool',
        'message': 'str'
    }

    attribute_map = {
        'is_compliant': 'isCompliant',
        'message': 'message'
    }

    def __init__(self, is_compliant=None, message=None):  # noqa: E501
        """InlineResponse200 - a model defined in OpenAPI"""  # noqa: E501

        self._is_compliant = None
        self._message = None
        self.discriminator = None

        self.is_compliant = is_compliant
        if message is not None:
            self.message = message

    @property
    def is_compliant(self):
        """Gets the is_compliant of this InlineResponse200.  # noqa: E501


        :return: The is_compliant of this InlineResponse200.  # noqa: E501
        :rtype: bool
        """
        return self._is_compliant

    @is_compliant.setter
    def is_compliant(self, is_compliant):
        """Sets the is_compliant of this InlineResponse200.


        :param is_compliant: The is_compliant of this InlineResponse200.  # noqa: E501
        :type: bool
        """
        if is_compliant is None:
            raise ValueError("Invalid value for `is_compliant`, must not be `None`")  # noqa: E501

        self._is_compliant = is_compliant

    @property
    def message(self):
        """Gets the message of this InlineResponse200.  # noqa: E501


        :return: The message of this InlineResponse200.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this InlineResponse200.


        :param message: The message of this InlineResponse200.  # noqa: E501
        :type: str
        """

        self._message = message

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
        if not isinstance(other, InlineResponse200):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other