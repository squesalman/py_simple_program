Milestone 2 Project

Blackjack Game
1. we will have computer dealer and human player
2. start w normal deck.
  - Create representation of deck
  - Computer dealer
  - human player
    -- human player will have a bankroll
      --- can place bet
  - Deal 2 cards (from deck) to dealer and player
    -- dealer - 1 face up and 1 face down
    -- player - both face up
  - Goal : To get closer to the total value of 21 than the dealer does
    -- total value is the total value of face up cards
  - Possible Actions :
    -- 'Hit' (Receive another card)(from the deck)
    -- Stay (Stop receiving card)
  - After player turn : 
    -- if value < 21, dealer hits until they win or bust (value over 21)
    --- how to access value from Card object?
  - End game logic : 
    - Player Bust
      -- if player keep hitting and value > 21, they bust and lost the bet (money reduce) ; dealer collect money
    - Computer beats Player
      -- if player.value < 21 , dealer keep on hitting until they win or bust
      -- computer.value > player.value and sums still below 21, then computer wins
    - Player win
      -- 
  Special Rules : 
  - Face cards count as a value of 10
  - Aces can count as either 1 or 11 (whicever value is preferable to the player)
  - 