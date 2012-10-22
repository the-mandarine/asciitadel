
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
        self.data.set("c.life.max", 100)
        self.data.set("c.life", self.data.get("c.life.max"))

        self.data.set("c.mana.max", 100)
        self.data.set("c.mana", self.data.get("c.mana.max"))

        while not self.terminated:
            self.data.add("c.life", -1)
            self.data.add("c.mana", -2)
            sleep(1)

