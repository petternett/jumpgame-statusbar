#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Petter Juterud Barhaugen (petter@petternett.no)

import curses
import Game


if __name__ == '__main__':
    stdscr = curses.initscr()
    app = Game.Game()
    stdscr.nodelay(1)
    stdscr.keypad(True)
    curses.noecho()
    curses.cbreak()
    curses.wrapper(app.run)
