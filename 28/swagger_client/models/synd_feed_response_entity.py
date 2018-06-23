# coding: utf-8

"""
    RSS2JSON APIs

    Rss to Json.<BR />[Endpoint] https://api.apitore.com/api/28  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.synd_entry_entity import SyndEntryEntity  # noqa: F401,E501


class SyndFeedResponseEntity(object):
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
        'author': 'str',
        'description': 'str',
        'end_time': 'str',
        'entries': 'list[SyndEntryEntity]',
        'link': 'str',
        'log': 'str',
        'num': 'int',
        'process_time': 'str',
        'pub_date': 'int',
        'rss': 'str',
        'start_time': 'str',
        'title': 'str'
    }

    attribute_map = {
        'author': 'author',
        'description': 'description',
        'end_time': 'endTime',
        'entries': 'entries',
        'link': 'link',
        'log': 'log',
        'num': 'num',
        'process_time': 'processTime',
        'pub_date': 'pubDate',
        'rss': 'rss',
        'start_time': 'startTime',
        'title': 'title'
    }

    def __init__(self, author=None, description=None, end_time=None, entries=None, link=None, log=None, num=None, process_time=None, pub_date=None, rss=None, start_time=None, title=None):  # noqa: E501
        """SyndFeedResponseEntity - a model defined in Swagger"""  # noqa: E501

        self._author = None
        self._description = None
        self._end_time = None
        self._entries = None
        self._link = None
        self._log = None
        self._num = None
        self._process_time = None
        self._pub_date = None
        self._rss = None
        self._start_time = None
        self._title = None
        self.discriminator = None

        if author is not None:
            self.author = author
        if description is not None:
            self.description = description
        self.end_time = end_time
        self.entries = entries
        self.link = link
        self.log = log
        self.num = num
        self.process_time = process_time
        self.pub_date = pub_date
        self.rss = rss
        self.start_time = start_time
        self.title = title

    @property
    def author(self):
        """Gets the author of this SyndFeedResponseEntity.  # noqa: E501

        Author  # noqa: E501

        :return: The author of this SyndFeedResponseEntity.  # noqa: E501
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this SyndFeedResponseEntity.

        Author  # noqa: E501

        :param author: The author of this SyndFeedResponseEntity.  # noqa: E501
        :type: str
        """

        self._author = author

    @property
    def description(self):
        """Gets the description of this SyndFeedResponseEntity.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this SyndFeedResponseEntity.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SyndFeedResponseEntity.

        Description  # noqa: E501

        :param description: The description of this SyndFeedResponseEntity.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def end_time(self):
        """Gets the end_time of this SyndFeedResponseEntity.  # noqa: E501

        End date  # noqa: E501

        :return: The end_time of this SyndFeedResponseEntity.  # noqa: E501
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this SyndFeedResponseEntity.

        End date  # noqa: E501

        :param end_time: The end_time of this SyndFeedResponseEntity.  # noqa: E501
        :type: str
        """
        if end_time is None:
            raise ValueError("Invalid value for `end_time`, must not be `None`")  # noqa: E501

        self._end_time = end_time

    @property
    def entries(self):
        """Gets the entries of this SyndFeedResponseEntity.  # noqa: E501

        Entries  # noqa: E501

        :return: The entries of this SyndFeedResponseEntity.  # noqa: E501
        :rtype: list[SyndEntryEntity]
        """
        return self._entries

    @entries.setter
    def entries(self, entries):
        """Sets the entries of this SyndFeedResponseEntity.

        Entries  # noqa: E501

        :param entries: The entries of this SyndFeedResponseEntity.  # noqa: E501
        :type: list[SyndEntryEntity]
        """
        if entries is None:
            raise ValueError("Invalid value for `entries`, must not be `None`")  # noqa: E501

        self._entries = entries

    @property
    def link(self):
        """Gets the link of this SyndFeedResponseEntity.  # noqa: E501

        Link  # noqa: E501

        :return: The link of this SyndFeedResponseEntity.  # noqa: E501
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this SyndFeedResponseEntity.

        Link  # noqa: E501

        :param link: The link of this SyndFeedResponseEntity.  # noqa: E501
        :type: str
        """
        if link is None:
            raise ValueError("Invalid value for `link`, must not be `None`")  # noqa: E501

        self._link = link

    @property
    def log(self):
        """Gets the log of this SyndFeedResponseEntity.  # noqa: E501

        Log message  # noqa: E501

        :return: The log of this SyndFeedResponseEntity.  # noqa: E501
        :rtype: str
        """
        return self._log

    @log.setter
    def log(self, log):
        """Sets the log of this SyndFeedResponseEntity.

        Log message  # noqa: E501

        :param log: The log of this SyndFeedResponseEntity.  # noqa: E501
        :type: str
        """
        if log is None:
            raise ValueError("Invalid value for `log`, must not be `None`")  # noqa: E501

        self._log = log

    @property
    def num(self):
        """Gets the num of this SyndFeedResponseEntity.  # noqa: E501

        Num  # noqa: E501

        :return: The num of this SyndFeedResponseEntity.  # noqa: E501
        :rtype: int
        """
        return self._num

    @num.setter
    def num(self, num):
        """Sets the num of this SyndFeedResponseEntity.

        Num  # noqa: E501

        :param num: The num of this SyndFeedResponseEntity.  # noqa: E501
        :type: int
        """
        if num is None:
            raise ValueError("Invalid value for `num`, must not be `None`")  # noqa: E501

        self._num = num

    @property
    def process_time(self):
        """Gets the process_time of this SyndFeedResponseEntity.  # noqa: E501

        Process time [millisecond]  # noqa: E501

        :return: The process_time of this SyndFeedResponseEntity.  # noqa: E501
        :rtype: str
        """
        return self._process_time

    @process_time.setter
    def process_time(self, process_time):
        """Sets the process_time of this SyndFeedResponseEntity.

        Process time [millisecond]  # noqa: E501

        :param process_time: The process_time of this SyndFeedResponseEntity.  # noqa: E501
        :type: str
        """
        if process_time is None:
            raise ValueError("Invalid value for `process_time`, must not be `None`")  # noqa: E501

        self._process_time = process_time

    @property
    def pub_date(self):
        """Gets the pub_date of this SyndFeedResponseEntity.  # noqa: E501

        Published Date  # noqa: E501

        :return: The pub_date of this SyndFeedResponseEntity.  # noqa: E501
        :rtype: int
        """
        return self._pub_date

    @pub_date.setter
    def pub_date(self, pub_date):
        """Sets the pub_date of this SyndFeedResponseEntity.

        Published Date  # noqa: E501

        :param pub_date: The pub_date of this SyndFeedResponseEntity.  # noqa: E501
        :type: int
        """
        if pub_date is None:
            raise ValueError("Invalid value for `pub_date`, must not be `None`")  # noqa: E501

        self._pub_date = pub_date

    @property
    def rss(self):
        """Gets the rss of this SyndFeedResponseEntity.  # noqa: E501

        Input RSS  # noqa: E501

        :return: The rss of this SyndFeedResponseEntity.  # noqa: E501
        :rtype: str
        """
        return self._rss

    @rss.setter
    def rss(self, rss):
        """Sets the rss of this SyndFeedResponseEntity.

        Input RSS  # noqa: E501

        :param rss: The rss of this SyndFeedResponseEntity.  # noqa: E501
        :type: str
        """
        if rss is None:
            raise ValueError("Invalid value for `rss`, must not be `None`")  # noqa: E501

        self._rss = rss

    @property
    def start_time(self):
        """Gets the start_time of this SyndFeedResponseEntity.  # noqa: E501

        Start date  # noqa: E501

        :return: The start_time of this SyndFeedResponseEntity.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this SyndFeedResponseEntity.

        Start date  # noqa: E501

        :param start_time: The start_time of this SyndFeedResponseEntity.  # noqa: E501
        :type: str
        """
        if start_time is None:
            raise ValueError("Invalid value for `start_time`, must not be `None`")  # noqa: E501

        self._start_time = start_time

    @property
    def title(self):
        """Gets the title of this SyndFeedResponseEntity.  # noqa: E501

        Title  # noqa: E501

        :return: The title of this SyndFeedResponseEntity.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this SyndFeedResponseEntity.

        Title  # noqa: E501

        :param title: The title of this SyndFeedResponseEntity.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

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
        if not isinstance(other, SyndFeedResponseEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other