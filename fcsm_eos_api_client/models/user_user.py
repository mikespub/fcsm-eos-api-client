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


class UserUser(object):
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
        'access_rights': 'list[UserAccessRight]',
        'email': 'str',
        'id': 'str',
        'is_internal': 'bool',
        'name': 'str',
        'role': 'str'
    }

    attribute_map = {
        'access_rights': 'accessRights',
        'email': 'email',
        'id': 'id',
        'is_internal': 'isInternal',
        'name': 'name',
        'role': 'role'
    }

    def __init__(self, access_rights=None, email=None, id=None, is_internal=None, name=None, role=None):  # noqa: E501
        """UserUser - a model defined in OpenAPI"""  # noqa: E501

        self._access_rights = None
        self._email = None
        self._id = None
        self._is_internal = None
        self._name = None
        self._role = None
        self.discriminator = None

        if access_rights is not None:
            self.access_rights = access_rights
        self.email = email
        if id is not None:
            self.id = id
        if is_internal is not None:
            self.is_internal = is_internal
        self.name = name
        self.role = role

    @property
    def access_rights(self):
        """Gets the access_rights of this UserUser.  # noqa: E501


        :return: The access_rights of this UserUser.  # noqa: E501
        :rtype: list[UserAccessRight]
        """
        return self._access_rights

    @access_rights.setter
    def access_rights(self, access_rights):
        """Sets the access_rights of this UserUser.


        :param access_rights: The access_rights of this UserUser.  # noqa: E501
        :type: list[UserAccessRight]
        """

        self._access_rights = access_rights

    @property
    def email(self):
        """Gets the email of this UserUser.  # noqa: E501


        :return: The email of this UserUser.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserUser.


        :param email: The email of this UserUser.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501
        if email is not None and len(email) < 1:
            raise ValueError("Invalid value for `email`, length must be greater than or equal to `1`")  # noqa: E501

        self._email = email

    @property
    def id(self):
        """Gets the id of this UserUser.  # noqa: E501


        :return: The id of this UserUser.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserUser.


        :param id: The id of this UserUser.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def is_internal(self):
        """Gets the is_internal of this UserUser.  # noqa: E501


        :return: The is_internal of this UserUser.  # noqa: E501
        :rtype: bool
        """
        return self._is_internal

    @is_internal.setter
    def is_internal(self, is_internal):
        """Sets the is_internal of this UserUser.


        :param is_internal: The is_internal of this UserUser.  # noqa: E501
        :type: bool
        """

        self._is_internal = is_internal

    @property
    def name(self):
        """Gets the name of this UserUser.  # noqa: E501


        :return: The name of this UserUser.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserUser.


        :param name: The name of this UserUser.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def role(self):
        """Gets the role of this UserUser.  # noqa: E501


        :return: The role of this UserUser.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this UserUser.


        :param role: The role of this UserUser.  # noqa: E501
        :type: str
        """
        if role is None:
            raise ValueError("Invalid value for `role`, must not be `None`")  # noqa: E501
        allowed_values = ["admin", "user"]  # noqa: E501
        if role not in allowed_values:
            raise ValueError(
                "Invalid value for `role` ({0}), must be one of {1}"  # noqa: E501
                .format(role, allowed_values)
            )

        self._role = role

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
        if not isinstance(other, UserUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
