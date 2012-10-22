
from time import sleep


class Game(object):
    def __init__(self, data):
        self.data = data
        self.terminated = False
        self.initialize()

    def __del__(self):
        self.stop()

    def initialize(self):
        pass

    def stop(self):
        self.terminated = True

    def run(self):
        sleep(1)
        self.data.set("c.life", 100)
        while not self.terminated:
            self.data.add("c.life", -1)
            sleep(0.5)

