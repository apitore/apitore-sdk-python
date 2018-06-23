# swagger_client.WordnetSimilarityControllerApi

All URIs are relative to *https://api.apitore.com/api/47*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hirststonge_using_get**](WordnetSimilarityControllerApi.md#hirststonge_using_get) | **GET** /wordnet-similarity/hirststonge | WordNet Similarity WebAPI.
[**hirststonge_using_get1**](WordnetSimilarityControllerApi.md#hirststonge_using_get1) | **GET** /wordnet-similarity/jiangconrath | WordNet Similarity WebAPI.
[**hirststonge_using_get2**](WordnetSimilarityControllerApi.md#hirststonge_using_get2) | **GET** /wordnet-similarity/leacockchodorow | WordNet Similarity WebAPI.
[**hirststonge_using_get3**](WordnetSimilarityControllerApi.md#hirststonge_using_get3) | **GET** /wordnet-similarity/lesk | WordNet Similarity WebAPI.
[**hirststonge_using_get4**](WordnetSimilarityControllerApi.md#hirststonge_using_get4) | **GET** /wordnet-similarity/lin | WordNet Similarity WebAPI.
[**hirststonge_using_get5**](WordnetSimilarityControllerApi.md#hirststonge_using_get5) | **GET** /wordnet-similarity/path | WordNet Similarity WebAPI.
[**hirststonge_using_get6**](WordnetSimilarityControllerApi.md#hirststonge_using_get6) | **GET** /wordnet-similarity/resnik | WordNet Similarity WebAPI.
[**hirststonge_using_get7**](WordnetSimilarityControllerApi.md#hirststonge_using_get7) | **GET** /wordnet-similarity/wupalmer | WordNet Similarity WebAPI.


# **hirststonge_using_get**
> WordnetSimilarityResponseEntity hirststonge_using_get(access_token, word1, word2, pos1=pos1, pos2=pos2)

WordNet Similarity WebAPI.

WordNet similarity.<BR />Response<BR />&nbsp; Github: <a href=\"https://github.com/keigohtr/apitore-response-parent/tree/master/wordnet-response\">wordnet-response</a><BR />

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WordnetSimilarityControllerApi()
access_token = 'access_token_example' # str | Access Token
word1 = 'word1_example' # str | Word1
word2 = 'word2_example' # str | Word2
pos1 = 'pos1_example' # str | Part-of-speech1. [n:noun,v:verb,a:adjective,r:adverb] (optional)
pos2 = 'pos2_example' # str | Part-of-speech2. [n:noun,v:verb,a:adjective,r:adverb] (optional)

try:
    # WordNet Similarity WebAPI.
    api_response = api_instance.hirststonge_using_get(access_token, word1, word2, pos1=pos1, pos2=pos2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordnetSimilarityControllerApi->hirststonge_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Access Token | 
 **word1** | **str**| Word1 | 
 **word2** | **str**| Word2 | 
 **pos1** | **str**| Part-of-speech1. [n:noun,v:verb,a:adjective,r:adverb] | [optional] 
 **pos2** | **str**| Part-of-speech2. [n:noun,v:verb,a:adjective,r:adverb] | [optional] 

### Return type

[**WordnetSimilarityResponseEntity**](WordnetSimilarityResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hirststonge_using_get1**
> WordnetSimilarityResponseEntity hirststonge_using_get1(access_token, word1, word2, pos1=pos1, pos2=pos2)

WordNet Similarity WebAPI.

WordNet similarity.<BR />Response<BR />&nbsp; Github: <a href=\"https://github.com/keigohtr/apitore-response-parent/tree/master/wordnet-response\">wordnet-response</a><BR />

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WordnetSimilarityControllerApi()
access_token = 'access_token_example' # str | Access Token
word1 = 'word1_example' # str | Word1
word2 = 'word2_example' # str | Word2
pos1 = 'pos1_example' # str | Part-of-speech1. [n:noun,v:verb,a:adjective,r:adverb] (optional)
pos2 = 'pos2_example' # str | Part-of-speech2. [n:noun,v:verb,a:adjective,r:adverb] (optional)

try:
    # WordNet Similarity WebAPI.
    api_response = api_instance.hirststonge_using_get1(access_token, word1, word2, pos1=pos1, pos2=pos2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordnetSimilarityControllerApi->hirststonge_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Access Token | 
 **word1** | **str**| Word1 | 
 **word2** | **str**| Word2 | 
 **pos1** | **str**| Part-of-speech1. [n:noun,v:verb,a:adjective,r:adverb] | [optional] 
 **pos2** | **str**| Part-of-speech2. [n:noun,v:verb,a:adjective,r:adverb] | [optional] 

### Return type

[**WordnetSimilarityResponseEntity**](WordnetSimilarityResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hirststonge_using_get2**
> WordnetSimilarityResponseEntity hirststonge_using_get2(access_token, word1, word2, pos1=pos1, pos2=pos2)

WordNet Similarity WebAPI.

WordNet similarity.<BR />Response<BR />&nbsp; Github: <a href=\"https://github.com/keigohtr/apitore-response-parent/tree/master/wordnet-response\">wordnet-response</a><BR />

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WordnetSimilarityControllerApi()
access_token = 'access_token_example' # str | Access Token
word1 = 'word1_example' # str | Word1
word2 = 'word2_example' # str | Word2
pos1 = 'pos1_example' # str | Part-of-speech1. [n:noun,v:verb,a:adjective,r:adverb] (optional)
pos2 = 'pos2_example' # str | Part-of-speech2. [n:noun,v:verb,a:adjective,r:adverb] (optional)

try:
    # WordNet Similarity WebAPI.
    api_response = api_instance.hirststonge_using_get2(access_token, word1, word2, pos1=pos1, pos2=pos2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordnetSimilarityControllerApi->hirststonge_using_get2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Access Token | 
 **word1** | **str**| Word1 | 
 **word2** | **str**| Word2 | 
 **pos1** | **str**| Part-of-speech1. [n:noun,v:verb,a:adjective,r:adverb] | [optional] 
 **pos2** | **str**| Part-of-speech2. [n:noun,v:verb,a:adjective,r:adverb] | [optional] 

### Return type

[**WordnetSimilarityResponseEntity**](WordnetSimilarityResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hirststonge_using_get3**
> WordnetSimilarityResponseEntity hirststonge_using_get3(access_token, word1, word2, pos1=pos1, pos2=pos2)

WordNet Similarity WebAPI.

WordNet similarity.<BR />Response<BR />&nbsp; Github: <a href=\"https://github.com/keigohtr/apitore-response-parent/tree/master/wordnet-response\">wordnet-response</a><BR />

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WordnetSimilarityControllerApi()
access_token = 'access_token_example' # str | Access Token
word1 = 'word1_example' # str | Word1
word2 = 'word2_example' # str | Word2
pos1 = 'pos1_example' # str | Part-of-speech1. [n:noun,v:verb,a:adjective,r:adverb] (optional)
pos2 = 'pos2_example' # str | Part-of-speech2. [n:noun,v:verb,a:adjective,r:adverb] (optional)

try:
    # WordNet Similarity WebAPI.
    api_response = api_instance.hirststonge_using_get3(access_token, word1, word2, pos1=pos1, pos2=pos2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordnetSimilarityControllerApi->hirststonge_using_get3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Access Token | 
 **word1** | **str**| Word1 | 
 **word2** | **str**| Word2 | 
 **pos1** | **str**| Part-of-speech1. [n:noun,v:verb,a:adjective,r:adverb] | [optional] 
 **pos2** | **str**| Part-of-speech2. [n:noun,v:verb,a:adjective,r:adverb] | [optional] 

### Return type

[**WordnetSimilarityResponseEntity**](WordnetSimilarityResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hirststonge_using_get4**
> WordnetSimilarityResponseEntity hirststonge_using_get4(access_token, word1, word2, pos1=pos1, pos2=pos2)

WordNet Similarity WebAPI.

WordNet similarity.<BR />Response<BR />&nbsp; Github: <a href=\"https://github.com/keigohtr/apitore-response-parent/tree/master/wordnet-response\">wordnet-response</a><BR />

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WordnetSimilarityControllerApi()
access_token = 'access_token_example' # str | Access Token
word1 = 'word1_example' # str | Word1
word2 = 'word2_example' # str | Word2
pos1 = 'pos1_example' # str | Part-of-speech1. [n:noun,v:verb,a:adjective,r:adverb] (optional)
pos2 = 'pos2_example' # str | Part-of-speech2. [n:noun,v:verb,a:adjective,r:adverb] (optional)

try:
    # WordNet Similarity WebAPI.
    api_response = api_instance.hirststonge_using_get4(access_token, word1, word2, pos1=pos1, pos2=pos2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordnetSimilarityControllerApi->hirststonge_using_get4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Access Token | 
 **word1** | **str**| Word1 | 
 **word2** | **str**| Word2 | 
 **pos1** | **str**| Part-of-speech1. [n:noun,v:verb,a:adjective,r:adverb] | [optional] 
 **pos2** | **str**| Part-of-speech2. [n:noun,v:verb,a:adjective,r:adverb] | [optional] 

### Return type

[**WordnetSimilarityResponseEntity**](WordnetSimilarityResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hirststonge_using_get5**
> WordnetSimilarityResponseEntity hirststonge_using_get5(access_token, word1, word2, pos1=pos1, pos2=pos2)

WordNet Similarity WebAPI.

WordNet similarity.<BR />Response<BR />&nbsp; Github: <a href=\"https://github.com/keigohtr/apitore-response-parent/tree/master/wordnet-response\">wordnet-response</a><BR />

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WordnetSimilarityControllerApi()
access_token = 'access_token_example' # str | Access Token
word1 = 'word1_example' # str | Word1
word2 = 'word2_example' # str | Word2
pos1 = 'pos1_example' # str | Part-of-speech1. [n:noun,v:verb,a:adjective,r:adverb] (optional)
pos2 = 'pos2_example' # str | Part-of-speech2. [n:noun,v:verb,a:adjective,r:adverb] (optional)

try:
    # WordNet Similarity WebAPI.
    api_response = api_instance.hirststonge_using_get5(access_token, word1, word2, pos1=pos1, pos2=pos2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordnetSimilarityControllerApi->hirststonge_using_get5: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Access Token | 
 **word1** | **str**| Word1 | 
 **word2** | **str**| Word2 | 
 **pos1** | **str**| Part-of-speech1. [n:noun,v:verb,a:adjective,r:adverb] | [optional] 
 **pos2** | **str**| Part-of-speech2. [n:noun,v:verb,a:adjective,r:adverb] | [optional] 

### Return type

[**WordnetSimilarityResponseEntity**](WordnetSimilarityResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hirststonge_using_get6**
> WordnetSimilarityResponseEntity hirststonge_using_get6(access_token, word1, word2, pos1=pos1, pos2=pos2)

WordNet Similarity WebAPI.

WordNet similarity.<BR />Response<BR />&nbsp; Github: <a href=\"https://github.com/keigohtr/apitore-response-parent/tree/master/wordnet-response\">wordnet-response</a><BR />

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WordnetSimilarityControllerApi()
access_token = 'access_token_example' # str | Access Token
word1 = 'word1_example' # str | Word1
word2 = 'word2_example' # str | Word2
pos1 = 'pos1_example' # str | Part-of-speech1. [n:noun,v:verb,a:adjective,r:adverb] (optional)
pos2 = 'pos2_example' # str | Part-of-speech2. [n:noun,v:verb,a:adjective,r:adverb] (optional)

try:
    # WordNet Similarity WebAPI.
    api_response = api_instance.hirststonge_using_get6(access_token, word1, word2, pos1=pos1, pos2=pos2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordnetSimilarityControllerApi->hirststonge_using_get6: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Access Token | 
 **word1** | **str**| Word1 | 
 **word2** | **str**| Word2 | 
 **pos1** | **str**| Part-of-speech1. [n:noun,v:verb,a:adjective,r:adverb] | [optional] 
 **pos2** | **str**| Part-of-speech2. [n:noun,v:verb,a:adjective,r:adverb] | [optional] 

### Return type

[**WordnetSimilarityResponseEntity**](WordnetSimilarityResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hirststonge_using_get7**
> WordnetSimilarityResponseEntity hirststonge_using_get7(access_token, word1, word2, pos1=pos1, pos2=pos2)

WordNet Similarity WebAPI.

WordNet similarity.<BR />Response<BR />&nbsp; Github: <a href=\"https://github.com/keigohtr/apitore-response-parent/tree/master/wordnet-response\">wordnet-response</a><BR />

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WordnetSimilarityControllerApi()
access_token = 'access_token_example' # str | Access Token
word1 = 'word1_example' # str | Word1
word2 = 'word2_example' # str | Word2
pos1 = 'pos1_example' # str | Part-of-speech1. [n:noun,v:verb,a:adjective,r:adverb] (optional)
pos2 = 'pos2_example' # str | Part-of-speech2. [n:noun,v:verb,a:adjective,r:adverb] (optional)

try:
    # WordNet Similarity WebAPI.
    api_response = api_instance.hirststonge_using_get7(access_token, word1, word2, pos1=pos1, pos2=pos2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordnetSimilarityControllerApi->hirststonge_using_get7: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Access Token | 
 **word1** | **str**| Word1 | 
 **word2** | **str**| Word2 | 
 **pos1** | **str**| Part-of-speech1. [n:noun,v:verb,a:adjective,r:adverb] | [optional] 
 **pos2** | **str**| Part-of-speech2. [n:noun,v:verb,a:adjective,r:adverb] | [optional] 

### Return type

[**WordnetSimilarityResponseEntity**](WordnetSimilarityResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

