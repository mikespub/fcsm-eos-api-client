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


class SubscrCreateSubscription(object):
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
        'platform_id': 'str',
        'name': 'str',
        'provisioning': 'bool',
        'contract_id': 'str',
        'project_id': 'str',
        'username': 'str',
        'password': 'str',
        'access_key': 'str',
        'secret_key': 'str',
        'platform_subscription_id': 'str',
        'tenant_id': 'str',
        'authentication_url': 'str',
        'api_url': 'str',
        'policy': 'SubscrPolicy',
        'region_id': 'str'
    }

    attribute_map = {
        'platform_id': 'platformId',
        'name': 'name',
        'provisioning': 'provisioning',
        'contract_id': 'contractId',
        'project_id': 'projectId',
        'username': 'username',
        'password': 'password',
        'access_key': 'accessKey',
        'secret_key': 'secretKey',
        'platform_subscription_id': 'platformSubscriptionId',
        'tenant_id': 'tenantId',
        'authentication_url': 'authenticationUrl',
        'api_url': 'apiUrl',
        'policy': 'policy',
        'region_id': 'regionId'
    }

    def __init__(self, platform_id=None, name=None, provisioning=None, contract_id=None, project_id=None, username=None, password=None, access_key=None, secret_key=None, platform_subscription_id=None, tenant_id=None, authentication_url=None, api_url=None, policy=None, region_id=None):  # noqa: E501
        """SubscrCreateSubscription - a model defined in OpenAPI"""  # noqa: E501

        self._platform_id = None
        self._name = None
        self._provisioning = None
        self._contract_id = None
        self._project_id = None
        self._username = None
        self._password = None
        self._access_key = None
        self._secret_key = None
        self._platform_subscription_id = None
        self._tenant_id = None
        self._authentication_url = None
        self._api_url = None
        self._policy = None
        self._region_id = None
        self.discriminator = None

        self.platform_id = platform_id
        self.name = name
        if provisioning is not None:
            self.provisioning = provisioning
        if contract_id is not None:
            self.contract_id = contract_id
        if project_id is not None:
            self.project_id = project_id
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if access_key is not None:
            self.access_key = access_key
        if secret_key is not None:
            self.secret_key = secret_key
        if platform_subscription_id is not None:
            self.platform_subscription_id = platform_subscription_id
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if authentication_url is not None:
            self.authentication_url = authentication_url
        if api_url is not None:
            self.api_url = api_url
        self.policy = policy
        self.region_id = region_id

    @property
    def platform_id(self):
        """Gets the platform_id of this SubscrCreateSubscription.  # noqa: E501

        Id of a platform  # noqa: E501

        :return: The platform_id of this SubscrCreateSubscription.  # noqa: E501
        :rtype: str
        """
        return self._platform_id

    @platform_id.setter
    def platform_id(self, platform_id):
        """Sets the platform_id of this SubscrCreateSubscription.

        Id of a platform  # noqa: E501

        :param platform_id: The platform_id of this SubscrCreateSubscription.  # noqa: E501
        :type: str
        """
        if platform_id is None:
            raise ValueError("Invalid value for `platform_id`, must not be `None`")  # noqa: E501

        self._platform_id = platform_id

    @property
    def name(self):
        """Gets the name of this SubscrCreateSubscription.  # noqa: E501

        Name of a subscription. Must be 1 to 32 char long, no trailing whitespace allowed.  # noqa: E501

        :return: The name of this SubscrCreateSubscription.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SubscrCreateSubscription.

        Name of a subscription. Must be 1 to 32 char long, no trailing whitespace allowed.  # noqa: E501

        :param name: The name of this SubscrCreateSubscription.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and not re.search(r'^[\w-][\w -]{,31}(?<! )$', name):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^[\w-][\w -]{,31}(?<! )$/`")  # noqa: E501

        self._name = name

    @property
    def provisioning(self):
        """Gets the provisioning of this SubscrCreateSubscription.  # noqa: E501

        States if provisioning is enabled  # noqa: E501

        :return: The provisioning of this SubscrCreateSubscription.  # noqa: E501
        :rtype: bool
        """
        return self._provisioning

    @provisioning.setter
    def provisioning(self, provisioning):
        """Sets the provisioning of this SubscrCreateSubscription.

        States if provisioning is enabled  # noqa: E501

        :param provisioning: The provisioning of this SubscrCreateSubscription.  # noqa: E501
        :type: bool
        """

        self._provisioning = provisioning

    @property
    def contract_id(self):
        """Gets the contract_id of this SubscrCreateSubscription.  # noqa: E501

        Subscription contract id for OpenStack|K5 account  # noqa: E501

        :return: The contract_id of this SubscrCreateSubscription.  # noqa: E501
        :rtype: str
        """
        return self._contract_id

    @contract_id.setter
    def contract_id(self, contract_id):
        """Sets the contract_id of this SubscrCreateSubscription.

        Subscription contract id for OpenStack|K5 account  # noqa: E501

        :param contract_id: The contract_id of this SubscrCreateSubscription.  # noqa: E501
        :type: str
        """

        self._contract_id = contract_id

    @property
    def project_id(self):
        """Gets the project_id of this SubscrCreateSubscription.  # noqa: E501

        Project ID for OpenStack|K5 platform  # noqa: E501

        :return: The project_id of this SubscrCreateSubscription.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this SubscrCreateSubscription.

        Project ID for OpenStack|K5 platform  # noqa: E501

        :param project_id: The project_id of this SubscrCreateSubscription.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def username(self):
        """Gets the username of this SubscrCreateSubscription.  # noqa: E501

        Subscription username for OpenStack|K5|Vmware subscription  # noqa: E501

        :return: The username of this SubscrCreateSubscription.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this SubscrCreateSubscription.

        Subscription username for OpenStack|K5|Vmware subscription  # noqa: E501

        :param username: The username of this SubscrCreateSubscription.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """Gets the password of this SubscrCreateSubscription.  # noqa: E501

        Password for a subscription for Openstack|K5|VMware subscription  # noqa: E501

        :return: The password of this SubscrCreateSubscription.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this SubscrCreateSubscription.

        Password for a subscription for Openstack|K5|VMware subscription  # noqa: E501

        :param password: The password of this SubscrCreateSubscription.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def access_key(self):
        """Gets the access_key of this SubscrCreateSubscription.  # noqa: E501

        Access key ID for AWS subscription. Parameter for AWS subscription only  # noqa: E501

        :return: The access_key of this SubscrCreateSubscription.  # noqa: E501
        :rtype: str
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        """Sets the access_key of this SubscrCreateSubscription.

        Access key ID for AWS subscription. Parameter for AWS subscription only  # noqa: E501

        :param access_key: The access_key of this SubscrCreateSubscription.  # noqa: E501
        :type: str
        """

        self._access_key = access_key

    @property
    def secret_key(self):
        """Gets the secret_key of this SubscrCreateSubscription.  # noqa: E501

        Secret access key for AWS subscription. Parameter for AWS subscription only  # noqa: E501

        :return: The secret_key of this SubscrCreateSubscription.  # noqa: E501
        :rtype: str
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        """Sets the secret_key of this SubscrCreateSubscription.

        Secret access key for AWS subscription. Parameter for AWS subscription only  # noqa: E501

        :param secret_key: The secret_key of this SubscrCreateSubscription.  # noqa: E501
        :type: str
        """

        self._secret_key = secret_key

    @property
    def platform_subscription_id(self):
        """Gets the platform_subscription_id of this SubscrCreateSubscription.  # noqa: E501

        Platform subscription ID for Azure subscription. Parameter for Azure subscription  # noqa: E501

        :return: The platform_subscription_id of this SubscrCreateSubscription.  # noqa: E501
        :rtype: str
        """
        return self._platform_subscription_id

    @platform_subscription_id.setter
    def platform_subscription_id(self, platform_subscription_id):
        """Sets the platform_subscription_id of this SubscrCreateSubscription.

        Platform subscription ID for Azure subscription. Parameter for Azure subscription  # noqa: E501

        :param platform_subscription_id: The platform_subscription_id of this SubscrCreateSubscription.  # noqa: E501
        :type: str
        """

        self._platform_subscription_id = platform_subscription_id

    @property
    def tenant_id(self):
        """Gets the tenant_id of this SubscrCreateSubscription.  # noqa: E501

        Tenant ID in Azure subscription. Parameter for Azure subscription  # noqa: E501

        :return: The tenant_id of this SubscrCreateSubscription.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this SubscrCreateSubscription.

        Tenant ID in Azure subscription. Parameter for Azure subscription  # noqa: E501

        :param tenant_id: The tenant_id of this SubscrCreateSubscription.  # noqa: E501
        :type: str
        """

        self._tenant_id = tenant_id

    @property
    def authentication_url(self):
        """Gets the authentication_url of this SubscrCreateSubscription.  # noqa: E501

        The URL which is used for authentication and token generation. Parameter for VMware subscription only  # noqa: E501

        :return: The authentication_url of this SubscrCreateSubscription.  # noqa: E501
        :rtype: str
        """
        return self._authentication_url

    @authentication_url.setter
    def authentication_url(self, authentication_url):
        """Sets the authentication_url of this SubscrCreateSubscription.

        The URL which is used for authentication and token generation. Parameter for VMware subscription only  # noqa: E501

        :param authentication_url: The authentication_url of this SubscrCreateSubscription.  # noqa: E501
        :type: str
        """

        self._authentication_url = authentication_url

    @property
    def api_url(self):
        """Gets the api_url of this SubscrCreateSubscription.  # noqa: E501

        The URL which is used for communication with vRO API. Parameter for VMware subscription only  # noqa: E501

        :return: The api_url of this SubscrCreateSubscription.  # noqa: E501
        :rtype: str
        """
        return self._api_url

    @api_url.setter
    def api_url(self, api_url):
        """Sets the api_url of this SubscrCreateSubscription.

        The URL which is used for communication with vRO API. Parameter for VMware subscription only  # noqa: E501

        :param api_url: The api_url of this SubscrCreateSubscription.  # noqa: E501
        :type: str
        """

        self._api_url = api_url

    @property
    def policy(self):
        """Gets the policy of this SubscrCreateSubscription.  # noqa: E501


        :return: The policy of this SubscrCreateSubscription.  # noqa: E501
        :rtype: SubscrPolicy
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this SubscrCreateSubscription.


        :param policy: The policy of this SubscrCreateSubscription.  # noqa: E501
        :type: SubscrPolicy
        """
        if policy is None:
            raise ValueError("Invalid value for `policy`, must not be `None`")  # noqa: E501

        self._policy = policy

    @property
    def region_id(self):
        """Gets the region_id of this SubscrCreateSubscription.  # noqa: E501

        Region of a subscription  # noqa: E501

        :return: The region_id of this SubscrCreateSubscription.  # noqa: E501
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this SubscrCreateSubscription.

        Region of a subscription  # noqa: E501

        :param region_id: The region_id of this SubscrCreateSubscription.  # noqa: E501
        :type: str
        """
        if region_id is None:
            raise ValueError("Invalid value for `region_id`, must not be `None`")  # noqa: E501

        self._region_id = region_id

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
        if not isinstance(other, SubscrCreateSubscription):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
