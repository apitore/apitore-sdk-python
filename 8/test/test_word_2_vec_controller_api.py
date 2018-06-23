# coding: utf-8

"""
    Word2Vec APIs

    Word2Vec.<BR />[Endpoint] https://api.apitore.com/api/8  # noqa: E501

    OpenAPI spec version: 1.0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.word_2_vec_controller_api import Word2VecControllerApi  # noqa: E501
from swagger_client.rest import ApiException


class TestWord2VecControllerApi(unittest.TestCase):
    """Word2VecControllerApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.word_2_vec_controller_api.Word2VecControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_analogy_using_get(self):
        """Test case for analogy_using_get

        Word2Vec analogy  # noqa: E501
        """
        pass

    def test_distance_using_get1(self):
        """Test case for distance_using_get1

        Word2Vec distance  # noqa: E501
        """
        pass

    def test_similarity_using_get(self):
        """Test case for similarity_using_get

        Word2Vec similarity  # noqa: E501
        """
        pass

    def test_vec_distance_using_get(self):
        """Test case for vec_distance_using_get

        Word2Vec distance (Vector version)  # noqa: E501
        """
        pass

    def test_wordvector_using_get1(self):
        """Test case for wordvector_using_get1

        Word2Vec wordvector  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
