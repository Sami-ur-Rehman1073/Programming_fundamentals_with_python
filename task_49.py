# Write a Python program to remove duplicates 
# from a list of integers, preserving order.

def duplicate_remover(x):
    list=[]
    for i in range(len(x)):
        if x[i] not in list:
            list.append(x[i])
    print(list)

duplicate_remover([10, 11, 13, 23, 11, 25, 23, 76, 99])