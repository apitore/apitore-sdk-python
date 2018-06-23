# coding: utf-8

# flake8: noqa

"""
    Twitter APIs with Word2Vec query expansion, and add sentiment by Apitore sentiment API

    Call Twitter APIs with word2vec query expansion and sentiment analysis.<BR />[Endpoint] https://api.apitore.com/api/26  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import apis into sdk package
from swagger_client.api.twitter_word_2_vec_with_sentiment_controller_api import TwitterWord2VecWithSentimentControllerApi

# import ApiClient
from swagger_client.api_client import ApiClient
from swagger_client.configuration import Configuration
# import models into sdk package
from swagger_client.models.tweet_entity import TweetEntity
from swagger_client.models.twitter_response_entity import TwitterResponseEntity
