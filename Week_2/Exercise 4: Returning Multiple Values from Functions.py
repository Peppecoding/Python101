# Exercise 4: Returning Multiple Values from Functions

# Write a function named calculate_statistics that takes a list of numbers as input and returns a tuple containing the mean and median of the numbers.

def calculate_statistics(numbers):
    mean = sum(numbers) / len(numbers)
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        median = (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2
    else:
        median = sorted_numbers[n//2]
    return mean, median

# Test the function with a sample list of numbers and print the result.

sample_numbers = [1, 3, 5, 7, 9]
mean, median = calculate_statistics(sample_numbers)
print("Mean:", mean)
print("Median:", median)
