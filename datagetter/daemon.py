import subprocess
import time
from get_data import get_data
from send_data import send_data
from Config import *
from Metrics import *


def __process__(timemap):
    count = 1
    while True:
        for m in timemap:
            if (count % timemap[m]) == 0:
                print("count = " + str(count))
                m.get_data()
        time.sleep(1)
        count += 1


def start(config):
    __process__(config.get_timemap())
