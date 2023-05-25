from Config import *
from daemon import start


if __name__ == '__main__':
    config = Config(read_config())
    start(config)

