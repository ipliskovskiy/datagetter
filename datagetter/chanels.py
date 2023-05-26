import requests


def send_output(data):
    print(data)


def send_post_data(url, data):
    r = requests.post(url=url, data=data)
    print(str(r.status_code))
    return r


def send_get(url, headers):
    r = requests.get(url, headers=headers)
    return r