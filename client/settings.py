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
import os, os.path
import string
import sys

class Settings:
    def __init__(self):
        logging.debug("")
        self.version = 0.00
        self.stringversion = "0.00.0"
        self.minsettingsversion = 1.01 #oldest version of scorched moon settings file is compatible with remember to update this number when any changes are made to the way settings.conf is read or written to
        self.minserverversion = 0.037 #oldest version of scorched moon server the client is compatible with
        self.debug = True
        self.tetherdir = None
        self.loglevel = 4
        self.WINDOW_SIZE = self.screen_width,self.screen_height = 1024,768
        self.username = ""
        self.serveraddress = "127.0.0.1"
        self.serverport = 6112
        self.screenwidth = 800
        self.screenheight = 600

    def load_settings(self):
        logging.debug("")
        logging.info("loading settings from settings.conf")
        badsettings = False
        settingsfile = os.path.join(self.tetherdir, "settings.cfg")
        if os.path.exists(settingsfile):
            settingsfile=open(settingsfile, mode="r", encoding="utf-8")
            for line in settingsfile:
                line=line.strip()
                if line == "" or line[0] == "#":
                    continue
                input_array = line.split("=", 1)
                if input_array[0].strip() == "version":
                    if float(input_array[1].strip()) < self.minsettingsversion: #checking file version to avoid incompatibilities
                        logging.info("Obsolete settings file detected Using defaults")
                        badsettings = True

                elif input_array[0].strip() == "debug":
                    if input_array[1].strip() == "True":
                        self.debug = True
                elif input_array[0].strip() == "loglevel":
                    self.loglevel = int(input_array[1].strip())
                elif input_array[0].strip()=="username":
                    self.username = input_array[1].strip()
                elif input_array[0].strip()=="lastIP":
                    self.serveraddress = input_array[1].strip()
                else:
                    logging.warning("unidentified input in settings file")
                    badsettings = True
            
        else:
            badsettings = True
        if badsettings == True:
            pass #add code to reset back to default settings


    def save_settings(self):
        logging.debug("")
        logging.info("saving settings to settings.conf")
        settingsfile = os.path.join(self.tetherdir, "settings.cfg")
        settingsfile=open(settingsfile, mode="w", encoding="utf-8")
        settingsfile.write("version="+str(self.version)+"\n")
        settingsfile.write("debug="+str(self.debug)+"\n")
        settingsfile.write("loglevel="+str(self.loglevel)+"\n")
        settingsfile.write("username="+str(self.username)+"\n")
        settingsfile.write("lastIP="+str(self.serveraddress)+"\n")
