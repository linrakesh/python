#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      acer
#
# Created:     06-05-2017
# Copyright:   (c) acer 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from subprocess import check_output

class Util:
  def strip_comments(self,source_code):
    process = check_output(['cpp', '-fpreprocessed', source_code],shell=False)
    return process

if __name__ == "__main__":
  util = Util()
  print util.strip_comments("file.cpp")

