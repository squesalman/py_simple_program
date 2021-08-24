from blackjack import *

if __name__ == "__main__":
  # Game Setup
  deck = Deck()
  deck.shuffle()

  player = Hand()
  dealer = Hand()
  
    
  game_on = True
  while game_on:
    
    for i in range(2):
      player.add_card(deck.deal_card())
      dealer.add_card(deck.deal_card())

    
    # check for value
    



