import belfry_magicbell


class TestCreatePushSubscription:
    async def test_response_is_parsed_properly(self, magicbell_client: belfry_magicbell.MagicBell):
        response = await magicbell_client.push_subscriptions.create_push_subscription(
            external_id="example_id",
            wrapped_push_subscription=belfry_magicbell.WrappedPushSubscription(
                push_subscription=belfry_magicbell.PushSubscription(
                    device_token="example_token", platform="ios"
                )
            ),
        )

        assert isinstance(response, belfry_magicbell.WrappedPushSubscription)

        assert response.push_subscription.device_token == "example_token"


class TestDeletePushSubscription:
    async def test_response_is_parsed_properly(self, magicbell_client: belfry_magicbell.MagicBell):
        await magicbell_client.push_subscriptions.delete_push_subscription(
            external_id="example_id", device_token="example_token"
        )
