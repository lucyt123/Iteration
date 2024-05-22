# Define an empty list 
numbers = []
# Define an empty string to use in the while loop
user_input = 0

# Iterates through this loop to check if user_input does not equal -1
while user_input != int(-1):
# Asks the user for a number again until -1 is reached
    user_input = int(input("Please enter a number "))
# Appends the other numbers entered into the empty list 
    numbers.append(user_input)

# Checks if the length of numbers given are enough valid input
if len(numbers) == 0:
    print("No valid input was given")
else:
# Removes -1 from the numbers list so it is not factored into the calculation 
    numbers.pop()
# Calculates average of all inputted numbers without -1
    average = sum(numbers)/len(numbers)
    print(average)

