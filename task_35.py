#  Write a search Python program to find the 
# largest integer divisor of a number n 
# that is less than n.

def divisor_finder(x):
    max=0
    for i in range(1,x):
        if x%i==0:
            n=i
            if n>max:
                max=n
    print(max)

divisor_finder(27)