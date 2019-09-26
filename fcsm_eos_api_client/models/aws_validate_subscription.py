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


class AwsValidateSubscription(object):
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
        'access_key': 'str',
        'region_id': 'str',
        'secret_key': 'str'
    }

    attribute_map = {
        'access_key': 'accessKey',
        'region_id': 'regionId',
        'secret_key': 'secretKey'
    }

    def __init__(self, access_key=None, region_id=None, secret_key=None):  # noqa: E501
        """AwsValidateSubscription - a model defined in OpenAPI"""  # noqa: E501

        self._access_key = None
        self._region_id = None
        self._secret_key = None
        self.discriminator = None

        self.access_key = access_key
        self.region_id = region_id
        self.secret_key = secret_key

    @property
    def access_key(self):
        """Gets the access_key of this AwsValidateSubscription.  # noqa: E501

        AWS subscription access key  # noqa: E501

        :return: The access_key of this AwsValidateSubscription.  # noqa: E501
        :rtype: str
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        """Sets the access_key of this AwsValidateSubscription.

        AWS subscription access key  # noqa: E501

        :param access_key: The access_key of this AwsValidateSubscription.  # noqa: E501
        :type: str
        """
        if access_key is None:
            raise ValueError("Invalid value for `access_key`, must not be `None`")  # noqa: E501

        self._access_key = access_key

    @property
    def region_id(self):
        """Gets the region_id of this AwsValidateSubscription.  # noqa: E501

        AWS region id  # noqa: E501

        :return: The region_id of this AwsValidateSubscription.  # noqa: E501
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this AwsValidateSubscription.

        AWS region id  # noqa: E501

        :param region_id: The region_id of this AwsValidateSubscription.  # noqa: E501
        :type: str
        """
        if region_id is None:
            raise ValueError("Invalid value for `region_id`, must not be `None`")  # noqa: E501

        self._region_id = region_id

    @property
    def secret_key(self):
        """Gets the secret_key of this AwsValidateSubscription.  # noqa: E501

        AWS subscription secret key  # noqa: E501

        :return: The secret_key of this AwsValidateSubscription.  # noqa: E501
        :rtype: str
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        """Sets the secret_key of this AwsValidateSubscription.

        AWS subscription secret key  # noqa: E501

        :param secret_key: The secret_key of this AwsValidateSubscription.  # noqa: E501
        :type: str
        """
        if secret_key is None:
            raise ValueError("Invalid value for `secret_key`, must not be `None`")  # noqa: E501

        self._secret_key = secret_key

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
        if not isinstance(other, AwsValidateSubscription):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
