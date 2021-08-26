import random
import math
from colorama import Fore
from colorama import Style

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
      self.value = self.value - 10
    return self.value

class Chips:

  def __init__(self):
    self.balance = 1000
    self.bet = 0

  def win_bet(self):
    self.balance = self.balance + self.bet

  def lose_bet(self):
    self.balance = self.balance - self.bet

"""Function to take bet"""
def take_bet(chips):
  check = True
  while check:
    try:
      chips.bet = int(input("Enter bet :"))
      if chips.bet > chips.balance:
        print("Amount more than balance. Pls re-enter")
        check = True
      else:
        break
    except ValueError:
      print('Enter num only')
  return chips.bet

"""Function to hit"""
def hit(deck,hand):
  # Function will be used when player request or dealer's hand less than 17
  # Either player can take hits until they bust
  #Need to have condition to check for Aces
  hand.add_card(deck.deal_card())
  if check_for_aces(hand):
    hand.adjust_for_aces()

"""Function to check for aces"""
def check_for_aces(hand):

    for i in range(len(hand.cards)):
        a = hand.cards[i]
        if a.rank == "Ace":
          return True
        else:
          return False

def hit_or_stand(deck,hand):

    global playing # to control an upcoming while loop
    while True:
      check_hit = input("Hit or Stand?")
      if check_hit[0].capitalize() =='H':
        hit(deck,hand)
        break
      elif check_hit[0].capitalize() == 'S':
        return playing == False
        break
      else:
        print('Pls Enter correct input')

"""Function to show player's cards and some of dealer's card"""
def show_some(player,dealer):

  for i in range(len(player.cards)):
    print(f'player cards {i} {player.cards[i]}')
  print(f'player score : {player.value}\n')
  for i in range(len(dealer.cards)-1):
      print(f'dealer cards {i} : {dealer.cards[i]}')
  print(f'dealer score : {dealer.value}\n')

def show_all(player,dealer):
  for i in range(len(player.cards)):
    print(f'{Fore.BLUE} player cards {i} {player.cards[i]} {Style.RESET_ALL}')
  print(f'{Fore.BLUE}player score : {player.value} {Style.RESET_ALL}\n')
  for i in range(len(dealer.cards)):
      print(f'{Fore.BLUE}dealer cards {i} : {dealer.cards[i]} {Style.RESET_ALL}')
  print(f'{Fore.BLUE}dealer score : {dealer.value} {Style.RESET_ALL}\n')
  

def player_busts(hand,hand_chips,dealer_chips):
  hand_chips.balance = hand_chips.balance - hand_chips.bet
  dealer_chips.balance = dealer_chips.balance + dealer_chips.bet + hand_chips.bet
  print(f"{Fore.RED}Bust!. Your score : {hand.value} {Style.RESET_ALL} \n")
  

def player_wins(hand,dealer,hand_chips,dealer_chips):
  hand_chips.balance = hand_chips.balance + hand_chips.bet + dealer_chips.bet
  dealer_chips.balance = dealer_chips.balance - dealer_chips.bet
  print(f"Dealer lose. Dealer score : {dealer.value} \n")
  print(f"{Fore.GREEN}Player wins! Player Score : {hand.value} Player wins bet : {hand_chips.bet + dealer_chips.bet} {Style.RESET_ALL} \n")

def dealer_busts(dealer,hand_chips,dealer_chips):
  dealer_chips.balance = dealer_chips.balance - dealer_chips.bet
  hand_chips.balance = hand_chips.balance + dealer_chips.bet + hand_chips.bet
  print(f"{Fore.RED}Dealer Bust!. Dealer score : {dealer.value} {Style.RESET_ALL} \n")
    
def dealer_wins(hand,dealer,hand_chips,dealer_chips):
  dealer_chips.balance = dealer_chips.balance + dealer_chips.bet
  hand_chips.balance = hand_chips.balance - hand_chips.bet
  print(f"Player lose. Player score : {hand.value} \n")
  print(f"{Fore.GREEN}Dealer wins! Dealer Score : {dealer.value} Dealer wins bet : {dealer_chips.bet + hand_chips.bet} {Style.RESET_ALL} \n")
    
def push():
  pass

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


