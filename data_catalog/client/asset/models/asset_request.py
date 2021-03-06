# coding: utf-8

"""
    Asset

    Data Catalog Asset API.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: katacseke@gmail.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from data_catalog.client.asset.configuration import Configuration


class AssetRequest(object):
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
        'name': 'str',
        'description': 'str',
        'location': 'Location',
        'tags': 'list[str]',
        'format': 'str',
        'size': 'str',
        'namespace': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'location': 'location',
        'tags': 'tags',
        'format': 'format',
        'size': 'size',
        'namespace': 'namespace'
    }

    def __init__(self, name=None, description=None, location=None, tags=None, format=None, size=None, namespace=None, local_vars_configuration=None):  # noqa: E501
        """AssetRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._description = None
        self._location = None
        self._tags = None
        self._format = None
        self._size = None
        self._namespace = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if location is not None:
            self.location = location
        if tags is not None:
            self.tags = tags
        if format is not None:
            self.format = format
        if size is not None:
            self.size = size
        if namespace is not None:
            self.namespace = namespace

    @property
    def name(self):
        """Gets the name of this AssetRequest.  # noqa: E501

        A short name of the data asset.  # noqa: E501

        :return: The name of this AssetRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AssetRequest.

        A short name of the data asset.  # noqa: E501

        :param name: The name of this AssetRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this AssetRequest.  # noqa: E501

        A longer description about the content of the data asset.  # noqa: E501

        :return: The description of this AssetRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AssetRequest.

        A longer description about the content of the data asset.  # noqa: E501

        :param description: The description of this AssetRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def location(self):
        """Gets the location of this AssetRequest.  # noqa: E501


        :return: The location of this AssetRequest.  # noqa: E501
        :rtype: Location
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this AssetRequest.


        :param location: The location of this AssetRequest.  # noqa: E501
        :type: Location
        """

        self._location = location

    @property
    def tags(self):
        """Gets the tags of this AssetRequest.  # noqa: E501

        Keywords assigned to the asset.  # noqa: E501

        :return: The tags of this AssetRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this AssetRequest.

        Keywords assigned to the asset.  # noqa: E501

        :param tags: The tags of this AssetRequest.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def format(self):
        """Gets the format of this AssetRequest.  # noqa: E501

        The file format of the asset.   # noqa: E501

        :return: The format of this AssetRequest.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this AssetRequest.

        The file format of the asset.   # noqa: E501

        :param format: The format of this AssetRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["csv", "json", "container"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and format not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `format` ({0}), must be one of {1}"  # noqa: E501
                .format(format, allowed_values)
            )

        self._format = format

    @property
    def size(self):
        """Gets the size of this AssetRequest.  # noqa: E501

        The approximate size of the asset.  # noqa: E501

        :return: The size of this AssetRequest.  # noqa: E501
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this AssetRequest.

        The approximate size of the asset.  # noqa: E501

        :param size: The size of this AssetRequest.  # noqa: E501
        :type: str
        """

        self._size = size

    @property
    def namespace(self):
        """Gets the namespace of this AssetRequest.  # noqa: E501

        The namespace of the asset. An asset has one namespace, which can be used to group assets together (eg. by projects).  # noqa: E501

        :return: The namespace of this AssetRequest.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this AssetRequest.

        The namespace of the asset. An asset has one namespace, which can be used to group assets together (eg. by projects).  # noqa: E501

        :param namespace: The namespace of this AssetRequest.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

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
        if not isinstance(other, AssetRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AssetRequest):
            return True

        return self.to_dict() != other.to_dict()
