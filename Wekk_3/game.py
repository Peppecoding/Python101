# https://gist.github.com/wynand1004/b5c521ea8392e9c6bfe101b025c39abe

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

class Validator:
    @staticmethod
    def validate_choice(choice):
        return choice.upper() in ["R", "P", "S"]

class Player:
    def __init__(self, name):
        self._name = name
        self._score = 0

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_score(self):
        return self._score

    def set_score(self, score):
        self._score = score

    def choose(self):
        while True:
            choice = input(f"{self.get_name()}, choose Rock (R), Paper (P), or Scissors (S): ")
            if Validator.validate_choice(choice):
                choices = {"R": ("Rock", rock), "P": ("Paper", paper), "S": ("Scissors", scissors)}
                return choices[choice.upper()]
            else:
                print("Invalid choice. Please try again.")

    def update_score(self, winner):
        if winner == self.get_name():
            self.set_score(self.get_score() + 1)

class AI:
    def __init__(self):
        self._name = "Computer"
        self._score = 0

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_score(self):
        return self._score

    def set_score(self, score):
        self._score = score

    def choose(self):
        choices = [("Rock", rock), ("Paper", paper), ("Scissors", scissors)]
        return random.choice(choices)

    def update_score(self, winner):
        if winner == self.get_name():
            self.set_score(self.get_score() + 1)

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def play_round(self):
        player1_choice, player1_art = self.player1.choose()
        player2_choice, player2_art = self.player2.choose()

        winner = self.determine_winner(player1_choice, player2_choice)

        print(f"\n{self.player1.get_name()} chose {player1_choice}.\n{player1_art}")
        print(f"{self.player2.get_name()} chose {player2_choice}.\n{player2_art}")
        print(f"{winner} wins this round!" if winner else "It's a draw!")

        self.player1.update_score(winner)
        self.player2.update_score(winner)

        print(f"Current score: {self.player1.get_name()} = {self.player1.get_score()}, {self.player2.get_name()} = {self.player2.get_score()}")

    def determine_winner(self, player1_choice, player2_choice):
        win_combos = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}

        if player1_choice == player2_choice:
            return None
        elif win_combos[player1_choice] == player2_choice:
            return self.player1.get_name()
        else:
            return self.player2.get_name()

    def is_game_over(self):
        pass

player1 = Player(input("What is your Name? "))
player2 = AI()
game = Game(player1, player2)

while True:
    game.play_round()
    if input("Play another round? (y/n): ").lower() != 'y':
        break