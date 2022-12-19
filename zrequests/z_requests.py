import requests as sync_req
from zrequests import logger
from zrequests.setting import Setting
import time
import json as f_json


def verify_success_text(s_text, response: sync_req.Response):
    if isinstance(s_text, dict):
        r_json = f_json.loads(response.text)
        for k, v in s_text.items():
            assert (k in r_json and v == r_json[k])
            continue
        return

    if isinstance(s_text, str):
        assert s_text in response.text
        return

    raise AssertionError


# todo remove sensitive info from url
def send_request(method, url, s_codes: list, params, headers, tag='N', json=None, data=None, count=0, sleep=False,
                 s_text=None):
    response = None
    try:
        response = sync_req.request(method, url=url, params=params, data=data, headers=headers, json=json)
        assert response.status_code in s_codes

        if not s_text:
            return True, response

        verify_success_text(s_text, response)
        return True, response

    except Exception as e:
        logger.warning(f'[ZREQUEST] [{tag}][{count}] {url}, e={e}, r={response}')
        count += 1
        if sleep:
            time.sleep(2 ** count)
        if count < Setting.MAX_RETRY:
            return send_request(method, url, s_codes, params, headers, tag, json, data, count, sleep, s_text)

        logger.error(f'[ZREQUEST] [{tag}] Failed to get proper response for {url} r={response},', exc_info=True)
        return False, response
