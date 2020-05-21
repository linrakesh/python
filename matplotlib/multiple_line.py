import matplotlib.pyplot as plt

names =("rakesh","mannat","pratham","pushkar")
mark1 =(56,78,56,34)
mark2 =(78,58,45,89)
mark3= (90,78,89,56)

plt.plot(names,mark1,label="UT-1")
plt.plot(names,mark2,label="UT-2")
plt.plot(names,mark3,label="UT-3")

plt.grid(True)
plt.xlabel('Names')
plt.ylabel('Marks')
plt.title('Student Performance')
plt.legend()
plt.show()
