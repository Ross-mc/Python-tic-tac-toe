game_on = True
game_indices = {1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:'',}
current_player = 'Player 1'
acceptable_num = ['1','2','3','4','5','6','7','8','9']
game_display1 = [game_indices[7],game_indices[8],game_indices[9]]
game_display2 = [game_indices[4],game_indices[5],game_indices[6]]
game_display3 = [game_indices[1],game_indices[2],game_indices[3]]
count = 0
import sys


def display_game():
    global game_display1
    global game_display2
    global game_display3


    game_display1 = [game_indices[7],game_indices[8],game_indices[9]]
    game_display2 = [game_indices[4],game_indices[5],game_indices[6]]
    game_display3 = [game_indices[1],game_indices[2],game_indices[3]]
    print(game_display1)
    print(game_display2)
    print(game_display3)

def position_choice():
    global current_player
    choice = 'DEFAULT'
    while choice not in acceptable_num:
        choice = input(f'{current_player}, please select a position between 1 and 9.\n7-8-9\n4-5-6\n1-2-3\n')
        if game_indices[int(choice)] != '':
            choice = 'DEFAULT'
        if choice not in acceptable_num:
            print('Invalid Selection')
    position = int(choice)
    if current_player == 'Player 1':
        game_indices[position] = 'X'
    else:
        game_indices[position] = 'O'

def game_choice():
    choice = "default"

    while choice not in ['Yes', 'No']:
        choice = input('Do you want to play again? (Yes or No)')
        if choice not in ['Yes', 'No']:
            print('Sorry I do not understand, please choose Yes or No')
    if choice == 'Yes':
        return True
    else:
        sys.exit(0)

def game_over():
    global game_display1
    global game_display2
    global game_display3
    global game_indices
    global current_player

    game_indices = {1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:'',}
    current_player = 'Player 1'    
    game_display1 = [game_indices[7],game_indices[8],game_indices[9]]
    game_display2 = [game_indices[4],game_indices[5],game_indices[6]]
    game_display3 = [game_indices[1],game_indices[2],game_indices[3]]
    game_choice()

def check_if_won():
    global current_player
    global count
    count = 0
    if game_display1[0] == game_display1[1] and game_display1[0] == game_display1[2] and game_display1[0] != '':
        print(f'{current_player} has won the game!')
        game_over()
    elif game_display2[0] == game_display2[1] and game_display2[0] == game_display2[2] and game_display2[0] != '':
        print(f'{current_player} has won the game!')
        game_over()
    elif game_display3[0] == game_display3[1] and game_display3[0] == game_display3[2] and game_display3[0] != '':
        print(f'{current_player} has won the game!')
        game_over()
    elif game_display1[0] == game_display2[0] and game_display1[0] == game_display3[0] and game_display3[0] != '':
        print(f'{current_player} has won the game!')
        game_over()
    elif game_display1[1] == game_display2[1] and game_display1[1] == game_display3[1] and game_display3[1] != '':
        print(f'{current_player} has won the game!')
        game_over()
    elif game_display1[2] == game_display2[2] and game_display1[2] == game_display3[2] and game_display3[2] != '':
        print(f'{current_player} has won the game!')
        game_over()
    elif game_display1[0] == game_display2[1] and game_display1[0] == game_display3[2] and game_display3[2] != '':
        print(f'{current_player} has won the game!')
        game_over()
    elif game_display3[0] == game_display2[1] and game_display3[0] == game_display1[2] and game_display1[2] != '':
        print(f'{current_player} has won the game!')
        game_over()
    for key, value in game_indices.items():
        if value != '':
            count += 1
    if count == 9:
        print('It is a draw!')
        game_over() 

    if current_player == 'Player 1':
        current_player = 'Player 2'
    elif current_player == 'Player 2':
        current_player = 'Player 1'


while game_on:
    position_choice()
    display_game()
    check_if_won()