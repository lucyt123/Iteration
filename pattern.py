# Define an algebreic variable
a = 4

# Create a singular for loop that iterates the '*' over 9 lines
for i in range(0,9):
# Create an if condition where if the number counted is lower than 5, it 
# prints the iteration multiplied by the '*' variable plus 1
    if i < 5:
        print('*'*(i+1))
# Prints '*' multiplied by the algebreic variable 
    else:
        print('*'*a)
# This allows the '*' to step down 1 in scale as the lines continue
        a = a -1
