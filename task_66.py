# Given a list of numbers and a number to inject, write a Python program to 
# create a list containing that number in between each pair 
# of adjacent numbers.

def separting_number(list,separator):
    modified_list=[]
    for i in range(len(list)):
        if i==len(list)-1:
            modified_list.append(list[i])
        else:
            modified_list.append(list[i])
            modified_list.append(separator)
    print(modified_list)

separting_number([1, 2, 3, 4, 5, 6],9)