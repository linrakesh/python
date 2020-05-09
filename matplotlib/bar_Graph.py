# program to print bar graph on the screen
# made by        : rakesh kumar

import numpy as np
import matplotlib.pyplot as plt
city = ['Delhi', 'Banglore', 'Chennai', 'Pune']
sales = [250, 300, 260, 400]
plt.xlabel('City')
plt.ylabel('Sales in Million')
plt.title('Sales Recorded in Major Cities')
plt.bar(city, sales)
plt.show()
