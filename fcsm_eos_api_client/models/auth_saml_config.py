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


class AuthSamlConfig(object):
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
        'certificate': 'str',
        'email_attribute': 'str',
        'groups_attribute': 'str',
        'name': 'str',
        'provider_id': 'str',
        'redirect_url': 'str',
        'sso_url': 'str',
        'username_attribute': 'str'
    }

    attribute_map = {
        'certificate': 'certificate',
        'email_attribute': 'emailAttribute',
        'groups_attribute': 'groupsAttribute',
        'name': 'name',
        'provider_id': 'providerId',
        'redirect_url': 'redirectURL',
        'sso_url': 'ssoURL',
        'username_attribute': 'usernameAttribute'
    }

    def __init__(self, certificate=None, email_attribute=None, groups_attribute=None, name=None, provider_id=None, redirect_url=None, sso_url=None, username_attribute=None):  # noqa: E501
        """AuthSamlConfig - a model defined in OpenAPI"""  # noqa: E501

        self._certificate = None
        self._email_attribute = None
        self._groups_attribute = None
        self._name = None
        self._provider_id = None
        self._redirect_url = None
        self._sso_url = None
        self._username_attribute = None
        self.discriminator = None

        self.certificate = certificate
        self.email_attribute = email_attribute
        self.groups_attribute = groups_attribute
        self.name = name
        self.provider_id = provider_id
        if redirect_url is not None:
            self.redirect_url = redirect_url
        self.sso_url = sso_url
        self.username_attribute = username_attribute

    @property
    def certificate(self):
        """Gets the certificate of this AuthSamlConfig.  # noqa: E501


        :return: The certificate of this AuthSamlConfig.  # noqa: E501
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """Sets the certificate of this AuthSamlConfig.


        :param certificate: The certificate of this AuthSamlConfig.  # noqa: E501
        :type: str
        """
        if certificate is None:
            raise ValueError("Invalid value for `certificate`, must not be `None`")  # noqa: E501

        self._certificate = certificate

    @property
    def email_attribute(self):
        """Gets the email_attribute of this AuthSamlConfig.  # noqa: E501


        :return: The email_attribute of this AuthSamlConfig.  # noqa: E501
        :rtype: str
        """
        return self._email_attribute

    @email_attribute.setter
    def email_attribute(self, email_attribute):
        """Sets the email_attribute of this AuthSamlConfig.


        :param email_attribute: The email_attribute of this AuthSamlConfig.  # noqa: E501
        :type: str
        """
        if email_attribute is None:
            raise ValueError("Invalid value for `email_attribute`, must not be `None`")  # noqa: E501
        if email_attribute is not None and len(email_attribute) > 256:
            raise ValueError("Invalid value for `email_attribute`, length must be less than or equal to `256`")  # noqa: E501
        if email_attribute is not None and len(email_attribute) < 1:
            raise ValueError("Invalid value for `email_attribute`, length must be greater than or equal to `1`")  # noqa: E501

        self._email_attribute = email_attribute

    @property
    def groups_attribute(self):
        """Gets the groups_attribute of this AuthSamlConfig.  # noqa: E501


        :return: The groups_attribute of this AuthSamlConfig.  # noqa: E501
        :rtype: str
        """
        return self._groups_attribute

    @groups_attribute.setter
    def groups_attribute(self, groups_attribute):
        """Sets the groups_attribute of this AuthSamlConfig.


        :param groups_attribute: The groups_attribute of this AuthSamlConfig.  # noqa: E501
        :type: str
        """
        if groups_attribute is None:
            raise ValueError("Invalid value for `groups_attribute`, must not be `None`")  # noqa: E501
        if groups_attribute is not None and len(groups_attribute) > 256:
            raise ValueError("Invalid value for `groups_attribute`, length must be less than or equal to `256`")  # noqa: E501
        if groups_attribute is not None and len(groups_attribute) < 1:
            raise ValueError("Invalid value for `groups_attribute`, length must be greater than or equal to `1`")  # noqa: E501

        self._groups_attribute = groups_attribute

    @property
    def name(self):
        """Gets the name of this AuthSamlConfig.  # noqa: E501


        :return: The name of this AuthSamlConfig.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AuthSamlConfig.


        :param name: The name of this AuthSamlConfig.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 32:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `32`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def provider_id(self):
        """Gets the provider_id of this AuthSamlConfig.  # noqa: E501


        :return: The provider_id of this AuthSamlConfig.  # noqa: E501
        :rtype: str
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        """Sets the provider_id of this AuthSamlConfig.


        :param provider_id: The provider_id of this AuthSamlConfig.  # noqa: E501
        :type: str
        """
        if provider_id is None:
            raise ValueError("Invalid value for `provider_id`, must not be `None`")  # noqa: E501
        if provider_id is not None and len(provider_id) > 32:
            raise ValueError("Invalid value for `provider_id`, length must be less than or equal to `32`")  # noqa: E501
        if provider_id is not None and len(provider_id) < 1:
            raise ValueError("Invalid value for `provider_id`, length must be greater than or equal to `1`")  # noqa: E501
        if provider_id is not None and not re.search(r'^[a-z0-9]+(-[a-z0-9]+)*$', provider_id):  # noqa: E501
            raise ValueError(r"Invalid value for `provider_id`, must be a follow pattern or equal to `/^[a-z0-9]+(-[a-z0-9]+)*$/`")  # noqa: E501

        self._provider_id = provider_id

    @property
    def redirect_url(self):
        """Gets the redirect_url of this AuthSamlConfig.  # noqa: E501


        :return: The redirect_url of this AuthSamlConfig.  # noqa: E501
        :rtype: str
        """
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, redirect_url):
        """Sets the redirect_url of this AuthSamlConfig.


        :param redirect_url: The redirect_url of this AuthSamlConfig.  # noqa: E501
        :type: str
        """

        self._redirect_url = redirect_url

    @property
    def sso_url(self):
        """Gets the sso_url of this AuthSamlConfig.  # noqa: E501


        :return: The sso_url of this AuthSamlConfig.  # noqa: E501
        :rtype: str
        """
        return self._sso_url

    @sso_url.setter
    def sso_url(self, sso_url):
        """Sets the sso_url of this AuthSamlConfig.


        :param sso_url: The sso_url of this AuthSamlConfig.  # noqa: E501
        :type: str
        """
        if sso_url is None:
            raise ValueError("Invalid value for `sso_url`, must not be `None`")  # noqa: E501

        self._sso_url = sso_url

    @property
    def username_attribute(self):
        """Gets the username_attribute of this AuthSamlConfig.  # noqa: E501


        :return: The username_attribute of this AuthSamlConfig.  # noqa: E501
        :rtype: str
        """
        return self._username_attribute

    @username_attribute.setter
    def username_attribute(self, username_attribute):
        """Sets the username_attribute of this AuthSamlConfig.


        :param username_attribute: The username_attribute of this AuthSamlConfig.  # noqa: E501
        :type: str
        """
        if username_attribute is None:
            raise ValueError("Invalid value for `username_attribute`, must not be `None`")  # noqa: E501
        if username_attribute is not None and len(username_attribute) > 256:
            raise ValueError("Invalid value for `username_attribute`, length must be less than or equal to `256`")  # noqa: E501
        if username_attribute is not None and len(username_attribute) < 1:
            raise ValueError("Invalid value for `username_attribute`, length must be greater than or equal to `1`")  # noqa: E501

        self._username_attribute = username_attribute

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
        if not isinstance(other, AuthSamlConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
