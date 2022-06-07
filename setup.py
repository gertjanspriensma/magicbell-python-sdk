# coding: utf-8

"""
    MagicBell REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "magicbell"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.25.3", "six >= 1.10", "python-dateutil"]
REQUIRES.append("aiohttp >= 3.0.0")

setup(
    name=NAME,
    version=VERSION,
    description="MagicBell REST API",
    author="OpenAPI Generator community",
    author_email="team@openapitools.org",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "MagicBell REST API"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description_content_type="text/markdown",
    long_description="""\
    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501
    """,
)
