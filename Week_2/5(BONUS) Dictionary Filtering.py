# Create a dictionary of temperatures in Celsius with days as keys
temperatures = {
    'Monday': 22, 'Tuesday': 28, 'Wednesday': 24, 'Thursday': 26,
    'Friday': 20, 'Saturday': 30, 'Sunday': 25
}
# Filter out the days where the temperature is above 25 degrees Celsius
hot_days = {day: temp for day, temp in temperatures.items() if temp > 25}

# Print out hot_days
print("Hot days:", hot_days)
