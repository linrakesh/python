# !python36
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
    address = "http://www.youtube.com/results?search_query={}".format(query)
    webbrowser.open(address)
else:
    webbrowser.open('http://www.youtube.com/results?search_query=binarynote')

