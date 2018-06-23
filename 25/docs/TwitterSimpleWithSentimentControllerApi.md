# swagger_client.TwitterSimpleWithSentimentControllerApi

All URIs are relative to *https://api.apitore.com/api/25*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_using_get1**](TwitterSimpleWithSentimentControllerApi.md#search_using_get1) | **GET** /twitter-sentiment/search | Search tweets.


# **search_using_get1**
> TwitterResponseEntity search_using_get1(access_token, q, since_id=since_id, max_id=max_id)

Search tweets.

Tweets search API with sentiment by Apitore sentiment API.<BR />Response<BR />&nbsp; Github: <a href=\"https://github.com/keigohtr/apitore-response-parent/tree/master/twitter-response\">twitter-response</a><BR />&nbsp; Class: com.apitore.banana.response.twitter.TwitterResponseEntity<BR />

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TwitterSimpleWithSentimentControllerApi()
access_token = 'access_token_example' # str | Access Token
q = 'q_example' # str | Search query
since_id = -1 # int | Get after this id. (optional) (default to -1)
max_id = -1 # int | Get before this id. (optional) (default to -1)

try:
    # Search tweets.
    api_response = api_instance.search_using_get1(access_token, q, since_id=since_id, max_id=max_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TwitterSimpleWithSentimentControllerApi->search_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Access Token | 
 **q** | **str**| Search query | 
 **since_id** | **int**| Get after this id. | [optional] [default to -1]
 **max_id** | **int**| Get before this id. | [optional] [default to -1]

### Return type

[**TwitterResponseEntity**](TwitterResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

