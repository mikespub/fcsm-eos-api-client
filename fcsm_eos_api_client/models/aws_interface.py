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


class AwsInterface(object):
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
        'attachment': 'AwsInterfaceAttachment',
        'id': 'str',
        'ipv4_addresses': 'list[AwsIPv4Address]',
        'mac_address': 'str',
        'name': 'str',
        'network_id': 'str',
        'network_name': 'str'
    }

    attribute_map = {
        'attachment': 'attachment',
        'id': 'id',
        'ipv4_addresses': 'ipv4Addresses',
        'mac_address': 'macAddress',
        'name': 'name',
        'network_id': 'networkId',
        'network_name': 'networkName'
    }

    def __init__(self, attachment=None, id=None, ipv4_addresses=None, mac_address=None, name=None, network_id=None, network_name=None):  # noqa: E501
        """AwsInterface - a model defined in OpenAPI"""  # noqa: E501

        self._attachment = None
        self._id = None
        self._ipv4_addresses = None
        self._mac_address = None
        self._name = None
        self._network_id = None
        self._network_name = None
        self.discriminator = None

        self.attachment = attachment
        self.id = id
        self.ipv4_addresses = ipv4_addresses
        self.mac_address = mac_address
        self.name = name
        self.network_id = network_id
        self.network_name = network_name

    @property
    def attachment(self):
        """Gets the attachment of this AwsInterface.  # noqa: E501


        :return: The attachment of this AwsInterface.  # noqa: E501
        :rtype: AwsInterfaceAttachment
        """
        return self._attachment

    @attachment.setter
    def attachment(self, attachment):
        """Sets the attachment of this AwsInterface.


        :param attachment: The attachment of this AwsInterface.  # noqa: E501
        :type: AwsInterfaceAttachment
        """
        if attachment is None:
            raise ValueError("Invalid value for `attachment`, must not be `None`")  # noqa: E501

        self._attachment = attachment

    @property
    def id(self):
        """Gets the id of this AwsInterface.  # noqa: E501


        :return: The id of this AwsInterface.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AwsInterface.


        :param id: The id of this AwsInterface.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def ipv4_addresses(self):
        """Gets the ipv4_addresses of this AwsInterface.  # noqa: E501


        :return: The ipv4_addresses of this AwsInterface.  # noqa: E501
        :rtype: list[AwsIPv4Address]
        """
        return self._ipv4_addresses

    @ipv4_addresses.setter
    def ipv4_addresses(self, ipv4_addresses):
        """Sets the ipv4_addresses of this AwsInterface.


        :param ipv4_addresses: The ipv4_addresses of this AwsInterface.  # noqa: E501
        :type: list[AwsIPv4Address]
        """
        if ipv4_addresses is None:
            raise ValueError("Invalid value for `ipv4_addresses`, must not be `None`")  # noqa: E501

        self._ipv4_addresses = ipv4_addresses

    @property
    def mac_address(self):
        """Gets the mac_address of this AwsInterface.  # noqa: E501


        :return: The mac_address of this AwsInterface.  # noqa: E501
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this AwsInterface.


        :param mac_address: The mac_address of this AwsInterface.  # noqa: E501
        :type: str
        """
        if mac_address is None:
            raise ValueError("Invalid value for `mac_address`, must not be `None`")  # noqa: E501

        self._mac_address = mac_address

    @property
    def name(self):
        """Gets the name of this AwsInterface.  # noqa: E501


        :return: The name of this AwsInterface.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AwsInterface.


        :param name: The name of this AwsInterface.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def network_id(self):
        """Gets the network_id of this AwsInterface.  # noqa: E501


        :return: The network_id of this AwsInterface.  # noqa: E501
        :rtype: str
        """
        return self._network_id

    @network_id.setter
    def network_id(self, network_id):
        """Sets the network_id of this AwsInterface.


        :param network_id: The network_id of this AwsInterface.  # noqa: E501
        :type: str
        """
        if network_id is None:
            raise ValueError("Invalid value for `network_id`, must not be `None`")  # noqa: E501

        self._network_id = network_id

    @property
    def network_name(self):
        """Gets the network_name of this AwsInterface.  # noqa: E501


        :return: The network_name of this AwsInterface.  # noqa: E501
        :rtype: str
        """
        return self._network_name

    @network_name.setter
    def network_name(self, network_name):
        """Sets the network_name of this AwsInterface.


        :param network_name: The network_name of this AwsInterface.  # noqa: E501
        :type: str
        """
        if network_name is None:
            raise ValueError("Invalid value for `network_name`, must not be `None`")  # noqa: E501

        self._network_name = network_name

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
        if not isinstance(other, AwsInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
