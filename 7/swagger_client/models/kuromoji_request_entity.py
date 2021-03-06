# coding: utf-8

"""
    Kuromoji APIs

    Kuromoji: japanese morphological analyzer.<BR />[Endpoint] https://api.apitore.com/api/7  # noqa: E501

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class KuromojiRequestEntity(object):
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
        'texts': 'list[str]'
    }

    attribute_map = {
        'texts': 'texts'
    }

    def __init__(self, texts=None):  # noqa: E501
        """KuromojiRequestEntity - a model defined in Swagger"""  # noqa: E501

        self._texts = None
        self.discriminator = None

        self.texts = texts

    @property
    def texts(self):
        """Gets the texts of this KuromojiRequestEntity.  # noqa: E501

        texts [max 1MB]  # noqa: E501

        :return: The texts of this KuromojiRequestEntity.  # noqa: E501
        :rtype: list[str]
        """
        return self._texts

    @texts.setter
    def texts(self, texts):
        """Sets the texts of this KuromojiRequestEntity.

        texts [max 1MB]  # noqa: E501

        :param texts: The texts of this KuromojiRequestEntity.  # noqa: E501
        :type: list[str]
        """
        if texts is None:
            raise ValueError("Invalid value for `texts`, must not be `None`")  # noqa: E501

        self._texts = texts

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
        if not isinstance(other, KuromojiRequestEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
