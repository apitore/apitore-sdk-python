# coding: utf-8

"""
    SentencePiece APIs (wikipedia)

    SentencePiece tokenizer (wikipedia).<BR />[Endpoint] https://api.apitore.com/api/37  # noqa: E501

    OpenAPI spec version: 0.0.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.sentence_piece_controller_api import SentencePieceControllerApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSentencePieceControllerApi(unittest.TestCase):
    """SentencePieceControllerApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.sentence_piece_controller_api.SentencePieceControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_using_get2(self):
        """Test case for get_using_get2

        SentencePiece (unigram)  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()