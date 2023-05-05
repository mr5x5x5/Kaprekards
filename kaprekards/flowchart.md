"""
Create a flow chart for a game based on Kaprekar's constant, so that four number cards (0-9) are dealt to each player, and the player with the most iterations wins.
"""

"""
START

1. Deal four number cards (0-9) to each player.
2. Set the current iteration to 0.
3. Set the winner to null.

LOOP UNTIL there is a winner:
4. For each player:
    a. Arrange their four cards to form the largest and smallest numbers possible.
    b. Subtract the smallest number from the largest number.
    c. Record the result.
    d. If the result is 6174, the player wins.
5. Increment the current iteration.
6. If the current iteration is greater than the maximum allowed iterations, end the game.
7. If there is a winner, set the winner variable to the winning player and end the game.
8. Otherwise, go back to step 4.

END
"""

"""
+-----------------------+
|  Start the game        |
+-----------------------+
            |
            v
+-----------------------+
|   Deal cards to each   |
|   player (4 cards)     |
+-----------------------+
            |
            v
+-----------------------+
| Arrange the cards in   |
| ascending and          |
| descending order       |
+-----------------------+
            |
            v
+-----------------------+
|   Compute the score    |
|   (largest - smallest) |
+-----------------------+
            |
            v
+-----------------------+
| Print the arrangement, |
| largest, smallest,     |
| and difference for the |
| initial score          |
+-----------------------+
            |
            v
+-----------------------+
|   Iterate the score    |
|   until it reaches     |
|   6174 or maximum      |
|   iterations           |
+-----------------------+
            |
            v
+-----------------------+
|  Print the results for |
|  each iteration (if    |
|  not 6174)             |
+-----------------------+
            |
            v
+-----------------------+
| Print the final results|
| and declare the winner |
+-----------------------+
            |
            v
+-----------------------+
|  End the game          |
+-----------------------+
"""