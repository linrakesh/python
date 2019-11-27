import glob
import os
import shutil
import time

source = 'e:/python'
dest_dir = "C:/test"

files = glob.glob(source+"/*.txt")
for file in files:
    print(file)
    shutil.move(file, dest_dir)


""" while True:
    print("Hello rakesh")
    time.sleep(5)
 """
