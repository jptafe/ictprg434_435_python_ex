import sys

# Method that takes two Strings and returns True
# if they are the same, False otherwise
def sameStrings(s1, s2):
    # Different if lengths don't match
    if len(s1) != len(s2):
        return False
        
    # Walk across both Strings
    for i in range(0, len(s1)):
        # Compare characters
        if (s1[i] != s2[i]):
            return False
        
    # We fell out of the loop; all characters
    # must therefore be the same
    return True

# Main program
a = sys.argv[1]
b = sys.argv[2]
if sameStrings(a,b):
    print("Same")
else:
    print("Different")
