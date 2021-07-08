Card Class : to create object of the card ie . "Two of hearts". In order to compare rank use dictionary to correspond with the int value 

Deck Class:
- Instantiate a new deck
-- Create all 52 cards
-- Hold as a list of Card objects

- Shuffle a Deck through a method call
-- Random library shuffle() function

- Deal cards from the Deck object
-- Pop method from cards list

- Deck class will holds a list of Card objects
- Deck class will return Card class object instances

Player Class : 
- use to hold a player's current list of cards
- A player should be able to add or remove cards from their 'hand'(list of card objects)
- player should be able to add a single card or multiple cards to their list
-- perform one method call
- Translate a Deck/Hand of cards with a top and bottom
--- list move left-to-right so w indexing we can use most left and most right as our top and bottom respectively


Game Logic : 
- Create two instances of the class player : 'Player one' & 'Player two'
- Create an instance of a new Deck
- Prior to split the deck to player; ensure shuffle is triggered
- split cards : for loop stack half the deck to p1 and half the deck to p2
- game starter : check if somebody has already lost the game. if length of the list == 0 game_on = False
- in game :
-- draw 2 cards (one from each player)
-- compare the cards
-- player w higher card value won and get both card to be added in their deck
--- in case of war triggered (where both player issued same card)
---- while at_war 
----- if one > two, then add card to one, at_war = False
----- if one < two , then add card to two, at_war = False
----- else, check if player have enough cards, then draw additional cards
