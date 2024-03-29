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


class VmwareOptionalWorkshift(object):
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
        'start': 'VmwareWorkshiftSchedule',
        'stop': 'VmwareWorkshiftSchedule'
    }

    attribute_map = {
        'start': 'start',
        'stop': 'stop'
    }

    def __init__(self, start=None, stop=None):  # noqa: E501
        """VmwareOptionalWorkshift - a model defined in OpenAPI"""  # noqa: E501

        self._start = None
        self._stop = None
        self.discriminator = None

        if start is not None:
            self.start = start
        if stop is not None:
            self.stop = stop

    @property
    def start(self):
        """Gets the start of this VmwareOptionalWorkshift.  # noqa: E501


        :return: The start of this VmwareOptionalWorkshift.  # noqa: E501
        :rtype: VmwareWorkshiftSchedule
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this VmwareOptionalWorkshift.


        :param start: The start of this VmwareOptionalWorkshift.  # noqa: E501
        :type: VmwareWorkshiftSchedule
        """

        self._start = start

    @property
    def stop(self):
        """Gets the stop of this VmwareOptionalWorkshift.  # noqa: E501


        :return: The stop of this VmwareOptionalWorkshift.  # noqa: E501
        :rtype: VmwareWorkshiftSchedule
        """
        return self._stop

    @stop.setter
    def stop(self, stop):
        """Sets the stop of this VmwareOptionalWorkshift.


        :param stop: The stop of this VmwareOptionalWorkshift.  # noqa: E501
        :type: VmwareWorkshiftSchedule
        """

        self._stop = stop

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
        if not isinstance(other, VmwareOptionalWorkshift):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
