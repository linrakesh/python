#   Program of cows and bulls number guessing game
#   program by          : rakesh kumar
#   website             : https://cbsetoday.com


import random as r
cows = 0
bulls = 0
n = str(r.randint(1000, 9999))
ans = input('Enter Your guess :')

for i in range(len(n)):
    if (n[i] == ans[i]):
        cows += 1
    elif ans[i] in n:
        bulls += 1

print("Actual No was : ", n)
print('Cows :', cows, " Bulls :", bulls)
