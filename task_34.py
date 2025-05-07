# Write a Python program to find the 
# largest k numbers from a given list of numbers.

def largest_finder(x,k):
    x.sort(reverse=True)
    p=[]
    for i in range(k):   
        p.append(x[i])
    print(p)
            
largest_finder([1, 2, 3, 4, 5, 5, 3, 6, 2],3)