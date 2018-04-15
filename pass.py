import random
chars ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+}{"
length = int(input("Enter password length "))
password=""
for i in range(length+1):
    password += random.choice(chars)
print(password)