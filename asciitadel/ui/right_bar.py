
from ui_window import UIWindow

MONITORED_ITEMS = ("c.life")
COMPONENT_KEY = "right_bar"

class RightBar(UIWindow):
    def __init__(self, data):
        UIWindow.__init__(self, COMPONENT_KEY, data, MONITORED_ITEMS, -3, 7, 3, -7)

    def populate(self):
        c_life = self.data.get("c.life")
        s_c_life = "%02i" % (c_life)
        self.addstr(1, 1, s_c_life)

    def static_draw(self):
        self.addstr(0, 2, "H")
        self.addstr(0, 4, "M")

