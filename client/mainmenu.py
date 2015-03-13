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

class MainMenu:

    def __init__(self, client):
        logging.debug("")
        self.client = client
        self.desktop = gui.Desktop(theme=gui.Theme("data/themes/default/"))
        self.desktop.connect(gui.QUIT, self.clickquit)
        self.container = gui.Container(width=self.client.settings.screenwidth,height=self.client.settings.screenheight)
        self.button_table = gui.Table(width=self.client.settings.screenwidth,height=(self.client.settings.screenheight / 2))
        self.server_label = gui.Label("Address:",align=-1)
        self.server_input = gui.Input(value=self.client.settings.serveraddress, size=25)
        self.connect_button = gui.Button("Connect to Server")
        self.connect_button.connect(gui.CLICK, self.clickconnect)
        self.settings_button = gui.Button("Settings")
        self.settings_button.connect(gui.CLICK,self.clicksettings)
        self.quit_button = gui.Button("Quit") #could use app.quit but this allows us to have a custom loop
        self.quit_button.connect(gui.CLICK,self.clickquit)

        self.button_table.tr()
        self.button_table.td(self.server_input,row=1)
        self.button_table.td(self.connect_button,row = 2)
        self.button_table.td(self.settings_button,row = 3)
        self.button_table.td(self.quit_button,row = 4)

        self.container.add(self.button_table, 0, 200)
        self.container.add(self.server_label, 205, 230)
        self.desktop.init(self.container)

    def clickconnect(self):
        logging.debug("")
        logging.info("Tried connecting to: {}" .format(self.server_input.value))
        self.client.settings.serveraddress = self.server_input.value
        self.client.load_connected_screen()

    def clicksettings(self):
        logging.debug("")
        self.client.load_settings_screen()

    def clickquit(self):
        logging.debug("")
        self.client.runclient = False
