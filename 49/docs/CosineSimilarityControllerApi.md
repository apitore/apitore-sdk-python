# swagger_client.CosineSimilarityControllerApi

All URIs are relative to *https://api.apitore.com/api/49*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vec_vec_using_post**](CosineSimilarityControllerApi.md#vec_vec_using_post) | **POST** /cosine-similarity/vec-vec | Calclate similarity
[**vec_word_using_post**](CosineSimilarityControllerApi.md#vec_word_using_post) | **POST** /cosine-similarity/vec-word | Calclate similarity by word


# **vec_vec_using_post**
> SimilarityResponseEntity vec_vec_using_post(access_token, req)

Calclate similarity

Cosine similarity.<BR />Response<BR />&nbsp; Github: <a href=\"https://github.com/keigohtr/apitore-response-parent/tree/master/clustering-response\">clustering-response</a><BR />&nbsp; Class: com.apitore.banana.response.clustering.SimilarityResponseEntity<BR />

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CosineSimilarityControllerApi()
access_token = 'access_token_example' # str | Access Token
req = swagger_client.VecvecRequestEntity() # VecvecRequestEntity | Input two vectors; vec1, vec2

try:
    # Calclate similarity
    api_response = api_instance.vec_vec_using_post(access_token, req)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CosineSimilarityControllerApi->vec_vec_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Access Token | 
 **req** | [**VecvecRequestEntity**](VecvecRequestEntity.md)| Input two vectors; vec1, vec2 | 

### Return type

[**SimilarityResponseEntity**](SimilarityResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vec_word_using_post**
> SimilarityResponseEntity vec_word_using_post(access_token, req)

Calclate similarity by word

Cosine similarity.<BR />Response<BR />&nbsp; Github: <a href=\"https://github.com/keigohtr/apitore-response-parent/tree/master/clustering-response\">clustering-response</a><BR />&nbsp; Class: com.apitore.banana.response.clustering.SimilarityResponseEntity<BR />

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CosineSimilarityControllerApi()
access_token = 'access_token_example' # str | Access Token
req = swagger_client.VecwordRequestEntity() # VecwordRequestEntity | Input vector and word. Word is transformed to wordvector.

try:
    # Calclate similarity by word
    api_response = api_instance.vec_word_using_post(access_token, req)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CosineSimilarityControllerApi->vec_word_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Access Token | 
 **req** | [**VecwordRequestEntity**](VecwordRequestEntity.md)| Input vector and word. Word is transformed to wordvector. | 

### Return type

[**SimilarityResponseEntity**](SimilarityResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

