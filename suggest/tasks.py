from celery import shared_task
from django.conf import settings

import requests

@shared_task
def send_notification(chatid, message):
    bot_token = settings.TELEGRAM_BOT_TOKEN
    chat_id = chatid # settings.TELEGRAM_CHAT_ID
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    try:
        response = requests.post(
            url,
            json={
                'chat_id': chat_id,
                'text': message,
                'parse_mode': 'HTML'
            },
            timeout=10
        )
        response.raise_for_status()
        return True
    except Exception as e:
        return False