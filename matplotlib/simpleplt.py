import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,2.0*np.pi,101)
# print(x)
y = np.sin(x)
plt.plot(x,y)
plt.show()