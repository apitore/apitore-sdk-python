# coding: utf-8

"""
    Url2Label by tfidf APIs

    Url to label by tfidf of contents.<BR />[Endpoint] https://api.apitore.com/api/20  # noqa: E501

    OpenAPI spec version: 0.0.1
    
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
    description="Url2Label by tfidf APIs",
    author_email="",
    url="",
    keywords=["Swagger", "Url2Label by tfidf APIs"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    Url to label by tfidf of contents.&lt;BR /&gt;[Endpoint] https://api.apitore.com/api/20  # noqa: E501
    """
)
