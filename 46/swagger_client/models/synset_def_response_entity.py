# coding: utf-8

"""
    WordNet APIs

    You can access ALL WordNet DB.<BR />[Endpoint] https://api.apitore.com/api/46  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SynsetDefResponseEntity(object):
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
        '_def': 'str',
        'end_time': 'str',
        'lang': 'str',
        'log': 'str',
        'process_time': 'str',
        'sid': 'int',
        'start_time': 'str',
        'synset': 'str'
    }

    attribute_map = {
        '_def': 'def',
        'end_time': 'endTime',
        'lang': 'lang',
        'log': 'log',
        'process_time': 'processTime',
        'sid': 'sid',
        'start_time': 'startTime',
        'synset': 'synset'
    }

    def __init__(self, _def=None, end_time=None, lang=None, log=None, process_time=None, sid=None, start_time=None, synset=None):  # noqa: E501
        """SynsetDefResponseEntity - a model defined in Swagger"""  # noqa: E501

        self.__def = None
        self._end_time = None
        self._lang = None
        self._log = None
        self._process_time = None
        self._sid = None
        self._start_time = None
        self._synset = None
        self.discriminator = None

        self._def = _def
        self.end_time = end_time
        self.lang = lang
        self.log = log
        self.process_time = process_time
        self.sid = sid
        self.start_time = start_time
        self.synset = synset

    @property
    def _def(self):
        """Gets the _def of this SynsetDefResponseEntity.  # noqa: E501

        Definition  # noqa: E501

        :return: The _def of this SynsetDefResponseEntity.  # noqa: E501
        :rtype: str
        """
        return self.__def

    @_def.setter
    def _def(self, _def):
        """Sets the _def of this SynsetDefResponseEntity.

        Definition  # noqa: E501

        :param _def: The _def of this SynsetDefResponseEntity.  # noqa: E501
        :type: str
        """
        if _def is None:
            raise ValueError("Invalid value for `_def`, must not be `None`")  # noqa: E501

        self.__def = _def

    @property
    def end_time(self):
        """Gets the end_time of this SynsetDefResponseEntity.  # noqa: E501

        End date  # noqa: E501

        :return: The end_time of this SynsetDefResponseEntity.  # noqa: E501
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this SynsetDefResponseEntity.

        End date  # noqa: E501

        :param end_time: The end_time of this SynsetDefResponseEntity.  # noqa: E501
        :type: str
        """
        if end_time is None:
            raise ValueError("Invalid value for `end_time`, must not be `None`")  # noqa: E501

        self._end_time = end_time

    @property
    def lang(self):
        """Gets the lang of this SynsetDefResponseEntity.  # noqa: E501

        Language  # noqa: E501

        :return: The lang of this SynsetDefResponseEntity.  # noqa: E501
        :rtype: str
        """
        return self._lang

    @lang.setter
    def lang(self, lang):
        """Sets the lang of this SynsetDefResponseEntity.

        Language  # noqa: E501

        :param lang: The lang of this SynsetDefResponseEntity.  # noqa: E501
        :type: str
        """
        if lang is None:
            raise ValueError("Invalid value for `lang`, must not be `None`")  # noqa: E501

        self._lang = lang

    @property
    def log(self):
        """Gets the log of this SynsetDefResponseEntity.  # noqa: E501

        Log message  # noqa: E501

        :return: The log of this SynsetDefResponseEntity.  # noqa: E501
        :rtype: str
        """
        return self._log

    @log.setter
    def log(self, log):
        """Sets the log of this SynsetDefResponseEntity.

        Log message  # noqa: E501

        :param log: The log of this SynsetDefResponseEntity.  # noqa: E501
        :type: str
        """
        if log is None:
            raise ValueError("Invalid value for `log`, must not be `None`")  # noqa: E501

        self._log = log

    @property
    def process_time(self):
        """Gets the process_time of this SynsetDefResponseEntity.  # noqa: E501

        Process time [millisecond]  # noqa: E501

        :return: The process_time of this SynsetDefResponseEntity.  # noqa: E501
        :rtype: str
        """
        return self._process_time

    @process_time.setter
    def process_time(self, process_time):
        """Sets the process_time of this SynsetDefResponseEntity.

        Process time [millisecond]  # noqa: E501

        :param process_time: The process_time of this SynsetDefResponseEntity.  # noqa: E501
        :type: str
        """
        if process_time is None:
            raise ValueError("Invalid value for `process_time`, must not be `None`")  # noqa: E501

        self._process_time = process_time

    @property
    def sid(self):
        """Gets the sid of this SynsetDefResponseEntity.  # noqa: E501

        sid  # noqa: E501

        :return: The sid of this SynsetDefResponseEntity.  # noqa: E501
        :rtype: int
        """
        return self._sid

    @sid.setter
    def sid(self, sid):
        """Sets the sid of this SynsetDefResponseEntity.

        sid  # noqa: E501

        :param sid: The sid of this SynsetDefResponseEntity.  # noqa: E501
        :type: int
        """
        if sid is None:
            raise ValueError("Invalid value for `sid`, must not be `None`")  # noqa: E501

        self._sid = sid

    @property
    def start_time(self):
        """Gets the start_time of this SynsetDefResponseEntity.  # noqa: E501

        Start date  # noqa: E501

        :return: The start_time of this SynsetDefResponseEntity.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this SynsetDefResponseEntity.

        Start date  # noqa: E501

        :param start_time: The start_time of this SynsetDefResponseEntity.  # noqa: E501
        :type: str
        """
        if start_time is None:
            raise ValueError("Invalid value for `start_time`, must not be `None`")  # noqa: E501

        self._start_time = start_time

    @property
    def synset(self):
        """Gets the synset of this SynsetDefResponseEntity.  # noqa: E501

        Synset  # noqa: E501

        :return: The synset of this SynsetDefResponseEntity.  # noqa: E501
        :rtype: str
        """
        return self._synset

    @synset.setter
    def synset(self, synset):
        """Sets the synset of this SynsetDefResponseEntity.

        Synset  # noqa: E501

        :param synset: The synset of this SynsetDefResponseEntity.  # noqa: E501
        :type: str
        """
        if synset is None:
            raise ValueError("Invalid value for `synset`, must not be `None`")  # noqa: E501

        self._synset = synset

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
        if not isinstance(other, SynsetDefResponseEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
