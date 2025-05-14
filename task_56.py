# Write a Python program to find the number which when appended 
# to the list makes the total 0.

def zero_maker_finder(x):
    sum=0
    for i in range(len(x)):
        sum=sum+x[i]
    num=-sum
    print(num)

zero_maker_finder([-1, -2, -3, -4, 5])