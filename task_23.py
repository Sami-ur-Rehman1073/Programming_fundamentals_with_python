#  Write a Python program to find the indices at which 
# the numbers in the list drop.
def drop_checker(x):
    list=[]
    index=1
    p=x[0]
    for i in range(len(x)):
        if i>=1:
            if p>x[i]:
                list.append(index)
            p=x[i]
            index+=1
    print(list)

drop_checker([0, -1, 3, 8, 5, 9, 8, 14, 2, 4, 3, -10, 10, 17, 41, 22, -4, -4, -15, 0]
)     