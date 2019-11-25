9#   Hangman Games
#   program by          : rakesh kumar
#   website             : https://cbsetoday.com


import random as r

# steps to select a random word from sowpods.txt file
with open("sowpods.txt") as file:
    data = file.read().split()
    number = r.randint(0, len(data))
    word = data[number]

# create a list of underscore -
# it contains exactly same number of underscore as the length of our random word
lines = []
for i in word:
    lines.append('_')

#   counter variable is used to track number of wrong letters.
#   a user can make If it is 6 then terminate the program and print message
for i in lines:
        print(i, end=" ")
        
counter = 0
while True:
    letter = input('\nGuess your letter :')
    if letter in word:
        for i in range(0, len(word)):
            if word[i] == letter:
                lines[i] = letter
    else:  # letter is not in the word
        counter += 1
    # print the word with inserted letters
    for i in lines:
        print(i, end=" ")

    # check letters remained in the list

    cnt = "".join(lines).count('_')

    if cnt == 0 or counter == 6:
        break
# end of while loop

if counter >= 6:
    print("\n\n\n You looser..............Think properly")
    print('Original Words : ',word)
else:
    print("\n\n\n Yes!!!!!!!!!!! You WON this match")
