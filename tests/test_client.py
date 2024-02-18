"""Tests for the MagicBell client.

The tests in this file aren't meant to be exhaustive over all the API endpoints, but rather to
ensure that the client handles expected responses as well as errors correctly.
"""
import pytest
from httpx._client import ClientState

import belfry_magicbell
from belfry_magicbell import errors
from belfry_magicbell.configuration import Configuration


class TestAuthenticationErrorHandling:
    @pytest.fixture(autouse=True)
    def clear_configuration(self, configuration: Configuration):
        configuration.api_key = None
        configuration.api_secret = None
        configuration.user_jwt = None

    async def test_when_api_key_isnt_sent_error_is_handled(
        self, magicbell_client: belfry_magicbell.MagicBell
    ):
        with pytest.raises(errors.MagicBellHTTPClientError) as exc_info:
            await magicbell_client.realtime.create_notification(
                belfry_magicbell.WrappedNotification(
<<<<<<< HEAD
                    notification=belfry_magicbell.Notification(
=======
                    broadcast=belfry_magicbell.Notification(
>>>>>>> 9e3c9fc6da0445ab7e73a859355319eae919dae5
                        title="Test",
                        recipients=[belfry_magicbell.Recipient(email="test@example.com")],
                    )
                )
            )

        assert exc_info.value.status_code == 403
        assert exc_info.value.json()["errors"][0]["code"] == "api_key_not_provided"

    async def test_when_api_secret_isnt_sent_error_is_handled(
        self, magicbell_client: belfry_magicbell.MagicBell, configuration: Configuration
    ):
        configuration.api_key = "my-api-key"

        with pytest.raises(errors.MagicBellHTTPClientError) as exc_info:
            await magicbell_client.realtime.create_notification(
                belfry_magicbell.WrappedNotification(
<<<<<<< HEAD
                    notification=belfry_magicbell.Notification(
=======
                    broadcast=belfry_magicbell.Notification(
>>>>>>> 9e3c9fc6da0445ab7e73a859355319eae919dae5
                        title="Test",
                        recipients=[belfry_magicbell.Recipient(email="test@example.com")],
                    )
                )
            )

        assert exc_info.value.status_code == 403
        assert exc_info.value.json()["errors"][0]["code"] == "api_secret_not_provided"

    async def test_when_user_jwt_isnt_sent_error_is_handled(
        self, magicbell_client: belfry_magicbell.MagicBell
    ):
        with pytest.raises(errors.MagicBellHTTPClientError) as exc_info:
            await magicbell_client.projects.list_projects(42)

        assert exc_info.value.status_code == 403
        assert exc_info.value.json()["errors"][0]["code"] == "forbidden"


class TestConnectionMethods:
    async def test_connect_sets_up_the_client(self, configuration: Configuration):
        client = belfry_magicbell.MagicBell(configuration)
        assert client.http_client._state == ClientState.UNOPENED

        await client.connect()

        assert client.http_client._state == ClientState.OPENED

    async def test_disconnect_closes_the_client(self, configuration: Configuration):
        client = belfry_magicbell.MagicBell(configuration)
        await client.connect()
        assert client.http_client._state == ClientState.OPENED

        await client.disconnect()
        assert client.http_client._state == ClientState.CLOSED


class TestContextManager:
    async def test_state_is_changed_correctly(self, configuration: Configuration):
        client = belfry_magicbell.MagicBell(configuration)
        assert client.http_client._state == ClientState.UNOPENED

        async with client:
            assert client.http_client._state == ClientState.OPENED

        assert client.http_client._state == ClientState.CLOSED
