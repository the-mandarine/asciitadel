import os

class DataHandler(object):
    def __init__(self, data, config):
        self.data = data
        self.conf = config
        self.monitored_keys = {}
        self.changed_keys = set()

    def monitore(self, bundle, key):
        if not bundle in self.monitored_keys:
            self.monitored_keys[bundle] = set()
        if type(key) is str:
            self.monitored_keys[bundle].add(key)
        elif type(key) in (list, tuple, set):
            for item in key:
                self.monitore(bundle, item)
        

    def change(self, key):
        self.changed_keys.add(key)

    def initialize(self):
        pass

    def set(self, key, value):
        self.change(key)
        self.data.data[key] = value

    def add(self, key, value):
        self.change(key)
        self.data.data[key] += value

    def get(self, key):
        value = self.data.data[key]
        return value

    def bundle_has_changed(self, bundle):
        monitored_changed = self.changed_keys & self.monitored_keys[bundle]
        if monitored_changed:
            for key in monitored_changed:
                self.changed_keys.remove(key)
            return True
        return False
        

class SharedData(object):
    def __init__(self):
        self.data = {}

