# coding: utf-8

"""
    Sentence Similarity

    Sentence Similarity.<BR />[Endpoint] https://api.apitore.com/api/53  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.sentence_similarity_controller_api import SentenceSimilarityControllerApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSentenceSimilarityControllerApi(unittest.TestCase):
    """SentenceSimilarityControllerApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.sentence_similarity_controller_api.SentenceSimilarityControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_eval_using_post(self):
        """Test case for eval_using_post

        Text similarity using word2vec  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
