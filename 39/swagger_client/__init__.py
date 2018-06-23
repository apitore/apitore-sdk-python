# coding: utf-8

# flake8: noqa

"""
    Sentiment APIs

    Japanese sentiment analyzer. (tokenized by SentencePiece)<BR />[Endpoint] https://api.apitore.com/api/39  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import apis into sdk package
from swagger_client.api.sentiment_v_2_controller_api import SentimentV2ControllerApi

# import ApiClient
from swagger_client.api_client import ApiClient
from swagger_client.configuration import Configuration
# import models into sdk package
from swagger_client.models.sentiment_entity import SentimentEntity
from swagger_client.models.sentiment_response_entity import SentimentResponseEntity