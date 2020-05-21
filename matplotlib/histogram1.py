import matplotlib.pyplot as plt
x=[12, 15, 23, 33, 35, 38, 39, 50, 52, 56, 43, 18]
plt.hist(x, bins=[10, 20, 30, 40, 50, 60],color="red",rwidth=0.80)
plt.show()