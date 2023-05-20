import yaml
from Metrics import Metrics


def read_config():
    with open("config/custom.yml", "r") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)


class Config:
    def __init__(self, yaml):
        self.timemap = self.__mapper__(yaml['groups'])


    def __mapper__(self, groups):
        self.timemap = {}
        for group in groups:
            for m in groups[group]['metrics']:
                metrics = Metrics(groups[group]['metrics'], groups[group]['prefix'])
                time = groups[group]['metrics'][m]['time']
                self.timemap[metrics] = time
        timemap = self.__sort__(self.timemap)
        return timemap


    def __sort__(self, timemap):
        sorted_values = sorted(timemap.values())
        new_sorted_dict = {}
        for i in sorted_values:
            for k in timemap.keys():
                if timemap[k] == i:
                    new_sorted_dict[k] = timemap[k]
                    continue
        return new_sorted_dict


    def get_timemap(self):
        return self.timemap