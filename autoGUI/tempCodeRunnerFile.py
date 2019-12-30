# purpose       : Program to check mouse position on the move
# author        : rakesh kumar
# licence       : MIT
import pyautogui
print("Press CTRL+C to stop")
try:
    while True:
        x,y = pyautogui.position()
        positionStr = "X :"+str(x).rjust(4) +" Y :"+ str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print("\n Done")