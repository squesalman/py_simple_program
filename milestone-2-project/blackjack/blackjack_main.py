from blackjack import *

if __name__ == "__main__":
  #Opening Statement
  print("Welcome to Blackjack Game")

  # Game Setup
  
  #check for double aces during initial deal
  global player_chips
  global dealer_chips
  playing = True
  game_on = True
  while game_on:
    deck = Deck()
    deck.shuffle()

    player = Hand()
    dealer = Hand()

  
    player_chips = Chips()
    dealer_chips = Chips()
    dealer_chips.balance = 99999

    print(f"Your balance is : {player_chips.balance} \n")
    take_bet(player_chips)

    for i in range(2):
      player.add_card(deck.deal_card())
      dealer.add_card(deck.deal_card())
    
    if check_for_aces(player):
      player.adjust_for_aces()
    
    show_some(player,dealer)
    # Condition to check blackjack during initial card dealing
    if player.value == 21:
      print(f'{Fore.RED}Blackjack!{Style.RESET_ALL}')
      player_wins(player,dealer,player_chips,dealer_chips)
      break
    elif dealer.value == 21:
      print(f'{Fore.RED}Blackjack!{Style.RESET_ALL}')
      dealer_wins(player,dealer,player_chips,dealer_chips)
      break

    while playing:

      if not hit_or_stand(deck,player):
        break
      show_some(player,dealer)
      
      if player.value > 21:
        player_busts(player,player_chips,dealer_chips)
        break

  
    while dealer.value <= 17:
      hit(deck,dealer)
    # Need to identify how to manage replay once break loop
    if dealer.value > 21:
      dealer_busts(dealer,player_chips,dealer_chips)
      break
        
    show_all(player,dealer)

    if player.value > 21:
      player_busts(player,player_chips,dealer_chips)
    elif player.value > dealer.value:
      player_wins(player,dealer,player_chips,dealer_chips)
    elif player.value == 21:
      print(f"{Fore.RED}Blackjack!{Style.RESET_ALL}")
      player_wins(player,dealer,player_chips,dealer_chips)
    elif dealer.value == 21:
      print(f"{Fore.RED}Blackjack!{Style.RESET_ALL}")
      dealer_wins(player,dealer,player_chips,dealer_chips)
    else:
      dealer_wins(player,dealer,player_chips,dealer_chips)
        
    print(f"Your total Chips : {player_chips.balance}")

    if replay():
      # check for balance
      if player_chips.balance <= 10 :
        print('Insufficient balance \n')
        print('Game Over')
      # elif len(deck.deck) < 10:
      #   deck = Deck()
      #   deck.shuffle()

      #   player = Hand()
      #   dealer = Hand()

      #   for i in range(2):
      #     player.add_card(deck.deal_card())
      #     dealer.add_card(deck.deal_card())
      #   show_some(player,dealer)
      #   game_on = True
      else:
        game_on = True
        # player = Hand()
        # dealer = Hand()

        # for i in range(2):
        #   player.add_card(deck.deal_card())
        #   dealer.add_card(deck.deal_card())
        # show_some(player,dealer)
        
    else:
      print('Game Over')
      break
