from wargame import *
import random

if __name__ == "__main__":
# Game Setup
  player_one = Player('Shafique')
  player_two = Player('Suhaila')

  new_deck = Deck()
  new_deck.shuffle()

  # split the card logic
  for i in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

  game_on = True

  # I dont get this part
  round_num = 0
  war = 0

  while game_on:
    
    round_num += 1
    print(f'Round : {round_num}')

    if len(player_one.in_hand) == 0 :
      print(f'{player_one.name}, out of cards, {player_two.name} wins!')
      game_on = False
      break

    if len(player_two.in_hand) == 0 :
      print(f'{player_two.name}, out of cards, {player_one.name} wins!')
      game_on = False
      break

    # Start a new round
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    at_war = True

    while at_war:
      
      if player_one_cards[-1].value > player_two_cards[-1].value:
        player_one.add_cards(player_one_cards)
        player_one.add_cards(player_two_cards)
        at_war = False
      elif player_one_cards[-1].value < player_two_cards[-1].value:
        player_two.add_cards(player_two_cards)
        player_two.add_cards(player_one_cards)
        at_war = False
      else:
        war += 1
        print('War Time!')
        if len(player_one.in_hand) < 3:
          print(f'not enough cards for {player_one.name} ')
          print(f'{player_two.name} wins! ')
          game_on = False
          break
        elif len(player_two.in_hand) < 3:
          print(f'not enough cards for {player_two.name} ')
          print(f'{player_one.name} wins! ')
          game_on = False
          break
        else:
          for num in range(3):
            player_one_cards.append(player_one.remove_one())
            player_two_cards.append(player_two.remove_one())
  
  print(f'total war :{war}')
  print(f'total Round : {round_num}')
