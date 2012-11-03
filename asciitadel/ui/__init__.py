
import logging
import curses
import traceback
from threading import Thread
from time import sleep

from top_bar import TopBar
from main_area import MainArea
from right_bar import RightBar
from bottom_bar import BottomBar

log = logging.getLogger(__name__)

class Interface(Thread):
    def __init__(self, data):
        Thread.__init__(self)
        self.data = data
        self.terminated = False
        self.components = set()

    def stop(self):
        self.terminated = True
        self.terminate()

    def initialize(self):
        self.scr = curses.initscr()
        curses.noecho()
        self.scr.keypad(1)
        curses.cbreak()
        curses.start_color()
        curses.use_default_colors()
        curses.init_pair(1, curses.COLOR_RED, -1)
        curses.init_pair(2, curses.COLOR_GREEN, -1)
        curses.init_pair(3, curses.COLOR_BLUE, -1)

        self.top_bar = TopBar(self.data)
        self.components.add(self.top_bar)
        
        self.main_area = MainArea(self.data)
        self.components.add(self.main_area)

        self.right_bar = RightBar(self.data)
        self.components.add(self.right_bar)
        
        self.bottom_bar = BottomBar(self.data)
        self.components.add(self.bottom_bar)

        self.draw_all()

    def draw_all(self):
        for component in self.components:
            component.draw()


    def terminate(self):
        self.scr.keypad(0)
        curses.echo()
        curses.nocbreak()
        curses.endwin()

    def run(self):
        self.initialize()
        sleep(1)
        while not self.terminated:
            try:
                for component in self.components:
                    if component.has_changed():
                        component.populate()
                        component.refresh()
                sleep(0.1)
            except:
                self.stop()
                traceback.print_exc()

