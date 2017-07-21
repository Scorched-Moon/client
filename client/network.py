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
import telnetlib

class Network:
    def __init__(self):
        logging.debug("")
        self.server = []
        self.connected = "False"
        self.buffer = ""

    def connectserver(self, address, port, minserverversion):
        logging.debug("")
        logging.info("Attempting to connect to {} {}" .format(address, port))
        self.connected = "False"
        try: 
            self.server = telnetlib.Telnet(address, port, 30)
        except:
            logging.info("unable to connect to server")
            self.connected = "Unable to connect at {}" .format(address)
        else:
            logging.debug("Connected to server")
            cmd = self.server.read_until(b"\n", 30)
            cmd = cmd.decode("ascii")
            cmd = cmd[:-1]
            if cmd == "Welcome to Scorched Moon":
                logging.debug("server said hello")
                cmd = self.server.read_until(b"\n", 30)
                cmd = cmd.decode("ascii")
                cmd = cmd[:-1]
                cmd, version = cmd.split(" ", 1)
                if cmd == "version":
                    if version < minserverversion:
                        logging.warning("Server is at version {} but client requires version {} or higher - disconnecting" .format(version, minserverversion))
                        self.connected = "Server is at version {} but client requires version {} or higher" .format(version, minserverversion)
                        self.server.close()
                    else:
                        logging.info("successfully connected to server version {}" .format(version))
                        self.connected = "True"
                else:
                    logging.warning("Server did not identify version after hello - disconnecting")
                    self.connected = "Unable to confirm server version"
                    self.server.close()
            else:
                logging.warning("Server did not give expected hello message - disconnecting")
                self.connected = "Server connected but does not\n appear to be running Scorched Moon"
                self.server.close()

    def disconnectserver(self):
        logging.debug("")
        self.server.close()
        self.connected = False

    def send(self, data):
        logging.debug("")
        logging.debug("sending {}" .format(data))
        data = ''.join([data, "\n"])
        data = data.encode("ascii")
        self.server.write(data)

    def receive(self):
        if self.buffer == "":
            cmd = self.server.read_until(b"\n")
            cmd = cmd.decode("ascii")
            self.buffer = cmd[:-1] #removes carriage return from string
        else:
            pass
        
