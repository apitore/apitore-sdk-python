# swagger_client.RssTechControllerApi

All URIs are relative to *https://api.apitore.com/api/35*

Method | HTTP request | Description
------------- | ------------- | -------------
[**feed_using_get7**](RssTechControllerApi.md#feed_using_get7) | **GET** /feeds/tech | Get tech feeds


# **feed_using_get7**
> FeedResponseEntity feed_using_get7(access_token, page=page)

Get tech feeds

Tech feeds.<BR />Response<BR />&nbsp; Github: <a href=\"https://github.com/keigohtr/apitore-response-parent/tree/master/rome-response\">rome-response</a><BR />&nbsp; Class: com.apitore.banana.response.org.rome.FeedResponseEntity<BR />

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RssTechControllerApi()
access_token = 'access_token_example' # str | Access Token
page = 1 # int | Page number [page x 10 feeds] (optional) (default to 1)

try:
    # Get tech feeds
    api_response = api_instance.feed_using_get7(access_token, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RssTechControllerApi->feed_using_get7: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Access Token | 
 **page** | **int**| Page number [page x 10 feeds] | [optional] [default to 1]

### Return type

[**FeedResponseEntity**](FeedResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

