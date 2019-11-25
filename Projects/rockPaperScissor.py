#   Program to play rock, paper, scissor
#   program by          : rakesh kumar
#   website             : https://cbsetoday.com

# Extra Tips for program
# rock  > scissor 
# scissor  > paper
# paper > rock

import random
games=0
won=0
lost=0
tie=0
choice ="Y"
while choice!='N':
    ans = int(input('Enter 1-Rock 2- Paper 3 -Scissor : '))
    comp = random.randint(1,3)
    if ans == comp:
        print("tie !!!!!!!!!!!!!!!!")
        tie+=1
    if ans==1:
        if(comp==3):
            print("You won")
            won+=1
        elif(comp==2):
            print("You lost")
            lost+=1
    if(ans==2):
        if(comp==1):
            print("You won")
            won+=1
        elif(comp==3):
            print("You lost")
            lost+=1
    if(ans==3):
        if(comp==2):
            print("You won")
            won+=1
        elif(comp==1):
            print("You lost")
            lost+=1
    games+=1
    choice= input("Want to play more( Y/N) :").upper() 

print('\n\n\n Simple stat of this Game \n')
print(' Total guess  :',games)
print("You won Games :",won)
print("You lost Games :",lost)
print("Tie Games :",tie)
