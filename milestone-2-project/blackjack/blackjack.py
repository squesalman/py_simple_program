import random
import math

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card():
  """Has 2 attributes suit and rank. card object will be used to instantiate deck class"""
  def __init__(self,suit,rank):
    self.suit = suit
    self.rank = rank
    self.value = values[rank]

  def __str__(self):
    try:
      return f'{self.rank} of {self.suit}'
    except IndexError:
      return "index out of range"


class Deck():
  """class to hold 52 cards objects"""
  def __init__(self):
    self.deck = []

    for suit in suits:
      for rank in ranks:
        created_card = Card(suit,rank)
        
        self.deck.append(created_card)

  def deal_card(self):
    return self.deck.pop()

  def shuffle(self):
    random.shuffle(self.deck)
  
  def __str__(self):
    
    for i in range(len(self.deck)):
      print(f"cards: {self.deck[i]}")
    #   print(f'card : {self.deck[item]}')
    return f'total cards : {len(self.deck)}'

  

class Hand:
  """class to create player's card in hand object"""
  def __init__(self):
    self.cards = []
    self.value = 0
    self.aces = 0


  def add_card(self,card):
    self.cards.append(card)
    self.value += card.value

  def adjust_for_aces(self):
    # Check condition if aces in list
    # Check condition total value in deck
    if self.value > 21 :
      self.aces = 1
    else:
      self.aces = 11
    return self.aces

class Chips:

  def __init__(self):
    self.balance = 1000
    self.bet = 0

  def win_bet(self):
    self.balance = self.balance + self.bet

  def lose_bet(self):
    self.balance = self.balance - self.bet

"""Function to take bet"""
def take_bet(Chips):
  
  check = True
  while check:
    try:
      bet = int(input("Enter bet :"))
      if bet > Chips.balance:
        print("Amount more than balance. Pls re-enter")
        check = True
      else:
        break
    except ValueError:
      print('Enter num only')
  return bet

"""Function to hit"""
def hit(deck,hand):
  # Function will be used when player request or dealer's hand less than 17
  # Either player can take hits until they bust
  #Need to have condition to check for Aces
  hand.add_card(deck.deal_card())

"""Function to check for aces"""
def check_for_aces(Hand):

    for i in range(len(Hand.cards)):
        a = Hand.cards[i]
        if a.rank == "Ace":
          return True
        else:
          return False

def hit_or_stand(deck,hand):

    global playing  # to control an upcoming while loop
    while True:
      check_hit = input("Hit or Stand?")
      if check_hit[0].capitalize() == 'H' or check_hit[0].capitalize() == 'S':
        break
      else:
        print('Enter correct input')

    if check_hit[0].upper() =='H':
      hit(deck,hand)
    else:
      playing = False

"""Function to show player's cards and some of dealer's card"""
def show_some(player,dealer):

  for i in range(len(player.cards)):
    print(f'player cards {i} {player.cards[i]}')
  print(f'player score : {player.value}\n')
  for i in range(len(dealer.cards)-1):
      print(f'dealer cards {i} : {player.cards[i]}')
  print(f'dealer score : {dealer.cards[i].value}')
  

deck=Deck()
deck.shuffle()
hand=Hand()
dealer = Hand()
