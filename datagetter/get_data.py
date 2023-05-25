import requests

def get_data(target):
    if target['type'] == 'math':
        return get_result_math(target['expression'])
    if target['type'] == 'request':
        return request_data(target['headers'], target['url'], target['type_result'])


def get_result_math(exp):
    return eval(exp)


def request_data(headers, url, type_result):
    data = None
    r = requests.get(url, headers=headers)
    if type_result == 'json':
        data = r.json()
    return data


def get_result_json(url, headers):
    r = requests.get(url, headers=headers)
    data_json = r.json()
    return data_json
