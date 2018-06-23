# swagger_client.Word2VecControllerApi

All URIs are relative to *https://api.apitore.com/api/8*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analogy_using_get**](Word2VecControllerApi.md#analogy_using_get) | **GET** /word2vec-neologd-jawiki/analogy | Word2Vec analogy
[**distance_using_get1**](Word2VecControllerApi.md#distance_using_get1) | **GET** /word2vec-neologd-jawiki/distance | Word2Vec distance
[**similarity_using_get**](Word2VecControllerApi.md#similarity_using_get) | **GET** /word2vec-neologd-jawiki/similarity | Word2Vec similarity
[**vec_distance_using_get**](Word2VecControllerApi.md#vec_distance_using_get) | **GET** /word2vec-neologd-jawiki/vec_distance | Word2Vec distance (Vector version)
[**wordvector_using_get1**](Word2VecControllerApi.md#wordvector_using_get1) | **GET** /word2vec-neologd-jawiki/wordvector | Word2Vec wordvector


# **analogy_using_get**
> AnalogyResponseEntity analogy_using_get(access_token, positives, negatives=negatives, num=num)

Word2Vec analogy

Word2Vec JaWikipedia 2016-9-15 dump.<BR />Response<BR />&nbsp; Github: <a href=\"https://github.com/keigohtr/apitore-response-parent/tree/master/word2vec-response\">word2vec-response</a><BR />&nbsp; Class: com.apitore.banana.response.word2vec.AnalogyResponseEntity<BR />

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.Word2VecControllerApi()
access_token = 'access_token_example' # str | Access Token
positives = 'positives_example' # str | positive1 positive2 ...[space separated strings]
negatives = 'negatives_example' # str | negative1 negative2 ...[space separated strings] (optional)
num = 1 # int | num [max 10, default 1] (optional) (default to 1)

try:
    # Word2Vec analogy
    api_response = api_instance.analogy_using_get(access_token, positives, negatives=negatives, num=num)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Word2VecControllerApi->analogy_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Access Token | 
 **positives** | **str**| positive1 positive2 ...[space separated strings] | 
 **negatives** | **str**| negative1 negative2 ...[space separated strings] | [optional] 
 **num** | **int**| num [max 10, default 1] | [optional] [default to 1]

### Return type

[**AnalogyResponseEntity**](AnalogyResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distance_using_get1**
> DistanceResponseEntity distance_using_get1(access_token, word, num=num)

Word2Vec distance

Word2Vec JaWikipedia 2016-9-15 dump.<BR />Response<BR />&nbsp; Github: <a href=\"https://github.com/keigohtr/apitore-response-parent/tree/master/word2vec-response\">word2vec-response</a><BR />&nbsp; Class: com.apitore.banana.response.word2vec.DistanceResponseEntity<BR />

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.Word2VecControllerApi()
access_token = 'access_token_example' # str | Access Token
word = 'word_example' # str | word
num = 1 # int | num [max 10, default 1] (optional) (default to 1)

try:
    # Word2Vec distance
    api_response = api_instance.distance_using_get1(access_token, word, num=num)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Word2VecControllerApi->distance_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Access Token | 
 **word** | **str**| word | 
 **num** | **int**| num [max 10, default 1] | [optional] [default to 1]

### Return type

[**DistanceResponseEntity**](DistanceResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **similarity_using_get**
> SimilarityResponseEntity similarity_using_get(access_token, word1, word2)

Word2Vec similarity

Word2Vec JaWikipedia 2016-9-15 dump.<BR />Response<BR />&nbsp; Github: <a href=\"https://github.com/keigohtr/apitore-response-parent/tree/master/word2vec-response\">word2vec-response</a><BR />&nbsp; Class: com.apitore.banana.response.word2vec.SimilarityResponseEntity<BR />

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.Word2VecControllerApi()
access_token = 'access_token_example' # str | Access Token
word1 = 'word1_example' # str | word1
word2 = 'word2_example' # str | word2

try:
    # Word2Vec similarity
    api_response = api_instance.similarity_using_get(access_token, word1, word2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Word2VecControllerApi->similarity_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Access Token | 
 **word1** | **str**| word1 | 
 **word2** | **str**| word2 | 

### Return type

[**SimilarityResponseEntity**](SimilarityResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vec_distance_using_get**
> VectorDistanceResponseEntity vec_distance_using_get(access_token, vector, num=num)

Word2Vec distance (Vector version)

Word2Vec JaWikipedia 2016-9-15 dump.<BR />Response<BR />&nbsp; Github: <a href=\"https://github.com/keigohtr/apitore-response-parent/tree/master/word2vec-response\">word2vec-response</a><BR />&nbsp; Class: com.apitore.banana.response.word2vec.DistanceResponseEntity<BR />

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.Word2VecControllerApi()
access_token = 'access_token_example' # str | Access Token
vector = [3.4] # list[float] | vector [length 200]
num = 1 # int | num [max 10, default 1] (optional) (default to 1)

try:
    # Word2Vec distance (Vector version)
    api_response = api_instance.vec_distance_using_get(access_token, vector, num=num)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Word2VecControllerApi->vec_distance_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Access Token | 
 **vector** | [**list[float]**](float.md)| vector [length 200] | 
 **num** | **int**| num [max 10, default 1] | [optional] [default to 1]

### Return type

[**VectorDistanceResponseEntity**](VectorDistanceResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wordvector_using_get1**
> WordVectorResponseEntity wordvector_using_get1(access_token, word)

Word2Vec wordvector

Word2Vec JaWikipedia 2016-9-15 dump.<BR />Response<BR />&nbsp; Github: <a href=\"https://github.com/keigohtr/apitore-response-parent/tree/master/word2vec-response\">word2vec-response</a><BR />&nbsp; Class: com.apitore.banana.response.word2vec.WordVectorResponseEntity<BR />

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.Word2VecControllerApi()
access_token = 'access_token_example' # str | Access Token
word = 'word_example' # str | word

try:
    # Word2Vec wordvector
    api_response = api_instance.wordvector_using_get1(access_token, word)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Word2VecControllerApi->wordvector_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Access Token | 
 **word** | **str**| word | 

### Return type

[**WordVectorResponseEntity**](WordVectorResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

