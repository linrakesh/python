sum = 0
for i in range(10):
  try: 
    if 10 / i == 2:
      break
  except ZeroDivisionError:
    sum = sum+1
  else:
    sum = sum +2
print("Sum :",sum)