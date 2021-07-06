import random
# Get User Input
def user_input():
  p2 = ''
  while True:

    p1 = input("Choose 'X' or 'O' : ")
    p1 = p1.capitalize()
    if p1 == 'X' or p1 == 'O':
      break
    else:
      print("enter 'X' or 'O' only")

  if p1 == 'X':
    p2 = 'O'
  else:
    p2 = 'X'
  return p1,p2

def display_board(board):
  try:
    print('   |   |')
    print(' ' + board[0] + '  | ' + board[1] + '  | ' + board[2])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[3] + '  | ' + board[4] + '  | ' + board[5])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[6] + '  | ' + board[7] + '  | ' + board[8])
    print('   |   |')
    
  except IndexError:
    print('Index out of range')

def choose_position(board):
  position = 'wrong'

  while position not in ['1','2','3','4','5','6','7','8','9']:
  
    try:
      position = int(input('Enter position from 1-9'))
      if position == 0:
        print("0 is not allowed")
        position = 'wrong'
      elif board[position-1] in ['X','O']:
        print('position occupied')
        position = 'wrong'
      else:
        break
    except ValueError:
      print('enter valid number')
    except IndexError:
      print('number out of bound')

  return int(position)-1

def update_board(marker,position,board):
  board[position] = marker
  return board

def check_win(board,marker):
  return board[0] == marker and board[1] == marker and board[2]== marker or board[3] == marker and board[4] == marker and board[5]== marker or board[6] == marker and board[7] == marker and board[8]== marker or board[0] == marker and board[3] == marker and board[6]== marker or board[1] == marker and board[4] == marker and board[7]== marker or board[2] == marker and board[5] == marker and board[8]== marker or board[0] == marker and board[4] == marker and board[8]== marker or board[2] == marker and board[4] == marker and board[6]== marker

def start_first():
  if random.randint(0,1) == 0:
    return 'Player 1'
  else:
    return 'Player 2'

def check_board_full(board):
  full = True
  for items in board:
    if '' in board:
      full = False
  return full


def replay():
  while True:
    replay = input("do you want to play again? Enter 'y' or 'n' : ")
    replay = replay.capitalize()
    if replay == 'Y' or replay == 'N':
      break
    else:
      print('enter y or n')
  
  if replay == 'Y':
    return True
  else:
    return False