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


class SourceRedshift(object):
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
        'database': 'str',
        'schema': 'str',
        'table_name': 'str',
        'incremental_field': 'str'
    }

    attribute_map = {
        'database': 'database',
        'schema': 'schema',
        'table_name': 'table_name',
        'incremental_field': 'incremental_field'
    }

    def __init__(self, database, schema, table_name, **kwargs):  # noqa: E501
        """SourceRedshift - a model defined in Swagger"""  # noqa: E501

        self._database = None
        self._schema = None
        self._table_name = None
        self._incremental_field = None
        self.discriminator = None

        self.database = database
        self.schema = schema
        self.table_name = table_name
        self.incremental_field = kwargs.pop('incremental_field', None)

    @property
    def database(self):
        """Gets the database of this SourceRedshift.  # noqa: E501

        name of the database in Redshift Cluster  # noqa: E501

        :return: The database of this SourceRedshift.  # noqa: E501
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        """Sets the database of this SourceRedshift.

        name of the database in Redshift Cluster  # noqa: E501

        :param database: The database of this SourceRedshift.  # noqa: E501
        :type: str
        """

        self._database = database

    @property
    def schema(self):
        """Gets the schema of this SourceRedshift.  # noqa: E501

        schema which contains the Redshift table  # noqa: E501

        :return: The schema of this SourceRedshift.  # noqa: E501
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this SourceRedshift.

        schema which contains the Redshift table  # noqa: E501

        :param schema: The schema of this SourceRedshift.  # noqa: E501
        :type: str
        """

        self._schema = schema

    @property
    def table_name(self):
        """Gets the table_name of this SourceRedshift.  # noqa: E501

        name of Redshift table containing data  # noqa: E501

        :return: The table_name of this SourceRedshift.  # noqa: E501
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this SourceRedshift.

        name of Redshift table containing data  # noqa: E501

        :param table_name: The table_name of this SourceRedshift.  # noqa: E501
        :type: str
        """

        self._table_name = table_name

    @property
    def incremental_field(self):
        """Gets the incremental_field of this SourceRedshift.  # noqa: E501

        field in Redshift source table to monitor for updates  # noqa: E501

        :return: The incremental_field of this SourceRedshift.  # noqa: E501
        :rtype: str
        """
        return self._incremental_field

    @incremental_field.setter
    def incremental_field(self, incremental_field):
        """Sets the incremental_field of this SourceRedshift.

        field in Redshift source table to monitor for updates  # noqa: E501

        :param incremental_field: The incremental_field of this SourceRedshift.  # noqa: E501
        :type: str
        """

        self._incremental_field = incremental_field

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
        if issubclass(SourceRedshift, dict):
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
        if not isinstance(other, SourceRedshift):
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