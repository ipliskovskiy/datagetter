import yaml


def read_config():
    with open("config/datagetter.yml", "r") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)


class Config:
    def __init__(self, yaml):
        self.yaml = yaml
        self.groups = self.yaml['groups']


    def getgroups(self):
        return self.groups
