# Write a Python program to compute the sum of the ASCII values 
# of the "upper-case" characters in 
# a given string.
def ascii_summer(x):
    sum=0
    for i in range(len(x)):
        if ord(x[i])>=65 and ord(x[i])<=90:
            p=ord(x[i])
            sum=sum+p
    print(sum)

ascii_summer("JavaScript")