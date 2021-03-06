# swagger_client.Url2LabelByTfidfControllerApi

All URIs are relative to *https://api.apitore.com/api/20*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_using_get3**](Url2LabelByTfidfControllerApi.md#get_using_get3) | **GET** /url2label-tfidf/get | Get labels from URL


# **get_using_get3**
> LabelResponseEntity get_using_get3(access_token, url, num=num)

Get labels from URL

Url2Label by tfidf.<BR />Response<BR />&nbsp; Github: <a href=\"https://github.com/keigohtr/apitore-response-parent/tree/master/summarize-response\">summarize-response</a><BR />&nbsp; Class: com.apitore.banana.response.summarize.LabelResponseEntity<BR />

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.Url2LabelByTfidfControllerApi()
access_token = 'access_token_example' # str | Access Token
url = 'url_example' # str | url
num = 1 # int | num [max 10, default 1] (optional) (default to 1)

try:
    # Get labels from URL
    api_response = api_instance.get_using_get3(access_token, url, num=num)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Url2LabelByTfidfControllerApi->get_using_get3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Access Token | 
 **url** | **str**| url | 
 **num** | **int**| num [max 10, default 1] | [optional] [default to 1]

### Return type

[**LabelResponseEntity**](LabelResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

