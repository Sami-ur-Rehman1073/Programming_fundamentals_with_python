# We are making n stone piles! The first pile has n stones.
# If n is even, then all piles have an even number of stones. 
# If n is odd, all piles have an odd number of stones. 
# Each pile must more stones than the previous pile but as few as possible. 
# Write a Python program to find the number of stones in each pile.
def stone_finder(n):
    print("The number of piles: ",n)
    list=[]
    p=n
    for i in range(n):
        list.append(p)
        p=p+2
    print(list)
  
stone_finder(17)
