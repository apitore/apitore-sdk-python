# coding: utf-8

"""
    Game feeds APIs

    Various game feeds.<BR />[Endpoint] https://api.apitore.com/api/33  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.feed_entry_entity import FeedEntryEntity  # noqa: F401,E501


class FeedResponseEntity(object):
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
        'entries': 'list[FeedEntryEntity]',
        'last_updated_at': 'int',
        'log': 'str',
        'num': 'int',
        'page': 'int',
        'process_time': 'str',
        'start_time': 'str'
    }

    attribute_map = {
        'end_time': 'endTime',
        'entries': 'entries',
        'last_updated_at': 'lastUpdatedAt',
        'log': 'log',
        'num': 'num',
        'page': 'page',
        'process_time': 'processTime',
        'start_time': 'startTime'
    }

    def __init__(self, end_time=None, entries=None, last_updated_at=None, log=None, num=None, page=None, process_time=None, start_time=None):  # noqa: E501
        """FeedResponseEntity - a model defined in Swagger"""  # noqa: E501

        self._end_time = None
        self._entries = None
        self._last_updated_at = None
        self._log = None
        self._num = None
        self._page = None
        self._process_time = None
        self._start_time = None
        self.discriminator = None

        self.end_time = end_time
        self.entries = entries
        self.last_updated_at = last_updated_at
        self.log = log
        self.num = num
        self.page = page
        self.process_time = process_time
        self.start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this FeedResponseEntity.  # noqa: E501

        End date  # noqa: E501

        :return: The end_time of this FeedResponseEntity.  # noqa: E501
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this FeedResponseEntity.

        End date  # noqa: E501

        :param end_time: The end_time of this FeedResponseEntity.  # noqa: E501
        :type: str
        """
        if end_time is None:
            raise ValueError("Invalid value for `end_time`, must not be `None`")  # noqa: E501

        self._end_time = end_time

    @property
    def entries(self):
        """Gets the entries of this FeedResponseEntity.  # noqa: E501

        Entries  # noqa: E501

        :return: The entries of this FeedResponseEntity.  # noqa: E501
        :rtype: list[FeedEntryEntity]
        """
        return self._entries

    @entries.setter
    def entries(self, entries):
        """Sets the entries of this FeedResponseEntity.

        Entries  # noqa: E501

        :param entries: The entries of this FeedResponseEntity.  # noqa: E501
        :type: list[FeedEntryEntity]
        """
        if entries is None:
            raise ValueError("Invalid value for `entries`, must not be `None`")  # noqa: E501

        self._entries = entries

    @property
    def last_updated_at(self):
        """Gets the last_updated_at of this FeedResponseEntity.  # noqa: E501

        Last Updated At  # noqa: E501

        :return: The last_updated_at of this FeedResponseEntity.  # noqa: E501
        :rtype: int
        """
        return self._last_updated_at

    @last_updated_at.setter
    def last_updated_at(self, last_updated_at):
        """Sets the last_updated_at of this FeedResponseEntity.

        Last Updated At  # noqa: E501

        :param last_updated_at: The last_updated_at of this FeedResponseEntity.  # noqa: E501
        :type: int
        """
        if last_updated_at is None:
            raise ValueError("Invalid value for `last_updated_at`, must not be `None`")  # noqa: E501

        self._last_updated_at = last_updated_at

    @property
    def log(self):
        """Gets the log of this FeedResponseEntity.  # noqa: E501

        Log message  # noqa: E501

        :return: The log of this FeedResponseEntity.  # noqa: E501
        :rtype: str
        """
        return self._log

    @log.setter
    def log(self, log):
        """Sets the log of this FeedResponseEntity.

        Log message  # noqa: E501

        :param log: The log of this FeedResponseEntity.  # noqa: E501
        :type: str
        """
        if log is None:
            raise ValueError("Invalid value for `log`, must not be `None`")  # noqa: E501

        self._log = log

    @property
    def num(self):
        """Gets the num of this FeedResponseEntity.  # noqa: E501

        Num  # noqa: E501

        :return: The num of this FeedResponseEntity.  # noqa: E501
        :rtype: int
        """
        return self._num

    @num.setter
    def num(self, num):
        """Sets the num of this FeedResponseEntity.

        Num  # noqa: E501

        :param num: The num of this FeedResponseEntity.  # noqa: E501
        :type: int
        """
        if num is None:
            raise ValueError("Invalid value for `num`, must not be `None`")  # noqa: E501

        self._num = num

    @property
    def page(self):
        """Gets the page of this FeedResponseEntity.  # noqa: E501

        Input page num  # noqa: E501

        :return: The page of this FeedResponseEntity.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this FeedResponseEntity.

        Input page num  # noqa: E501

        :param page: The page of this FeedResponseEntity.  # noqa: E501
        :type: int
        """
        if page is None:
            raise ValueError("Invalid value for `page`, must not be `None`")  # noqa: E501

        self._page = page

    @property
    def process_time(self):
        """Gets the process_time of this FeedResponseEntity.  # noqa: E501

        Process time [millisecond]  # noqa: E501

        :return: The process_time of this FeedResponseEntity.  # noqa: E501
        :rtype: str
        """
        return self._process_time

    @process_time.setter
    def process_time(self, process_time):
        """Sets the process_time of this FeedResponseEntity.

        Process time [millisecond]  # noqa: E501

        :param process_time: The process_time of this FeedResponseEntity.  # noqa: E501
        :type: str
        """
        if process_time is None:
            raise ValueError("Invalid value for `process_time`, must not be `None`")  # noqa: E501

        self._process_time = process_time

    @property
    def start_time(self):
        """Gets the start_time of this FeedResponseEntity.  # noqa: E501

        Start date  # noqa: E501

        :return: The start_time of this FeedResponseEntity.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this FeedResponseEntity.

        Start date  # noqa: E501

        :param start_time: The start_time of this FeedResponseEntity.  # noqa: E501
        :type: str
        """
        if start_time is None:
            raise ValueError("Invalid value for `start_time`, must not be `None`")  # noqa: E501

        self._start_time = start_time

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
        if not isinstance(other, FeedResponseEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
