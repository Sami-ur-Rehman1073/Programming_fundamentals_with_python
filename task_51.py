# Write a Python program to find an integer exponent x such that a^x = n.

def exponent_finder(a,n):
    product=a
    x=1
    for i in range(1,n):
        if product==n:
            break
        product=product*a
        x+=1
    print(x)                 

exponent_finder(3,1290070078170102666248196035845070394933441741644993085810116441344597492642263849)