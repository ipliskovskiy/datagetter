from Config import *
from daemon import start


if __name__ == '__main__':
    config = Config(read_config())
    for metrics in config.get_timemap():
        metrics.get_data()
    exit(1)

    # start(config.groups)
