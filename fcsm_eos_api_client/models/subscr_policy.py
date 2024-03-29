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


class SubscrPolicy(object):
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
        'management': 'SubscrStatus',
        'monitoring': 'SubscrStatus',
        'backup': 'SubscrStatus',
        'patching': 'SubscrStatus',
        'workload_management': 'SubscrStatus',
        'workshift_rule': 'SubscrWorkshiftRule'
    }

    attribute_map = {
        'management': 'management',
        'monitoring': 'monitoring',
        'backup': 'backup',
        'patching': 'patching',
        'workload_management': 'workloadManagement',
        'workshift_rule': 'workshiftRule'
    }

    def __init__(self, management=None, monitoring=None, backup=None, patching=None, workload_management=None, workshift_rule=None):  # noqa: E501
        """SubscrPolicy - a model defined in OpenAPI"""  # noqa: E501

        self._management = None
        self._monitoring = None
        self._backup = None
        self._patching = None
        self._workload_management = None
        self._workshift_rule = None
        self.discriminator = None

        if management is not None:
            self.management = management
        if monitoring is not None:
            self.monitoring = monitoring
        if backup is not None:
            self.backup = backup
        if patching is not None:
            self.patching = patching
        if workload_management is not None:
            self.workload_management = workload_management
        if workshift_rule is not None:
            self.workshift_rule = workshift_rule

    @property
    def management(self):
        """Gets the management of this SubscrPolicy.  # noqa: E501


        :return: The management of this SubscrPolicy.  # noqa: E501
        :rtype: SubscrStatus
        """
        return self._management

    @management.setter
    def management(self, management):
        """Sets the management of this SubscrPolicy.


        :param management: The management of this SubscrPolicy.  # noqa: E501
        :type: SubscrStatus
        """

        self._management = management

    @property
    def monitoring(self):
        """Gets the monitoring of this SubscrPolicy.  # noqa: E501


        :return: The monitoring of this SubscrPolicy.  # noqa: E501
        :rtype: SubscrStatus
        """
        return self._monitoring

    @monitoring.setter
    def monitoring(self, monitoring):
        """Sets the monitoring of this SubscrPolicy.


        :param monitoring: The monitoring of this SubscrPolicy.  # noqa: E501
        :type: SubscrStatus
        """

        self._monitoring = monitoring

    @property
    def backup(self):
        """Gets the backup of this SubscrPolicy.  # noqa: E501


        :return: The backup of this SubscrPolicy.  # noqa: E501
        :rtype: SubscrStatus
        """
        return self._backup

    @backup.setter
    def backup(self, backup):
        """Sets the backup of this SubscrPolicy.


        :param backup: The backup of this SubscrPolicy.  # noqa: E501
        :type: SubscrStatus
        """

        self._backup = backup

    @property
    def patching(self):
        """Gets the patching of this SubscrPolicy.  # noqa: E501


        :return: The patching of this SubscrPolicy.  # noqa: E501
        :rtype: SubscrStatus
        """
        return self._patching

    @patching.setter
    def patching(self, patching):
        """Sets the patching of this SubscrPolicy.


        :param patching: The patching of this SubscrPolicy.  # noqa: E501
        :type: SubscrStatus
        """

        self._patching = patching

    @property
    def workload_management(self):
        """Gets the workload_management of this SubscrPolicy.  # noqa: E501


        :return: The workload_management of this SubscrPolicy.  # noqa: E501
        :rtype: SubscrStatus
        """
        return self._workload_management

    @workload_management.setter
    def workload_management(self, workload_management):
        """Sets the workload_management of this SubscrPolicy.


        :param workload_management: The workload_management of this SubscrPolicy.  # noqa: E501
        :type: SubscrStatus
        """

        self._workload_management = workload_management

    @property
    def workshift_rule(self):
        """Gets the workshift_rule of this SubscrPolicy.  # noqa: E501


        :return: The workshift_rule of this SubscrPolicy.  # noqa: E501
        :rtype: SubscrWorkshiftRule
        """
        return self._workshift_rule

    @workshift_rule.setter
    def workshift_rule(self, workshift_rule):
        """Sets the workshift_rule of this SubscrPolicy.


        :param workshift_rule: The workshift_rule of this SubscrPolicy.  # noqa: E501
        :type: SubscrWorkshiftRule
        """

        self._workshift_rule = workshift_rule

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
        if not isinstance(other, SubscrPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
