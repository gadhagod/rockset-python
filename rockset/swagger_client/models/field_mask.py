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

from rockset.swagger_client.models.field_mask_mask import FieldMaskMask  # noqa: F401,E501


class FieldMask(object):
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
        'input_path': 'list[str]',
        'mask': 'FieldMaskMask'
    }

    attribute_map = {
        'input_path': 'input_path',
        'mask': 'mask'
    }

    def __init__(self, input_path, **kwargs):  # noqa: E501
        """FieldMask - a model defined in Swagger"""  # noqa: E501

        self._input_path = None
        self._mask = None
        self.discriminator = None

        self.input_path = input_path
        self.mask = kwargs.pop('mask', None)

    @property
    def input_path(self):
        """Gets the input_path of this FieldMask.  # noqa: E501


        :return: The input_path of this FieldMask.  # noqa: E501
        :rtype: list[str]
        """
        return self._input_path

    @input_path.setter
    def input_path(self, input_path):
        """Sets the input_path of this FieldMask.


        :param input_path: The input_path of this FieldMask.  # noqa: E501
        :type: list[str]
        """

        self._input_path = input_path

    @property
    def mask(self):
        """Gets the mask of this FieldMask.  # noqa: E501


        :return: The mask of this FieldMask.  # noqa: E501
        :rtype: FieldMaskMask
        """
        return self._mask

    @mask.setter
    def mask(self, mask):
        """Sets the mask of this FieldMask.


        :param mask: The mask of this FieldMask.  # noqa: E501
        :type: FieldMaskMask
        """

        self._mask = mask

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
        if issubclass(FieldMask, dict):
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
        if not isinstance(other, FieldMask):
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