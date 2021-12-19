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

from rockset.swagger_client.models.input_field import InputField  # noqa: F401,E501
from rockset.swagger_client.models.output_field import OutputField  # noqa: F401,E501


class FieldMappingV2(object):
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
        'name': 'str',
        'is_drop_all_fields': 'bool',
        'input_fields': 'list[InputField]',
        'output_field': 'OutputField'
    }

    attribute_map = {
        'name': 'name',
        'is_drop_all_fields': 'is_drop_all_fields',
        'input_fields': 'input_fields',
        'output_field': 'output_field'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """FieldMappingV2 - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._is_drop_all_fields = None
        self._input_fields = None
        self._output_field = None
        self.discriminator = None

        self.name = kwargs.pop('name', None)
        self.is_drop_all_fields = kwargs.pop('is_drop_all_fields', None)
        self.input_fields = kwargs.pop('input_fields', None)
        self.output_field = kwargs.pop('output_field', None)

    @property
    def name(self):
        """Gets the name of this FieldMappingV2.  # noqa: E501

        A user specified string that is a name for this mapping  # noqa: E501

        :return: The name of this FieldMappingV2.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FieldMappingV2.

        A user specified string that is a name for this mapping  # noqa: E501

        :param name: The name of this FieldMappingV2.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def is_drop_all_fields(self):
        """Gets the is_drop_all_fields of this FieldMappingV2.  # noqa: E501

        A boolean that determines whether to drop all fields in this document. If set, input and output fields should not be set  # noqa: E501

        :return: The is_drop_all_fields of this FieldMappingV2.  # noqa: E501
        :rtype: bool
        """
        return self._is_drop_all_fields

    @is_drop_all_fields.setter
    def is_drop_all_fields(self, is_drop_all_fields):
        """Sets the is_drop_all_fields of this FieldMappingV2.

        A boolean that determines whether to drop all fields in this document. If set, input and output fields should not be set  # noqa: E501

        :param is_drop_all_fields: The is_drop_all_fields of this FieldMappingV2.  # noqa: E501
        :type: bool
        """

        self._is_drop_all_fields = is_drop_all_fields

    @property
    def input_fields(self):
        """Gets the input_fields of this FieldMappingV2.  # noqa: E501

        A List of InputField for this mapping  # noqa: E501

        :return: The input_fields of this FieldMappingV2.  # noqa: E501
        :rtype: list[InputField]
        """
        return self._input_fields

    @input_fields.setter
    def input_fields(self, input_fields):
        """Sets the input_fields of this FieldMappingV2.

        A List of InputField for this mapping  # noqa: E501

        :param input_fields: The input_fields of this FieldMappingV2.  # noqa: E501
        :type: list[InputField]
        """

        self._input_fields = input_fields

    @property
    def output_field(self):
        """Gets the output_field of this FieldMappingV2.  # noqa: E501

        An OutputField for this mapping  # noqa: E501

        :return: The output_field of this FieldMappingV2.  # noqa: E501
        :rtype: OutputField
        """
        return self._output_field

    @output_field.setter
    def output_field(self, output_field):
        """Sets the output_field of this FieldMappingV2.

        An OutputField for this mapping  # noqa: E501

        :param output_field: The output_field of this FieldMappingV2.  # noqa: E501
        :type: OutputField
        """

        self._output_field = output_field

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
        if issubclass(FieldMappingV2, dict):
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
        if not isinstance(other, FieldMappingV2):
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