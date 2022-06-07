# coding: utf-8

"""
    MagicBell REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import magicbell
from magicbell.models.wrapped_user import WrappedUser  # noqa: E501
from magicbell.rest import ApiException


class TestWrappedUser(unittest.TestCase):
    """WrappedUser unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test WrappedUser
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # model = magicbell.models.wrapped_user.WrappedUser()  # noqa: E501
        if include_optional:
            return WrappedUser(
                user=magicbell.models.user.User(
                    external_id="",
                    email="",
                    first_name="",
                    last_name="",
                    custom_attributes=magicbell.models.custom_attributes.custom_attributes(),
                )
            )
        else:
            return WrappedUser()

    def testWrappedUser(self):
        """Test WrappedUser"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
