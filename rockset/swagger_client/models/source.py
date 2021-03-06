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

from rockset.swagger_client.models.format_params import FormatParams  # noqa: F401,E501
from rockset.swagger_client.models.source_dynamo_db import SourceDynamoDb  # noqa: F401,E501
from rockset.swagger_client.models.source_file_upload import SourceFileUpload  # noqa: F401,E501
from rockset.swagger_client.models.source_gcs import SourceGcs  # noqa: F401,E501
from rockset.swagger_client.models.source_kafka import SourceKafka  # noqa: F401,E501
from rockset.swagger_client.models.source_kinesis import SourceKinesis  # noqa: F401,E501
from rockset.swagger_client.models.source_mongo_db import SourceMongoDb  # noqa: F401,E501
from rockset.swagger_client.models.source_redshift import SourceRedshift  # noqa: F401,E501
from rockset.swagger_client.models.source_s3 import SourceS3  # noqa: F401,E501
from rockset.swagger_client.models.status import Status  # noqa: F401,E501


class Source(object):
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
        'integration_name': 'str',
        's3': 'SourceS3',
        'kinesis': 'SourceKinesis',
        'gcs': 'SourceGcs',
        'redshift': 'SourceRedshift',
        'dynamodb': 'SourceDynamoDb',
        'file_upload': 'SourceFileUpload',
        'kafka': 'SourceKafka',
        'mongodb': 'SourceMongoDb',
        'status': 'Status',
        'format_params': 'FormatParams'
    }

    attribute_map = {
        'integration_name': 'integration_name',
        's3': 's3',
        'kinesis': 'kinesis',
        'gcs': 'gcs',
        'redshift': 'redshift',
        'dynamodb': 'dynamodb',
        'file_upload': 'file_upload',
        'kafka': 'kafka',
        'mongodb': 'mongodb',
        'status': 'status',
        'format_params': 'format_params'
    }

    def __init__(self, integration_name, **kwargs):  # noqa: E501
        """Source - a model defined in Swagger"""  # noqa: E501

        self._integration_name = None
        self._s3 = None
        self._kinesis = None
        self._gcs = None
        self._redshift = None
        self._dynamodb = None
        self._file_upload = None
        self._kafka = None
        self._mongodb = None
        self._status = None
        self._format_params = None
        self.discriminator = None

        self.integration_name = integration_name
        self.s3 = kwargs.pop('s3', None)
        self.kinesis = kwargs.pop('kinesis', None)
        self.gcs = kwargs.pop('gcs', None)
        self.redshift = kwargs.pop('redshift', None)
        self.dynamodb = kwargs.pop('dynamodb', None)
        self.file_upload = kwargs.pop('file_upload', None)
        self.kafka = kwargs.pop('kafka', None)
        self.mongodb = kwargs.pop('mongodb', None)
        self.status = kwargs.pop('status', None)
        self.format_params = kwargs.pop('format_params', None)

    @property
    def integration_name(self):
        """Gets the integration_name of this Source.  # noqa: E501

        name of integration to use  # noqa: E501

        :return: The integration_name of this Source.  # noqa: E501
        :rtype: str
        """
        return self._integration_name

    @integration_name.setter
    def integration_name(self, integration_name):
        """Sets the integration_name of this Source.

        name of integration to use  # noqa: E501

        :param integration_name: The integration_name of this Source.  # noqa: E501
        :type: str
        """

        self._integration_name = integration_name

    @property
    def s3(self):
        """Gets the s3 of this Source.  # noqa: E501

        configuration for ingestion from S3  # noqa: E501

        :return: The s3 of this Source.  # noqa: E501
        :rtype: SourceS3
        """
        return self._s3

    @s3.setter
    def s3(self, s3):
        """Sets the s3 of this Source.

        configuration for ingestion from S3  # noqa: E501

        :param s3: The s3 of this Source.  # noqa: E501
        :type: SourceS3
        """

        self._s3 = s3

    @property
    def kinesis(self):
        """Gets the kinesis of this Source.  # noqa: E501

        configuration for ingestion from kinesis stream  # noqa: E501

        :return: The kinesis of this Source.  # noqa: E501
        :rtype: SourceKinesis
        """
        return self._kinesis

    @kinesis.setter
    def kinesis(self, kinesis):
        """Sets the kinesis of this Source.

        configuration for ingestion from kinesis stream  # noqa: E501

        :param kinesis: The kinesis of this Source.  # noqa: E501
        :type: SourceKinesis
        """

        self._kinesis = kinesis

    @property
    def gcs(self):
        """Gets the gcs of this Source.  # noqa: E501

        configuration for ingestion from GCS  # noqa: E501

        :return: The gcs of this Source.  # noqa: E501
        :rtype: SourceGcs
        """
        return self._gcs

    @gcs.setter
    def gcs(self, gcs):
        """Sets the gcs of this Source.

        configuration for ingestion from GCS  # noqa: E501

        :param gcs: The gcs of this Source.  # noqa: E501
        :type: SourceGcs
        """

        self._gcs = gcs

    @property
    def redshift(self):
        """Gets the redshift of this Source.  # noqa: E501

        configuration for ingestion from Redshift  # noqa: E501

        :return: The redshift of this Source.  # noqa: E501
        :rtype: SourceRedshift
        """
        return self._redshift

    @redshift.setter
    def redshift(self, redshift):
        """Sets the redshift of this Source.

        configuration for ingestion from Redshift  # noqa: E501

        :param redshift: The redshift of this Source.  # noqa: E501
        :type: SourceRedshift
        """

        self._redshift = redshift

    @property
    def dynamodb(self):
        """Gets the dynamodb of this Source.  # noqa: E501

        configuration for ingestion from  a dynamodb table  # noqa: E501

        :return: The dynamodb of this Source.  # noqa: E501
        :rtype: SourceDynamoDb
        """
        return self._dynamodb

    @dynamodb.setter
    def dynamodb(self, dynamodb):
        """Sets the dynamodb of this Source.

        configuration for ingestion from  a dynamodb table  # noqa: E501

        :param dynamodb: The dynamodb of this Source.  # noqa: E501
        :type: SourceDynamoDb
        """

        self._dynamodb = dynamodb

    @property
    def file_upload(self):
        """Gets the file_upload of this Source.  # noqa: E501

        file upload details  # noqa: E501

        :return: The file_upload of this Source.  # noqa: E501
        :rtype: SourceFileUpload
        """
        return self._file_upload

    @file_upload.setter
    def file_upload(self, file_upload):
        """Sets the file_upload of this Source.

        file upload details  # noqa: E501

        :param file_upload: The file_upload of this Source.  # noqa: E501
        :type: SourceFileUpload
        """

        self._file_upload = file_upload

    @property
    def kafka(self):
        """Gets the kafka of this Source.  # noqa: E501

        kafka collection identifier  # noqa: E501

        :return: The kafka of this Source.  # noqa: E501
        :rtype: SourceKafka
        """
        return self._kafka

    @kafka.setter
    def kafka(self, kafka):
        """Sets the kafka of this Source.

        kafka collection identifier  # noqa: E501

        :param kafka: The kafka of this Source.  # noqa: E501
        :type: SourceKafka
        """

        self._kafka = kafka

    @property
    def mongodb(self):
        """Gets the mongodb of this Source.  # noqa: E501

        MongoDB collection details  # noqa: E501

        :return: The mongodb of this Source.  # noqa: E501
        :rtype: SourceMongoDb
        """
        return self._mongodb

    @mongodb.setter
    def mongodb(self, mongodb):
        """Sets the mongodb of this Source.

        MongoDB collection details  # noqa: E501

        :param mongodb: The mongodb of this Source.  # noqa: E501
        :type: SourceMongoDb
        """

        self._mongodb = mongodb

    @property
    def status(self):
        """Gets the status of this Source.  # noqa: E501

        the ingest status of this source  # noqa: E501

        :return: The status of this Source.  # noqa: E501
        :rtype: Status
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Source.

        the ingest status of this source  # noqa: E501

        :param status: The status of this Source.  # noqa: E501
        :type: Status
        """

        self._status = status

    @property
    def format_params(self):
        """Gets the format_params of this Source.  # noqa: E501

        format parameters for data from this source  # noqa: E501

        :return: The format_params of this Source.  # noqa: E501
        :rtype: FormatParams
        """
        return self._format_params

    @format_params.setter
    def format_params(self, format_params):
        """Sets the format_params of this Source.

        format parameters for data from this source  # noqa: E501

        :param format_params: The format_params of this Source.  # noqa: E501
        :type: FormatParams
        """

        self._format_params = format_params

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
        if issubclass(Source, dict):
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
        if not isinstance(other, Source):
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
