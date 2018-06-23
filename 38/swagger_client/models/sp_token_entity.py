# coding: utf-8

"""
    SentencePiece APIs (tweet)

    SentencePiece tokenizer (tweet).<BR />[Endpoint] https://api.apitore.com/api/38  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SPTokenEntity(object):
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
        'token': 'str',
        'wid': 'int'
    }

    attribute_map = {
        'token': 'token',
        'wid': 'wid'
    }

    def __init__(self, token=None, wid=None):  # noqa: E501
        """SPTokenEntity - a model defined in Swagger"""  # noqa: E501

        self._token = None
        self._wid = None
        self.discriminator = None

        self.token = token
        self.wid = wid

    @property
    def token(self):
        """Gets the token of this SPTokenEntity.  # noqa: E501

        Token  # noqa: E501

        :return: The token of this SPTokenEntity.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this SPTokenEntity.

        Token  # noqa: E501

        :param token: The token of this SPTokenEntity.  # noqa: E501
        :type: str
        """
        if token is None:
            raise ValueError("Invalid value for `token`, must not be `None`")  # noqa: E501

        self._token = token

    @property
    def wid(self):
        """Gets the wid of this SPTokenEntity.  # noqa: E501

        Word ID  # noqa: E501

        :return: The wid of this SPTokenEntity.  # noqa: E501
        :rtype: int
        """
        return self._wid

    @wid.setter
    def wid(self, wid):
        """Sets the wid of this SPTokenEntity.

        Word ID  # noqa: E501

        :param wid: The wid of this SPTokenEntity.  # noqa: E501
        :type: int
        """
        if wid is None:
            raise ValueError("Invalid value for `wid`, must not be `None`")  # noqa: E501

        self._wid = wid

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
        if not isinstance(other, SPTokenEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other