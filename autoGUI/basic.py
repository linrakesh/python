import pyautogui
width,height = pyautogui.size()
print("\n\n Width = {} height ={} \n\n".format(width,height))

# for i in range(10):
#       pyautogui.moveTo(100, 100, duration=0.25)
#       pyautogui.moveTo(200, 100, duration=0.25)
#       pyautogui.moveTo(200, 200, duration=0.25)
#       pyautogui.moveTo(100, 200, duration=0.25)

# for i in range(10):
#       pyautogui.moveRel(100, 0, duration=0.25)
#       pyautogui.moveRel(0, 100, duration=0.25)
#       pyautogui.moveRel(-100, 0, duration=0.25)
#       pyautogui.moveRel(0, -100, duration=0.25)

#mouse current positions
x,y = pyautogui.position()
print("Current mouse position : x = {}  y = {}".format(x,y))

