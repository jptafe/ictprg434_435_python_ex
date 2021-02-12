# Method to return the biggest of two integer values
def maxOfTwoValues(a, b):
  # a and b are the argument variables
  # If a is bigger, return its value
  # otherwise return b's value
  if a > b:
    return a
  else:
    return b

# Main program
x = 23
y = 98
max = maxOfTwoValues(x, y)
print("max is", max)

# Now get user input
num1 = int(input("Enter a whole num: "))
num2 = int(input("Enter a second whole num: "))
biggest = maxOfTwoValues(num1, num2)
print("The biggest is: ", biggest)
