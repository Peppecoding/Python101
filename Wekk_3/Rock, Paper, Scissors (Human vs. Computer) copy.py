import random  # Imports the random module for generating random choices.

# ASCII Art representations of Rock, Paper, and Scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''  # ASCII art representation of rock.

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''  # ASCII art representation of paper.

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''  # ASCII art representation of scissors.

# Validator Class: Validates user input
class Validator:
    @staticmethod
    def validate_choice(choice):
        # Check if input is one of "R", "P", or "S"
        return choice.upper() in ["R", "P", "S"]

# Player (Human) Class: Represents a human player
class Player:
    def __init__(self, name):
        self.name = name  # Player's name
        self.score = 0    # Player's score, initialized to 0

    def choose(self):
        # Prompt player for input and validate it
        while True:
            choice = input(f"{self.name}, choose Rock (R), Paper (P), or Scissors (S): ")
            if Validator.validate_choice(choice):
                # Map short choices to tuples of choice names and ASCII art
                choices = {"R": ("Rock", rock), "P": ("Paper", paper), "S": ("Scissors", scissors)}
                return choices[choice.upper()]
            else:
                print("Invalid choice. Please try again.")

    def update_score(self, winner):
        # Increment score if this player is the winner
        if winner == self.name:
            self.score += 1

# ComputerPlayer Class: Represents an AI player
class ComputerPlayer:
    def __init__(self):
        self.name = "Computer"  # Computer player's name
        self.score = 0          # Computer player's score, initialized to 0

    def choose(self):
        # Randomly select between Rock, Paper, and Scissors
        choices = [("Rock", rock), ("Paper", paper), ("Scissors", scissors)]
        return random.choice(choices)

    def update_score(self, winner):
        # Increment score if this player is the winner
        if winner == self.name:
            self.score += 1

# Game Class: Manages the overall game flow
class Game:
    def __init__(self, player1, player2):
        self.player1 = player1  # First player
        self.player2 = player2  # Second player

    def play_round(self):
        # Handles process for each game round
        player1_choice, player1_art = self.player1.choose()
        player2_choice, player2_art = self.player2.choose()

        # Determine the winner of the round
        winner = self.determine_winner(player1_choice, player2_choice)

        # Announce choices and winner
        print(f"\n{self.player1.name} chose {player1_choice}.\n{player1_art}")
        print(f"{self.player2.name} chose {player2_choice}.\n{player2_art}")
        print(f"{winner} wins this round!" if winner else "It's a draw!")

        # Update scores based on round winner
        self.player1.update_score(winner)
        self.player2.update_score(winner)

        # Display current scores
        print(f"Current score: {self.player1.name} = {self.player1.score}, {self.player2.name} = {self.player2.score}")

    def determine_winner(self, player1_choice, player2_choice):
        # Classic game rules to determine winner
        win_combos = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}

        if player1_choice == player2_choice:
            return None  # It's a draw if both players choose the same
        elif win_combos[player1_choice] == player2_choice:
            return self.player1.name  # Player 1 wins
        else:
            return self.player2.name  # Player 2 wins

    def is_game_over(self):
        # Placeholder for end game logic
        pass

# Game Initialization
player1 = Player(input("What is your Name? "))  # Create a human player
player2 = ComputerPlayer()                      # Create a computer player
game = Game(player1, player2)                   # Initialize the game with two players

# Game Loop: Allows multiple rounds of play
while True:
    game.play_round()  # Play a round of the game
    # Ask if the players want to continue, break the loop
