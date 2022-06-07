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
from magicbell.models.channel_overrides import ChannelOverrides  # noqa: E501
from magicbell.rest import ApiException


class TestChannelOverrides(unittest.TestCase):
    """ChannelOverrides unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ChannelOverrides
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # model = magicbell.models.channel_overrides.ChannelOverrides()  # noqa: E501
        if include_optional:
            return ChannelOverrides(title="", content="", action_url="")
        else:
            return ChannelOverrides()

    def testChannelOverrides(self):
        """Test ChannelOverrides"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
