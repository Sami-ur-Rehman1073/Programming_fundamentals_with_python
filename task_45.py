# Write a search Python program to find the indices 
# of two entries that show that the list is not in increasing order.
# If there are no violations (they are increasing), return an empty list.

def index_finder(x):
    list=[]
    index=0
    p=x[0]
    for i in range(1,len(x)):
        if p>x[i]:
            list.append(index)
            list.append(index+1)
        p=x[i]
        index+=1
    print(list)

index_finder([-3, -2, -3, 0, 2, 3, 4])