# swagger-client
Japanese sentiment analyzer. (tokenized by SentencePiece)<BR />[Endpoint] https://api.apitore.com/api/39

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.0.1
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SentimentV2ControllerApi(swagger_client.ApiClient(configuration))
access_token = 'access_token_example' # str | Access Token
text = 'text_example' # str | text

try:
    # Sentiment predict
    api_response = api_instance.predict_using_get(access_token, text)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SentimentV2ControllerApi->predict_using_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.apitore.com/api/39*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*SentimentV2ControllerApi* | [**predict_using_get**](docs/SentimentV2ControllerApi.md#predict_using_get) | **GET** /sentiment-v2/predict | Sentiment predict


## Documentation For Models

 - [SentimentEntity](docs/SentimentEntity.md)
 - [SentimentResponseEntity](docs/SentimentResponseEntity.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author


