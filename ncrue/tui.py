#!/usr/bin/python

"""Curse Rue Text User Interface"""

from argparse import ArgumentParser
from . import __version__


class TUI:
    """Defines the TUI Class.

    Class that is responsible for creating and displaying the TUI.
    """

    def __init__(self):
        """Instantiates the TUI"""
        self.parser = ArgumentParser(
            description="Navigate and view\
                                        Rue RSS feeds in ncurses"
        )
        self.parser.add_argument(
            "--version", action="version", version=__version__
        )

    def draw_window(self):
        """Draw new window?"""

    def main(self):
        """Launch main window"""
        args = self.parser.parse_args()
        print(f"tui main: {args}")
