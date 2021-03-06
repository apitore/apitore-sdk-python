# coding: utf-8

"""
    Japanese WordNet APIs

    Return all WordNet words.<BR />[Endpoint] https://api.apitore.com/api/40  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.link_words_entity import LinkWordsEntity  # noqa: F401,E501


class LinksResponseEntity(object):
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
        'entries': 'list[LinkWordsEntity]',
        'log': 'str',
        'process_time': 'str',
        'start_time': 'str',
        'word': 'str'
    }

    attribute_map = {
        'end_time': 'endTime',
        'entries': 'entries',
        'log': 'log',
        'process_time': 'processTime',
        'start_time': 'startTime',
        'word': 'word'
    }

    def __init__(self, end_time=None, entries=None, log=None, process_time=None, start_time=None, word=None):  # noqa: E501
        """LinksResponseEntity - a model defined in Swagger"""  # noqa: E501

        self._end_time = None
        self._entries = None
        self._log = None
        self._process_time = None
        self._start_time = None
        self._word = None
        self.discriminator = None

        self.end_time = end_time
        self.entries = entries
        self.log = log
        self.process_time = process_time
        self.start_time = start_time
        self.word = word

    @property
    def end_time(self):
        """Gets the end_time of this LinksResponseEntity.  # noqa: E501

        End date  # noqa: E501

        :return: The end_time of this LinksResponseEntity.  # noqa: E501
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this LinksResponseEntity.

        End date  # noqa: E501

        :param end_time: The end_time of this LinksResponseEntity.  # noqa: E501
        :type: str
        """
        if end_time is None:
            raise ValueError("Invalid value for `end_time`, must not be `None`")  # noqa: E501

        self._end_time = end_time

    @property
    def entries(self):
        """Gets the entries of this LinksResponseEntity.  # noqa: E501

        Entries  # noqa: E501

        :return: The entries of this LinksResponseEntity.  # noqa: E501
        :rtype: list[LinkWordsEntity]
        """
        return self._entries

    @entries.setter
    def entries(self, entries):
        """Sets the entries of this LinksResponseEntity.

        Entries  # noqa: E501

        :param entries: The entries of this LinksResponseEntity.  # noqa: E501
        :type: list[LinkWordsEntity]
        """
        if entries is None:
            raise ValueError("Invalid value for `entries`, must not be `None`")  # noqa: E501

        self._entries = entries

    @property
    def log(self):
        """Gets the log of this LinksResponseEntity.  # noqa: E501

        Log message  # noqa: E501

        :return: The log of this LinksResponseEntity.  # noqa: E501
        :rtype: str
        """
        return self._log

    @log.setter
    def log(self, log):
        """Sets the log of this LinksResponseEntity.

        Log message  # noqa: E501

        :param log: The log of this LinksResponseEntity.  # noqa: E501
        :type: str
        """
        if log is None:
            raise ValueError("Invalid value for `log`, must not be `None`")  # noqa: E501

        self._log = log

    @property
    def process_time(self):
        """Gets the process_time of this LinksResponseEntity.  # noqa: E501

        Process time [millisecond]  # noqa: E501

        :return: The process_time of this LinksResponseEntity.  # noqa: E501
        :rtype: str
        """
        return self._process_time

    @process_time.setter
    def process_time(self, process_time):
        """Sets the process_time of this LinksResponseEntity.

        Process time [millisecond]  # noqa: E501

        :param process_time: The process_time of this LinksResponseEntity.  # noqa: E501
        :type: str
        """
        if process_time is None:
            raise ValueError("Invalid value for `process_time`, must not be `None`")  # noqa: E501

        self._process_time = process_time

    @property
    def start_time(self):
        """Gets the start_time of this LinksResponseEntity.  # noqa: E501

        Start date  # noqa: E501

        :return: The start_time of this LinksResponseEntity.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this LinksResponseEntity.

        Start date  # noqa: E501

        :param start_time: The start_time of this LinksResponseEntity.  # noqa: E501
        :type: str
        """
        if start_time is None:
            raise ValueError("Invalid value for `start_time`, must not be `None`")  # noqa: E501

        self._start_time = start_time

    @property
    def word(self):
        """Gets the word of this LinksResponseEntity.  # noqa: E501

        Input word  # noqa: E501

        :return: The word of this LinksResponseEntity.  # noqa: E501
        :rtype: str
        """
        return self._word

    @word.setter
    def word(self, word):
        """Sets the word of this LinksResponseEntity.

        Input word  # noqa: E501

        :param word: The word of this LinksResponseEntity.  # noqa: E501
        :type: str
        """
        if word is None:
            raise ValueError("Invalid value for `word`, must not be `None`")  # noqa: E501

        self._word = word

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
        if not isinstance(other, LinksResponseEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
