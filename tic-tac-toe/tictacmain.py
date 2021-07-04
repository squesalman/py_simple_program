from tictactoe import *

if __name__ == "__main__":
  print('WELCOME to TIC TAC TOE')

  while True:
    game_board = ['']*9
    player1,player2 = user_input()
    turn = start_first()
    print(f"{turn} will go first")

    try:
      play_game = input("Are you ready to play : 'Y' or 'N'")
      play_game = play_game.capitalize()[0]
      if play_game == 'Y':
        game_on = True
      else:
        game_on = False
    except : 
      print('Error occur')
    
    while game_on:
      if turn == 'Player 1':
        print(f'{player1} turns to play')
        position = choose_position(game_board)
        update_board(player1,position,game_board)
        display_board(game_board)
      
        if check_win(game_board,player1):
          display_board(game_board)
          print(f"{player1} have won the game!")
          game_on = False
        else:
          if check_board_full(game_board):
            display_board(game_board)
            print("Game is a draw")
            break
          else:
            turn = 'Player 2'
        
      else:
        print(f'{player2} Turns to play')
        position = choose_position(game_board)
        update_board(player2,position,game_board)
        display_board(game_board)
      
        if check_win(game_board,player2):
          display_board(game_board)
          print(f"{player2} have won the game!")
          game_on = False
        else:
          if check_board_full(game_board):
            display_board(game_board)
            print("Game is a draw")
            break
          else:
            turn = 'Player 1'
    if not replay():
      break


