
from ui_window import UIWindow

MONITORED_ITEMS = ()
COMPONENT_KEY = "top_bar"

class TopBar(UIWindow):
    def __init__(self, data):
        UIWindow.__init__(self, COMPONENT_KEY, data, MONITORED_ITEMS, 3, 0, 0, 0)

    def populate(self):
        pass

    def static_draw(self):
        pass
