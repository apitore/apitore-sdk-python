# coding: utf-8

"""
    Url2Html APIs

    Url to Html.<BR />[Endpoint] https://api.apitore.com/api/12  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.jsoup_controller_api import JsoupControllerApi  # noqa: E501
from swagger_client.rest import ApiException


class TestJsoupControllerApi(unittest.TestCase):
    """JsoupControllerApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.jsoup_controller_api.JsoupControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_url2html_using_get(self):
        """Test case for url2html_using_get

        Extract HTML from URL  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
