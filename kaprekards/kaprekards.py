
import random

def arrange_cards(cards):
    # arrange cards to form the largest and smallest numbers possible
    largest_num = int(''.join(sorted(cards, reverse=True)))
    smallest_num = int(''.join(sorted(cards)))
    return largest_num, smallest_num

def play_game(num_players, max_iterations):
    # initialize the game
    players = [f"Player {i+1}" for i in range(num_players)]
    current_iteration = 0
    winner = None

    # loop until there is a winner or the maximum iterations is reached
    while not winner and current_iteration < max_iterations:
        print(f"Iteration {current_iteration+1}:")
        scores = {}

        # each player plays one round
        for player in players:
            print(f"{player}'s turn:")
            cards = [random.randint(0, 9) for _ in range(4)]
            print(f"Cards dealt: {cards}")

            # arrange cards and compute the score
            largest_num, smallest_num = arrange_cards(cards)
            score = largest_num - smallest_num
            scores[player] = score

            print(f"Largest number: {largest_num}")
            print(f"Smallest number: {smallest_num}")
            print(f"Score: {score}\n")

            # check if the player wins
            if score == 6174:
                winner = player
                break

        current_iteration += 1

    # print the results of the game
    if winner:
        print(f"{winner} wins after {current_iteration} iterations!")
    else:
        print(f"The game ended after {current_iteration} iterations with no winner.")
    print("Final scores:")
    for player, score in scores.items():
        print(f"{player}: {score}")


if __name__ == '__main__':
    play_game(num_players=2, max_iterations=10)