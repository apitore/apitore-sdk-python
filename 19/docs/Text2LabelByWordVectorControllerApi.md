# swagger_client.Text2LabelByWordVectorControllerApi

All URIs are relative to *https://api.apitore.com/api/19*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_using_get2**](Text2LabelByWordVectorControllerApi.md#get_using_get2) | **GET** /text2label-wordvector/get | Get labels from text


# **get_using_get2**
> LabelResponseEntity get_using_get2(access_token, text, num=num)

Get labels from text

Text2Label by kmeans of word vectors.<BR />Response<BR />&nbsp; Github: <a href=\"https://github.com/keigohtr/apitore-response-parent/tree/master/summarize-response\">summarize-response</a><BR />&nbsp; Class: com.apitore.banana.response.summarize.LabelResponseEntity<BR />

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.Text2LabelByWordVectorControllerApi()
access_token = 'access_token_example' # str | Access Token
text = 'text_example' # str | text
num = 1 # int | num [max 10, default 1] (optional) (default to 1)

try:
    # Get labels from text
    api_response = api_instance.get_using_get2(access_token, text, num=num)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Text2LabelByWordVectorControllerApi->get_using_get2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Access Token | 
 **text** | **str**| text | 
 **num** | **int**| num [max 10, default 1] | [optional] [default to 1]

### Return type

[**LabelResponseEntity**](LabelResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

