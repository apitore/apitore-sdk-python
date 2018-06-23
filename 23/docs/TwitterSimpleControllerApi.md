# swagger_client.TwitterSimpleControllerApi

All URIs are relative to *https://api.apitore.com/api/23*

Method | HTTP request | Description
------------- | ------------- | -------------
[**my_timeline_using_get**](TwitterSimpleControllerApi.md#my_timeline_using_get) | **GET** /twitter/mytimeline | Get my tweets.
[**my_tweet_using_get**](TwitterSimpleControllerApi.md#my_tweet_using_get) | **GET** /twitter/mytweet | Get my tweets.
[**search_using_get**](TwitterSimpleControllerApi.md#search_using_get) | **GET** /twitter/search | Search tweets.


# **my_timeline_using_get**
> TwitterResponseEntity my_timeline_using_get(access_token, since_id=since_id, max_id=max_id, iter=iter)

Get my tweets.

Get my timeline tweets.<BR />Response<BR />&nbsp; Github: <a href=\"https://github.com/keigohtr/apitore-response-parent/tree/master/twitter-response\">twitter-response</a><BR />&nbsp; Class: com.apitore.banana.response.twitter.TwitterResponseEntity<BR />

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TwitterSimpleControllerApi()
access_token = 'access_token_example' # str | Access Token
since_id = -1 # int | Get after this id. (optional) (default to -1)
max_id = -1 # int | Get before this id. (optional) (default to -1)
iter = 1 # int | Numof requests. Return up to 200 x iter tweets. (optional) (default to 1)

try:
    # Get my tweets.
    api_response = api_instance.my_timeline_using_get(access_token, since_id=since_id, max_id=max_id, iter=iter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TwitterSimpleControllerApi->my_timeline_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Access Token | 
 **since_id** | **int**| Get after this id. | [optional] [default to -1]
 **max_id** | **int**| Get before this id. | [optional] [default to -1]
 **iter** | **int**| Numof requests. Return up to 200 x iter tweets. | [optional] [default to 1]

### Return type

[**TwitterResponseEntity**](TwitterResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **my_tweet_using_get**
> TwitterResponseEntity my_tweet_using_get(access_token, since_id=since_id, max_id=max_id, iter=iter)

Get my tweets.

Get my tweets.<BR />Response<BR />&nbsp; Github: <a href=\"https://github.com/keigohtr/apitore-response-parent/tree/master/twitter-response\">twitter-response</a><BR />&nbsp; Class: com.apitore.banana.response.twitter.TwitterResponseEntity<BR />

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TwitterSimpleControllerApi()
access_token = 'access_token_example' # str | Access Token
since_id = -1 # int | Get after this id. (optional) (default to -1)
max_id = -1 # int | Get before this id. (optional) (default to -1)
iter = 1 # int | Numof requests. Return up to 200 x iter tweets. (optional) (default to 1)

try:
    # Get my tweets.
    api_response = api_instance.my_tweet_using_get(access_token, since_id=since_id, max_id=max_id, iter=iter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TwitterSimpleControllerApi->my_tweet_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Access Token | 
 **since_id** | **int**| Get after this id. | [optional] [default to -1]
 **max_id** | **int**| Get before this id. | [optional] [default to -1]
 **iter** | **int**| Numof requests. Return up to 200 x iter tweets. | [optional] [default to 1]

### Return type

[**TwitterResponseEntity**](TwitterResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_using_get**
> TwitterResponseEntity search_using_get(access_token, q, since_id=since_id, max_id=max_id, iter=iter)

Search tweets.

Tweets search API.<BR />Response<BR />&nbsp; Github: <a href=\"https://github.com/keigohtr/apitore-response-parent/tree/master/twitter-response\">twitter-response</a><BR />&nbsp; Class: com.apitore.banana.response.twitter.TwitterResponseEntity<BR />

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TwitterSimpleControllerApi()
access_token = 'access_token_example' # str | Access Token
q = 'q_example' # str | Search query
since_id = -1 # int | Search after this id. (optional) (default to -1)
max_id = -1 # int | Search before this id. (optional) (default to -1)
iter = 1 # int | Numof search requests. Return up to 100 x iter tweets. (optional) (default to 1)

try:
    # Search tweets.
    api_response = api_instance.search_using_get(access_token, q, since_id=since_id, max_id=max_id, iter=iter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TwitterSimpleControllerApi->search_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Access Token | 
 **q** | **str**| Search query | 
 **since_id** | **int**| Search after this id. | [optional] [default to -1]
 **max_id** | **int**| Search before this id. | [optional] [default to -1]
 **iter** | **int**| Numof search requests. Return up to 100 x iter tweets. | [optional] [default to 1]

### Return type

[**TwitterResponseEntity**](TwitterResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

