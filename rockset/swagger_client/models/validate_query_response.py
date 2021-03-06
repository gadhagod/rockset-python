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


class ValidateQueryResponse(object):
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
        'name': 'list[str]',
        'collections': 'list[str]',
        'parameters': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'collections': 'collections',
        'parameters': 'parameters'
    }

    def __init__(self, name, collections, parameters, **kwargs):  # noqa: E501
        """ValidateQueryResponse - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._collections = None
        self._parameters = None
        self.discriminator = None

        self.name = name
        self.collections = collections
        self.parameters = parameters

    @property
    def name(self):
        """Gets the name of this ValidateQueryResponse.  # noqa: E501

        list of collection specified in query  # noqa: E501

        :return: The name of this ValidateQueryResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ValidateQueryResponse.

        list of collection specified in query  # noqa: E501

        :param name: The name of this ValidateQueryResponse.  # noqa: E501
        :type: list[str]
        """

        self._name = name

    @property
    def collections(self):
        """Gets the collections of this ValidateQueryResponse.  # noqa: E501

        list of collection specified in query  # noqa: E501

        :return: The collections of this ValidateQueryResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._collections

    @collections.setter
    def collections(self, collections):
        """Sets the collections of this ValidateQueryResponse.

        list of collection specified in query  # noqa: E501

        :param collections: The collections of this ValidateQueryResponse.  # noqa: E501
        :type: list[str]
        """

        self._collections = collections

    @property
    def parameters(self):
        """Gets the parameters of this ValidateQueryResponse.  # noqa: E501

        list of parameters specified in query  # noqa: E501

        :return: The parameters of this ValidateQueryResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this ValidateQueryResponse.

        list of parameters specified in query  # noqa: E501

        :param parameters: The parameters of this ValidateQueryResponse.  # noqa: E501
        :type: list[str]
        """

        self._parameters = parameters

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
        if issubclass(ValidateQueryResponse, dict):
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
        if not isinstance(other, ValidateQueryResponse):
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
