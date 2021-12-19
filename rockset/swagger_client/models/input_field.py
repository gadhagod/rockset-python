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


class InputField(object):
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
        'field_name': 'str',
        'if_missing': 'str',
        'is_drop': 'bool',
        'param': 'str'
    }

    attribute_map = {
        'field_name': 'field_name',
        'if_missing': 'if_missing',
        'is_drop': 'is_drop',
        'param': 'param'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """InputField - a model defined in Swagger"""  # noqa: E501

        self._field_name = None
        self._if_missing = None
        self._is_drop = None
        self._param = None
        self.discriminator = None

        self.field_name = kwargs.pop('field_name', None)
        self.if_missing = kwargs.pop('if_missing', None)
        self.is_drop = kwargs.pop('is_drop', None)
        self.param = kwargs.pop('param', None)

    @property
    def field_name(self):
        """Gets the field_name of this InputField.  # noqa: E501

        The name of a field, parsed as a SQL qualified name  # noqa: E501

        :return: The field_name of this InputField.  # noqa: E501
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """Sets the field_name of this InputField.

        The name of a field, parsed as a SQL qualified name  # noqa: E501

        :param field_name: The field_name of this InputField.  # noqa: E501
        :type: str
        """

        self._field_name = field_name

    @property
    def if_missing(self):
        """Gets the if_missing of this InputField.  # noqa: E501

        Define the behaviour if fieldName is missing or is null  # noqa: E501

        :return: The if_missing of this InputField.  # noqa: E501
        :rtype: str
        """
        return self._if_missing

    @if_missing.setter
    def if_missing(self, if_missing):
        """Sets the if_missing of this InputField.

        Define the behaviour if fieldName is missing or is null  # noqa: E501

        :param if_missing: The if_missing of this InputField.  # noqa: E501
        :type: str
        """

        self._if_missing = if_missing

    @property
    def is_drop(self):
        """Gets the is_drop of this InputField.  # noqa: E501

        If true, then drop fieldName from the document  # noqa: E501

        :return: The is_drop of this InputField.  # noqa: E501
        :rtype: bool
        """
        return self._is_drop

    @is_drop.setter
    def is_drop(self, is_drop):
        """Sets the is_drop of this InputField.

        If true, then drop fieldName from the document  # noqa: E501

        :param is_drop: The is_drop of this InputField.  # noqa: E501
        :type: bool
        """

        self._is_drop = is_drop

    @property
    def param(self):
        """Gets the param of this InputField.  # noqa: E501

        Sql parameter name  # noqa: E501

        :return: The param of this InputField.  # noqa: E501
        :rtype: str
        """
        return self._param

    @param.setter
    def param(self, param):
        """Sets the param of this InputField.

        Sql parameter name  # noqa: E501

        :param param: The param of this InputField.  # noqa: E501
        :type: str
        """

        self._param = param

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
        if issubclass(InputField, dict):
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
        if not isinstance(other, InputField):
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
