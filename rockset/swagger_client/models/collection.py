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

from rockset.swagger_client.models.collection_stats import CollectionStats  # noqa: F401,E501
from rockset.swagger_client.models.field_mapping_v2 import FieldMappingV2  # noqa: F401,E501
from rockset.swagger_client.models.source import Source  # noqa: F401,E501


class Collection(object):
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
        'workspace': 'str',
        'status': 'str',
        'sources': 'list[Source]',
        'stats': 'CollectionStats',
        'retention_secs': 'int',
        'field_mappings': 'list[FieldMappingV2]'
    }

    attribute_map = {
        'created_at': 'created_at',
        'created_by': 'created_by',
        'name': 'name',
        'description': 'description',
        'workspace': 'workspace',
        'status': 'status',
        'sources': 'sources',
        'stats': 'stats',
        'retention_secs': 'retention_secs',
        'field_mappings': 'field_mappings'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """Collection - a model defined in Swagger"""  # noqa: E501

        self._created_at = None
        self._created_by = None
        self._name = None
        self._description = None
        self._workspace = None
        self._status = None
        self._sources = None
        self._stats = None
        self._retention_secs = None
        self._field_mappings = None
        self.discriminator = None

        self.created_at = kwargs.pop('created_at', None)
        self.created_by = kwargs.pop('created_by', None)
        self.name = kwargs.pop('name', None)
        self.description = kwargs.pop('description', None)
        self.workspace = kwargs.pop('workspace', None)
        self.status = kwargs.pop('status', None)
        self.sources = kwargs.pop('sources', None)
        self.stats = kwargs.pop('stats', None)
        self.retention_secs = kwargs.pop('retention_secs', None)
        self.field_mappings = kwargs.pop('field_mappings', None)

    @property
    def created_at(self):
        """Gets the created_at of this Collection.  # noqa: E501

        ISO-8601 date  # noqa: E501

        :return: The created_at of this Collection.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Collection.

        ISO-8601 date  # noqa: E501

        :param created_at: The created_at of this Collection.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def created_by(self):
        """Gets the created_by of this Collection.  # noqa: E501

        email of user who created the collection  # noqa: E501

        :return: The created_by of this Collection.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Collection.

        email of user who created the collection  # noqa: E501

        :param created_by: The created_by of this Collection.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def name(self):
        """Gets the name of this Collection.  # noqa: E501

        unique identifer for collection, can contain alphanumeric or dash characters  # noqa: E501

        :return: The name of this Collection.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Collection.

        unique identifer for collection, can contain alphanumeric or dash characters  # noqa: E501

        :param name: The name of this Collection.  # noqa: E501
        :type: str
        """
        if name is not None and not re.search('^[A-Za-z0-9_\\-.]+$', name):  # noqa: E501
            raise ValueError("Invalid value for `name`, must be a follow pattern or equal to `/^[A-Za-z0-9_\\-.]+$/`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this Collection.  # noqa: E501

        text describing the collection  # noqa: E501

        :return: The description of this Collection.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Collection.

        text describing the collection  # noqa: E501

        :param description: The description of this Collection.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def workspace(self):
        """Gets the workspace of this Collection.  # noqa: E501

        name of the workspace that the collection is in  # noqa: E501

        :return: The workspace of this Collection.  # noqa: E501
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this Collection.

        name of the workspace that the collection is in  # noqa: E501

        :param workspace: The workspace of this Collection.  # noqa: E501
        :type: str
        """

        self._workspace = workspace

    @property
    def status(self):
        """Gets the status of this Collection.  # noqa: E501

        current status of collection, one of: CREATED, READY, DELETED  # noqa: E501

        :return: The status of this Collection.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Collection.

        current status of collection, one of: CREATED, READY, DELETED  # noqa: E501

        :param status: The status of this Collection.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def sources(self):
        """Gets the sources of this Collection.  # noqa: E501

        list of sources from which collection ingests  # noqa: E501

        :return: The sources of this Collection.  # noqa: E501
        :rtype: list[Source]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """Sets the sources of this Collection.

        list of sources from which collection ingests  # noqa: E501

        :param sources: The sources of this Collection.  # noqa: E501
        :type: list[Source]
        """

        self._sources = sources

    @property
    def stats(self):
        """Gets the stats of this Collection.  # noqa: E501

        metrics about the collection  # noqa: E501

        :return: The stats of this Collection.  # noqa: E501
        :rtype: CollectionStats
        """
        return self._stats

    @stats.setter
    def stats(self, stats):
        """Sets the stats of this Collection.

        metrics about the collection  # noqa: E501

        :param stats: The stats of this Collection.  # noqa: E501
        :type: CollectionStats
        """

        self._stats = stats

    @property
    def retention_secs(self):
        """Gets the retention_secs of this Collection.  # noqa: E501

        number of seconds after which data is purged based on event time  # noqa: E501

        :return: The retention_secs of this Collection.  # noqa: E501
        :rtype: int
        """
        return self._retention_secs

    @retention_secs.setter
    def retention_secs(self, retention_secs):
        """Sets the retention_secs of this Collection.

        number of seconds after which data is purged based on event time  # noqa: E501

        :param retention_secs: The retention_secs of this Collection.  # noqa: E501
        :type: int
        """

        self._retention_secs = retention_secs

    @property
    def field_mappings(self):
        """Gets the field_mappings of this Collection.  # noqa: E501

        list of mappings applied on all documents in a collection  # noqa: E501

        :return: The field_mappings of this Collection.  # noqa: E501
        :rtype: list[FieldMappingV2]
        """
        return self._field_mappings

    @field_mappings.setter
    def field_mappings(self, field_mappings):
        """Sets the field_mappings of this Collection.

        list of mappings applied on all documents in a collection  # noqa: E501

        :param field_mappings: The field_mappings of this Collection.  # noqa: E501
        :type: list[FieldMappingV2]
        """

        self._field_mappings = field_mappings

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
        if issubclass(Collection, dict):
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
        if not isinstance(other, Collection):
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