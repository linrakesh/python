import os
path = r"C:\Users\acer\Desktop\PythonBox\python_video"
os.chdir(path)
for file in os.listdir():
    if os.path.isfile(file):
        filename,ext = os.path.splitext(file)
        files = filename.split(' ')  #now filenames in tuples
        newname = files[4] + '-'.join(files[5:])+ext 
        # print(newname)
        os.rename(file,newname)
        