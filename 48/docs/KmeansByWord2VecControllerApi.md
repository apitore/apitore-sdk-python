# swagger_client.KmeansByWord2VecControllerApi

All URIs are relative to *https://api.apitore.com/api/48*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cluster_using_post**](KmeansByWord2VecControllerApi.md#cluster_using_post) | **POST** /kmeans-wordvector/cluster | Words clustering by word2vec


# **cluster_using_post**
> ClusterResponseEntity cluster_using_post(access_token, req)

Words clustering by word2vec

kmeans clustering by word2vec.<BR />Response<BR />&nbsp; Github: <a href=\"https://github.com/keigohtr/apitore-response-parent/tree/master/clustering-response\">clustering-response</a><BR />&nbsp; Class: com.apitore.banana.response.clustering.ClusterResponseEntity<BR />

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KmeansByWord2VecControllerApi()
access_token = 'access_token_example' # str | Access Token
req = swagger_client.ClusteringRequestEntity() # ClusteringRequestEntity | Clustering request entity

try:
    # Words clustering by word2vec
    api_response = api_instance.cluster_using_post(access_token, req)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KmeansByWord2VecControllerApi->cluster_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Access Token | 
 **req** | [**ClusteringRequestEntity**](ClusteringRequestEntity.md)| Clustering request entity | 

### Return type

[**ClusterResponseEntity**](ClusterResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

