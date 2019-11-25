import glob
import os
import shutil
dest_dir = "C:/test"
for file in glob.glob('e:/python/*.mp4'):
    print(file)
    shutil.copy(file, dest_dir)
    os.unlink(file)
