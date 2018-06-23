# swagger_client.TwitterSimpleSummarizeControllerApi

All URIs are relative to *https://api.apitore.com/api/27*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_using_get**](TwitterSimpleSummarizeControllerApi.md#get_using_get) | **GET** /twitter-summarize/get | Summarize tweets.


# **get_using_get**
> TwitterSummarizeResponseEntity get_using_get(access_token, q, since_id=since_id, max_id=max_id, iter=iter, num=num)

Summarize tweets.

Tweet summarization API.<BR />Response<BR />&nbsp; Github: <a href=\"https://github.com/keigohtr/apitore-response-parent/tree/master/twitter-response\">twitter-response</a><BR />&nbsp; Class: com.apitore.banana.response.twitter.TwitterSummarizeResponseEntity<BR />

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TwitterSimpleSummarizeControllerApi()
access_token = 'access_token_example' # str | Access Token
q = 'q_example' # str | Search query
since_id = -1 # int | Get after this id. (optional) (default to -1)
max_id = -1 # int | Get before this id. (optional) (default to -1)
iter = 1 # int | Numof search requests. Return up to 100 x iter tweets. (optional) (default to 1)
num = 3 # int | Numof summarization tweets. (optional) (default to 3)

try:
    # Summarize tweets.
    api_response = api_instance.get_using_get(access_token, q, since_id=since_id, max_id=max_id, iter=iter, num=num)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TwitterSimpleSummarizeControllerApi->get_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Access Token | 
 **q** | **str**| Search query | 
 **since_id** | **int**| Get after this id. | [optional] [default to -1]
 **max_id** | **int**| Get before this id. | [optional] [default to -1]
 **iter** | **int**| Numof search requests. Return up to 100 x iter tweets. | [optional] [default to 1]
 **num** | **int**| Numof summarization tweets. | [optional] [default to 3]

### Return type

[**TwitterSummarizeResponseEntity**](TwitterSummarizeResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

