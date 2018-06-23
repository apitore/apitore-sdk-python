# swagger_client.JsoupControllerApi

All URIs are relative to *https://api.apitore.com/api/12*

Method | HTTP request | Description
------------- | ------------- | -------------
[**url2html_using_get**](JsoupControllerApi.md#url2html_using_get) | **GET** /jsoup/url2html | Extract HTML from URL


# **url2html_using_get**
> TextResponseEntity url2html_using_get(access_token, url)

Extract HTML from URL

Jsoup Web scraper.<BR />Response<BR />&nbsp; Github: <a href=\"https://github.com/keigohtr/apitore-response-parent/tree/master/jsoup-response\">jsoup-response</a><BR />&nbsp; Class: com.apitore.banana.response.org.jsoup.TextResponseEntity<BR />

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JsoupControllerApi()
access_token = 'access_token_example' # str | Access Token
url = 'url_example' # str | URL

try:
    # Extract HTML from URL
    api_response = api_instance.url2html_using_get(access_token, url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JsoupControllerApi->url2html_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Access Token | 
 **url** | **str**| URL | 

### Return type

[**TextResponseEntity**](TextResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

