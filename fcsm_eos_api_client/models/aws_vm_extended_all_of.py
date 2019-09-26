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


class AwsVMExtendedAllOf(object):
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
        'allowed_power_actions': 'list[AwsVMPowerAction]',
        'interface_ids': 'list[str]',
        'interfaces': 'list[str]',
        'status': 'str',
        'status_message': 'str',
        'volume_ids': 'list[str]',
        'volumes': 'list[str]',
        'workshift': 'AwsOptionalWorkshift'
    }

    attribute_map = {
        'allowed_power_actions': 'allowedPowerActions',
        'interface_ids': 'interfaceIds',
        'interfaces': 'interfaces',
        'status': 'status',
        'status_message': 'statusMessage',
        'volume_ids': 'volumeIds',
        'volumes': 'volumes',
        'workshift': 'workshift'
    }

    def __init__(self, allowed_power_actions=None, interface_ids=None, interfaces=None, status=None, status_message=None, volume_ids=None, volumes=None, workshift=None):  # noqa: E501
        """AwsVMExtendedAllOf - a model defined in OpenAPI"""  # noqa: E501

        self._allowed_power_actions = None
        self._interface_ids = None
        self._interfaces = None
        self._status = None
        self._status_message = None
        self._volume_ids = None
        self._volumes = None
        self._workshift = None
        self.discriminator = None

        self.allowed_power_actions = allowed_power_actions
        self.interface_ids = interface_ids
        if interfaces is not None:
            self.interfaces = interfaces
        self.status = status
        self.status_message = status_message
        self.volume_ids = volume_ids
        if volumes is not None:
            self.volumes = volumes
        if workshift is not None:
            self.workshift = workshift

    @property
    def allowed_power_actions(self):
        """Gets the allowed_power_actions of this AwsVMExtendedAllOf.  # noqa: E501


        :return: The allowed_power_actions of this AwsVMExtendedAllOf.  # noqa: E501
        :rtype: list[AwsVMPowerAction]
        """
        return self._allowed_power_actions

    @allowed_power_actions.setter
    def allowed_power_actions(self, allowed_power_actions):
        """Sets the allowed_power_actions of this AwsVMExtendedAllOf.


        :param allowed_power_actions: The allowed_power_actions of this AwsVMExtendedAllOf.  # noqa: E501
        :type: list[AwsVMPowerAction]
        """
        if allowed_power_actions is None:
            raise ValueError("Invalid value for `allowed_power_actions`, must not be `None`")  # noqa: E501

        self._allowed_power_actions = allowed_power_actions

    @property
    def interface_ids(self):
        """Gets the interface_ids of this AwsVMExtendedAllOf.  # noqa: E501


        :return: The interface_ids of this AwsVMExtendedAllOf.  # noqa: E501
        :rtype: list[str]
        """
        return self._interface_ids

    @interface_ids.setter
    def interface_ids(self, interface_ids):
        """Sets the interface_ids of this AwsVMExtendedAllOf.


        :param interface_ids: The interface_ids of this AwsVMExtendedAllOf.  # noqa: E501
        :type: list[str]
        """
        if interface_ids is None:
            raise ValueError("Invalid value for `interface_ids`, must not be `None`")  # noqa: E501

        self._interface_ids = interface_ids

    @property
    def interfaces(self):
        """Gets the interfaces of this AwsVMExtendedAllOf.  # noqa: E501


        :return: The interfaces of this AwsVMExtendedAllOf.  # noqa: E501
        :rtype: list[str]
        """
        return self._interfaces

    @interfaces.setter
    def interfaces(self, interfaces):
        """Sets the interfaces of this AwsVMExtendedAllOf.


        :param interfaces: The interfaces of this AwsVMExtendedAllOf.  # noqa: E501
        :type: list[str]
        """

        self._interfaces = interfaces

    @property
    def status(self):
        """Gets the status of this AwsVMExtendedAllOf.  # noqa: E501


        :return: The status of this AwsVMExtendedAllOf.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AwsVMExtendedAllOf.


        :param status: The status of this AwsVMExtendedAllOf.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["ok", "error", "pending"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def status_message(self):
        """Gets the status_message of this AwsVMExtendedAllOf.  # noqa: E501


        :return: The status_message of this AwsVMExtendedAllOf.  # noqa: E501
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """Sets the status_message of this AwsVMExtendedAllOf.


        :param status_message: The status_message of this AwsVMExtendedAllOf.  # noqa: E501
        :type: str
        """

        self._status_message = status_message

    @property
    def volume_ids(self):
        """Gets the volume_ids of this AwsVMExtendedAllOf.  # noqa: E501


        :return: The volume_ids of this AwsVMExtendedAllOf.  # noqa: E501
        :rtype: list[str]
        """
        return self._volume_ids

    @volume_ids.setter
    def volume_ids(self, volume_ids):
        """Sets the volume_ids of this AwsVMExtendedAllOf.


        :param volume_ids: The volume_ids of this AwsVMExtendedAllOf.  # noqa: E501
        :type: list[str]
        """
        if volume_ids is None:
            raise ValueError("Invalid value for `volume_ids`, must not be `None`")  # noqa: E501

        self._volume_ids = volume_ids

    @property
    def volumes(self):
        """Gets the volumes of this AwsVMExtendedAllOf.  # noqa: E501


        :return: The volumes of this AwsVMExtendedAllOf.  # noqa: E501
        :rtype: list[str]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """Sets the volumes of this AwsVMExtendedAllOf.


        :param volumes: The volumes of this AwsVMExtendedAllOf.  # noqa: E501
        :type: list[str]
        """

        self._volumes = volumes

    @property
    def workshift(self):
        """Gets the workshift of this AwsVMExtendedAllOf.  # noqa: E501


        :return: The workshift of this AwsVMExtendedAllOf.  # noqa: E501
        :rtype: AwsOptionalWorkshift
        """
        return self._workshift

    @workshift.setter
    def workshift(self, workshift):
        """Sets the workshift of this AwsVMExtendedAllOf.


        :param workshift: The workshift of this AwsVMExtendedAllOf.  # noqa: E501
        :type: AwsOptionalWorkshift
        """

        self._workshift = workshift

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
        if not isinstance(other, AwsVMExtendedAllOf):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other