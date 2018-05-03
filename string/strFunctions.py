str = '''   Python has a built-in string class named "str" with many handy 
        features (there is an older module named "string" which you
         should not use Python. String literals can be enclosed
         by either double or single quotes, 
         although single quotes are more commonly used   '''

print("String length :", len(str))   
upper = str.upper()      
print("String in upper case : ")
print(upper)

lower = upper.lower()
print("\n\nString in lower case :", lower)

strip = str.strip()
print("\n\nString without space at begining and end :", strip)

startwith = str.startswith('python')  #return true or fals
endwith   = str.endswith('hello')
print(startwith)
print(endwith)

find = str.find('quotes')  # display the index of first occurance of the string
print("First appeared at :",find)

newstr = str.replace('Python','c++')
print("\n\n New string where 'Python' was replaced with 'C++' \n", newstr)

split = str.split(' ')  # return result in a list
print(split)

