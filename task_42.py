#  Given an array of numbers representing a branch on a binary tree, 
# write a search Python program to find the minimum even value and its index. 
# In the case of a tie, return the smallest index. 
# If there are no even numbers, the answer is [].

def smallest_index_finder(x):
    min_value=10000000000000000000000
    min_index=0
    index=0
    list=[]
    for i in range(len(x)):
        if x[i]%2==0:
            if x[i]<min_value:
                min_value=x[i]
                min_index=index
        index+=1
    if min_value!=10000000000000000000000:
        list.append(min_value)
        list.append(min_index)
    print(list)

smallest_index_finder([1, 7, 7, 5, 9])       