"""Copyright 2015:
    Kevin Clement

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
"""

import logging
from .pgu import gui

class SettingsScreen:
    def __init__(self, client):
        logging.debug("")
        self.client = client
        self.desktop = gui.Desktop(theme=gui.Theme("data/themes/default/"))
        self.desktop.connect(gui.QUIT, self.clickquit)
        self.menu_table = gui.Table(width=self.client.settings.screenwidth,height=self.client.settings.screenheight)
        self.test_label = gui.Label("Unchanged label")
        self.back_button = gui.Button("Return to Main Menu")
        self.back_button.connect(gui.CLICK,self.clickback)
        self.test_button = gui.Button("Test the popup!")
        self.test_button.connect(gui.CLICK, self.clicktest)
        self.test_button2 = gui.Button("Change the label!")
        self.test_button2.connect(gui.CLICK, self.clicktest2)
        self.menu_table.tr()
        self.menu_table.td(self.test_label, row=1,col=1)
        self.menu_table.td(self.test_button, row=2,col=1)
        self.menu_table.td(self.test_button2, row=3,col=1)
        self.menu_table.td(self.back_button,row=4,col=1)
        self.desktop.init(self.menu_table)
        self.client.popup("There are currently no settings yet to change")

    def clickback(self):
        logging.debug("")
        self.client.load_main_menu()

    def clickquit(self):
        logging.debug("")
        self.client.runclient = False

    def clicktest(self):
        self.client.popup("The popups work!")

    def clicktest2(self):
        self.test_label.set_text("the label changed!")
