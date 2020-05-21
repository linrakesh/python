import matplotlib.pyplot as plt
import numpy as np
import numpy as np
x = np.arange(1,100)
y = np.arange(101,200)
z=  np.arange(201,250)
plt.boxplot([x,y,z])
plt.show()