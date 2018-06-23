# swagger_client.SentenceSeparatorControllerApi

All URIs are relative to *https://api.apitore.com/api/17*

Method | HTTP request | Description
------------- | ------------- | -------------
[**heuristics_using_get**](SentenceSeparatorControllerApi.md#heuristics_using_get) | **GET** /sentence-separate/heuristics | Separate from text to sentence.


# **heuristics_using_get**
> SentenceResponseEntity heuristics_using_get(access_token, text)

Separate from text to sentence.

Sentence separator.<BR />Response<BR />&nbsp; Github: <a href=\"https://github.com/keigohtr/apitore-response-parent/tree/master/summarize-response\">summarize-response</a><BR />&nbsp; Class: com.apitore.banana.response.summarize.SentenceResponseEntity<BR />

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SentenceSeparatorControllerApi()
access_token = 'access_token_example' # str | Access Token
text = 'text_example' # str | text

try:
    # Separate from text to sentence.
    api_response = api_instance.heuristics_using_get(access_token, text)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SentenceSeparatorControllerApi->heuristics_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Access Token | 
 **text** | **str**| text | 

### Return type

[**SentenceResponseEntity**](SentenceResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

