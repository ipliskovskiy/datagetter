import subprocess
import time
from get_data import get_data
from send_data import send_data


def __process__(groups):
    count = 0
    while True:
        for group in groups:
            prefix = groups[group]['prefix']
            for metrics in groups[group]['metrics']:
                timeoffset = groups[group]['metrics'][metrics]['time']
                if count % timeoffset == 0:
                    rules = groups[group]['metrics'][metrics]['sending']
                    result = get_data(groups[group]['metrics'][metrics]['target'])
                    send_data(rules, prefix, metrics, result)
        time.sleep(1)
        count = count + 1
        if count >= 59: count = 0


def start(groups):
    __process__(groups)
