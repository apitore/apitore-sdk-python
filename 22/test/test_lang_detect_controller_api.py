# coding: utf-8

"""
    Language Detection APIs

    Language detection.<BR />[Endpoint] https://api.apitore.com/api/22  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.lang_detect_controller_api import LangDetectControllerApi  # noqa: E501
from swagger_client.rest import ApiException


class TestLangDetectControllerApi(unittest.TestCase):
    """LangDetectControllerApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.lang_detect_controller_api.LangDetectControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_using_get(self):
        """Test case for get_using_get

        Language Detection. This supports 53 languages.  # noqa: E501
        """
        pass

    def test_sm_get_using_get(self):
        """Test case for sm_get_using_get

        Language Detection for Short Messages. This supports 53 languages.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
