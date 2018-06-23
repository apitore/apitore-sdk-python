# swagger_client.WordnetControllerApi

All URIs are relative to *https://api.apitore.com/api/46*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sensebysynset_using_get**](WordnetControllerApi.md#sensebysynset_using_get) | **GET** /wordnet/sense/bysynset | WordNet WebAPI. Return Sense object.
[**sensebywordid_using_get**](WordnetControllerApi.md#sensebywordid_using_get) | **GET** /wordnet/sense/bywordid | WordNet WebAPI. Return Sense object.
[**synlinkby_synset_using_get**](WordnetControllerApi.md#synlinkby_synset_using_get) | **GET** /wordnet/synlink/bysynset | WordNet WebAPI. Return SynLink object.
[**synsetby_name_using_get**](WordnetControllerApi.md#synsetby_name_using_get) | **GET** /wordnet/synset/byname | WordNet WebAPI. Return Synset object.
[**synsetbysynset_using_get**](WordnetControllerApi.md#synsetbysynset_using_get) | **GET** /wordnet/synset/bysynset | WordNet WebAPI. Return Synset object.
[**synsetdefbysynset_using_get**](WordnetControllerApi.md#synsetdefbysynset_using_get) | **GET** /wordnet/synsetdef/bysynset | WordNet WebAPI. Return SynsetDef object.
[**wordbyid_using_get**](WordnetControllerApi.md#wordbyid_using_get) | **GET** /wordnet/word/bywordid | WordNet WebAPI. Return Word object.
[**wordbylemma_using_get**](WordnetControllerApi.md#wordbylemma_using_get) | **GET** /wordnet/word/bylemma | WordNet WebAPI. Return Word object.


# **sensebysynset_using_get**
> SenseResponseEntity sensebysynset_using_get(access_token, synset, lang=lang)

WordNet WebAPI. Return Sense object.

Japanese WordNet.<BR />Response<BR />&nbsp; Github: <a href=\"https://github.com/keigohtr/apitore-response-parent/tree/master/wordnet-response\">wordnet-response</a><BR />

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WordnetControllerApi()
access_token = 'access_token_example' # str | Access Token
synset = 'synset_example' # str | Synset
lang = 'jpn' # str | Language. [jpn:japanese,eng:english] (optional) (default to jpn)

try:
    # WordNet WebAPI. Return Sense object.
    api_response = api_instance.sensebysynset_using_get(access_token, synset, lang=lang)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordnetControllerApi->sensebysynset_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Access Token | 
 **synset** | **str**| Synset | 
 **lang** | **str**| Language. [jpn:japanese,eng:english] | [optional] [default to jpn]

### Return type

[**SenseResponseEntity**](SenseResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sensebywordid_using_get**
> SenseResponseEntity sensebywordid_using_get(access_token, wordid)

WordNet WebAPI. Return Sense object.

Japanese WordNet.<BR />Response<BR />&nbsp; Github: <a href=\"https://github.com/keigohtr/apitore-response-parent/tree/master/wordnet-response\">wordnet-response</a><BR />

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WordnetControllerApi()
access_token = 'access_token_example' # str | Access Token
wordid = 56 # int | Word ID

try:
    # WordNet WebAPI. Return Sense object.
    api_response = api_instance.sensebywordid_using_get(access_token, wordid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordnetControllerApi->sensebywordid_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Access Token | 
 **wordid** | **int**| Word ID | 

### Return type

[**SenseResponseEntity**](SenseResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **synlinkby_synset_using_get**
> SynlinkResponseEntity synlinkby_synset_using_get(access_token, synset, link=link)

WordNet WebAPI. Return SynLink object.

Japanese WordNet.<BR />Response<BR />&nbsp; Github: <a href=\"https://github.com/keigohtr/apitore-response-parent/tree/master/wordnet-response\">wordnet-response</a><BR />

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WordnetControllerApi()
access_token = 'access_token_example' # str | Access Token
synset = 'synset_example' # str | Synset
link = 'syns' # str | Link. You can specify several link by csv format. [also, syns, hype, inst, hypo, hasi, mero, mmem, msub, mprt, holo, hmem, hsub, hprt, attr, sim, enta, caus, dmnc, dmnu, dmnr, dmtc, dmtu, dmtr, ants] (optional) (default to syns)

try:
    # WordNet WebAPI. Return SynLink object.
    api_response = api_instance.synlinkby_synset_using_get(access_token, synset, link=link)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordnetControllerApi->synlinkby_synset_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Access Token | 
 **synset** | **str**| Synset | 
 **link** | **str**| Link. You can specify several link by csv format. [also, syns, hype, inst, hypo, hasi, mero, mmem, msub, mprt, holo, hmem, hsub, hprt, attr, sim, enta, caus, dmnc, dmnu, dmnr, dmtc, dmtu, dmtr, ants] | [optional] [default to syns]

### Return type

[**SynlinkResponseEntity**](SynlinkResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **synsetby_name_using_get**
> SynsetResponseEntity synsetby_name_using_get(access_token, name, pos)

WordNet WebAPI. Return Synset object.

Japanese WordNet.<BR />Response<BR />&nbsp; Github: <a href=\"https://github.com/keigohtr/apitore-response-parent/tree/master/wordnet-response\">wordnet-response</a><BR />

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WordnetControllerApi()
access_token = 'access_token_example' # str | Access Token
name = 'name_example' # str | Name
pos = 'pos_example' # str | Part-of-speech. [n:noun,v:verb,a:adjective,r:adverb]

try:
    # WordNet WebAPI. Return Synset object.
    api_response = api_instance.synsetby_name_using_get(access_token, name, pos)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordnetControllerApi->synsetby_name_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Access Token | 
 **name** | **str**| Name | 
 **pos** | **str**| Part-of-speech. [n:noun,v:verb,a:adjective,r:adverb] | 

### Return type

[**SynsetResponseEntity**](SynsetResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **synsetbysynset_using_get**
> SynsetResponseEntity synsetbysynset_using_get(access_token, synset)

WordNet WebAPI. Return Synset object.

Japanese WordNet.<BR />Response<BR />&nbsp; Github: <a href=\"https://github.com/keigohtr/apitore-response-parent/tree/master/wordnet-response\">wordnet-response</a><BR />

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WordnetControllerApi()
access_token = 'access_token_example' # str | Access Token
synset = 'synset_example' # str | Synset

try:
    # WordNet WebAPI. Return Synset object.
    api_response = api_instance.synsetbysynset_using_get(access_token, synset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordnetControllerApi->synsetbysynset_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Access Token | 
 **synset** | **str**| Synset | 

### Return type

[**SynsetResponseEntity**](SynsetResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **synsetdefbysynset_using_get**
> SynsetDefResponseEntity synsetdefbysynset_using_get(access_token, synset, lang)

WordNet WebAPI. Return SynsetDef object.

Japanese WordNet.<BR />Response<BR />&nbsp; Github: <a href=\"https://github.com/keigohtr/apitore-response-parent/tree/master/wordnet-response\">wordnet-response</a><BR />

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WordnetControllerApi()
access_token = 'access_token_example' # str | Access Token
synset = 'synset_example' # str | Synset
lang = 'lang_example' # str | Language. [jpn:japanese,eng:english]

try:
    # WordNet WebAPI. Return SynsetDef object.
    api_response = api_instance.synsetdefbysynset_using_get(access_token, synset, lang)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordnetControllerApi->synsetdefbysynset_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Access Token | 
 **synset** | **str**| Synset | 
 **lang** | **str**| Language. [jpn:japanese,eng:english] | 

### Return type

[**SynsetDefResponseEntity**](SynsetDefResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wordbyid_using_get**
> WordResponseEntity wordbyid_using_get(access_token, wordid)

WordNet WebAPI. Return Word object.

Japanese WordNet.<BR />Response<BR />&nbsp; Github: <a href=\"https://github.com/keigohtr/apitore-response-parent/tree/master/wordnet-response\">wordnet-response</a><BR />

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WordnetControllerApi()
access_token = 'access_token_example' # str | Access Token
wordid = 56 # int | Word ID

try:
    # WordNet WebAPI. Return Word object.
    api_response = api_instance.wordbyid_using_get(access_token, wordid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordnetControllerApi->wordbyid_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Access Token | 
 **wordid** | **int**| Word ID | 

### Return type

[**WordResponseEntity**](WordResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wordbylemma_using_get**
> WordResponseEntity wordbylemma_using_get(access_token, lemma, pos=pos)

WordNet WebAPI. Return Word object.

Japanese WordNet.<BR />Response<BR />&nbsp; Github: <a href=\"https://github.com/keigohtr/apitore-response-parent/tree/master/wordnet-response\">wordnet-response</a><BR />

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WordnetControllerApi()
access_token = 'access_token_example' # str | Access Token
lemma = 'lemma_example' # str | Lemma
pos = 'n,v,a,r' # str | Part-of-speech. You can specify several pos by csv format. [n:noun,v:verb,a:adjective,r:adverb] (optional) (default to n,v,a,r)

try:
    # WordNet WebAPI. Return Word object.
    api_response = api_instance.wordbylemma_using_get(access_token, lemma, pos=pos)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WordnetControllerApi->wordbylemma_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| Access Token | 
 **lemma** | **str**| Lemma | 
 **pos** | **str**| Part-of-speech. You can specify several pos by csv format. [n:noun,v:verb,a:adjective,r:adverb] | [optional] [default to n,v,a,r]

### Return type

[**WordResponseEntity**](WordResponseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

