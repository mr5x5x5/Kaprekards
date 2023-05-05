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

def play_game(num_players, max_iterations):
    # initialize the game
    players = [f"Player {i+1}" for i in range(num_players)]
    current_iteration = 0
    winner = None
    max_iterations_played = 0
    scores = {player: 0 for player in players}

    # loop until the maximum iterations is reached
    while current_iteration < max_iterations:
        print(f"Iteration {current_iteration+1}:")
        # each player plays one round
        for player in players:
            print(f"{player}'s turn:")
            cards = [random.randint(0, 9) for _ in range(4)]
            print(f"Cards dealt: {cards}")

            # arrange cards and compute the score
            largest_num, smallest_num = arrange_cards(cards)
            score = largest_num - smallest_num

            # print column headers
            print("Arrangement".ljust(16), "Largest".ljust(16), "Smallest".ljust(16), "Difference".ljust(16))
            print("-" * 64)

            # iterate until the maximum iterations is reached
            num_iterations = 0
            while num_iterations < max_iterations:
                # print current iteration's results
                print(str(cards).ljust(16), str(largest_num).ljust(16), str(smallest_num).ljust(16), str(score).ljust(16))

                largest_num, smallest_num = arrange_cards(str(score).zfill(4))
                score = largest_num - smallest_num
                num_iterations += 1

                # check if result is equal to (6, 1, 7, 4)
                if tuple(map(int, str(score).zfill(4))) == (6, 1, 7, 4):
                    break

            # print final result's column
            print(str(cards).ljust(16), str(largest_num).ljust(16), str(smallest_num).ljust(16), str(score).ljust(16))
            print()

            scores[player] += num_iterations

        current_iteration += 1

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
    play_game(num_players=2, max_iterations=7)
