# coding: utf-8

"""
    SentencePiece APIs (wikipedia)

    SentencePiece tokenizer (wikipedia).<BR />[Endpoint] https://api.apitore.com/api/37  # noqa: E501

    OpenAPI spec version: 0.0.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "swagger-client"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="SentencePiece APIs (wikipedia)",
    author_email="",
    url="",
    keywords=["Swagger", "SentencePiece APIs (wikipedia)"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    SentencePiece tokenizer (wikipedia).&lt;BR /&gt;[Endpoint] https://api.apitore.com/api/37  # noqa: E501
    """
)
