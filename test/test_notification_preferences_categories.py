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
from magicbell.models.notification_preferences_categories import (
    NotificationPreferencesCategories,
)  # noqa: E501
from magicbell.rest import ApiException


class TestNotificationPreferencesCategories(unittest.TestCase):
    """NotificationPreferencesCategories unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test NotificationPreferencesCategories
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # model = magicbell.models.notification_preferences_categories.NotificationPreferencesCategories()  # noqa: E501
        if include_optional:
            return NotificationPreferencesCategories(
                categories=magicbell.models.notification_preferences.NotificationPreferences(
                    new_message=magicbell.models.user_preferences_category.UserPreferencesCategory(
                        email=True,
                        in_app=True,
                        mobile_push=True,
                        web_push=True,
                    ),
                )
            )
        else:
            return NotificationPreferencesCategories()

    def testNotificationPreferencesCategories(self):
        """Test NotificationPreferencesCategories"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
