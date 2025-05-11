#  Write a Python program to find numbers that are greater than 10 
# and have odd first and last digits.

def first_and_last_odd_numbers(x):
    list=[]
    for i in range(len(x)):
        p=str(x[i])
        if len(p)>1:
            q=int(p[0])
            r=int(p[len(p)-1])
            if q%2!=0 and r%2!=0:
                list.append(x[i])
    print(list)  

first_and_last_odd_numbers([11, 31, 77, 93, 48, 1, 57])       