# program to print bar graph on the screen
# made by        : rakesh kumar

import matplotlib.pyplot as plt
x = ['Delhi', 'Banglore', 'Chennai', 'Pune']
y = [250, 300, 260, 400]
plt.xlabel('City')
plt.ylabel('Sales in Million')
plt.title('Sales Recorded in Major Cities')
plt.bar(x, y)
plt.show()
