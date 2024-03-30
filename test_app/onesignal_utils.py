from onesignal_sdk.client import Client
from django.conf import settings

def send_push_notification(player_ids, message):
    client = Client(user_auth_key=settings.ONESIGNAL_API_KEY)
    notification_data = {
        'contents': {'en': message},
        'include_player_ids': player_ids
    }
    response = client.send_notification(notification_data)
    return response
