file = open('C:/python/PracticalFileQuestion/diary.txt', 'r')
data = file.read().split()
for x in data[-1:0:-1]:
    print(x[-1::-1], end=' ')
file.close()
