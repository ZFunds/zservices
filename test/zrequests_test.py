from zrequests.z_requests import send_request

url = "https://staging.zfunds.in/butler/status"
r, rr = send_request('GET', url, [200], {}, {})
print(r, '\n', rr.json())

# todo do a post check also
url = "https://staging.zfunds.in/butler/status"
pr, prr = send_request('GET', url, [200], {}, {})
print(pr, '\n', prr.json())
