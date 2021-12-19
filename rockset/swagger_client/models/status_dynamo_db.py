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


class StatusDynamoDb(object):
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
        'scan_start_time': 'str',
        'scan_end_time': 'str',
        'scan_records_processed': 'int',
        'scan_total_records': 'int',
        'state': 'str',
        'stream_last_processed_at': 'str'
    }

    attribute_map = {
        'scan_start_time': 'scan_start_time',
        'scan_end_time': 'scan_end_time',
        'scan_records_processed': 'scan_records_processed',
        'scan_total_records': 'scan_total_records',
        'state': 'state',
        'stream_last_processed_at': 'stream_last_processed_at'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """StatusDynamoDb - a model defined in Swagger"""  # noqa: E501

        self._scan_start_time = None
        self._scan_end_time = None
        self._scan_records_processed = None
        self._scan_total_records = None
        self._state = None
        self._stream_last_processed_at = None
        self.discriminator = None

        self.scan_start_time = kwargs.pop('scan_start_time', None)
        self.scan_end_time = kwargs.pop('scan_end_time', None)
        self.scan_records_processed = kwargs.pop('scan_records_processed', None)
        self.scan_total_records = kwargs.pop('scan_total_records', None)
        self.state = kwargs.pop('state', None)
        self.stream_last_processed_at = kwargs.pop('stream_last_processed_at', None)

    @property
    def scan_start_time(self):
        """Gets the scan_start_time of this StatusDynamoDb.  # noqa: E501

        DynamoDB scan start time  # noqa: E501

        :return: The scan_start_time of this StatusDynamoDb.  # noqa: E501
        :rtype: str
        """
        return self._scan_start_time

    @scan_start_time.setter
    def scan_start_time(self, scan_start_time):
        """Sets the scan_start_time of this StatusDynamoDb.

        DynamoDB scan start time  # noqa: E501

        :param scan_start_time: The scan_start_time of this StatusDynamoDb.  # noqa: E501
        :type: str
        """

        self._scan_start_time = scan_start_time

    @property
    def scan_end_time(self):
        """Gets the scan_end_time of this StatusDynamoDb.  # noqa: E501

        DynamoDb scan end time  # noqa: E501

        :return: The scan_end_time of this StatusDynamoDb.  # noqa: E501
        :rtype: str
        """
        return self._scan_end_time

    @scan_end_time.setter
    def scan_end_time(self, scan_end_time):
        """Sets the scan_end_time of this StatusDynamoDb.

        DynamoDb scan end time  # noqa: E501

        :param scan_end_time: The scan_end_time of this StatusDynamoDb.  # noqa: E501
        :type: str
        """

        self._scan_end_time = scan_end_time

    @property
    def scan_records_processed(self):
        """Gets the scan_records_processed of this StatusDynamoDb.  # noqa: E501

        Number of records inserted using scan  # noqa: E501

        :return: The scan_records_processed of this StatusDynamoDb.  # noqa: E501
        :rtype: int
        """
        return self._scan_records_processed

    @scan_records_processed.setter
    def scan_records_processed(self, scan_records_processed):
        """Sets the scan_records_processed of this StatusDynamoDb.

        Number of records inserted using scan  # noqa: E501

        :param scan_records_processed: The scan_records_processed of this StatusDynamoDb.  # noqa: E501
        :type: int
        """

        self._scan_records_processed = scan_records_processed

    @property
    def scan_total_records(self):
        """Gets the scan_total_records of this StatusDynamoDb.  # noqa: E501

        Number of records in DynamoDB table at time of scan  # noqa: E501

        :return: The scan_total_records of this StatusDynamoDb.  # noqa: E501
        :rtype: int
        """
        return self._scan_total_records

    @scan_total_records.setter
    def scan_total_records(self, scan_total_records):
        """Sets the scan_total_records of this StatusDynamoDb.

        Number of records in DynamoDB table at time of scan  # noqa: E501

        :param scan_total_records: The scan_total_records of this StatusDynamoDb.  # noqa: E501
        :type: int
        """

        self._scan_total_records = scan_total_records

    @property
    def state(self):
        """Gets the state of this StatusDynamoDb.  # noqa: E501

        state of current ingest for this table  # noqa: E501

        :return: The state of this StatusDynamoDb.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this StatusDynamoDb.

        state of current ingest for this table  # noqa: E501

        :param state: The state of this StatusDynamoDb.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def stream_last_processed_at(self):
        """Gets the stream_last_processed_at of this StatusDynamoDb.  # noqa: E501

        ISO-8601 date when source was last processed  # noqa: E501

        :return: The stream_last_processed_at of this StatusDynamoDb.  # noqa: E501
        :rtype: str
        """
        return self._stream_last_processed_at

    @stream_last_processed_at.setter
    def stream_last_processed_at(self, stream_last_processed_at):
        """Sets the stream_last_processed_at of this StatusDynamoDb.

        ISO-8601 date when source was last processed  # noqa: E501

        :param stream_last_processed_at: The stream_last_processed_at of this StatusDynamoDb.  # noqa: E501
        :type: str
        """

        self._stream_last_processed_at = stream_last_processed_at

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
        if issubclass(StatusDynamoDb, dict):
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
        if not isinstance(other, StatusDynamoDb):
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