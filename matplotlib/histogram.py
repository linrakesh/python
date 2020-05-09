import matplotlib.pyplot as plt
sugar_men = [121,153,243,33,95,138,339,150,252,156,143,118]
sugar_women = [67,101,120,135,180,125,68,95,92,102,47,78,135,225]
sugar_child =[120,89,123,145,100,89,135,120,102,125,123,170,180]
plt.hist([sugar_men, sugar_women,sugar_child], bins=[100, 130, 150, 200],
         rwidth=0.80, color=['green', 'orange','purple'], label=['Men', 'Women', 'children'])
plt.legend()
plt.xlabel('Sugar Readings')
plt.ylabel('No of Patient')
plt.title('Sugar Patient Stats')
plt.show()
