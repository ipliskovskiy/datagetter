import chanels


class Metrics:
    def __init__(self, params, prefix):
        self.params = params
        # self.params = group
        self.prefix = prefix

        self.status_last_exec = None
        self.error_count = 0
        self.success_count = 0
        self.hold = False
        # self.name = None
        # self.target_type = None
        # self.target_headers = None
        # self.target_url = None
        # self.target_data = None
        # self.target_expression = None
        # self.sending_target = None
        # self.sending_url = None
        # self.sending_json = None
        # self.sending_metrics = {}
        # self.sending_metrics_name = None
        # self.sending_metrics_calc = None
        # self.senfing_format = None
        # self.time = None

    def get_data(self):
        for metrics_name in self.params:
            result = self.__exec_target__(self.params[metrics_name]['target'])
            data = self.__prepare_data__(self.params[metrics_name]['sending'], metrics_name, result)
            self.__send_data__(self.params[metrics_name]['sending'], data)

    def __exec_target__(self, target):
        if target["type"] == 'math':
            return self.__execute_math__(target['expression'])
        if target["type"] == 'request':
            return self.__execute_request__(target)

    def __execute_math__(self, expression):
        return eval(expression)

    def __execute_request__(self, target):
        result = chanels.send_get(target['url'], target['headers'])
        if result.status_code == 200:
            self.__successful__()
            return result
        else:
            self.__failure__()
        return None

    def __prepare_data__(self, send_params, metrics_name ,result):
        data = ''
        if send_params.get('keys_json'):
            data = self.__prepare_data_json__(send_params, metrics_name, result)
        elif send_params.get('calc'):
            data = send_params['calc'].replace("%v", str(result))
            data = eval(data)
            data = self.__format_string__(send_params, metrics_name, data)
        else:
            data = self.__format_string__(send_params, metrics_name, result)
        return data

    def __prepare_data_json__(self, send_params, metrics_name, result):
        j = result.json()
        data = ''
        for key in send_params['keys_json']:
            if send_params['keys_json'][key].get('calc'):
                r = send_params['keys_json'][key]['calc'].replace("%v", str(j[key]))
                r = eval(r)
                r = self.__format_string_json__(send_params, metrics_name, r, key)
                data = data + r + '\n'
        return data

    def __format_string_json__(self, send_params, metrics_name ,result, json_key):
        format = send_params['format']
        return format.replace("%p", self.prefix)\
            .replace("%k", metrics_name)\
            .replace("%v", str(result))\
            .replace("%n", json_key)

    def __format_string__(self, send_params, metrics_name ,result):
        format = send_params['format']
        return format.replace("%p", self.prefix)\
            .replace("%k", metrics_name)\
            .replace("%v", str(result))

    def __send_data__(self, send_params, data):
        if send_params['target'] == 'stdout':
            chanels.send_output(data)
        if send_params['target'] == 'post':
            chanels.send_post_data(send_params["url"], data)

    def __successful__(self):
        self.success_count += 1
        self.status_last_exec = True
        self.error_count = 0

    def __failure__(self):
        self.success_count = 0
        self.status_last_exec = False
        self.error_count += 1