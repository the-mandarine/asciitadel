
from ui_window import UIWindow

MONITORED_ITEMS = ("c.life")
COMPONENT_KEY = "right_bar"

class RightBar(UIWindow):
    def __init__(self, data):
        UIWindow.__init__(self, COMPONENT_KEY, data, MONITORED_ITEMS, -3, 7, 3, -7)

    def populate(self):
        #s_c_life = "%02i" % (c_life)
        self.draw_health()

    def draw_health(self):
        c_life = self.data.get("c.life")
        scaled_c_life = self.__get_col_size__(c_life, 100)
        s_c_life = "%02i" % (scaled_c_life)
        self.addstr(1, 1, s_c_life)
        

    def draw_mana(self):
        pass

    def __get_col_size__(self, level, maximum):
        size = level * (self.dim_y - 2) / maximum
        return size

    def static_draw(self):
        self.addstr(0, 2, "H")
        self.addstr(0, 4, "M")

