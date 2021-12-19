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

from rockset.swagger_client.models.query_parameter import QueryParameter  # noqa: F401,E501


class ExecuteQueryLambdaRequest(object):
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
        'parameters': 'list[QueryParameter]',
        'default_row_limit': 'int',
        'generate_warnings': 'bool'
    }

    attribute_map = {
        'parameters': 'parameters',
        'default_row_limit': 'default_row_limit',
        'generate_warnings': 'generate_warnings'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """ExecuteQueryLambdaRequest - a model defined in Swagger"""  # noqa: E501

        self._parameters = None
        self._default_row_limit = None
        self._generate_warnings = None
        self.discriminator = None

        self.parameters = kwargs.pop('parameters', None)
        self.default_row_limit = kwargs.pop('default_row_limit', None)
        self.generate_warnings = kwargs.pop('generate_warnings', None)

    @property
    def parameters(self):
        """Gets the parameters of this ExecuteQueryLambdaRequest.  # noqa: E501

        list of named parameters  # noqa: E501

        :return: The parameters of this ExecuteQueryLambdaRequest.  # noqa: E501
        :rtype: list[QueryParameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this ExecuteQueryLambdaRequest.

        list of named parameters  # noqa: E501

        :param parameters: The parameters of this ExecuteQueryLambdaRequest.  # noqa: E501
        :type: list[QueryParameter]
        """

        self._parameters = parameters

    @property
    def default_row_limit(self):
        """Gets the default_row_limit of this ExecuteQueryLambdaRequest.  # noqa: E501

        Row limit to use if no limit specified in the SQL query text  # noqa: E501

        :return: The default_row_limit of this ExecuteQueryLambdaRequest.  # noqa: E501
        :rtype: int
        """
        return self._default_row_limit

    @default_row_limit.setter
    def default_row_limit(self, default_row_limit):
        """Sets the default_row_limit of this ExecuteQueryLambdaRequest.

        Row limit to use if no limit specified in the SQL query text  # noqa: E501

        :param default_row_limit: The default_row_limit of this ExecuteQueryLambdaRequest.  # noqa: E501
        :type: int
        """

        self._default_row_limit = default_row_limit

    @property
    def generate_warnings(self):
        """Gets the generate_warnings of this ExecuteQueryLambdaRequest.  # noqa: E501

        Whether to generate warnings  # noqa: E501

        :return: The generate_warnings of this ExecuteQueryLambdaRequest.  # noqa: E501
        :rtype: bool
        """
        return self._generate_warnings

    @generate_warnings.setter
    def generate_warnings(self, generate_warnings):
        """Sets the generate_warnings of this ExecuteQueryLambdaRequest.

        Whether to generate warnings  # noqa: E501

        :param generate_warnings: The generate_warnings of this ExecuteQueryLambdaRequest.  # noqa: E501
        :type: bool
        """

        self._generate_warnings = generate_warnings

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
        if issubclass(ExecuteQueryLambdaRequest, dict):
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
        if not isinstance(other, ExecuteQueryLambdaRequest):
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
