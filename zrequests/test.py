from zrequests.z_requests import send_request

url = "https://staging.zfunds.in/butler/status"
r, rr = send_request('GET', url, [200], {}, {})
print(r, '\n', rr.json())
