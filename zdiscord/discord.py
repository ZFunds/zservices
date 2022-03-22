import requests
from zdiscord import logger
import time


def send_notification(url, user_name, channel, payload, retry_sleep=1):
    response = None
    url = url
    headers = {'Content-Type': 'application/json'}

    data = {
        "content": payload, "username": user_name
    }

    try:
        response = requests.post(url=url, data=data, headers=headers)
    except Exception as e:
        logger.warning(f'[DISCORD] Unable to send notification, error={e}')
        time.sleep(retry_sleep)
        response = requests.post(url=url, data=data, headers=headers)

    return response
