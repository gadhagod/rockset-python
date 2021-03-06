# coding: utf-8

"""
    REST API

    Rockset's REST API allows for creating and managing all resources in Rockset. Each supported endpoint is documented below.  All requests must be authorized with a Rockset API key, which can be created in the [Rockset console](https://console.rockset.com). The API key must be provided as `ApiKey <api_key>` in the `Authorization` request header. For example: ``` Authorization: ApiKey aB35kDjg93J5nsf4GjwMeErAVd832F7ad4vhsW1S02kfZiab42sTsfW5Sxt25asT ```  All endpoints are only accessible via https.  Build something awesome!  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Workspace(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'created_at': 'str',
        'created_by': 'str',
        'name': 'str',
        'description': 'str',
        'collection_count': 'int'
    }

    attribute_map = {
        'created_at': 'created_at',
        'created_by': 'created_by',
        'name': 'name',
        'description': 'description',
        'collection_count': 'collection_count'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """Workspace - a model defined in Swagger"""  # noqa: E501

        self._created_at = None
        self._created_by = None
        self._name = None
        self._description = None
        self._collection_count = None
        self.discriminator = None

        self.created_at = kwargs.pop('created_at', None)
        self.created_by = kwargs.pop('created_by', None)
        self.name = kwargs.pop('name', None)
        self.description = kwargs.pop('description', None)
        self.collection_count = kwargs.pop('collection_count', None)

    @property
    def created_at(self):
        """Gets the created_at of this Workspace.  # noqa: E501

        ISO-8601 date of when workspace was created  # noqa: E501

        :return: The created_at of this Workspace.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Workspace.

        ISO-8601 date of when workspace was created  # noqa: E501

        :param created_at: The created_at of this Workspace.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def created_by(self):
        """Gets the created_by of this Workspace.  # noqa: E501

        email of user who created the workspace  # noqa: E501

        :return: The created_by of this Workspace.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Workspace.

        email of user who created the workspace  # noqa: E501

        :param created_by: The created_by of this Workspace.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def name(self):
        """Gets the name of this Workspace.  # noqa: E501

        descriptive label and unique identifier  # noqa: E501

        :return: The name of this Workspace.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Workspace.

        descriptive label and unique identifier  # noqa: E501

        :param name: The name of this Workspace.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this Workspace.  # noqa: E501

        longer explanation for the workspace  # noqa: E501

        :return: The description of this Workspace.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Workspace.

        longer explanation for the workspace  # noqa: E501

        :param description: The description of this Workspace.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def collection_count(self):
        """Gets the collection_count of this Workspace.  # noqa: E501

        number of collections that are immediate children of workspace  # noqa: E501

        :return: The collection_count of this Workspace.  # noqa: E501
        :rtype: int
        """
        return self._collection_count

    @collection_count.setter
    def collection_count(self, collection_count):
        """Sets the collection_count of this Workspace.

        number of collections that are immediate children of workspace  # noqa: E501

        :param collection_count: The collection_count of this Workspace.  # noqa: E501
        :type: int
        """

        self._collection_count = collection_count

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(Workspace, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Workspace):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

    def __getitem__(self, item):
        return getattr(self, item)

    def get(self, item):
        return getattr(self, item)

    def items(self):
        return self.to_dict().items()

    def __setitem__(self, item, value):
        return seattr(self, item, value)
