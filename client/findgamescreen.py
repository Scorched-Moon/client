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

class FindGameScreen:
    def __init__(self, client):
        logging.debug("")
        self.client = client
        self.desktop = gui.Desktop(theme=gui.Theme("data/themes/default/"))
        self.desktop.connect(gui.QUIT, self.clickquit)
        self.container = gui.Container(width=self.client.settings.screenwidth,height=self.client.settings.screenheight)
        self.chatinput = gui.Input(size=65)
        self.chatdoc = gui.Document(width=1, height=10)
        self.chatscroll = gui.ScrollArea(self.chatdoc,width=600,height=100,hscrollbar=False)

        self.chatinput.connect("activate", self.chatentered)
        self.container.add(self.chatinput, 10, 550)
        self.container.add(self.chatscroll, 10, 440)
        self.desktop.init(self.container)
        self.chathistory = []

    def clickquit(self):
        logging.debug("")
        self.client.runclient = False

    def chatentered(self): #processes chat commands
        logging.debug("")
        cmd = self.chatinput.value
        logging.debug("Raw chat input: {}" .format(cmd))
        if cmd[:1] == "/": #determine if this is chat or server command
            cmd = cmd[1:]
            self.client.network.send(cmd)
            notice = "Sent server command: " + cmd
            self.chatmessage(notice)
        else: #not a command so send as chat to channel
            self.client.network.send("chat {} channel {}" .format(self.client.settings.username, cmd))
        self.chatinput.value = "" #clearing text input for next chat

    def chatmessage(self, message):
        logging.debug("")
        if len(self.chathistory) > 50: #determines how far back to keep old chat messages
            oldmessage = self.chathistory.pop(0)
            self.chatdoc.remove(oldmessage) #removing old messages to save on memory
        self.chathistory.append(gui.Label(message))
        self.chatdoc.add(self.chathistory[len(self.chathistory)-1])
        self.chatdoc.br(1)
        if self.chatscroll.hasfocus() != True: #do not scroll chat when chat window has focus so players can scroll through old messages
            self.client.display.desktop.loop()
            self.chatscroll.set_vertical_scroll(5000) #force chat window to most recent message
