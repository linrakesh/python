def addition(a, b=0):
    return a+b


result = addition(10)
print(result)
result = addition('rakesh', ' You are awesome')
print(result)
result = addition(20, 30.45)
print(result)
result = addition([10, 20, 30], [40, 50, 60])
print(result)
result = addition((10, 20, 30), (40, 50, 60))
print(result)
