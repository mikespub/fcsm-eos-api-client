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


class WebhookWebhook(object):
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
        'content_type': 'str',
        'enabled': 'bool',
        'event_types_ids': 'list[str]',
        'id': 'str',
        'secret': 'str',
        'url': 'str'
    }

    attribute_map = {
        'content_type': 'contentType',
        'enabled': 'enabled',
        'event_types_ids': 'eventTypesIds',
        'id': 'id',
        'secret': 'secret',
        'url': 'url'
    }

    def __init__(self, content_type=None, enabled=None, event_types_ids=None, id=None, secret=None, url=None):  # noqa: E501
        """WebhookWebhook - a model defined in OpenAPI"""  # noqa: E501

        self._content_type = None
        self._enabled = None
        self._event_types_ids = None
        self._id = None
        self._secret = None
        self._url = None
        self.discriminator = None

        self.content_type = content_type
        self.enabled = enabled
        if event_types_ids is not None:
            self.event_types_ids = event_types_ids
        self.id = id
        if secret is not None:
            self.secret = secret
        self.url = url

    @property
    def content_type(self):
        """Gets the content_type of this WebhookWebhook.  # noqa: E501


        :return: The content_type of this WebhookWebhook.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this WebhookWebhook.


        :param content_type: The content_type of this WebhookWebhook.  # noqa: E501
        :type: str
        """
        if content_type is None:
            raise ValueError("Invalid value for `content_type`, must not be `None`")  # noqa: E501
        if content_type is not None and len(content_type) < 1:
            raise ValueError("Invalid value for `content_type`, length must be greater than or equal to `1`")  # noqa: E501

        self._content_type = content_type

    @property
    def enabled(self):
        """Gets the enabled of this WebhookWebhook.  # noqa: E501


        :return: The enabled of this WebhookWebhook.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this WebhookWebhook.


        :param enabled: The enabled of this WebhookWebhook.  # noqa: E501
        :type: bool
        """
        if enabled is None:
            raise ValueError("Invalid value for `enabled`, must not be `None`")  # noqa: E501

        self._enabled = enabled

    @property
    def event_types_ids(self):
        """Gets the event_types_ids of this WebhookWebhook.  # noqa: E501


        :return: The event_types_ids of this WebhookWebhook.  # noqa: E501
        :rtype: list[str]
        """
        return self._event_types_ids

    @event_types_ids.setter
    def event_types_ids(self, event_types_ids):
        """Sets the event_types_ids of this WebhookWebhook.


        :param event_types_ids: The event_types_ids of this WebhookWebhook.  # noqa: E501
        :type: list[str]
        """

        self._event_types_ids = event_types_ids

    @property
    def id(self):
        """Gets the id of this WebhookWebhook.  # noqa: E501


        :return: The id of this WebhookWebhook.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WebhookWebhook.


        :param id: The id of this WebhookWebhook.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def secret(self):
        """Gets the secret of this WebhookWebhook.  # noqa: E501


        :return: The secret of this WebhookWebhook.  # noqa: E501
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this WebhookWebhook.


        :param secret: The secret of this WebhookWebhook.  # noqa: E501
        :type: str
        """

        self._secret = secret

    @property
    def url(self):
        """Gets the url of this WebhookWebhook.  # noqa: E501


        :return: The url of this WebhookWebhook.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this WebhookWebhook.


        :param url: The url of this WebhookWebhook.  # noqa: E501
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501
        if url is not None and len(url) > 256:
            raise ValueError("Invalid value for `url`, length must be less than or equal to `256`")  # noqa: E501
        if url is not None and len(url) < 1:
            raise ValueError("Invalid value for `url`, length must be greater than or equal to `1`")  # noqa: E501

        self._url = url

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
        if not isinstance(other, WebhookWebhook):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
