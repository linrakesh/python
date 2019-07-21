# program to print scatter graph on the screen
# made by        : rakesh kumar

import matplotlib.pyplot as plt
import numpy as np
x = ['Delhi','Banglore','Chennai','Pune','Ghaziabad','Udupi']
y = [250,300,260,400,599,320]
plt.pie(y,labels=x,autopct='%1.2f',startangle=90,explode=(0,0.1,0,0,0.2,0))
plt.show()