import requests


def get_data(target):
    if target['type'] == 'math':
        return get_result_math(target['expression'])


def get_result_math(exp):
    return eval(exp)


def get_result_json(url):
    r = requests.get(url, headers=headers)
    data_json = r.json()
    return data_json
