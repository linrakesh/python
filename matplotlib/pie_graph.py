# program to print scatter graph on the screen
# made by        : rakesh kumar

import matplotlib.pyplot as plt
import numpy as np
x = ['Delhi','Banglore','Chennai','Pune','Ghaziabad','Udupi']
y = [250,300,260,400,599,320]
plt.pie(y,labels=x,autopct='%.2f',)
plt.show()