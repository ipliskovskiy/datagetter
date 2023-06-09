def send_data(rules, prefix, key, data):
    result = __format__(rules, prefix, key, data)
    if rules['target'] == 'stdout':
        print_data(result)


def __format__(rules, prefix, key, data):
    format = rules['format']
    result = format.replace("%p", prefix).replace("%k", key).replace("%v", str(data))
    return result


def print_data(result):
    print(result)