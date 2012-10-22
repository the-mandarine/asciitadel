#!/usr/bin/env python2

import logging
import curses, traceback
from data import SharedData, DataHandler
from config import Config
from game import Game
from ui import Interface

logging.basicConfig(filename="asciitadel.log", level=logging.DEBUG)

def main():
    config = Config()
    data = SharedData()

    # Load data
    data_handler = DataHandler(data, config)

    # Create interface thread
    interface = Interface(data_handler)
    interface.start()

    game = Game(data_handler)
    try:
        game.run()
    except KeyboardInterrupt:
        game.stop()
        interface.stop()

if __name__ == '__main__':
    main()

