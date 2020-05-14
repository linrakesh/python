# program to print line graph on the screen
# made by        : rakesh kumar

import matplotlib.pyplot as plt
import numpy as np
x = ['week-1', 'week-2', 'week-3', 'week-4',"Week-6","Week-6","week-7","week-8"]
y = [1250, 1300, 1260, 1400,2420,3180,6550,1220]   
plt.plot(x, y)
plt.xlabel('Week wise Sales')
plt.ylabel('No of Unit Sold')
plt.title('Sales of Electronics in Deepawali')
plt.grid()
plt.show()
