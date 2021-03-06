# coding: utf-8

# flake8: noqa

"""
    Word2Vec APIs

    Word2Vec.<BR />[Endpoint] https://api.apitore.com/api/8  # noqa: E501

    OpenAPI spec version: 1.0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import apis into sdk package
from swagger_client.api.word_2_vec_controller_api import Word2VecControllerApi

# import ApiClient
from swagger_client.api_client import ApiClient
from swagger_client.configuration import Configuration
# import models into sdk package
from swagger_client.models.analogy_response_entity import AnalogyResponseEntity
from swagger_client.models.distance_entity import DistanceEntity
from swagger_client.models.distance_response_entity import DistanceResponseEntity
from swagger_client.models.similarity_response_entity import SimilarityResponseEntity
from swagger_client.models.vector_distance_response_entity import VectorDistanceResponseEntity
from swagger_client.models.word_vector_response_entity import WordVectorResponseEntity
