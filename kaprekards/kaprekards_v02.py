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
# Solution File: tinker_week15_v22.py
# Date: 05/05/23

import random

class CardGame:
    def __init__(self, num_players, max_games):
        self.num_players = num_players
        self.max_games = max_games
        self.players = [f"Player {i+1}" for i in range(num_players)]
        self.scores = {player: 0 for player in self.players}

    def play_game(self):
        current_game = 0
        winner = None
        max_iterations_played = 0

        while current_game < self.max_games:
            print(f"\nGame {current_game + 1}:")
            game_results = []

            for player in self.players:
                print(f"\n{player}'s turn:")
                while True:
                    cards = [random.randint(0, 9) for _ in range(4)]
                    if len(set(cards)) != 1: # exclude 4 repeating numbers.
                        break

                if player >= self.players[0]: # this may be redundant
                    print(f"Cards dealt: {cards}")

                iterations = self.play_turn(player, cards)
                self.scores[player] += iterations

            current_game += 1

        winner, max_iterations_played = self.determine_winner()

        printer = Printer()
        printer.print_final_results(winner, max_iterations_played, self.scores)

    def play_turn(self, player, cards):
        calculator = Calculator()
        iterations = 0
        game_results = []

        printer = Printer()
        printer.print_column_headers()

        while True:
            descending, ascending = calculator.arrange_cards(cards)
            score = descending - ascending

            if player == self.players[0]:
                printer.print_game_results(cards, descending, ascending, score)
            else:
                printer.print_game_results(cards, descending, ascending, score)

            if score == 6174:
                break

            iterations += 1
            cards = [int(digit) for digit in str(score).zfill(4)]

        return iterations

    def determine_winner(self):
        max_iterations_played = max(self.scores.values())
        winner = [player for player, score in self.scores.items() if score == max_iterations_played][0]
        return winner, max_iterations_played


class Calculator:
    def arrange_cards(self, cards):
        descending = int(''.join([str(x) for x in sorted(cards, reverse=True)]))
        ascending = int(''.join([str(x) for x in sorted(cards)]).ljust(4, '0'))
        return descending, ascending


class Printer:
    def print_column_headers(self):
        print("Hand".ljust(15), "Descending".ljust(15), "Ascending".ljust(15), "Difference".ljust(15))
        print("-" * 64)

    def print_game_results(self, cards, descending, ascending, score):
        hand = str(cards).ljust(16)
        descending = str(descending).ljust(16)
        ascending = str(ascending).ljust(16)
        difference = str(score).ljust(16)
        print(f"{hand}{descending}{ascending}{difference}")
        
    def print_final_results(self, winner, max_iterations_played, scores):
        print(f"\n{winner} wins with {max_iterations_played} iterations!")
        print("Final scores:")
        for player, score in scores.items():
            print(f"     {player}: {score}")
        print()


if __name__ == '__main__':
    num_players = 2
    max_games = 20

    game = CardGame(num_players, max_games)
    game.play_game()
