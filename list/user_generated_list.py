''' program to create a user generated list and then find out largest and lowest element
    made by         : rakesh kumar
    last modified   : 20-auguest-2018 '''

number = []
while True:
    x = int(input('Enter any number :'))
    if x == 0:
        break
    number.append(x)

largest = max(number)
lowest = min(number)

print("\n\n")
print("largest Number  :", largest)
print("Lowest Number  :", lowest)
