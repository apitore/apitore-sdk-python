# coding: utf-8

"""
    WordNet hypernym APIs

    Return hypernym words.<BR />[Endpoint] https://api.apitore.com/api/42  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class WordnetSimplePartsControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def simple_hypernym_using_get(self, access_token, word, **kwargs):  # noqa: E501
        """Simple WordNet WebAPI. Return hypernym words.  # noqa: E501

        Japanese WordNet.<BR />Response<BR />&nbsp; Github: <a href=\"https://github.com/keigohtr/apitore-response-parent/tree/master/wordnet-response\">wordnet-response</a><BR />&nbsp; Class: com.apitore.banana.response.de.sciss.ws4j.LinksResponseEntity<BR />  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.simple_hypernym_using_get(access_token, word, async=True)
        >>> result = thread.get()

        :param async bool
        :param str access_token: Access Token (required)
        :param str word: Word (required)
        :param str pos: Part-of-speech. You can specify several pos by csv format. [n:noun,v:verb,a:adjective,r:adverb]
        :return: LinksResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.simple_hypernym_using_get_with_http_info(access_token, word, **kwargs)  # noqa: E501
        else:
            (data) = self.simple_hypernym_using_get_with_http_info(access_token, word, **kwargs)  # noqa: E501
            return data

    def simple_hypernym_using_get_with_http_info(self, access_token, word, **kwargs):  # noqa: E501
        """Simple WordNet WebAPI. Return hypernym words.  # noqa: E501

        Japanese WordNet.<BR />Response<BR />&nbsp; Github: <a href=\"https://github.com/keigohtr/apitore-response-parent/tree/master/wordnet-response\">wordnet-response</a><BR />&nbsp; Class: com.apitore.banana.response.de.sciss.ws4j.LinksResponseEntity<BR />  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.simple_hypernym_using_get_with_http_info(access_token, word, async=True)
        >>> result = thread.get()

        :param async bool
        :param str access_token: Access Token (required)
        :param str word: Word (required)
        :param str pos: Part-of-speech. You can specify several pos by csv format. [n:noun,v:verb,a:adjective,r:adverb]
        :return: LinksResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['access_token', 'word', 'pos']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method simple_hypernym_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params or
                params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `simple_hypernym_using_get`")  # noqa: E501
        # verify the required parameter 'word' is set
        if ('word' not in params or
                params['word'] is None):
            raise ValueError("Missing the required parameter `word` when calling `simple_hypernym_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'access_token' in params:
            query_params.append(('access_token', params['access_token']))  # noqa: E501
        if 'word' in params:
            query_params.append(('word', params['word']))  # noqa: E501
        if 'pos' in params:
            query_params.append(('pos', params['pos']))  # noqa: E501

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
            '/wordnet-simple/hypernym', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LinksResponseEntity',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
