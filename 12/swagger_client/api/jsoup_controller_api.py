# coding: utf-8

"""
    Url2Html APIs

    Url to Html.<BR />[Endpoint] https://api.apitore.com/api/12  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class JsoupControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def url2html_using_get(self, access_token, url, **kwargs):  # noqa: E501
        """Extract HTML from URL  # noqa: E501

        Jsoup Web scraper.<BR />Response<BR />&nbsp; Github: <a href=\"https://github.com/keigohtr/apitore-response-parent/tree/master/jsoup-response\">jsoup-response</a><BR />&nbsp; Class: com.apitore.banana.response.org.jsoup.TextResponseEntity<BR />  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.url2html_using_get(access_token, url, async=True)
        >>> result = thread.get()

        :param async bool
        :param str access_token: Access Token (required)
        :param str url: URL (required)
        :return: TextResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.url2html_using_get_with_http_info(access_token, url, **kwargs)  # noqa: E501
        else:
            (data) = self.url2html_using_get_with_http_info(access_token, url, **kwargs)  # noqa: E501
            return data

    def url2html_using_get_with_http_info(self, access_token, url, **kwargs):  # noqa: E501
        """Extract HTML from URL  # noqa: E501

        Jsoup Web scraper.<BR />Response<BR />&nbsp; Github: <a href=\"https://github.com/keigohtr/apitore-response-parent/tree/master/jsoup-response\">jsoup-response</a><BR />&nbsp; Class: com.apitore.banana.response.org.jsoup.TextResponseEntity<BR />  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.url2html_using_get_with_http_info(access_token, url, async=True)
        >>> result = thread.get()

        :param async bool
        :param str access_token: Access Token (required)
        :param str url: URL (required)
        :return: TextResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['access_token', 'url']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method url2html_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params or
                params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `url2html_using_get`")  # noqa: E501
        # verify the required parameter 'url' is set
        if ('url' not in params or
                params['url'] is None):
            raise ValueError("Missing the required parameter `url` when calling `url2html_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'access_token' in params:
            query_params.append(('access_token', params['access_token']))  # noqa: E501
        if 'url' in params:
            query_params.append(('url', params['url']))  # noqa: E501

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
            '/jsoup/url2html', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TextResponseEntity',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
