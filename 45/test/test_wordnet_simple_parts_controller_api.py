# coding: utf-8

"""
    WordNet translation APIs

    Return translation words.<BR />[Endpoint] https://api.apitore.com/api/45  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.wordnet_simple_parts_controller_api import WordnetSimplePartsControllerApi  # noqa: E501
from swagger_client.rest import ApiException


class TestWordnetSimplePartsControllerApi(unittest.TestCase):
    """WordnetSimplePartsControllerApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.wordnet_simple_parts_controller_api.WordnetSimplePartsControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_simple_translation_using_get(self):
        """Test case for simple_translation_using_get

        Simple WordNet WebAPI. Return translation words.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
