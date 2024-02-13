import random

# Function to roll the dice
def roll_dice():
    # Generate a random number between 1 and 6
    roll = random.randint(1, 6)
    
    # Check if the roll is 6
    if roll == 6:
        print("Congrats! Move 2 spaces!")
    else:
        print("Try again!")

# Call the roll_dice function
roll_dice()
