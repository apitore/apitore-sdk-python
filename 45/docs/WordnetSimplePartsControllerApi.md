# swagger_client.WordnetSimplePartsControllerApi

All URIs are relative to *https://api.apitore.com/api/45*

Method | HTTP request | Description
------------- | ------------- | -------------
[**simple_translation_using_get**](WordnetSimplePartsControllerApi.md#simple_translation_using_get) | **GET** /wordnet-simple/translation | Simple WordNet WebAPI. Return translation words.


# **simple_translation_using_get**
> LinksResponseEntity simple_translation_using_get(access_token, word, pos=pos)

Simple WordNet WebAPI. Return translation words.

Japanese WordNet.<BR />Response<BR />&nbsp; Github: <a href=\"https://github.com/keigohtr/apitore-response-parent/tree/master/wordnet-response\">wordnet-response</a><BR />&nbsp; Class: com.apitore.banana.response.de.sciss.ws4j.LinksResponseEntity<BR />

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WordnetSimplePartsControllerApi()
access_token = 'access_token_example' # str | Access Token
word = 'word_example' # str | Word
pos = 'n,v,a,r' # str | Part-of-speech. You can specify several pos by csv format. [n:noun,v:verb,a:adjective,r:adverb] (optional) (default to n,v,a,r)

try:
    # Simple WordNet WebAPI. Return translation words.
    api_response = api_instance.simple_translation_using_get(access_token, word, pos=pos)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordnetSimplePartsControllerApi->simple_translation_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Access Token | 
 **word** | **str**| Word | 
 **pos** | **str**| Part-of-speech. You can specify several pos by csv format. [n:noun,v:verb,a:adjective,r:adverb] | [optional] [default to n,v,a,r]

### Return type

[**LinksResponseEntity**](LinksResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

