# coding: utf-8

"""
    Url2Label by tfidf APIs

    Url to label by tfidf of contents.<BR />[Endpoint] https://api.apitore.com/api/20  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.url_2_label_by_tfidf_controller_api import Url2LabelByTfidfControllerApi  # noqa: E501
from swagger_client.rest import ApiException


class TestUrl2LabelByTfidfControllerApi(unittest.TestCase):
    """Url2LabelByTfidfControllerApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.url_2_label_by_tfidf_controller_api.Url2LabelByTfidfControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_using_get3(self):
        """Test case for get_using_get3

        Get labels from URL  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
