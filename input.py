#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      acer
#
# Created:     03-02-2018
# Copyright:   (c) acer 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys,webbrowser
if( len (sys.argv) > 1):
    query = "+".join(sys.argv[1:])
    address = "http://www.google.co.in/search?q={}".format(query)
    webbrowser.open(address)

