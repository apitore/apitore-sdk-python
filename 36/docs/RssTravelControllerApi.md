# swagger_client.RssTravelControllerApi

All URIs are relative to *https://api.apitore.com/api/36*

Method | HTTP request | Description
------------- | ------------- | -------------
[**feed_using_get8**](RssTravelControllerApi.md#feed_using_get8) | **GET** /feeds/travel | Get travel feeds


# **feed_using_get8**
> FeedResponseEntity feed_using_get8(access_token, page=page)

Get travel feeds

Travel feeds.<BR />Response<BR />&nbsp; Github: <a href=\"https://github.com/keigohtr/apitore-response-parent/tree/master/rome-response\">rome-response</a><BR />&nbsp; Class: com.apitore.banana.response.org.rome.FeedResponseEntity<BR />

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RssTravelControllerApi()
access_token = 'access_token_example' # str | Access Token
page = 1 # int | Page number [page x 10 feeds] (optional) (default to 1)

try:
    # Get travel feeds
    api_response = api_instance.feed_using_get8(access_token, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RssTravelControllerApi->feed_using_get8: %s\n" % e)
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

