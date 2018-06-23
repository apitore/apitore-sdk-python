# swagger_client.SentenceSimilarityControllerApi

All URIs are relative to *https://api.apitore.com/api/53*

Method | HTTP request | Description
------------- | ------------- | -------------
[**eval_using_post**](SentenceSimilarityControllerApi.md#eval_using_post) | **POST** /sentence-similarity/eval | Text similarity using word2vec


# **eval_using_post**
> TextSimilarityResponseEntity eval_using_post(access_token, req)

Text similarity using word2vec

Sentence similarity.<BR />Response<BR />&nbsp; Github: <a href=\"https://github.com/keigohtr/apitore-response-parent/tree/master/text-similarity-response\">text-similarity-response</a><BR />&nbsp; Class: com.apitore.banana.response.textsimilarity.TextSimilarityResponseEntity<BR />

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SentenceSimilarityControllerApi()
access_token = 'access_token_example' # str | Access Token
req = swagger_client.TextRequestEntity() # TextRequestEntity | Input texts. Text must be a sentence.

try:
    # Text similarity using word2vec
    api_response = api_instance.eval_using_post(access_token, req)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SentenceSimilarityControllerApi->eval_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Access Token | 
 **req** | [**TextRequestEntity**](TextRequestEntity.md)| Input texts. Text must be a sentence. | 

### Return type

[**TextSimilarityResponseEntity**](TextSimilarityResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

