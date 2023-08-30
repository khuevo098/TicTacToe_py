#input position funtion
from IPython.display import clear_output
import random
def place_pos():
    position=int(input('Input position to where place new marker: '))
    while position not in range(1,10):
        print('Position must be in range from 1 to 10!')
        position=int(input('New valid position: '))
    return position


def display_board(board):
    print(board[1]+'|'+board[2]+'|'+board[3])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[7]+'|'+board[8]+'|'+board[9])

def player_input():
    marker=input('Which one you choose X or O?: ')
    while marker not in ['X', 'O']:
        marker=input('Invalid marker choice! Only X or O: ')
    return marker

def place_marker(board,marker,pos):
    board[pos]=marker

def win_check(board, mark):
    if board[1]==board[2]==board[3]==mark:
        return True
    if board[4]==board[5]==board[6]==mark:
        return True
    if board[7]==board[8]==board[9]==mark:
        return True
    for i in range(1,4):
        if board[i]==board[i + 3]==board[i + 6]==mark:
            return True
    if board[1]==board[5]==board[9]==mark:
        return True
    if board[3]==board[5]==board[7]==mark:
        return True
    return False


def choose_first():
    who_first=random.randint(1,2)
    if who_first==1:
        print('Player 1 go first!')
    else:
        print('Player 2 go first!')
    return who_first

def space_check(board, position):
    if board[position] == 'X' or board[position] == 'O':
        return False
    return True

def full_board_check(board):
    for i in range(1,10):
        isEmpty=space_check(board,i)
        if isEmpty:
            return False
    return True

def player_choice(board):
    pos=place_pos()
    check=space_check(board,pos)
    if not check:
        print('The current position is occupied!')
        pos=place_pos()
    return pos

def replay():
    choice=input('Do you want to replay? Type Y for Yes or N for No: ')
    while choice not in ['Y', 'N']:
        choice=input('Invalid choice! Only Y or N: ')
    if choice== 'N':
        return False
    return True

def player_turn(board,marker,marker_No):
    key=list(marker_No.keys())
    value=list(marker_No.values())
    pos=player_choice(board)
    place_marker(board,marker,pos)
    display_board(board)
    print("\n")
    if win_check(board, marker) and marker==value[0] and key[0]== '1':
        print('Player 1 win!')
        return False
    if win_check(board, marker) and marker==value[0] and key[0]== '2':
        print('Player 2 win!')
        return False
    if full_board_check(board):
        print('Board is full! Drawwwww.')
        return False
    return True