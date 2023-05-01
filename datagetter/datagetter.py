from get_config import read_config
from get_config import Config
from daemon import start


if __name__ == '__main__':
    config = Config(read_config())
    start(config.groups)
