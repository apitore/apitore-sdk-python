# coding: utf-8

"""
    Sentiment APIs

    Japanese sentiment analyzer.<BR />[Endpoint] https://api.apitore.com/api/11  # noqa: E501

    OpenAPI spec version: 1.0.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.sentiment_entity import SentimentEntity  # noqa: F401,E501


class SentimentResponseEntity(object):
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
        'end_time': 'str',
        'log': 'str',
        'predict': 'SentimentEntity',
        'process_time': 'str',
        'sentiments': 'list[SentimentEntity]',
        'start_time': 'str',
        'text': 'str'
    }

    attribute_map = {
        'end_time': 'endTime',
        'log': 'log',
        'predict': 'predict',
        'process_time': 'processTime',
        'sentiments': 'sentiments',
        'start_time': 'startTime',
        'text': 'text'
    }

    def __init__(self, end_time=None, log=None, predict=None, process_time=None, sentiments=None, start_time=None, text=None):  # noqa: E501
        """SentimentResponseEntity - a model defined in Swagger"""  # noqa: E501

        self._end_time = None
        self._log = None
        self._predict = None
        self._process_time = None
        self._sentiments = None
        self._start_time = None
        self._text = None
        self.discriminator = None

        self.end_time = end_time
        self.log = log
        self.predict = predict
        self.process_time = process_time
        self.sentiments = sentiments
        self.start_time = start_time
        self.text = text

    @property
    def end_time(self):
        """Gets the end_time of this SentimentResponseEntity.  # noqa: E501

        End date  # noqa: E501

        :return: The end_time of this SentimentResponseEntity.  # noqa: E501
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this SentimentResponseEntity.

        End date  # noqa: E501

        :param end_time: The end_time of this SentimentResponseEntity.  # noqa: E501
        :type: str
        """
        if end_time is None:
            raise ValueError("Invalid value for `end_time`, must not be `None`")  # noqa: E501

        self._end_time = end_time

    @property
    def log(self):
        """Gets the log of this SentimentResponseEntity.  # noqa: E501

        Log message  # noqa: E501

        :return: The log of this SentimentResponseEntity.  # noqa: E501
        :rtype: str
        """
        return self._log

    @log.setter
    def log(self, log):
        """Sets the log of this SentimentResponseEntity.

        Log message  # noqa: E501

        :param log: The log of this SentimentResponseEntity.  # noqa: E501
        :type: str
        """
        if log is None:
            raise ValueError("Invalid value for `log`, must not be `None`")  # noqa: E501

        self._log = log

    @property
    def predict(self):
        """Gets the predict of this SentimentResponseEntity.  # noqa: E501

        Output: prediction  # noqa: E501

        :return: The predict of this SentimentResponseEntity.  # noqa: E501
        :rtype: SentimentEntity
        """
        return self._predict

    @predict.setter
    def predict(self, predict):
        """Sets the predict of this SentimentResponseEntity.

        Output: prediction  # noqa: E501

        :param predict: The predict of this SentimentResponseEntity.  # noqa: E501
        :type: SentimentEntity
        """
        if predict is None:
            raise ValueError("Invalid value for `predict`, must not be `None`")  # noqa: E501

        self._predict = predict

    @property
    def process_time(self):
        """Gets the process_time of this SentimentResponseEntity.  # noqa: E501

        Process time [millisecond]  # noqa: E501

        :return: The process_time of this SentimentResponseEntity.  # noqa: E501
        :rtype: str
        """
        return self._process_time

    @process_time.setter
    def process_time(self, process_time):
        """Sets the process_time of this SentimentResponseEntity.

        Process time [millisecond]  # noqa: E501

        :param process_time: The process_time of this SentimentResponseEntity.  # noqa: E501
        :type: str
        """
        if process_time is None:
            raise ValueError("Invalid value for `process_time`, must not be `None`")  # noqa: E501

        self._process_time = process_time

    @property
    def sentiments(self):
        """Gets the sentiments of this SentimentResponseEntity.  # noqa: E501

        Output: sentiments  # noqa: E501

        :return: The sentiments of this SentimentResponseEntity.  # noqa: E501
        :rtype: list[SentimentEntity]
        """
        return self._sentiments

    @sentiments.setter
    def sentiments(self, sentiments):
        """Sets the sentiments of this SentimentResponseEntity.

        Output: sentiments  # noqa: E501

        :param sentiments: The sentiments of this SentimentResponseEntity.  # noqa: E501
        :type: list[SentimentEntity]
        """
        if sentiments is None:
            raise ValueError("Invalid value for `sentiments`, must not be `None`")  # noqa: E501

        self._sentiments = sentiments

    @property
    def start_time(self):
        """Gets the start_time of this SentimentResponseEntity.  # noqa: E501

        Start date  # noqa: E501

        :return: The start_time of this SentimentResponseEntity.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this SentimentResponseEntity.

        Start date  # noqa: E501

        :param start_time: The start_time of this SentimentResponseEntity.  # noqa: E501
        :type: str
        """
        if start_time is None:
            raise ValueError("Invalid value for `start_time`, must not be `None`")  # noqa: E501

        self._start_time = start_time

    @property
    def text(self):
        """Gets the text of this SentimentResponseEntity.  # noqa: E501

        Input: text  # noqa: E501

        :return: The text of this SentimentResponseEntity.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this SentimentResponseEntity.

        Input: text  # noqa: E501

        :param text: The text of this SentimentResponseEntity.  # noqa: E501
        :type: str
        """
        if text is None:
            raise ValueError("Invalid value for `text`, must not be `None`")  # noqa: E501

        self._text = text

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SentimentResponseEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
