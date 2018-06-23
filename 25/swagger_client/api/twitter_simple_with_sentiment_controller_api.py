# coding: utf-8

"""
    Twitter APIs with sentiment by Apitore sentiment API

    Call Twitter APIs with sentiment by Apitore sentiment API.<BR />[Endpoint] https://api.apitore.com/api/25  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class TwitterSimpleWithSentimentControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def search_using_get1(self, access_token, q, **kwargs):  # noqa: E501
        """Search tweets.  # noqa: E501

        Tweets search API with sentiment by Apitore sentiment API.<BR />Response<BR />&nbsp; Github: <a href=\"https://github.com/keigohtr/apitore-response-parent/tree/master/twitter-response\">twitter-response</a><BR />&nbsp; Class: com.apitore.banana.response.twitter.TwitterResponseEntity<BR />  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.search_using_get1(access_token, q, async=True)
        >>> result = thread.get()

        :param async bool
        :param str access_token: Access Token (required)
        :param str q: Search query (required)
        :param int since_id: Get after this id.
        :param int max_id: Get before this id.
        :return: TwitterResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.search_using_get1_with_http_info(access_token, q, **kwargs)  # noqa: E501
        else:
            (data) = self.search_using_get1_with_http_info(access_token, q, **kwargs)  # noqa: E501
            return data

    def search_using_get1_with_http_info(self, access_token, q, **kwargs):  # noqa: E501
        """Search tweets.  # noqa: E501

        Tweets search API with sentiment by Apitore sentiment API.<BR />Response<BR />&nbsp; Github: <a href=\"https://github.com/keigohtr/apitore-response-parent/tree/master/twitter-response\">twitter-response</a><BR />&nbsp; Class: com.apitore.banana.response.twitter.TwitterResponseEntity<BR />  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.search_using_get1_with_http_info(access_token, q, async=True)
        >>> result = thread.get()

        :param async bool
        :param str access_token: Access Token (required)
        :param str q: Search query (required)
        :param int since_id: Get after this id.
        :param int max_id: Get before this id.
        :return: TwitterResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['access_token', 'q', 'since_id', 'max_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_using_get1" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params or
                params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `search_using_get1`")  # noqa: E501
        # verify the required parameter 'q' is set
        if ('q' not in params or
                params['q'] is None):
            raise ValueError("Missing the required parameter `q` when calling `search_using_get1`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'access_token' in params:
            query_params.append(('access_token', params['access_token']))  # noqa: E501
        if 'q' in params:
            query_params.append(('q', params['q']))  # noqa: E501
        if 'since_id' in params:
            query_params.append(('sinceId', params['since_id']))  # noqa: E501
        if 'max_id' in params:
            query_params.append(('maxId', params['max_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/twitter-sentiment/search', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TwitterResponseEntity',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
