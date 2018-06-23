# swagger_client.RomeControllerApi

All URIs are relative to *https://api.apitore.com/api/28*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rss2json_using_get**](RomeControllerApi.md#rss2json_using_get) | **GET** /rome/rss2json | RSS to JSON


# **rss2json_using_get**
> SyndFeedResponseEntity rss2json_using_get(access_token, rss)

RSS to JSON

RSS to Json.<BR />Response<BR />&nbsp; Github: <a href=\"https://github.com/keigohtr/apitore-response-parent/tree/master/rome-response\">rome-response</a><BR />&nbsp; Class: com.apitore.banana.response.org.rome.SyndFeedResponseEntity<BR />

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RomeControllerApi()
access_token = 'access_token_example' # str | Access Token
rss = 'rss_example' # str | RSS

try:
    # RSS to JSON
    api_response = api_instance.rss2json_using_get(access_token, rss)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RomeControllerApi->rss2json_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Access Token | 
 **rss** | **str**| RSS | 

### Return type

[**SyndFeedResponseEntity**](SyndFeedResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

