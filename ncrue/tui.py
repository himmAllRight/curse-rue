#!/usr/bin/python

"""Curse Rue Text User Interface"""

from argparse import ArgumentParser
import curses
import time
from . import __version__


class TUI():
    """Defines the TUI Class.

    Class that is responsible for creating and displaying the TUI.
    """

    def __init__(self):
        """Instantiates the TUI"""
        self.parser = ArgumentParser(description='Navigate and view\
                                        Rue RSS feeds in ncurses')
        self.parser.add_argument('--version', action='version',
                                 version=__version__)
        self.stdscr = None

    def run_curses_loop(self, window):
        """Run the curses sequence loop"""
        self.stdscr = window
        self.stdscr.refresh()
        self.stdscr.addstr(20, 10, 'Hello World!')
        self.stdscr.refresh()
        time.sleep(2)

    def main(self, in_args):
        """Launch main window"""
        print(in_args)
        args = self.parser.parse_args()
        print(f"tui main: {args}")
        curses.wrapper(self.run_curses_loop)
        print('Exited Curses.')
