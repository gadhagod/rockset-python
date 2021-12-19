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

from rockset.swagger_client.models.org_membership import OrgMembership  # noqa: F401,E501
from rockset.swagger_client.models.organization import Organization  # noqa: F401,E501


class User(object):
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
        'created_at': 'str',
        'email': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'roles': 'list[str]',
        'state': 'str',
        'org': 'str',
        'invite_state': 'str',
        'orgs': 'list[Organization]',
        'org_memberships': 'list[OrgMembership]'
    }

    attribute_map = {
        'created_at': 'created_at',
        'email': 'email',
        'first_name': 'first_name',
        'last_name': 'last_name',
        'roles': 'roles',
        'state': 'state',
        'org': 'org',
        'invite_state': 'invite_state',
        'orgs': 'orgs',
        'org_memberships': 'org_memberships'
    }

    def __init__(self, email, **kwargs):  # noqa: E501
        """User - a model defined in Swagger"""  # noqa: E501

        self._created_at = None
        self._email = None
        self._first_name = None
        self._last_name = None
        self._roles = None
        self._state = None
        self._org = None
        self._invite_state = None
        self._orgs = None
        self._org_memberships = None
        self.discriminator = None

        self.created_at = kwargs.pop('created_at', None)
        self.email = email
        self.first_name = kwargs.pop('first_name', None)
        self.last_name = kwargs.pop('last_name', None)
        self.roles = kwargs.pop('roles', None)
        self.state = kwargs.pop('state', None)
        self.org = kwargs.pop('org', None)
        self.invite_state = kwargs.pop('invite_state', None)
        self.orgs = kwargs.pop('orgs', None)
        self.org_memberships = kwargs.pop('org_memberships', None)

    @property
    def created_at(self):
        """Gets the created_at of this User.  # noqa: E501

        ISO-8601 date  # noqa: E501

        :return: The created_at of this User.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this User.

        ISO-8601 date  # noqa: E501

        :param created_at: The created_at of this User.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def email(self):
        """Gets the email of this User.  # noqa: E501

        user email  # noqa: E501

        :return: The email of this User.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this User.

        user email  # noqa: E501

        :param email: The email of this User.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def first_name(self):
        """Gets the first_name of this User.  # noqa: E501

        user first name  # noqa: E501

        :return: The first_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this User.

        user first name  # noqa: E501

        :param first_name: The first_name of this User.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this User.  # noqa: E501

        user last name  # noqa: E501

        :return: The last_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this User.

        user last name  # noqa: E501

        :param last_name: The last_name of this User.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def roles(self):
        """Gets the roles of this User.  # noqa: E501

        List of roles for a given user  # noqa: E501

        :return: The roles of this User.  # noqa: E501
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this User.

        List of roles for a given user  # noqa: E501

        :param roles: The roles of this User.  # noqa: E501
        :type: list[str]
        """

        self._roles = roles

    @property
    def state(self):
        """Gets the state of this User.  # noqa: E501

        state of user - NEW / ACTIVE  # noqa: E501

        :return: The state of this User.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this User.

        state of user - NEW / ACTIVE  # noqa: E501

        :param state: The state of this User.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def org(self):
        """Gets the org of this User.  # noqa: E501


        :return: The org of this User.  # noqa: E501
        :rtype: str
        """
        return self._org

    @org.setter
    def org(self, org):
        """Sets the org of this User.


        :param org: The org of this User.  # noqa: E501
        :type: str
        """

        self._org = org

    @property
    def invite_state(self):
        """Gets the invite_state of this User.  # noqa: E501


        :return: The invite_state of this User.  # noqa: E501
        :rtype: str
        """
        return self._invite_state

    @invite_state.setter
    def invite_state(self, invite_state):
        """Sets the invite_state of this User.


        :param invite_state: The invite_state of this User.  # noqa: E501
        :type: str
        """

        self._invite_state = invite_state

    @property
    def orgs(self):
        """Gets the orgs of this User.  # noqa: E501


        :return: The orgs of this User.  # noqa: E501
        :rtype: list[Organization]
        """
        return self._orgs

    @orgs.setter
    def orgs(self, orgs):
        """Sets the orgs of this User.


        :param orgs: The orgs of this User.  # noqa: E501
        :type: list[Organization]
        """

        self._orgs = orgs

    @property
    def org_memberships(self):
        """Gets the org_memberships of this User.  # noqa: E501


        :return: The org_memberships of this User.  # noqa: E501
        :rtype: list[OrgMembership]
        """
        return self._org_memberships

    @org_memberships.setter
    def org_memberships(self, org_memberships):
        """Sets the org_memberships of this User.


        :param org_memberships: The org_memberships of this User.  # noqa: E501
        :type: list[OrgMembership]
        """

        self._org_memberships = org_memberships

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
        if issubclass(User, dict):
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
        if not isinstance(other, User):
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
