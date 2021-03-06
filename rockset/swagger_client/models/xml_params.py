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


class XmlParams(object):
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
        'root_tag': 'str',
        'encoding': 'str',
        'doc_tag': 'str',
        'value_tag': 'str',
        'attribute_prefix': 'str'
    }

    attribute_map = {
        'root_tag': 'root_tag',
        'encoding': 'encoding',
        'doc_tag': 'doc_tag',
        'value_tag': 'value_tag',
        'attribute_prefix': 'attribute_prefix'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """XmlParams - a model defined in Swagger"""  # noqa: E501

        self._root_tag = None
        self._encoding = None
        self._doc_tag = None
        self._value_tag = None
        self._attribute_prefix = None
        self.discriminator = None

        self.root_tag = kwargs.pop('root_tag', None)
        self.encoding = kwargs.pop('encoding', None)
        self.doc_tag = kwargs.pop('doc_tag', None)
        self.value_tag = kwargs.pop('value_tag', None)
        self.attribute_prefix = kwargs.pop('attribute_prefix', None)

    @property
    def root_tag(self):
        """Gets the root_tag of this XmlParams.  # noqa: E501

        tag until which xml is ignored  # noqa: E501

        :return: The root_tag of this XmlParams.  # noqa: E501
        :rtype: str
        """
        return self._root_tag

    @root_tag.setter
    def root_tag(self, root_tag):
        """Sets the root_tag of this XmlParams.

        tag until which xml is ignored  # noqa: E501

        :param root_tag: The root_tag of this XmlParams.  # noqa: E501
        :type: str
        """

        self._root_tag = root_tag

    @property
    def encoding(self):
        """Gets the encoding of this XmlParams.  # noqa: E501

        encoding in which data source is encoded  # noqa: E501

        :return: The encoding of this XmlParams.  # noqa: E501
        :rtype: str
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        """Sets the encoding of this XmlParams.

        encoding in which data source is encoded  # noqa: E501

        :param encoding: The encoding of this XmlParams.  # noqa: E501
        :type: str
        """

        self._encoding = encoding

    @property
    def doc_tag(self):
        """Gets the doc_tag of this XmlParams.  # noqa: E501

        tags with which documents are identified  # noqa: E501

        :return: The doc_tag of this XmlParams.  # noqa: E501
        :rtype: str
        """
        return self._doc_tag

    @doc_tag.setter
    def doc_tag(self, doc_tag):
        """Sets the doc_tag of this XmlParams.

        tags with which documents are identified  # noqa: E501

        :param doc_tag: The doc_tag of this XmlParams.  # noqa: E501
        :type: str
        """

        self._doc_tag = doc_tag

    @property
    def value_tag(self):
        """Gets the value_tag of this XmlParams.  # noqa: E501

        tag used for the value when there are attributes in the element having no child  # noqa: E501

        :return: The value_tag of this XmlParams.  # noqa: E501
        :rtype: str
        """
        return self._value_tag

    @value_tag.setter
    def value_tag(self, value_tag):
        """Sets the value_tag of this XmlParams.

        tag used for the value when there are attributes in the element having no child  # noqa: E501

        :param value_tag: The value_tag of this XmlParams.  # noqa: E501
        :type: str
        """

        self._value_tag = value_tag

    @property
    def attribute_prefix(self):
        """Gets the attribute_prefix of this XmlParams.  # noqa: E501

        tag to differentiate between attributes and elements  # noqa: E501

        :return: The attribute_prefix of this XmlParams.  # noqa: E501
        :rtype: str
        """
        return self._attribute_prefix

    @attribute_prefix.setter
    def attribute_prefix(self, attribute_prefix):
        """Sets the attribute_prefix of this XmlParams.

        tag to differentiate between attributes and elements  # noqa: E501

        :param attribute_prefix: The attribute_prefix of this XmlParams.  # noqa: E501
        :type: str
        """

        self._attribute_prefix = attribute_prefix

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
        if issubclass(XmlParams, dict):
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
        if not isinstance(other, XmlParams):
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
