# swagger_client.SentencePieceBpeTweetControllerApi

All URIs are relative to *https://api.apitore.com/api/38*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_using_get**](SentencePieceBpeTweetControllerApi.md#get_using_get) | **GET** /sentencepiece-bpe-tweet/get | SentencePiece (bpe)


# **get_using_get**
> SentencePieceTokenResponseEntity get_using_get(access_token, text)

SentencePiece (bpe)

SentencePiece (bpe).<BR />Response<BR />&nbsp; Github: <a href=\"https://github.com/keigohtr/apitore-response-parent/tree/master/sentencepiece-response\">sentencepiece-response</a><BR />&nbsp; Class: com.apitore.banana.response.com.atilika.sentencepiece.SentencePieceTokenResponseEntity<BR />

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SentencePieceBpeTweetControllerApi()
access_token = 'access_token_example' # str | Access Token
text = 'text_example' # str | Text [up to 400 characters]

try:
    # SentencePiece (bpe)
    api_response = api_instance.get_using_get(access_token, text)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SentencePieceBpeTweetControllerApi->get_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Access Token | 
 **text** | **str**| Text [up to 400 characters] | 

### Return type

[**SentencePieceTokenResponseEntity**](SentencePieceTokenResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

