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

from rockset.swagger_client.models.query_lambda_version import QueryLambdaVersion  # noqa: F401,E501


class QueryLambdaTag(object):
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
        'tag_name': 'str',
        'version': 'QueryLambdaVersion'
    }

    attribute_map = {
        'tag_name': 'tag_name',
        'version': 'version'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """QueryLambdaTag - a model defined in Swagger"""  # noqa: E501

        self._tag_name = None
        self._version = None
        self.discriminator = None

        self.tag_name = kwargs.pop('tag_name', None)
        self.version = kwargs.pop('version', None)

    @property
    def tag_name(self):
        """Gets the tag_name of this QueryLambdaTag.  # noqa: E501

        name of Query Lambda tag  # noqa: E501

        :return: The tag_name of this QueryLambdaTag.  # noqa: E501
        :rtype: str
        """
        return self._tag_name

    @tag_name.setter
    def tag_name(self, tag_name):
        """Sets the tag_name of this QueryLambdaTag.

        name of Query Lambda tag  # noqa: E501

        :param tag_name: The tag_name of this QueryLambdaTag.  # noqa: E501
        :type: str
        """

        self._tag_name = tag_name

    @property
    def version(self):
        """Gets the version of this QueryLambdaTag.  # noqa: E501

        query lambda version  # noqa: E501

        :return: The version of this QueryLambdaTag.  # noqa: E501
        :rtype: QueryLambdaVersion
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this QueryLambdaTag.

        query lambda version  # noqa: E501

        :param version: The version of this QueryLambdaTag.  # noqa: E501
        :type: QueryLambdaVersion
        """

        self._version = version

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
        if issubclass(QueryLambdaTag, dict):
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
        if not isinstance(other, QueryLambdaTag):
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
