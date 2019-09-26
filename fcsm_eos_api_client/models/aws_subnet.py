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


class AwsSubnet(object):
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
        'availability_zone': 'str',
        'availability_zone_id': 'str',
        'cidr': 'str',
        'id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'availability_zone': 'availabilityZone',
        'availability_zone_id': 'availabilityZoneId',
        'cidr': 'cidr',
        'id': 'id',
        'name': 'name'
    }

    def __init__(self, availability_zone=None, availability_zone_id=None, cidr=None, id=None, name=None):  # noqa: E501
        """AwsSubnet - a model defined in OpenAPI"""  # noqa: E501

        self._availability_zone = None
        self._availability_zone_id = None
        self._cidr = None
        self._id = None
        self._name = None
        self.discriminator = None

        if availability_zone is not None:
            self.availability_zone = availability_zone
        self.availability_zone_id = availability_zone_id
        self.cidr = cidr
        self.id = id
        self.name = name

    @property
    def availability_zone(self):
        """Gets the availability_zone of this AwsSubnet.  # noqa: E501

        Availability Zone  # noqa: E501

        :return: The availability_zone of this AwsSubnet.  # noqa: E501
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this AwsSubnet.

        Availability Zone  # noqa: E501

        :param availability_zone: The availability_zone of this AwsSubnet.  # noqa: E501
        :type: str
        """

        self._availability_zone = availability_zone

    @property
    def availability_zone_id(self):
        """Gets the availability_zone_id of this AwsSubnet.  # noqa: E501

        Availability Zone  # noqa: E501

        :return: The availability_zone_id of this AwsSubnet.  # noqa: E501
        :rtype: str
        """
        return self._availability_zone_id

    @availability_zone_id.setter
    def availability_zone_id(self, availability_zone_id):
        """Sets the availability_zone_id of this AwsSubnet.

        Availability Zone  # noqa: E501

        :param availability_zone_id: The availability_zone_id of this AwsSubnet.  # noqa: E501
        :type: str
        """
        if availability_zone_id is None:
            raise ValueError("Invalid value for `availability_zone_id`, must not be `None`")  # noqa: E501

        self._availability_zone_id = availability_zone_id

    @property
    def cidr(self):
        """Gets the cidr of this AwsSubnet.  # noqa: E501


        :return: The cidr of this AwsSubnet.  # noqa: E501
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this AwsSubnet.


        :param cidr: The cidr of this AwsSubnet.  # noqa: E501
        :type: str
        """
        if cidr is None:
            raise ValueError("Invalid value for `cidr`, must not be `None`")  # noqa: E501

        self._cidr = cidr

    @property
    def id(self):
        """Gets the id of this AwsSubnet.  # noqa: E501


        :return: The id of this AwsSubnet.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AwsSubnet.


        :param id: The id of this AwsSubnet.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this AwsSubnet.  # noqa: E501


        :return: The name of this AwsSubnet.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AwsSubnet.


        :param name: The name of this AwsSubnet.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

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
        if not isinstance(other, AwsSubnet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
