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


class VmwareVolume(object):
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
        'attachment': 'VmwareVolumeAttachment',
        'id': 'str',
        'is_os_disk': 'bool',
        'name': 'str',
        'size_in_gb': 'int',
        'status': 'VmwareVolumeStatus',
        'tags': 'list[VmwareTag]',
        'type_id': 'str'
    }

    attribute_map = {
        'attachment': 'attachment',
        'id': 'id',
        'is_os_disk': 'isOsDisk',
        'name': 'name',
        'size_in_gb': 'sizeInGb',
        'status': 'status',
        'tags': 'tags',
        'type_id': 'typeId'
    }

    def __init__(self, attachment=None, id=None, is_os_disk=None, name=None, size_in_gb=None, status=None, tags=None, type_id=None):  # noqa: E501
        """VmwareVolume - a model defined in OpenAPI"""  # noqa: E501

        self._attachment = None
        self._id = None
        self._is_os_disk = None
        self._name = None
        self._size_in_gb = None
        self._status = None
        self._tags = None
        self._type_id = None
        self.discriminator = None

        self.attachment = attachment
        self.id = id
        self.is_os_disk = is_os_disk
        self.name = name
        self.size_in_gb = size_in_gb
        self.status = status
        if tags is not None:
            self.tags = tags
        self.type_id = type_id

    @property
    def attachment(self):
        """Gets the attachment of this VmwareVolume.  # noqa: E501


        :return: The attachment of this VmwareVolume.  # noqa: E501
        :rtype: VmwareVolumeAttachment
        """
        return self._attachment

    @attachment.setter
    def attachment(self, attachment):
        """Sets the attachment of this VmwareVolume.


        :param attachment: The attachment of this VmwareVolume.  # noqa: E501
        :type: VmwareVolumeAttachment
        """

        self._attachment = attachment

    @property
    def id(self):
        """Gets the id of this VmwareVolume.  # noqa: E501


        :return: The id of this VmwareVolume.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VmwareVolume.


        :param id: The id of this VmwareVolume.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def is_os_disk(self):
        """Gets the is_os_disk of this VmwareVolume.  # noqa: E501


        :return: The is_os_disk of this VmwareVolume.  # noqa: E501
        :rtype: bool
        """
        return self._is_os_disk

    @is_os_disk.setter
    def is_os_disk(self, is_os_disk):
        """Sets the is_os_disk of this VmwareVolume.


        :param is_os_disk: The is_os_disk of this VmwareVolume.  # noqa: E501
        :type: bool
        """
        if is_os_disk is None:
            raise ValueError("Invalid value for `is_os_disk`, must not be `None`")  # noqa: E501

        self._is_os_disk = is_os_disk

    @property
    def name(self):
        """Gets the name of this VmwareVolume.  # noqa: E501


        :return: The name of this VmwareVolume.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VmwareVolume.


        :param name: The name of this VmwareVolume.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 300:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `300`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def size_in_gb(self):
        """Gets the size_in_gb of this VmwareVolume.  # noqa: E501


        :return: The size_in_gb of this VmwareVolume.  # noqa: E501
        :rtype: int
        """
        return self._size_in_gb

    @size_in_gb.setter
    def size_in_gb(self, size_in_gb):
        """Sets the size_in_gb of this VmwareVolume.


        :param size_in_gb: The size_in_gb of this VmwareVolume.  # noqa: E501
        :type: int
        """
        if size_in_gb is None:
            raise ValueError("Invalid value for `size_in_gb`, must not be `None`")  # noqa: E501

        self._size_in_gb = size_in_gb

    @property
    def status(self):
        """Gets the status of this VmwareVolume.  # noqa: E501


        :return: The status of this VmwareVolume.  # noqa: E501
        :rtype: VmwareVolumeStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this VmwareVolume.


        :param status: The status of this VmwareVolume.  # noqa: E501
        :type: VmwareVolumeStatus
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def tags(self):
        """Gets the tags of this VmwareVolume.  # noqa: E501

        A list of tags  # noqa: E501

        :return: The tags of this VmwareVolume.  # noqa: E501
        :rtype: list[VmwareTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this VmwareVolume.

        A list of tags  # noqa: E501

        :param tags: The tags of this VmwareVolume.  # noqa: E501
        :type: list[VmwareTag]
        """

        self._tags = tags

    @property
    def type_id(self):
        """Gets the type_id of this VmwareVolume.  # noqa: E501


        :return: The type_id of this VmwareVolume.  # noqa: E501
        :rtype: str
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this VmwareVolume.


        :param type_id: The type_id of this VmwareVolume.  # noqa: E501
        :type: str
        """
        if type_id is None:
            raise ValueError("Invalid value for `type_id`, must not be `None`")  # noqa: E501

        self._type_id = type_id

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
        if not isinstance(other, VmwareVolume):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
