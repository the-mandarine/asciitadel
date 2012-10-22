
from ui_window import UIWindow
import curses

MONITORED_ITEMS = ("c.life", "c.life.max", "c.mana", "c.mana.max")
COMPONENT_KEY = "right_bar"

class RightBar(UIWindow):
    def __init__(self, data):
        UIWindow.__init__(self, COMPONENT_KEY, data, MONITORED_ITEMS, -3, 7, 3, -7)

    def populate(self):
        self.draw_health()
        self.draw_mana()

    def draw_health(self):
        c_life = self.data.get("c.life")
        c_life_max = self.data.get("c.life.max")
        scaled_c_life = self.__get_col_size__(c_life, c_life_max)
        space_limit = self.dim_y - scaled_c_life - 1
        for case in xrange(self.dim_y - 2):
            if case >= space_limit:
                to_print = "#"
            else:
                to_print = " "
            
            self.addstr(case + 1, 2, to_print, curses.color_pair(1))

    def draw_mana(self):
        c_mana = self.data.get("c.mana")
        c_mana_max = self.data.get("c.mana.max")

        scaled_c_mana = self.__get_col_size__(c_mana, c_mana_max)
        space_limit = self.dim_y - scaled_c_mana - 1
        for case in xrange(self.dim_y - 2):
            if case >= space_limit:
                to_print = "#"
            else:
                to_print = " "
            
            self.addstr(case + 1, 4, to_print, curses.color_pair(3))
        pass

    def __get_col_size__(self, level, maximum):
        size = level * self.dim_y / maximum
        return size

    def static_draw(self):
        self.addstr(0, 2, "H")
        self.addstr(0, 4, "M")

