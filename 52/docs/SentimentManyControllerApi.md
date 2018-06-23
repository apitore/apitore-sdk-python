# swagger_client.SentimentManyControllerApi

All URIs are relative to *https://api.apitore.com/api/52*

Method | HTTP request | Description
------------- | ------------- | -------------
[**predict_using_post**](SentimentManyControllerApi.md#predict_using_post) | **POST** /sentiments/predict | Sentiment predict


# **predict_using_post**
> ListSentimentResponseEntity predict_using_post(access_token, req)

Sentiment predict

Sentiment Analysis, last update at 2017-5-12.<BR />Response<BR />&nbsp; Github: <a href=\"https://github.com/keigohtr/apitore-response-parent/tree/master/word2vec-response\">word2vec-response</a><BR />&nbsp; Class: com.apitore.banana.response.sentiment.ListSentimentResponseEntity<BR />

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SentimentManyControllerApi()
access_token = 'access_token_example' # str | Access Token
req = swagger_client.SentimentRequestEntity() # SentimentRequestEntity | req

try:
    # Sentiment predict
    api_response = api_instance.predict_using_post(access_token, req)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SentimentManyControllerApi->predict_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Access Token | 
 **req** | [**SentimentRequestEntity**](SentimentRequestEntity.md)| req | 

### Return type

[**ListSentimentResponseEntity**](ListSentimentResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

