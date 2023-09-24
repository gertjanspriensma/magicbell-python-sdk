import pytest

import belfry_magicbell
from magicbell import errors


class TestCreateNotification:
    @pytest.mark.parametrize("body", [{}, {"notification": {}}])
    async def test_validation_error_is_handled_properly(
        self, magicbell_client: belfry_magicbell.MagicBell, body: dict
    ):
        with pytest.raises(errors.MagicBellHTTPClientError) as exc_info:
            await magicbell_client.realtime.create_notification(body)

        assert exc_info.value.status_code == 422

    async def test_response_is_parsed(self, magicbell_client: belfry_magicbell.MagicBell):
        response = await magicbell_client.realtime.create_notification(
            belfry_magicbell.WrappedNotification(
                notification=belfry_magicbell.Notification(
                    title="Test notification",
                    recipients=[belfry_magicbell.Recipient(email="foo@bar.com")],
                    overrides=belfry_magicbell.NotificationOverrides(
                        providers=belfry_magicbell.NotificationProvidersOverrides(
                            mailgun={"template": "test-template"}
                        )
                    ),
                )
            )
        )

        assert isinstance(response, belfry_magicbell.WrappedCreatedNotificationBroadcast)
        assert response.notification.id is not None
