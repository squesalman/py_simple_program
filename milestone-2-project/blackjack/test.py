from blackjack import *
player = Player("Shafique")
deck = Deck()
deck.shuffle()
for i in range(2):
  player.receive_card(deck.deal_card())
# get_answer = True
# while get_answer:
  
#   try:
#     ans = int(input(f"{player.name} enter 1-hit or 2-stay"))
#     if ans == 1:
#       player.receive_card(deck.deal_card())
#       break
#     elif ans == 2:
#       break
#     else:
#       print("enter '1' or '2' only")
#   except ValueError:
#     print("enter number only")
# print(len(player.in_hand))
print(player.in_hand[0])
deck.deck.val