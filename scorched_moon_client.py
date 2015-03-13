#!/usr/bin/python3
 
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


import sys
import subprocess

def main():

    logready = False
    loglevel = 0
    debug = False
    skip = False
    check = 0

    for argument in sys.argv:
        if argument == "--no-intro":
            skip = True
        elif argument == "--debug" or argument == "-d":
            debug = True
        elif argument == "--help" or argument == "-h":
            usage()
        elif argument == "--skip" or argument == "-s":
            skip = True
        elif argument == "--log" or argument == "-l":
            logready = True
        elif argument == "1":
            if logready == True: #don't combine if statements to make it easier to add further 
                logready = False
                loglevel = 1
            else:
                print("Unknown argument: {}" .format(argument))
                usage()
        elif argument == "2":
            if logready == True: #don't combine if statements to make it easier to add further 
                logready = False
                loglevel = 2
            else:
                print("Unknown argument: {}" .format(argument))
                usage()
        elif argument == "3":
            if logready == True: #don't combine if statements to make it easier to add further 
                logready = False
                loglevel = 3
            else:
                print("Unknown argument: {}" .format(argument))
                usage()
        elif argument == "4":
            if logready == True: #don't combine if statements to make it easier to add further 
                logready = False
                loglevel = 4
            else:
                print("Unknown argument: {}" .format(argument))
                usage()
        elif argument == "--create" or argument == "-c":
            makesettings = True
        elif check > 0:
            print("Unknown argument: {}" .format(argument))
            usage()
        elif check > 0:
            print("Unknown argument: {}" .format(argument))
            usage()
        check += 1

    import client.main
    client = client.main.Main(debug, loglevel, skip)

def usage():
    print(" ")
    print("scorched_moon_client [options]")
    print(" ")
    print("Options are:")
    print(" ")
    print("-d               --debug             Run client in debug mode, this also forces log to level 1")
    print(" ")
    print("-l <number>      --log <number>      Set log level from 1 - 4")
    print(" ")
    print("-h               --help              Display this help screen")
    print(" ")
    print("-s               --skip              Skip intro scree")
    sys.exit(0)

main()

