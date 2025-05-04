#  Write a Python program to check, for each string in a given list,
#  whether the last character is an isolated letter or not.
#  Return True otherwise False.
def isolation_checker(x):
    list=[]
    for i in range(len(x)):
        p=x[i]
        q=len(x[i])
        if p[q-2]==" ":
            list.append("True")
        if p[q-2]!=" ":
            list.append("False")    
    print(list)

isolation_checker(['ca t', 'car', 'fea r', 'cente r'])
