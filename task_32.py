# Write a Python program to find the sum of the numbers in 
# a given list among the 
# first k with more than 2 digits.

def sum_finder(x,k):
    sum=0
    index=0
    for i in range(len(x)):
        p=str(x[i])
        if (len(p))>2:
            q=int(p)
            sum+=q
        if index==k-1:
            break
        index+=1
    print(sum)

sum_finder([114, 215, -117, 119, 14, 108, -9, 12, 76],2)       