import matplotlib.pyplot as plt
list1 = [10, 33, 43, 74, 84, 8, 9,35,63,5,3,67,8,78,35,2,57,7,78,34,67,34]
list2 = [23,3,5,67,67,78,98,90,100,12,45,67,89,45,56,78,9,23,69,56,23,5]
plt.boxplot([list1,list2],labels=['Girls','Boys'])
plt.grid()
plt.legend()
plt.show()
