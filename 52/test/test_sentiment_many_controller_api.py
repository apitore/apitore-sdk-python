# coding: utf-8

"""
    Sentiment APIs

    Japanese sentiment analyzer.<BR />[Endpoint] https://api.apitore.com/api/52  # noqa: E501

    OpenAPI spec version: 1.0.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.sentiment_many_controller_api import SentimentManyControllerApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSentimentManyControllerApi(unittest.TestCase):
    """SentimentManyControllerApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.sentiment_many_controller_api.SentimentManyControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_predict_using_post(self):
        """Test case for predict_using_post

        Sentiment predict  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
