import random

def draw_board(bo):
    print('    '+bo[0].rjust(4)+"  | "+bo[1].rjust(4) + " | "+bo[2].rjust(4) )
    print('------------------------')
    print('     '+bo[3].rjust(4)+" | "+bo[4].rjust(4) + " | "+bo[5].rjust(4) )
    print('------------------------')
    print('     '+bo[6].rjust(4)+" | "+bo[7].rjust(4) + " | "+bo[8].rjust(4) )
    print('------------------------')
    print()
    print()

#Get user's entry from keyboard
def get_user_entry(board,sbl):
    while True:
        if sbl =='O':
            position = random.randint(1,9)
        else:
            position = int(input('Enter your position between 1-9 : '))

        if board[position-1] =='X' or board[position-1]=='O':
            print('Position already filled...try again')
            continue
        else:
            board[position-1]=sbl
            break
    sbl ='O'    
    return

def check_winner(board,sbl):
    return(( board[0] ==sbl and board[1]==sbl and board[2]==sbl ) or 
        ( board[3] ==sbl and board[4]==sbl and board[5]==sbl ) or
        ( board[6] ==sbl and board[7]==sbl and board[8]==sbl ) or 
        ( board[0] ==sbl and board[3]==sbl and board[6]==sbl ) or
        ( board[1] ==sbl and board[4]==sbl and board[7]==sbl ) or
        ( board[2] ==sbl and board[5]==sbl and board[8]==sbl ) or
        ( board[0] ==sbl and board[4]==sbl and board[7]==sbl ) or
        ( board[2] ==sbl and board[4]==sbl and board[6]==sbl ))
        
def clear():
    print()
    print()
    print()

def check_blank(board):
    found = False
    for x in board:
        if x ==' ':
            return True 
    return found    

#main program start from here
board = [' ']*9
# user_symbol = input("Choose Your symbol (X|O) : ")
# comp_symbol = 'X' if user_symbol =='O' else 'O'
# print('Computer Symbol :', comp_symbol)
# print('User Symbol :', user_symbol)
user_symbol='X'
while True:
    result = check_blank(board)
    if result==True:
        get_user_entry(board,user_symbol)
        if(user_symbol=='O'):
            print("Computer's Move")
        draw_board(board)
        win = check_winner(board,user_symbol)
        if win==True:
            if user_symbol=='O':
                print("You Lost this match my dear")
            else:
                print("You Won this Match my dearS")
            board = [' ']*9
            break
    else:
        print("No position left Blank....Try again") 
        break
    user_symbol = 'X' if user_symbol =='O' else 'O'
    