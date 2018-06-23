# swagger_client.Word2VecControllerApi

All URIs are relative to *https://api.apitore.com/api/9*

Method | HTTP request | Description
------------- | ------------- | -------------
[**distance_using_get**](Word2VecControllerApi.md#distance_using_get) | **GET** /word2vec-neologd-jawiki/distance | Word2Vec distance


# **distance_using_get**
> DistanceResponseEntity distance_using_get(access_token, word, num=num)

Word2Vec distance

Word2Vec JaWikipedia 2016-9-15 dump.<BR />Response<BR />&nbsp; Github: <a href=\"https://github.com/keigohtr/apitore-response-parent/tree/master/word2vec-response\">word2vec-response</a><BR />&nbsp; Class: com.apitore.banana.response.word2vec.DistanceResponseEntity<BR />

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.Word2VecControllerApi()
access_token = 'access_token_example' # str | Access Token
word = 'word_example' # str | word
num = 1 # int | num [max 10, default 1] (optional) (default to 1)

try:
    # Word2Vec distance
    api_response = api_instance.distance_using_get(access_token, word, num=num)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Word2VecControllerApi->distance_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Access Token | 
 **word** | **str**| word | 
 **num** | **int**| num [max 10, default 1] | [optional] [default to 1]

### Return type

[**DistanceResponseEntity**](DistanceResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

