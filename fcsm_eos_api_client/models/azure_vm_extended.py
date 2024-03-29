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


class AzureVMExtended(object):
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
        'id': 'str',
        'name': 'str',
        'is_managed': 'bool',
        'management_tool_id': 'AnyOfUUIDobject',
        'flavor_id': 'str',
        'image_id': 'AnyOfstringobject',
        'power_state': 'str',
        'created_at': 'str',
        'availability_zone_id': 'str',
        'availability_zone': 'str',
        'availability_set_id': 'AnyOfstringobject',
        'tags': 'list[AzureTag]',
        'interface_ids': 'list[str]',
        'interfaces': 'list[str]',
        'volume_ids': 'list[str]',
        'volumes': 'list[str]',
        'allowed_power_actions': 'list[AzureVMPowerAction]',
        'status': 'str',
        'status_message': 'str',
        'workshift': 'AzureOptionalWorkshift'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'is_managed': 'isManaged',
        'management_tool_id': 'managementToolId',
        'flavor_id': 'flavorId',
        'image_id': 'imageId',
        'power_state': 'powerState',
        'created_at': 'createdAt',
        'availability_zone_id': 'availabilityZoneId',
        'availability_zone': 'availabilityZone',
        'availability_set_id': 'availabilitySetId',
        'tags': 'tags',
        'interface_ids': 'interfaceIds',
        'interfaces': 'interfaces',
        'volume_ids': 'volumeIds',
        'volumes': 'volumes',
        'allowed_power_actions': 'allowedPowerActions',
        'status': 'status',
        'status_message': 'statusMessage',
        'workshift': 'workshift'
    }

    def __init__(self, id=None, name=None, is_managed=None, management_tool_id=None, flavor_id=None, image_id=None, power_state=None, created_at=None, availability_zone_id='default', availability_zone=None, availability_set_id=None, tags=None, interface_ids=None, interfaces=None, volume_ids=None, volumes=None, allowed_power_actions=None, status=None, status_message=None, workshift=None):  # noqa: E501
        """AzureVMExtended - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._name = None
        self._is_managed = None
        self._management_tool_id = None
        self._flavor_id = None
        self._image_id = None
        self._power_state = None
        self._created_at = None
        self._availability_zone_id = None
        self._availability_zone = None
        self._availability_set_id = None
        self._tags = None
        self._interface_ids = None
        self._interfaces = None
        self._volume_ids = None
        self._volumes = None
        self._allowed_power_actions = None
        self._status = None
        self._status_message = None
        self._workshift = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.is_managed = is_managed
        self.management_tool_id = management_tool_id
        self.flavor_id = flavor_id
        self.image_id = image_id
        self.power_state = power_state
        self.created_at = created_at
        self.availability_zone_id = availability_zone_id
        self.availability_zone = availability_zone
        if availability_set_id is not None:
            self.availability_set_id = availability_set_id
        self.tags = tags
        self.interface_ids = interface_ids
        if interfaces is not None:
            self.interfaces = interfaces
        self.volume_ids = volume_ids
        if volumes is not None:
            self.volumes = volumes
        self.allowed_power_actions = allowed_power_actions
        self.status = status
        self.status_message = status_message
        if workshift is not None:
            self.workshift = workshift

    @property
    def id(self):
        """Gets the id of this AzureVMExtended.  # noqa: E501


        :return: The id of this AzureVMExtended.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AzureVMExtended.


        :param id: The id of this AzureVMExtended.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this AzureVMExtended.  # noqa: E501


        :return: The name of this AzureVMExtended.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AzureVMExtended.


        :param name: The name of this AzureVMExtended.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def is_managed(self):
        """Gets the is_managed of this AzureVMExtended.  # noqa: E501


        :return: The is_managed of this AzureVMExtended.  # noqa: E501
        :rtype: bool
        """
        return self._is_managed

    @is_managed.setter
    def is_managed(self, is_managed):
        """Sets the is_managed of this AzureVMExtended.


        :param is_managed: The is_managed of this AzureVMExtended.  # noqa: E501
        :type: bool
        """
        if is_managed is None:
            raise ValueError("Invalid value for `is_managed`, must not be `None`")  # noqa: E501

        self._is_managed = is_managed

    @property
    def management_tool_id(self):
        """Gets the management_tool_id of this AzureVMExtended.  # noqa: E501


        :return: The management_tool_id of this AzureVMExtended.  # noqa: E501
        :rtype: AnyOfUUIDobject
        """
        return self._management_tool_id

    @management_tool_id.setter
    def management_tool_id(self, management_tool_id):
        """Sets the management_tool_id of this AzureVMExtended.


        :param management_tool_id: The management_tool_id of this AzureVMExtended.  # noqa: E501
        :type: AnyOfUUIDobject
        """
        if management_tool_id is None:
            raise ValueError("Invalid value for `management_tool_id`, must not be `None`")  # noqa: E501

        self._management_tool_id = management_tool_id

    @property
    def flavor_id(self):
        """Gets the flavor_id of this AzureVMExtended.  # noqa: E501


        :return: The flavor_id of this AzureVMExtended.  # noqa: E501
        :rtype: str
        """
        return self._flavor_id

    @flavor_id.setter
    def flavor_id(self, flavor_id):
        """Sets the flavor_id of this AzureVMExtended.


        :param flavor_id: The flavor_id of this AzureVMExtended.  # noqa: E501
        :type: str
        """
        if flavor_id is None:
            raise ValueError("Invalid value for `flavor_id`, must not be `None`")  # noqa: E501

        self._flavor_id = flavor_id

    @property
    def image_id(self):
        """Gets the image_id of this AzureVMExtended.  # noqa: E501


        :return: The image_id of this AzureVMExtended.  # noqa: E501
        :rtype: AnyOfstringobject
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this AzureVMExtended.


        :param image_id: The image_id of this AzureVMExtended.  # noqa: E501
        :type: AnyOfstringobject
        """
        if image_id is None:
            raise ValueError("Invalid value for `image_id`, must not be `None`")  # noqa: E501

        self._image_id = image_id

    @property
    def power_state(self):
        """Gets the power_state of this AzureVMExtended.  # noqa: E501


        :return: The power_state of this AzureVMExtended.  # noqa: E501
        :rtype: str
        """
        return self._power_state

    @power_state.setter
    def power_state(self, power_state):
        """Sets the power_state of this AzureVMExtended.


        :param power_state: The power_state of this AzureVMExtended.  # noqa: E501
        :type: str
        """
        if power_state is None:
            raise ValueError("Invalid value for `power_state`, must not be `None`")  # noqa: E501
        allowed_values = ["unknown", "running", "stopped", "pending"]  # noqa: E501
        if power_state not in allowed_values:
            raise ValueError(
                "Invalid value for `power_state` ({0}), must be one of {1}"  # noqa: E501
                .format(power_state, allowed_values)
            )

        self._power_state = power_state

    @property
    def created_at(self):
        """Gets the created_at of this AzureVMExtended.  # noqa: E501


        :return: The created_at of this AzureVMExtended.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this AzureVMExtended.


        :param created_at: The created_at of this AzureVMExtended.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def availability_zone_id(self):
        """Gets the availability_zone_id of this AzureVMExtended.  # noqa: E501


        :return: The availability_zone_id of this AzureVMExtended.  # noqa: E501
        :rtype: str
        """
        return self._availability_zone_id

    @availability_zone_id.setter
    def availability_zone_id(self, availability_zone_id):
        """Sets the availability_zone_id of this AzureVMExtended.


        :param availability_zone_id: The availability_zone_id of this AzureVMExtended.  # noqa: E501
        :type: str
        """
        if availability_zone_id is None:
            raise ValueError("Invalid value for `availability_zone_id`, must not be `None`")  # noqa: E501

        self._availability_zone_id = availability_zone_id

    @property
    def availability_zone(self):
        """Gets the availability_zone of this AzureVMExtended.  # noqa: E501

        Deprecated after 3 months. Please use `availabilityZoneId`  # noqa: E501

        :return: The availability_zone of this AzureVMExtended.  # noqa: E501
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this AzureVMExtended.

        Deprecated after 3 months. Please use `availabilityZoneId`  # noqa: E501

        :param availability_zone: The availability_zone of this AzureVMExtended.  # noqa: E501
        :type: str
        """
        if availability_zone is None:
            raise ValueError("Invalid value for `availability_zone`, must not be `None`")  # noqa: E501

        self._availability_zone = availability_zone

    @property
    def availability_set_id(self):
        """Gets the availability_set_id of this AzureVMExtended.  # noqa: E501


        :return: The availability_set_id of this AzureVMExtended.  # noqa: E501
        :rtype: AnyOfstringobject
        """
        return self._availability_set_id

    @availability_set_id.setter
    def availability_set_id(self, availability_set_id):
        """Sets the availability_set_id of this AzureVMExtended.


        :param availability_set_id: The availability_set_id of this AzureVMExtended.  # noqa: E501
        :type: AnyOfstringobject
        """

        self._availability_set_id = availability_set_id

    @property
    def tags(self):
        """Gets the tags of this AzureVMExtended.  # noqa: E501


        :return: The tags of this AzureVMExtended.  # noqa: E501
        :rtype: list[AzureTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this AzureVMExtended.


        :param tags: The tags of this AzureVMExtended.  # noqa: E501
        :type: list[AzureTag]
        """
        if tags is None:
            raise ValueError("Invalid value for `tags`, must not be `None`")  # noqa: E501

        self._tags = tags

    @property
    def interface_ids(self):
        """Gets the interface_ids of this AzureVMExtended.  # noqa: E501


        :return: The interface_ids of this AzureVMExtended.  # noqa: E501
        :rtype: list[str]
        """
        return self._interface_ids

    @interface_ids.setter
    def interface_ids(self, interface_ids):
        """Sets the interface_ids of this AzureVMExtended.


        :param interface_ids: The interface_ids of this AzureVMExtended.  # noqa: E501
        :type: list[str]
        """
        if interface_ids is None:
            raise ValueError("Invalid value for `interface_ids`, must not be `None`")  # noqa: E501

        self._interface_ids = interface_ids

    @property
    def interfaces(self):
        """Gets the interfaces of this AzureVMExtended.  # noqa: E501

        Deprecated after 3 months. Please use `interfaceIds`  # noqa: E501

        :return: The interfaces of this AzureVMExtended.  # noqa: E501
        :rtype: list[str]
        """
        return self._interfaces

    @interfaces.setter
    def interfaces(self, interfaces):
        """Sets the interfaces of this AzureVMExtended.

        Deprecated after 3 months. Please use `interfaceIds`  # noqa: E501

        :param interfaces: The interfaces of this AzureVMExtended.  # noqa: E501
        :type: list[str]
        """

        self._interfaces = interfaces

    @property
    def volume_ids(self):
        """Gets the volume_ids of this AzureVMExtended.  # noqa: E501

        List will contain at least one item which will be an ID of the OS volume virtual machine boots from   # noqa: E501

        :return: The volume_ids of this AzureVMExtended.  # noqa: E501
        :rtype: list[str]
        """
        return self._volume_ids

    @volume_ids.setter
    def volume_ids(self, volume_ids):
        """Sets the volume_ids of this AzureVMExtended.

        List will contain at least one item which will be an ID of the OS volume virtual machine boots from   # noqa: E501

        :param volume_ids: The volume_ids of this AzureVMExtended.  # noqa: E501
        :type: list[str]
        """
        if volume_ids is None:
            raise ValueError("Invalid value for `volume_ids`, must not be `None`")  # noqa: E501

        self._volume_ids = volume_ids

    @property
    def volumes(self):
        """Gets the volumes of this AzureVMExtended.  # noqa: E501

        Deprecated after 3 months. Please use `volumeIds`  # noqa: E501

        :return: The volumes of this AzureVMExtended.  # noqa: E501
        :rtype: list[str]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """Sets the volumes of this AzureVMExtended.

        Deprecated after 3 months. Please use `volumeIds`  # noqa: E501

        :param volumes: The volumes of this AzureVMExtended.  # noqa: E501
        :type: list[str]
        """

        self._volumes = volumes

    @property
    def allowed_power_actions(self):
        """Gets the allowed_power_actions of this AzureVMExtended.  # noqa: E501


        :return: The allowed_power_actions of this AzureVMExtended.  # noqa: E501
        :rtype: list[AzureVMPowerAction]
        """
        return self._allowed_power_actions

    @allowed_power_actions.setter
    def allowed_power_actions(self, allowed_power_actions):
        """Sets the allowed_power_actions of this AzureVMExtended.


        :param allowed_power_actions: The allowed_power_actions of this AzureVMExtended.  # noqa: E501
        :type: list[AzureVMPowerAction]
        """
        if allowed_power_actions is None:
            raise ValueError("Invalid value for `allowed_power_actions`, must not be `None`")  # noqa: E501

        self._allowed_power_actions = allowed_power_actions

    @property
    def status(self):
        """Gets the status of this AzureVMExtended.  # noqa: E501


        :return: The status of this AzureVMExtended.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AzureVMExtended.


        :param status: The status of this AzureVMExtended.  # noqa: E501
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
        """Gets the status_message of this AzureVMExtended.  # noqa: E501


        :return: The status_message of this AzureVMExtended.  # noqa: E501
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """Sets the status_message of this AzureVMExtended.


        :param status_message: The status_message of this AzureVMExtended.  # noqa: E501
        :type: str
        """

        self._status_message = status_message

    @property
    def workshift(self):
        """Gets the workshift of this AzureVMExtended.  # noqa: E501


        :return: The workshift of this AzureVMExtended.  # noqa: E501
        :rtype: AzureOptionalWorkshift
        """
        return self._workshift

    @workshift.setter
    def workshift(self, workshift):
        """Sets the workshift of this AzureVMExtended.


        :param workshift: The workshift of this AzureVMExtended.  # noqa: E501
        :type: AzureOptionalWorkshift
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
        if not isinstance(other, AzureVMExtended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
