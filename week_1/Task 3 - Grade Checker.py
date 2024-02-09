# Ask for a grade and then convert it to a letter grade.
grade = int(input("What is your numerical grade? "))

# Determine the letter grade and the points to the next grade.
if grade >= 90:
    letter = 'A'
    points_to_next = "You are at the top grade."
elif grade >= 80:
    letter = 'B'
    points_to_next = f"You need {90 - grade} more points to reach an A."
elif grade >= 70:
    letter = 'C'
    points_to_next = f"You need {80 - grade} more points to reach a B."
elif grade >= 60:
    letter = 'D'
    points_to_next = f"You need {70 - grade} more points to reach a C."
else:
    letter = 'F'
    points_to_next = f"You need {60 - grade} more points to reach a D." if grade > 0 else "You need to start gaining points!"

# Print out the results.
print(f"Your letter grade is {letter}.")
print(points_to_next)