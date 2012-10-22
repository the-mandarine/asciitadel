
from ui_window import UIWindow

MONITORED_ITEMS = ()
COMPONENT_KEY = "bottom_bar"

class BottomBar(UIWindow):
    def __init__(self, data):
        UIWindow.__init__(self, COMPONENT_KEY, data, MONITORED_ITEMS, 0, 0, -3, 0)

    def static_draw(self):
        pass

    def populate(self):
        pass

