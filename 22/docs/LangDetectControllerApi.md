# swagger_client.LangDetectControllerApi

All URIs are relative to *https://api.apitore.com/api/22*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_using_get**](LangDetectControllerApi.md#get_using_get) | **GET** /langdetect/get | Language Detection. This supports 53 languages.
[**sm_get_using_get**](LangDetectControllerApi.md#sm_get_using_get) | **GET** /langdetect/short/get | Language Detection for Short Messages. This supports 53 languages.


# **get_using_get**
> LanguageResponseEntity get_using_get(access_token, text)

Language Detection. This supports 53 languages.

Language Detection.<BR />Response<BR />&nbsp; Github: <a href=\"https://github.com/keigohtr/apitore-response-parent/tree/master/langdetect-response\">langdetect-response</a><BR />&nbsp; Class: com.apitore.banana.response.org.jsoup.LanguageResponseEntity<BR />

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LangDetectControllerApi()
access_token = 'access_token_example' # str | Access Token
text = 'text_example' # str | Text [10-20 words over is recommended]

try:
    # Language Detection. This supports 53 languages.
    api_response = api_instance.get_using_get(access_token, text)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LangDetectControllerApi->get_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Access Token | 
 **text** | **str**| Text [10-20 words over is recommended] | 

### Return type

[**LanguageResponseEntity**](LanguageResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sm_get_using_get**
> LanguageResponseEntity sm_get_using_get(access_token, text)

Language Detection for Short Messages. This supports 53 languages.

Language Detection.<BR />Response<BR />&nbsp; Github: <a href=\"https://github.com/keigohtr/apitore-response-parent/tree/master/langdetect-response\">langdetect-response</a><BR />&nbsp; Class: com.apitore.banana.response.org.jsoup.LanguageResponseEntity<BR />

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LangDetectControllerApi()
access_token = 'access_token_example' # str | Access Token
text = 'text_example' # str | Text [Short message like tweet is supported]

try:
    # Language Detection for Short Messages. This supports 53 languages.
    api_response = api_instance.sm_get_using_get(access_token, text)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LangDetectControllerApi->sm_get_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Access Token | 
 **text** | **str**| Text [Short message like tweet is supported] | 

### Return type

[**LanguageResponseEntity**](LanguageResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

