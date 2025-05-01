# Write a Python program to check a given list 
# of integers where the sum of the first i integers is i.
def sum_checker(x):
    sum=0
    for i in range(len(x)):
        sum=sum+x[i]
    if sum==len(x):
        print("True")
    else:
        print("False")

sum_checker([1,1,1,1,1])