# swagger_client.KuromojiIpadicNeologdControllerApi

All URIs are relative to *https://api.apitore.com/api/7*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tokenize_using_get1**](KuromojiIpadicNeologdControllerApi.md#tokenize_using_get1) | **GET** /kuromoji-ipadic-neologd/tokenize | Kuromoji IPADIC NEologd
[**tokenize_using_post1**](KuromojiIpadicNeologdControllerApi.md#tokenize_using_post1) | **POST** /kuromoji-ipadic-neologd/tokenize | Kuromoji IPADIC NEologd


# **tokenize_using_get1**
> TokenResponseEntity tokenize_using_get1(access_token, text)

Kuromoji IPADIC NEologd

Kuromoji IPADIC NEologd dictionary.<BR />Response<BR />&nbsp; Github: <a href=\"https://github.com/keigohtr/apitore-response-parent/tree/master/kuromoji-response\">kuromoji-response</a><BR />&nbsp; Class: com.apitore.banana.response.com.atilika.kuromoji.TokenResponseEntity<BR />

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KuromojiIpadicNeologdControllerApi()
access_token = 'access_token_example' # str | Access Token
text = 'text_example' # str | Text [up to 400 characters]

try:
    # Kuromoji IPADIC NEologd
    api_response = api_instance.tokenize_using_get1(access_token, text)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KuromojiIpadicNeologdControllerApi->tokenize_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Access Token | 
 **text** | **str**| Text [up to 400 characters] | 

### Return type

[**TokenResponseEntity**](TokenResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tokenize_using_post1**
> TokensResponseEntity tokenize_using_post1(access_token, req)

Kuromoji IPADIC NEologd

Kuromoji IPADIC NEologd dictionary.<BR />Response<BR />&nbsp; Github: <a href=\"https://github.com/keigohtr/apitore-response-parent/tree/master/kuromoji-response\">kuromoji-response</a><BR />&nbsp; Class: com.apitore.banana.response.com.atilika.kuromoji.TokenResponseEntity<BR />

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KuromojiIpadicNeologdControllerApi()
access_token = 'access_token_example' # str | Access Token
req = swagger_client.KuromojiRequestEntity() # KuromojiRequestEntity | Input Text

try:
    # Kuromoji IPADIC NEologd
    api_response = api_instance.tokenize_using_post1(access_token, req)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KuromojiIpadicNeologdControllerApi->tokenize_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Access Token | 
 **req** | [**KuromojiRequestEntity**](KuromojiRequestEntity.md)| Input Text | 

### Return type

[**TokensResponseEntity**](TokensResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

