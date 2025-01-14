#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2023, Pending. Some rights reserved.
# Jesse B.
# Mr. 5 x 5 Productions presents
# Kaprekards
# Application: Kaprekards App.
# Description: Card sorting game based on Kaprekar's constant.
# Testing Validation: .
# Development Environment: VS Code
# Version: Python 3.9.15 / 3.11.3
# Solution File: tinker_week14_v23.py
# Date: 04/29/23

import random

def arrange_cards(cards):
    # arrange cards to form the largest and smallest numbers possible
    largest_num = int(''.join([str(x) for x in sorted(cards, reverse=True)]))
    smallest_num = int(''.join([str(x) for x in sorted(cards)]))
    return largest_num, smallest_num

def play_game(num_players, max_games):
    # initialize the game
    players = [f"Player {i+1}" for i in range(num_players)]
    current_game = 0
    winner = None
    max_iterations_played = 0
    scores = {player: 0 for player in players}

    # loop until the maximum number of games is reached
    while current_game < max_games:
        print(f"Game {current_game+1}:")
        # each player plays one round
        for player in players:
            print(f"{player}'s turn:")
            cards = [random.randint(0, 9) for _ in range(4)]
            if player == players[0]:
                print(f"Cards dealt: {cards}")

            # arrange cards and compute the score
            largest_num, smallest_num = arrange_cards(cards)
            score = largest_num - smallest_num

            # print column headers (only once per player's turn)
            if player == players[0]:
                print("Hand".ljust(16), "Descending".ljust(16), "Ascending".ljust(16), "Difference".ljust(16))
                print("-" * 64)

            # iterate until the score reaches 6174
            num_iterations = 0
            hand = cards.copy()
            while score != 6174:
                descending = str(largest_num).ljust(16)
                ascending = str(smallest_num).ljust(16)
                difference = str(score).ljust(16)

                hand_str = str(hand).ljust(16)

                print(f"{hand_str}{descending}{ascending}{difference}")

                largest_num, smallest_num = arrange_cards(str(score).zfill(4))
                score = largest_num - smallest_num
                num_iterations += 1

                hand = [score // 1000, (score // 100) % 10, (score // 10) % 10, score % 10]

            # print final result's column
            descending = str(largest_num).ljust(16)
            ascending = str(smallest_num).ljust(16)
            difference = str(score).ljust(16)

            hand_str = str(hand).ljust(16)

            print(f"{hand_str}{descending}{ascending}{difference}")
            print()

            scores[player] += num_iterations

        current_game += 1

    # determine the winner
    for player, score in scores.items():
        if score > max_iterations_played:
            max_iterations_played = score
            winner = player

    # print the results of the game
    print(f"{winner} wins with {max_iterations_played} iterations!")
    print("Final scores:")
    for player, score in scores.items():
        print(f"{player}: {score}")


if __name__ == '__main__':
    play_game(num_players=2, max_games=3)
