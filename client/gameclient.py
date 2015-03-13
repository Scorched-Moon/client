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
from . import settings
from . import mainmenu
from . import settingsscreen
from . import network
from . import findgamescreen

class ClientState:
    def __init__(self):
        logging.debug("")
        self.runclient = True
        self.playinggame = False
        self.settings = settings.Settings()
        self.network = network.Network()
        self.display = []

    def popup(self, message): #used for alerts and similar popups at any time
        logging.debug("")
        from .pgu import gui
        poptitle = gui.Label("")
        poptable = gui.Table(width=100, height=100)
        popwindow = gui.Dialog(poptitle, poptable)
        okaybutton = gui.Button("Okay")
        okaybutton.connect(gui.CLICK, popwindow.close)
        popupmessage = gui.Label(message)
        poptable.tr()
        poptable.td(popupmessage,row=1)
        poptable.td(okaybutton,row=2)
        popwindow.open()

    def load_main_menu(self): #loads main mneu
        logging.debug("")
        self.display = mainmenu.MainMenu(self)

    def load_settings_screen(self): #loads settings screen
        logging.debug("")
        self.display = settingsscreen.SettingsScreen(self)

    def load_connected_screen(self): #connecting to server
        logging.debug("")
        self.network.connectserver(self.settings.serveraddress, self.settings.serverport, self.settings.minserverversion)
        if self.network.connected == "True":
            logincmd = "login " + self.settings.username
            logging.debug("Logging in as: {}" .format(self.settings.username))
            self.network.send("login " + self.settings.username)
            self.display = findgamescreen.FindGameScreen(self)
            self.settings.savesettings()
        else:
            self.popup(self.network.connected)

        
