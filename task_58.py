# Write a Python program to find the sum of the even elements 
# that are at odd indices in a given list.

def odd_index_sum_finder(x):
    sum=0
    for i in range(len(x)):
        if i%2!=0 and i!=0:
            sum=sum+x[i]
    print(sum)

odd_index_sum_finder([1, 2, 8, 3, 9, 4])