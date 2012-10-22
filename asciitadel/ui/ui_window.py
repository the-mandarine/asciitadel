
import curses
class UIWindow(object):
    def __init__(self, name, data, monitored, dim_y, dim_x, pos_y, pos_x):
        self.name = name
        self.data = data
        
        if dim_y < 0:
            self.dim_y = curses.LINES + dim_y - pos_y
        else:
            self.dim_y = dim_y

        if dim_x < 0:
            self.dim_x = curses.COLS + dim_x - pos_x
        else:
            self.dim_x = dim_x

        if pos_x < 0:
            self.pos_x = curses.COLS + pos_x
        else:
            self.pos_x = pos_x

        if pos_y < 0:
            self.pos_y = curses.LINES + pos_y
        else:
            self.pos_y = pos_y

        # bind data source to window
        self.data.monitore(name, monitored)
        # lines, cols, posy, posx
        self.win = curses.newwin(self.dim_y, self.dim_x, self.pos_y, self.pos_x)
        self.draw()

    def draw(self):
        self.__static_draw__()
        self.static_draw()
        self.refresh()

    def __static_draw__(self):
        self.box()

    def static_draw(self):
        raise NotImplementedError

    def populate(self):
        raise NotImplementedError

    def __getattr__(self, attr):
        try:
            return getattr(self.win, attr)
        except AttributeError:
            return object.__getattributes__(self)

