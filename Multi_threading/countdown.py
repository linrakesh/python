import time
import subprocess

timeleft =10
while timeleft>0:
    print("Time left {}".format(timeleft))
    time.sleep(1)
    timeleft = timeleft -1
subprocess.Popen(['start', r'C:\Users\acer\Desktop\PythonBox\pythonPrograms\Multi_threading\alarm.wav'], shell=True)