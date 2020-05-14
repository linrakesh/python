import matplotlib.pyplot as plt
import numpy as np

girls =(79,67,82)
boys = (89,78,56)
y_pos = np.arange(3)

width=0.30

plt.bar(width+y_pos,girls,width,color='r',label="Girls")
plt.bar(2*width+y_pos,boys,width,color='green',label="boys")

plt.xlabel('Students')
plt.ylabel('Marks')
plt.legend()
plt.show()
