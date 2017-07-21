"""Copyright 2017:
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

# this file is for useful tools and calculations 

class Tools:
    def __init__(self):
        logging.debug("")

    def checkversion(version1, version2): #compares version numbers, returns true version1 is higher, false is version2 is higher
        logging.debug("")
        majorversion1, minorversion1, revision1 = (int(temp) for temp in version1.split(".", 3))
        majorversion2, minorversion2, revision2 = (int(temp) for temp in version2.split(".", 3))
        if majorversion2 > majorversion1:
            return False
        elif minorversion2 > minorversion1:
            return False
        elif revision2 > revision1:
            return False
        else:
            return True
