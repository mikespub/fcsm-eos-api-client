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


class SubscrWorkshiftRule(object):
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
        'status': 'SubscrStatus',
        'default_workshift': 'SubscrWorkshift'
    }

    attribute_map = {
        'status': 'status',
        'default_workshift': 'defaultWorkshift'
    }

    def __init__(self, status=None, default_workshift=None):  # noqa: E501
        """SubscrWorkshiftRule - a model defined in OpenAPI"""  # noqa: E501

        self._status = None
        self._default_workshift = None
        self.discriminator = None

        if status is not None:
            self.status = status
        self.default_workshift = default_workshift

    @property
    def status(self):
        """Gets the status of this SubscrWorkshiftRule.  # noqa: E501


        :return: The status of this SubscrWorkshiftRule.  # noqa: E501
        :rtype: SubscrStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SubscrWorkshiftRule.


        :param status: The status of this SubscrWorkshiftRule.  # noqa: E501
        :type: SubscrStatus
        """

        self._status = status

    @property
    def default_workshift(self):
        """Gets the default_workshift of this SubscrWorkshiftRule.  # noqa: E501


        :return: The default_workshift of this SubscrWorkshiftRule.  # noqa: E501
        :rtype: SubscrWorkshift
        """
        return self._default_workshift

    @default_workshift.setter
    def default_workshift(self, default_workshift):
        """Sets the default_workshift of this SubscrWorkshiftRule.


        :param default_workshift: The default_workshift of this SubscrWorkshiftRule.  # noqa: E501
        :type: SubscrWorkshift
        """

        self._default_workshift = default_workshift

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
        if not isinstance(other, SubscrWorkshiftRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
