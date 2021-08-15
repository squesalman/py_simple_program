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
    return f'{self.rank} of {self.suit}'


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
    for i in range(len(self.cards)):
      if self.cards[i][0:2] == "Ace":
        pass
    if self.value <= 10 :
      self.aces = 11
    else:
      self.aces = 1
    return self.aces

class Chips:

  def __init__(self):
    self.balance = 1000
    self.bet = 0

  def win_bet(self):
    self.balance = self.balance + self.bet

  def lose_bet(self):
    self.balance = self.balance - self.bet

  

def take_bet():
  while True:
    try:
      bet = int(input("Enter bet :"))
      break
    except ValueError:
      print('Enter num only')
  return bet

def hit(Deck,Hand):
  #Need to have condition to check for Aces
  return Hand.add_card(Deck.deal_card())

def check_for_aces(Hand):
    for i in range(len(Hand.cards)):
        a = Hand.cards[i]
        if a.rank == "Ace":
          return True
        else:
          return False
