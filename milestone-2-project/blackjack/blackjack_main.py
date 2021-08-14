from blackjack import *

if __name__ == "__main__":
  # Game Setup
  deck = Deck()
  deck.shuffle()

  player = Chips()
  def take_bet():
    
  game_on = True
  print(f"{player.name} will have {player.balance} for starter")
  while game_on:
    
    for i in range(2):
      player.receive_card(deck.deal_card())
      dealer.receive_card(deck.deal_card())
    
    print(f"{player.name} have {player.in_hand[0]} and {player.in_hand[1]} and sum is")
    print(f"{dealer.name} have {dealer.in_hand[0]}")

    get_answer = True
    while get_answer:
      try:
        ans = int(input(f"{player.name} enter 1-hit or 2-stay"))
        if ans == 1:
          player.receive_card(deck.deal_card())
          break
        elif ans == 2:
          break
        else:
          print("enter '1' or '2' only")
      except ValueError:
        print("enter number only")
    
    # check for value
    



