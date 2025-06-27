# Write a Python program to find the following strange sort 
# of list of numbers: the first element is the smallest,
# the second is the largest of the remaining, 
# the third is the smallest of the remaining, the fourth is the smallest 
# of the remaining, etc.

def strange_pattern(nums):
    final_list=[]
    x = []
    for i in nums:
        if i not in x:
            x.append(i)    
    while x != []:
        if len(x) != 1:
            final_list.append(min(x))
            final_list.append(max(x))      
            x.remove(min(x))
            x.remove(max(x))
        else:
            final_list.append(x[0])
            x.remove(x[0])

    return final_list

print(strange_pattern([27, 3, 8, 5, 1, 31]))