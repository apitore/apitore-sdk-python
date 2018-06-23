# swagger_client.SentimentV2ControllerApi

All URIs are relative to *https://api.apitore.com/api/39*

Method | HTTP request | Description
------------- | ------------- | -------------
[**predict_using_get**](SentimentV2ControllerApi.md#predict_using_get) | **GET** /sentiment-v2/predict | Sentiment predict


# **predict_using_get**
> SentimentResponseEntity predict_using_get(access_token, text)

Sentiment predict

Sentiment Analysis, last update at 2017-4-29.<BR />Response<BR />&nbsp; Github: <a href=\"https://github.com/keigohtr/apitore-response-parent/tree/master/word2vec-response\">word2vec-response</a><BR />&nbsp; Class: com.apitore.banana.response.sentiment.SentimentResponseEntity<BR />

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SentimentV2ControllerApi()
access_token = 'access_token_example' # str | Access Token
text = 'text_example' # str | text

try:
    # Sentiment predict
    api_response = api_instance.predict_using_get(access_token, text)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SentimentV2ControllerApi->predict_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Access Token | 
 **text** | **str**| text | 

### Return type

[**SentimentResponseEntity**](SentimentResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

