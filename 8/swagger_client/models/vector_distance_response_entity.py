# coding: utf-8

"""
    Word2Vec APIs

    Word2Vec.<BR />[Endpoint] https://api.apitore.com/api/8  # noqa: E501

    OpenAPI spec version: 1.0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.distance_entity import DistanceEntity  # noqa: F401,E501


class VectorDistanceResponseEntity(object):
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
        'distances': 'list[DistanceEntity]',
        'end_time': 'str',
        'input': 'list[float]',
        'log': 'str',
        'num': 'str',
        'process_time': 'str',
        'start_time': 'str'
    }

    attribute_map = {
        'distances': 'distances',
        'end_time': 'endTime',
        'input': 'input',
        'log': 'log',
        'num': 'num',
        'process_time': 'processTime',
        'start_time': 'startTime'
    }

    def __init__(self, distances=None, end_time=None, input=None, log=None, num=None, process_time=None, start_time=None):  # noqa: E501
        """VectorDistanceResponseEntity - a model defined in Swagger"""  # noqa: E501

        self._distances = None
        self._end_time = None
        self._input = None
        self._log = None
        self._num = None
        self._process_time = None
        self._start_time = None
        self.discriminator = None

        if distances is not None:
            self.distances = distances
        self.end_time = end_time
        self.input = input
        self.log = log
        self.num = num
        self.process_time = process_time
        self.start_time = start_time

    @property
    def distances(self):
        """Gets the distances of this VectorDistanceResponseEntity.  # noqa: E501

        Distances  # noqa: E501

        :return: The distances of this VectorDistanceResponseEntity.  # noqa: E501
        :rtype: list[DistanceEntity]
        """
        return self._distances

    @distances.setter
    def distances(self, distances):
        """Sets the distances of this VectorDistanceResponseEntity.

        Distances  # noqa: E501

        :param distances: The distances of this VectorDistanceResponseEntity.  # noqa: E501
        :type: list[DistanceEntity]
        """

        self._distances = distances

    @property
    def end_time(self):
        """Gets the end_time of this VectorDistanceResponseEntity.  # noqa: E501

        End date  # noqa: E501

        :return: The end_time of this VectorDistanceResponseEntity.  # noqa: E501
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this VectorDistanceResponseEntity.

        End date  # noqa: E501

        :param end_time: The end_time of this VectorDistanceResponseEntity.  # noqa: E501
        :type: str
        """
        if end_time is None:
            raise ValueError("Invalid value for `end_time`, must not be `None`")  # noqa: E501

        self._end_time = end_time

    @property
    def input(self):
        """Gets the input of this VectorDistanceResponseEntity.  # noqa: E501

        Input vector  # noqa: E501

        :return: The input of this VectorDistanceResponseEntity.  # noqa: E501
        :rtype: list[float]
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this VectorDistanceResponseEntity.

        Input vector  # noqa: E501

        :param input: The input of this VectorDistanceResponseEntity.  # noqa: E501
        :type: list[float]
        """
        if input is None:
            raise ValueError("Invalid value for `input`, must not be `None`")  # noqa: E501

        self._input = input

    @property
    def log(self):
        """Gets the log of this VectorDistanceResponseEntity.  # noqa: E501

        Log message  # noqa: E501

        :return: The log of this VectorDistanceResponseEntity.  # noqa: E501
        :rtype: str
        """
        return self._log

    @log.setter
    def log(self, log):
        """Sets the log of this VectorDistanceResponseEntity.

        Log message  # noqa: E501

        :param log: The log of this VectorDistanceResponseEntity.  # noqa: E501
        :type: str
        """
        if log is None:
            raise ValueError("Invalid value for `log`, must not be `None`")  # noqa: E501

        self._log = log

    @property
    def num(self):
        """Gets the num of this VectorDistanceResponseEntity.  # noqa: E501

        Input num  # noqa: E501

        :return: The num of this VectorDistanceResponseEntity.  # noqa: E501
        :rtype: str
        """
        return self._num

    @num.setter
    def num(self, num):
        """Sets the num of this VectorDistanceResponseEntity.

        Input num  # noqa: E501

        :param num: The num of this VectorDistanceResponseEntity.  # noqa: E501
        :type: str
        """
        if num is None:
            raise ValueError("Invalid value for `num`, must not be `None`")  # noqa: E501

        self._num = num

    @property
    def process_time(self):
        """Gets the process_time of this VectorDistanceResponseEntity.  # noqa: E501

        Process time [millisecond]  # noqa: E501

        :return: The process_time of this VectorDistanceResponseEntity.  # noqa: E501
        :rtype: str
        """
        return self._process_time

    @process_time.setter
    def process_time(self, process_time):
        """Sets the process_time of this VectorDistanceResponseEntity.

        Process time [millisecond]  # noqa: E501

        :param process_time: The process_time of this VectorDistanceResponseEntity.  # noqa: E501
        :type: str
        """
        if process_time is None:
            raise ValueError("Invalid value for `process_time`, must not be `None`")  # noqa: E501

        self._process_time = process_time

    @property
    def start_time(self):
        """Gets the start_time of this VectorDistanceResponseEntity.  # noqa: E501

        Start date  # noqa: E501

        :return: The start_time of this VectorDistanceResponseEntity.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this VectorDistanceResponseEntity.

        Start date  # noqa: E501

        :param start_time: The start_time of this VectorDistanceResponseEntity.  # noqa: E501
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
        if not isinstance(other, VectorDistanceResponseEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
