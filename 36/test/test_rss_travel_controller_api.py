# coding: utf-8

"""
    Travel feeds APIs

    Various travel feeds.<BR />[Endpoint] https://api.apitore.com/api/36  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.rss_travel_controller_api import RssTravelControllerApi  # noqa: E501
from swagger_client.rest import ApiException


class TestRssTravelControllerApi(unittest.TestCase):
    """RssTravelControllerApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.rss_travel_controller_api.RssTravelControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_feed_using_get8(self):
        """Test case for feed_using_get8

        Get travel feeds  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
