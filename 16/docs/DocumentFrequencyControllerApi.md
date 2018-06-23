# swagger_client.DocumentFrequencyControllerApi

All URIs are relative to *https://api.apitore.com/api/16*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_using_get**](DocumentFrequencyControllerApi.md#get_using_get) | **GET** /documentfrequency/get | Get document frequency


# **get_using_get**
> DocumentFrequencyResponseEntity get_using_get(access_token, word)

Get document frequency

Document Frequency by JaWikipedia 2016-9-15 dump.<BR />Response<BR />&nbsp; Github: <a href=\"https://github.com/keigohtr/apitore-response-parent/tree/master/summarize-response\">summarize-response</a><BR />&nbsp; Class: com.apitore.banana.response.summarize.DocumentFrequencyResponseEntity<BR />

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DocumentFrequencyControllerApi()
access_token = 'access_token_example' # str | Access Token
word = 'word_example' # str | word

try:
    # Get document frequency
    api_response = api_instance.get_using_get(access_token, word)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentFrequencyControllerApi->get_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Access Token | 
 **word** | **str**| word | 

### Return type

[**DocumentFrequencyResponseEntity**](DocumentFrequencyResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

