#!/usr/bin/env python3

## This is an example of curses: https://docs.python.org/2/library/curses.panel.html#module-curses.panel
## working to turn it into my own

import curses
from curses import panel

class Menu(object):

    def __init__(self, items, stdscreen):
        self.window = stdscreen.subwin(0,0)
        self.window.keypad(1)
        self.panel = panel.new_panel(self.window)
        self.panel.hide()
        panel.update_panels()

        self.position = 0
        self.items = items
        self.items.append(('exit','exit'))
        print(items)

    def navigate(self, n):
        self.position += n
        if self.position < 0:
            self.position = 0 
        elif self.position >= len(self.items):
            self.position = len(self.items)-1

    def display(self):
        self.panel.top()
        self.panel.show()
        self.window.clear()

        while True:
            self.window.refresh()
            curses.doupdate()
            for index, item in enumerate(self.items):
                if index == self.position:
                    mode = curses.A_REVERSE
                else:
                    mode = curses.A_NORMAL

                msg = '%d. %s (%s)' % (index, item[0], str(item[1]))
                self.window.addstr(1+index, 1, msg, mode)

            key = self.window.getch()

            if key in [curses.KEY_ENTER, ord('\n')]:
                ## If last item in list, break
                if self.position == len(self.items)-1:
                    break
                else:
                    self.items[self.position][1]()


            elif key == curses.KEY_UP:
                self.navigate(-1)

            elif key == curses.KEY_DOWN:
                self.navigate(1)

        self.window.clear()
        self.panel.hide()
        panel.update_panels()
        curses.doupdate()

class MyApp(object):

    def __init__(self, stdscreen):
        self.screen = stdscreen
        curses.curs_set(0)

        ## Panel Menu for adding a new Feed
        add_feed_items = [
                ('Feed URL', curses.flash),      ## These need to be input fields
                ('Feed Category', curses.flash), ## These need to be input fields
                ('Add Feed', curses.flash)
                ]
        add_feed_submenu = Menu(add_feed_items, self.screen)

        ## Panel Menu for Reading Feeds
        read_feeds_items = [
                 ('Read All Feeds', curses.flash),
                 ('Read A Feed Category', curses.flash),
                 ('Read a Single Feed', curses.flash)
                ]
        read_feeds_submenu = Menu(add_feed_items, self.screen)
        
        main_menu_items = [
                ('Add Feed', add_feed_submenu.display),
                ('Read Feeds', read_feeds_submenu.display),
                ('flash', curses.flash),
                ]
        main_menu = Menu(main_menu_items, self.screen)
        main_menu.display()

if __name__ == '__main__':
    curses.wrapper(MyApp)
