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

from rockset.swagger_client.models.status_dynamo_db import StatusDynamoDb  # noqa: F401,E501


class SourceDynamoDb(object):
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
        'aws_region': 'str',
        'table_name': 'str',
        'status': 'StatusDynamoDb',
        'rcu': 'int'
    }

    attribute_map = {
        'aws_region': 'aws_region',
        'table_name': 'table_name',
        'status': 'status',
        'rcu': 'rcu'
    }

    def __init__(self, table_name, **kwargs):  # noqa: E501
        """SourceDynamoDb - a model defined in Swagger"""  # noqa: E501

        self._aws_region = None
        self._table_name = None
        self._status = None
        self._rcu = None
        self.discriminator = None

        self.aws_region = kwargs.pop('aws_region', None)
        self.table_name = table_name
        self.status = kwargs.pop('status', None)
        self.rcu = kwargs.pop('rcu', None)

    @property
    def aws_region(self):
        """Gets the aws_region of this SourceDynamoDb.  # noqa: E501

        AWS region name of DynamoDB table, by default us-west-2 is used  # noqa: E501

        :return: The aws_region of this SourceDynamoDb.  # noqa: E501
        :rtype: str
        """
        return self._aws_region

    @aws_region.setter
    def aws_region(self, aws_region):
        """Sets the aws_region of this SourceDynamoDb.

        AWS region name of DynamoDB table, by default us-west-2 is used  # noqa: E501

        :param aws_region: The aws_region of this SourceDynamoDb.  # noqa: E501
        :type: str
        """

        self._aws_region = aws_region

    @property
    def table_name(self):
        """Gets the table_name of this SourceDynamoDb.  # noqa: E501

        name of DynamoDB table containing data  # noqa: E501

        :return: The table_name of this SourceDynamoDb.  # noqa: E501
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this SourceDynamoDb.

        name of DynamoDB table containing data  # noqa: E501

        :param table_name: The table_name of this SourceDynamoDb.  # noqa: E501
        :type: str
        """

        self._table_name = table_name

    @property
    def status(self):
        """Gets the status of this SourceDynamoDb.  # noqa: E501

        DynamoDB source status  # noqa: E501

        :return: The status of this SourceDynamoDb.  # noqa: E501
        :rtype: StatusDynamoDb
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SourceDynamoDb.

        DynamoDB source status  # noqa: E501

        :param status: The status of this SourceDynamoDb.  # noqa: E501
        :type: StatusDynamoDb
        """

        self._status = status

    @property
    def rcu(self):
        """Gets the rcu of this SourceDynamoDb.  # noqa: E501

        Max RCU usage for scan  # noqa: E501

        :return: The rcu of this SourceDynamoDb.  # noqa: E501
        :rtype: int
        """
        return self._rcu

    @rcu.setter
    def rcu(self, rcu):
        """Sets the rcu of this SourceDynamoDb.

        Max RCU usage for scan  # noqa: E501

        :param rcu: The rcu of this SourceDynamoDb.  # noqa: E501
        :type: int
        """

        self._rcu = rcu

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
        if issubclass(SourceDynamoDb, dict):
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
        if not isinstance(other, SourceDynamoDb):
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
