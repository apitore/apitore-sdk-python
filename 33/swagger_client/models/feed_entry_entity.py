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


class FeedEntryEntity(object):
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
        'link': 'str',
        'pub_date': 'int',
        'source_link': 'str',
        'source_title': 'str',
        'title': 'str'
    }

    attribute_map = {
        'author': 'author',
        'description': 'description',
        'link': 'link',
        'pub_date': 'pubDate',
        'source_link': 'sourceLink',
        'source_title': 'sourceTitle',
        'title': 'title'
    }

    def __init__(self, author=None, description=None, link=None, pub_date=None, source_link=None, source_title=None, title=None):  # noqa: E501
        """FeedEntryEntity - a model defined in Swagger"""  # noqa: E501

        self._author = None
        self._description = None
        self._link = None
        self._pub_date = None
        self._source_link = None
        self._source_title = None
        self._title = None
        self.discriminator = None

        if author is not None:
            self.author = author
        if description is not None:
            self.description = description
        self.link = link
        self.pub_date = pub_date
        self.source_link = source_link
        self.source_title = source_title
        self.title = title

    @property
    def author(self):
        """Gets the author of this FeedEntryEntity.  # noqa: E501

        Author  # noqa: E501

        :return: The author of this FeedEntryEntity.  # noqa: E501
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this FeedEntryEntity.

        Author  # noqa: E501

        :param author: The author of this FeedEntryEntity.  # noqa: E501
        :type: str
        """

        self._author = author

    @property
    def description(self):
        """Gets the description of this FeedEntryEntity.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this FeedEntryEntity.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FeedEntryEntity.

        Description  # noqa: E501

        :param description: The description of this FeedEntryEntity.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def link(self):
        """Gets the link of this FeedEntryEntity.  # noqa: E501

        Link  # noqa: E501

        :return: The link of this FeedEntryEntity.  # noqa: E501
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this FeedEntryEntity.

        Link  # noqa: E501

        :param link: The link of this FeedEntryEntity.  # noqa: E501
        :type: str
        """
        if link is None:
            raise ValueError("Invalid value for `link`, must not be `None`")  # noqa: E501

        self._link = link

    @property
    def pub_date(self):
        """Gets the pub_date of this FeedEntryEntity.  # noqa: E501

        Published Date  # noqa: E501

        :return: The pub_date of this FeedEntryEntity.  # noqa: E501
        :rtype: int
        """
        return self._pub_date

    @pub_date.setter
    def pub_date(self, pub_date):
        """Sets the pub_date of this FeedEntryEntity.

        Published Date  # noqa: E501

        :param pub_date: The pub_date of this FeedEntryEntity.  # noqa: E501
        :type: int
        """
        if pub_date is None:
            raise ValueError("Invalid value for `pub_date`, must not be `None`")  # noqa: E501

        self._pub_date = pub_date

    @property
    def source_link(self):
        """Gets the source_link of this FeedEntryEntity.  # noqa: E501

        Source Link  # noqa: E501

        :return: The source_link of this FeedEntryEntity.  # noqa: E501
        :rtype: str
        """
        return self._source_link

    @source_link.setter
    def source_link(self, source_link):
        """Sets the source_link of this FeedEntryEntity.

        Source Link  # noqa: E501

        :param source_link: The source_link of this FeedEntryEntity.  # noqa: E501
        :type: str
        """
        if source_link is None:
            raise ValueError("Invalid value for `source_link`, must not be `None`")  # noqa: E501

        self._source_link = source_link

    @property
    def source_title(self):
        """Gets the source_title of this FeedEntryEntity.  # noqa: E501

        Source Title  # noqa: E501

        :return: The source_title of this FeedEntryEntity.  # noqa: E501
        :rtype: str
        """
        return self._source_title

    @source_title.setter
    def source_title(self, source_title):
        """Sets the source_title of this FeedEntryEntity.

        Source Title  # noqa: E501

        :param source_title: The source_title of this FeedEntryEntity.  # noqa: E501
        :type: str
        """
        if source_title is None:
            raise ValueError("Invalid value for `source_title`, must not be `None`")  # noqa: E501

        self._source_title = source_title

    @property
    def title(self):
        """Gets the title of this FeedEntryEntity.  # noqa: E501

        Title  # noqa: E501

        :return: The title of this FeedEntryEntity.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this FeedEntryEntity.

        Title  # noqa: E501

        :param title: The title of this FeedEntryEntity.  # noqa: E501
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
        if not isinstance(other, FeedEntryEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
