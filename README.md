# Rock Paper Scissors

This is the boilerplate for the Rock Paper Scissors project. Instructions for building your project can be found at https://www.freecodecamp.org/learn/machine-learning-with-python/machine-learning-with-python-projects/rock-paper-scissors

# Overview of Tactics
The code uses a pattern recognition approach to counter specific players in the Rock-Paper-Scissors game. It does so by identifying the opponent's play patterns and then selecting the optimal move to counter their predicted behavior.

`Default Play:` If no specific pattern is detected for the opponent, the code defaults to playing "Rock." Using this strategy for the first 10 round we have a clue of the strategy our opponent is using.

## Opponent-Specific Tactics

### Quincy:

`Pattern:` Quincy follows a fixed pattern of moves: Rock, Paper, Paper, Scissors, Rock.

`Detection:` The code checks if the opponent's first 10 moves match this pattern.

`Counter Strategy: `Once Quincy is detected, the code predicts Quincy's next move based on his fixed pattern and counters it. For example, if the next predicted move is Paper, the counter move will be Scissors.

### Mrugesh:

`Pattern:` Mrugesh has a tendency to play "Paper" very frequently after the first few rounds, with a specific sequence of "R, R, P, P, P, P, P, P, P, P".

`Detection:` The code checks if the first 10 moves match this pattern.

`Counter Strategy:` Upon detecting Mrugesh, the code identifies the most frequent move in Mrugesh's recent history (especially the last 5 moves) and plays the counter move. 

### Kris:

`Pattern:` Kris consistently plays "Paper" for 10 consecutive rounds.

`Detection:` The code checks if the last 10 moves are all "Paper".

`Counter Strategy: `Once Kris's pattern is detected, the player switches to a counter-strategy: Kris plays the move that should have won last round

### Abbey:

`Pattern:` Abbey’s behavior is inferred based on the opponent's last two moves, and the code assumes Abbey will play the move that counters the player’s previous response.

`Detection:` The code tracks the frequency of pairs of consecutive moves and uses this to predict Abbey’s next move.

`Counter Strategy:` The player counters Abbey by predicting Abbey’s expected move and then playing the move that would beat Abbey’s expected choice.

### Problem

The test chooses the player to play against randomly. My code detects the strategy to use correctly for the first 3 players but when it comes to Abbey, since the pattern is the same as Kris we can't tell what strategy to use, also a combined strategy was impossible to develop since they have completely different playstyle. 
