#-------------------------------------------------------------------------------
# Name:        google.py
# Purpose:     search google using command line
# Author:      rakesh kumar
# Created:     03-02-2018
# Copyright:   binarynote.com
# Licence:     MIT
#-------------------------------------------------------------------------------

import sys,webbrowser
if( len (sys.argv) > 1):
    query = "+".join(sys.argv[1:])
    address = "http://www.google.co.in/search?q={}".format(query)
    webbrowser.open(address)
else:
    webbrowser.open('http://www.google.co.in/search?q=binarynote')

