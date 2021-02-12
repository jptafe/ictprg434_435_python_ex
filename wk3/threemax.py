# Return the biggest of three integers
def threeMax(x,y,z):
    if x > y and x > z:
        return x
    if y > z and y > x:
        return y
    if z > x and z > y:
        return z
    
    
# Main program
a = 12
b = 6
c = 8
answer = threeMax(a,b,c)
print(answer)

# The following shows that we don't have to
# store the return result into a variable.
# We can use the return value immediately.
print(threeMax(4,6,7))
