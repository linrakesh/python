import matplotlib.pyplot as plt
<<<<<<< HEAD
=======
from numpy import linspace,pi,sin,cos,tan

#multiple figures
data=[1,2,3,4,5,
      10,11,12,14,15,18,16,14,13,12,19,20,16,14,19,
      22, 21, 22, 23, 24, 25, 23, 26, 28, 26,27,25,28,29,30, 
      32,33,37,38,38,39,34,36,
      42,43,45,46,48,46,49,50,43,42,44,45,47,49,50,49,48,42,46,41,45,46,48,45,44,
      51,52,54,55,53,58,57,59,60,52,51,54,53
      ]
frequency = [5,15,18,8,25,13]
x = [5,15,25.5,35.5,45.5,55.5]


plt.figure(1)
plt.hist(data,bins=[0,10,20,30,40,50,60],color="green")
plt.scatter(frequency,x)
plt.show()
>>>>>>> da25a2a32ac30d0980ed6d1d3ad58008d8ff0b21
