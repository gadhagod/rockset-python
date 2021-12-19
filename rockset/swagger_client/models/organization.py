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


class Organization(object):
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
        'id': 'str',
        'created_at': 'str',
        'display_name': 'str',
        'company_name': 'str',
        'external_id': 'str',
        'rockset_user': 'str',
        'state': 'str',
        'num_dedicated_pods': 'int'
    }

    attribute_map = {
        'id': 'id',
        'created_at': 'created_at',
        'display_name': 'display_name',
        'company_name': 'company_name',
        'external_id': 'external_id',
        'rockset_user': 'rockset_user',
        'state': 'state',
        'num_dedicated_pods': 'num_dedicated_pods'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """Organization - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._created_at = None
        self._display_name = None
        self._company_name = None
        self._external_id = None
        self._rockset_user = None
        self._state = None
        self._num_dedicated_pods = None
        self.discriminator = None

        self.id = kwargs.pop('id', None)
        self.created_at = kwargs.pop('created_at', None)
        self.display_name = kwargs.pop('display_name', None)
        self.company_name = kwargs.pop('company_name', None)
        self.external_id = kwargs.pop('external_id', None)
        self.rockset_user = kwargs.pop('rockset_user', None)
        self.state = kwargs.pop('state', None)
        self.num_dedicated_pods = kwargs.pop('num_dedicated_pods', None)

    @property
    def id(self):
        """Gets the id of this Organization.  # noqa: E501

        unique identifier for the organization  # noqa: E501

        :return: The id of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Organization.

        unique identifier for the organization  # noqa: E501

        :param id: The id of this Organization.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def created_at(self):
        """Gets the created_at of this Organization.  # noqa: E501

        ISO-8601 date  # noqa: E501

        :return: The created_at of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Organization.

        ISO-8601 date  # noqa: E501

        :param created_at: The created_at of this Organization.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def display_name(self):
        """Gets the display_name of this Organization.  # noqa: E501

        name of the organization  # noqa: E501

        :return: The display_name of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Organization.

        name of the organization  # noqa: E501

        :param display_name: The display_name of this Organization.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def company_name(self):
        """Gets the company_name of this Organization.  # noqa: E501

        name of the company  # noqa: E501

        :return: The company_name of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this Organization.

        name of the company  # noqa: E501

        :param company_name: The company_name of this Organization.  # noqa: E501
        :type: str
        """

        self._company_name = company_name

    @property
    def external_id(self):
        """Gets the external_id of this Organization.  # noqa: E501

        organization's unique external ID within Rockset  # noqa: E501

        :return: The external_id of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this Organization.

        organization's unique external ID within Rockset  # noqa: E501

        :param external_id: The external_id of this Organization.  # noqa: E501
        :type: str
        """

        self._external_id = external_id

    @property
    def rockset_user(self):
        """Gets the rockset_user of this Organization.  # noqa: E501


        :return: The rockset_user of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._rockset_user

    @rockset_user.setter
    def rockset_user(self, rockset_user):
        """Sets the rockset_user of this Organization.


        :param rockset_user: The rockset_user of this Organization.  # noqa: E501
        :type: str
        """

        self._rockset_user = rockset_user

    @property
    def state(self):
        """Gets the state of this Organization.  # noqa: E501

        org state  # noqa: E501

        :return: The state of this Organization.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Organization.

        org state  # noqa: E501

        :param state: The state of this Organization.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def num_dedicated_pods(self):
        """Gets the num_dedicated_pods of this Organization.  # noqa: E501

        number of dedicated pods  # noqa: E501

        :return: The num_dedicated_pods of this Organization.  # noqa: E501
        :rtype: int
        """
        return self._num_dedicated_pods

    @num_dedicated_pods.setter
    def num_dedicated_pods(self, num_dedicated_pods):
        """Sets the num_dedicated_pods of this Organization.

        number of dedicated pods  # noqa: E501

        :param num_dedicated_pods: The num_dedicated_pods of this Organization.  # noqa: E501
        :type: int
        """

        self._num_dedicated_pods = num_dedicated_pods

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
        if issubclass(Organization, dict):
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
        if not isinstance(other, Organization):
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
