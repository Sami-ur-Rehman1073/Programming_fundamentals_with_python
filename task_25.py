# Write a Python program to find x that minimizes the mean squared deviation 
# from a given list of numbers.
def mean_finder(x):
    sum=0
    for i in range(len(x)):
        p=x[i]
        sum=sum+p
    mean=sum/(len(x))
    print(mean)

mean_finder([4, -5, 17, -9, 14, 108, -9])