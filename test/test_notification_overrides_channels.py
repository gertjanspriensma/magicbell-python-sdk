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
from magicbell.models.notification_overrides_channels import (
    NotificationOverridesChannels,
)  # noqa: E501
from magicbell.rest import ApiException


class TestNotificationOverridesChannels(unittest.TestCase):
    """NotificationOverridesChannels unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test NotificationOverridesChannels
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # model = magicbell.models.notification_overrides_channels.NotificationOverridesChannels()  # noqa: E501
        if include_optional:
            return NotificationOverridesChannels(
                in_app=magicbell.models.channel_overrides.ChannelOverrides(
                    title="",
                    content="",
                    action_url="",
                ),
                email=magicbell.models.channel_overrides.ChannelOverrides(
                    title="",
                    content="",
                    action_url="",
                ),
                web_push=magicbell.models.channel_overrides.ChannelOverrides(
                    title="",
                    content="",
                    action_url="",
                ),
                mobile_push=magicbell.models.channel_overrides.ChannelOverrides(
                    title="",
                    content="",
                    action_url="",
                ),
            )
        else:
            return NotificationOverridesChannels()

    def testNotificationOverridesChannels(self):
        """Test NotificationOverridesChannels"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
