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


class SenseEntity(object):
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
        'freq': 'int',
        'lang': 'str',
        'lexid': 'int',
        'rank': 'int',
        'src': 'str',
        'synset': 'str',
        'wordid': 'int'
    }

    attribute_map = {
        'freq': 'freq',
        'lang': 'lang',
        'lexid': 'lexid',
        'rank': 'rank',
        'src': 'src',
        'synset': 'synset',
        'wordid': 'wordid'
    }

    def __init__(self, freq=None, lang=None, lexid=None, rank=None, src=None, synset=None, wordid=None):  # noqa: E501
        """SenseEntity - a model defined in Swagger"""  # noqa: E501

        self._freq = None
        self._lang = None
        self._lexid = None
        self._rank = None
        self._src = None
        self._synset = None
        self._wordid = None
        self.discriminator = None

        self.freq = freq
        self.lang = lang
        self.lexid = lexid
        self.rank = rank
        self.src = src
        self.synset = synset
        self.wordid = wordid

    @property
    def freq(self):
        """Gets the freq of this SenseEntity.  # noqa: E501

        Freq  # noqa: E501

        :return: The freq of this SenseEntity.  # noqa: E501
        :rtype: int
        """
        return self._freq

    @freq.setter
    def freq(self, freq):
        """Sets the freq of this SenseEntity.

        Freq  # noqa: E501

        :param freq: The freq of this SenseEntity.  # noqa: E501
        :type: int
        """
        if freq is None:
            raise ValueError("Invalid value for `freq`, must not be `None`")  # noqa: E501

        self._freq = freq

    @property
    def lang(self):
        """Gets the lang of this SenseEntity.  # noqa: E501

        Language  # noqa: E501

        :return: The lang of this SenseEntity.  # noqa: E501
        :rtype: str
        """
        return self._lang

    @lang.setter
    def lang(self, lang):
        """Sets the lang of this SenseEntity.

        Language  # noqa: E501

        :param lang: The lang of this SenseEntity.  # noqa: E501
        :type: str
        """
        if lang is None:
            raise ValueError("Invalid value for `lang`, must not be `None`")  # noqa: E501

        self._lang = lang

    @property
    def lexid(self):
        """Gets the lexid of this SenseEntity.  # noqa: E501

        Lexicon ID  # noqa: E501

        :return: The lexid of this SenseEntity.  # noqa: E501
        :rtype: int
        """
        return self._lexid

    @lexid.setter
    def lexid(self, lexid):
        """Sets the lexid of this SenseEntity.

        Lexicon ID  # noqa: E501

        :param lexid: The lexid of this SenseEntity.  # noqa: E501
        :type: int
        """
        if lexid is None:
            raise ValueError("Invalid value for `lexid`, must not be `None`")  # noqa: E501

        self._lexid = lexid

    @property
    def rank(self):
        """Gets the rank of this SenseEntity.  # noqa: E501

        Rank  # noqa: E501

        :return: The rank of this SenseEntity.  # noqa: E501
        :rtype: int
        """
        return self._rank

    @rank.setter
    def rank(self, rank):
        """Sets the rank of this SenseEntity.

        Rank  # noqa: E501

        :param rank: The rank of this SenseEntity.  # noqa: E501
        :type: int
        """
        if rank is None:
            raise ValueError("Invalid value for `rank`, must not be `None`")  # noqa: E501

        self._rank = rank

    @property
    def src(self):
        """Gets the src of this SenseEntity.  # noqa: E501

        Src  # noqa: E501

        :return: The src of this SenseEntity.  # noqa: E501
        :rtype: str
        """
        return self._src

    @src.setter
    def src(self, src):
        """Sets the src of this SenseEntity.

        Src  # noqa: E501

        :param src: The src of this SenseEntity.  # noqa: E501
        :type: str
        """
        if src is None:
            raise ValueError("Invalid value for `src`, must not be `None`")  # noqa: E501

        self._src = src

    @property
    def synset(self):
        """Gets the synset of this SenseEntity.  # noqa: E501

        Synset  # noqa: E501

        :return: The synset of this SenseEntity.  # noqa: E501
        :rtype: str
        """
        return self._synset

    @synset.setter
    def synset(self, synset):
        """Sets the synset of this SenseEntity.

        Synset  # noqa: E501

        :param synset: The synset of this SenseEntity.  # noqa: E501
        :type: str
        """
        if synset is None:
            raise ValueError("Invalid value for `synset`, must not be `None`")  # noqa: E501

        self._synset = synset

    @property
    def wordid(self):
        """Gets the wordid of this SenseEntity.  # noqa: E501

        Word ID  # noqa: E501

        :return: The wordid of this SenseEntity.  # noqa: E501
        :rtype: int
        """
        return self._wordid

    @wordid.setter
    def wordid(self, wordid):
        """Sets the wordid of this SenseEntity.

        Word ID  # noqa: E501

        :param wordid: The wordid of this SenseEntity.  # noqa: E501
        :type: int
        """
        if wordid is None:
            raise ValueError("Invalid value for `wordid`, must not be `None`")  # noqa: E501

        self._wordid = wordid

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
        if not isinstance(other, SenseEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
