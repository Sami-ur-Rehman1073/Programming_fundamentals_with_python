# Write a Python program that accepts a list of integers and 
# calculates the length and the fifth element. 
# Return true if the length of the list is 8 and the fifth element occurs thrice in the said list.
x=[]
def double_string_operation(x):
    count=0
    for i in range(len(x)):
        count+=1
        if i==4:
            num=x[i]
    print(count)
    count_2=0
    for i in range(len(x)):
        if x[i]==num:
            count_2+=1
    print(count_2)
    if count_2==3:
        print("True")
    else:
        print("False")

double_string_operation([1,2,3,4,5,5,5,6,7,8])   