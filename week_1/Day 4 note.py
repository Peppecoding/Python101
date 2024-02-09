def looper():
    numbers = [4, 2, 7, 5, 4, 3, 2]
    
    # Looping through the list of numbers
    for i in range(len(numbers)):
        # If the current number is 3, print "skipping" and stop the loop
        if numbers[i] == 3:
            print("skipping")
            break
        # Otherwise, print the position and the number at that position
        else:
            print(f"Position {i}: {numbers[i]}")

# Calling the function to execute the code
looper()

# loops inside functions

def fizzbuzz(n):
  for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
      print("FizzBuzz")
    elif i % 3 == 0:
      print("Fizz")
    elif i % 5 == 0:
      print("Buzz")
    else:
      print(i)

# add the number
fizzbuzz(100)

