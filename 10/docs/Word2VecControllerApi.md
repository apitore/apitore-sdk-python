# swagger_client.Word2VecControllerApi

All URIs are relative to *https://api.apitore.com/api/10*

Method | HTTP request | Description
------------- | ------------- | -------------
[**wordvector_using_get**](Word2VecControllerApi.md#wordvector_using_get) | **GET** /word2vec-neologd-jawiki/wordvector | Word2Vec wordvector


# **wordvector_using_get**
> WordVectorResponseEntity wordvector_using_get(access_token, word)

Word2Vec wordvector

Word2Vec JaWikipedia 2016-9-15 dump.<BR />Response<BR />&nbsp; Github: <a href=\"https://github.com/keigohtr/apitore-response-parent/tree/master/word2vec-response\">word2vec-response</a><BR />&nbsp; Class: com.apitore.banana.response.word2vec.WordVectorResponseEntity<BR />

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

try:
    # Word2Vec wordvector
    api_response = api_instance.wordvector_using_get(access_token, word)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Word2VecControllerApi->wordvector_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Access Token | 
 **word** | **str**| word | 

### Return type

[**WordVectorResponseEntity**](WordVectorResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

