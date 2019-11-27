import os
import glob

for root, folders, files in os.walk(os.getcwd()):
    files = glob.glob(files + '/*.py')
    print(files)
