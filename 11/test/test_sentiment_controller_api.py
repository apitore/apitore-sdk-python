# coding: utf-8

"""
    Sentiment APIs

    Japanese sentiment analyzer.<BR />[Endpoint] https://api.apitore.com/api/11  # noqa: E501

    OpenAPI spec version: 1.0.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.sentiment_controller_api import SentimentControllerApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSentimentControllerApi(unittest.TestCase):
    """SentimentControllerApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.sentiment_controller_api.SentimentControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_predict_using_get(self):
        """Test case for predict_using_get

        Sentiment predict  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()