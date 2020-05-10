import matplotlib.pyplot as plt
import numpy as np

names = ["Arushi","Pratham","Mannat"]
marks1 = (82, 80, 63)
marks2 = (98,  73,  30)
marks3  =(78,87,45)
marks4  =(99,92,90)
final = (99,67,78)

x = np.arange(len(marks1))
width = 0.15

fig, axes = plt.subplots(ncols=1, nrows=1)

axes.bar(x, marks1, width, align='edge',color="orange", label="UT-1")
axes.bar(x+width, marks2, width, align='edge', color='purple', label="UT-2")
axes.bar(x+2*width, marks3, width, align='edge', color='green', label="Half Yearly")
axes.bar(x+3*width, marks4, width, align='edge', color='red', label="PreBoard")
axes.bar(x+4*width, final, width, align='edge', color='blue', label="Final")

axes.set_xticks(x)
axes.set_xticklabels(names)
plt.xlabel('Student Names')
plt.ylabel('Marks Obtained')
plt.title('Student Performance')
plt.legend()
plt.show()