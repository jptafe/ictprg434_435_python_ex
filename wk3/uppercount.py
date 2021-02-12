# Method to count the number of uppercase
# letters in a String argument and return the count
def countUpper(str):
    # Start with no uppercase letters so far
    count = 0
    
    # For each character in the argument
    for ch in str:
        # Add one if it is an uppercase letter
        if ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            count = count + 1
            
    # Return the number of uppercase letters found
    return count 

print(countUpper("TAFE Queensland"))

sentence = input("Enter a line of text: ")
cnt = countUpper(sentence)
print("That has ", cnt, " uppercase letters")
