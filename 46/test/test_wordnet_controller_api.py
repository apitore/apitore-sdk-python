# coding: utf-8

"""
    WordNet APIs

    You can access ALL WordNet DB.<BR />[Endpoint] https://api.apitore.com/api/46  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.wordnet_controller_api import WordnetControllerApi  # noqa: E501
from swagger_client.rest import ApiException


class TestWordnetControllerApi(unittest.TestCase):
    """WordnetControllerApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.wordnet_controller_api.WordnetControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_sensebysynset_using_get(self):
        """Test case for sensebysynset_using_get

        WordNet WebAPI. Return Sense object.  # noqa: E501
        """
        pass

    def test_sensebywordid_using_get(self):
        """Test case for sensebywordid_using_get

        WordNet WebAPI. Return Sense object.  # noqa: E501
        """
        pass

    def test_synlinkby_synset_using_get(self):
        """Test case for synlinkby_synset_using_get

        WordNet WebAPI. Return SynLink object.  # noqa: E501
        """
        pass

    def test_synsetby_name_using_get(self):
        """Test case for synsetby_name_using_get

        WordNet WebAPI. Return Synset object.  # noqa: E501
        """
        pass

    def test_synsetbysynset_using_get(self):
        """Test case for synsetbysynset_using_get

        WordNet WebAPI. Return Synset object.  # noqa: E501
        """
        pass

    def test_synsetdefbysynset_using_get(self):
        """Test case for synsetdefbysynset_using_get

        WordNet WebAPI. Return SynsetDef object.  # noqa: E501
        """
        pass

    def test_wordbyid_using_get(self):
        """Test case for wordbyid_using_get

        WordNet WebAPI. Return Word object.  # noqa: E501
        """
        pass

    def test_wordbylemma_using_get(self):
        """Test case for wordbylemma_using_get

        WordNet WebAPI. Return Word object.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()