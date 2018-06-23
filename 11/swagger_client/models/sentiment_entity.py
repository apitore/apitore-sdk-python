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


class SentimentEntity(object):
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
        'score': 'float',
        'sentiment': 'str'
    }

    attribute_map = {
        'score': 'score',
        'sentiment': 'sentiment'
    }

    def __init__(self, score=None, sentiment=None):  # noqa: E501
        """SentimentEntity - a model defined in Swagger"""  # noqa: E501

        self._score = None
        self._sentiment = None
        self.discriminator = None

        self.score = score
        self.sentiment = sentiment

    @property
    def score(self):
        """Gets the score of this SentimentEntity.  # noqa: E501

        cosine distance  # noqa: E501

        :return: The score of this SentimentEntity.  # noqa: E501
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this SentimentEntity.

        cosine distance  # noqa: E501

        :param score: The score of this SentimentEntity.  # noqa: E501
        :type: float
        """
        if score is None:
            raise ValueError("Invalid value for `score`, must not be `None`")  # noqa: E501

        self._score = score

    @property
    def sentiment(self):
        """Gets the sentiment of this SentimentEntity.  # noqa: E501

        sentiment  # noqa: E501

        :return: The sentiment of this SentimentEntity.  # noqa: E501
        :rtype: str
        """
        return self._sentiment

    @sentiment.setter
    def sentiment(self, sentiment):
        """Sets the sentiment of this SentimentEntity.

        sentiment  # noqa: E501

        :param sentiment: The sentiment of this SentimentEntity.  # noqa: E501
        :type: str
        """
        if sentiment is None:
            raise ValueError("Invalid value for `sentiment`, must not be `None`")  # noqa: E501

        self._sentiment = sentiment

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
        if not isinstance(other, SentimentEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
