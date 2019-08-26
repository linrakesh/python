''' program to find out substring in a given substring
    made by         : rakesh kumar
    last editted    : 26-auguest 2019 '''

string = "this is orange juice"
sub = 'orange'

# method -1
# if sub in string:
#     print("present")
# else:
#     print("non present")

#method - 2

# found = string.find(sub)
# if(found != -1):
#     print("found")
# else:
#     print("not found")

# method -3
# if sub in string.split():
#     print("found")
# else:
#     print("not found")

# method -4
# count = string.count(sub)
# if(count != 0):
#     print("found")
# else:
#     print("not found")

#method - 5

# result = "found" if sub in string else "not found"
# print(result)

#method -6
print("found" if sub in string else "not found")
