# swagger_client.TwitterWord2VecControllerApi

All URIs are relative to *https://api.apitore.com/api/24*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_using_get2**](TwitterWord2VecControllerApi.md#search_using_get2) | **GET** /twitter-word2vec/search | Search tweets.


# **search_using_get2**
> TwitterResponseEntity search_using_get2(access_token, q, since_id=since_id, max_id=max_id, iter=iter)

Search tweets.

Tweets search API with Word2Vec query expansion.<BR />Response<BR />&nbsp; Github: <a href=\"https://github.com/keigohtr/apitore-response-parent/tree/master/twitter-response\">twitter-response</a><BR />&nbsp; Class: com.apitore.banana.response.twitter.TwitterResponseEntity<BR />

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TwitterWord2VecControllerApi()
access_token = 'access_token_example' # str | Access Token
q = 'q_example' # str | Search query
since_id = -1 # int | Get after this id. (optional) (default to -1)
max_id = -1 # int | Get before this id. (optional) (default to -1)
iter = 1 # int | Numof search requests. Return up to 100 x iter tweets. (optional) (default to 1)

try:
    # Search tweets.
    api_response = api_instance.search_using_get2(access_token, q, since_id=since_id, max_id=max_id, iter=iter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TwitterWord2VecControllerApi->search_using_get2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Access Token | 
 **q** | **str**| Search query | 
 **since_id** | **int**| Get after this id. | [optional] [default to -1]
 **max_id** | **int**| Get before this id. | [optional] [default to -1]
 **iter** | **int**| Numof search requests. Return up to 100 x iter tweets. | [optional] [default to 1]

### Return type

[**TwitterResponseEntity**](TwitterResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

