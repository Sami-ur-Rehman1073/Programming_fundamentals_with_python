#  Write a Python program to 
# find a list of integers containing exactly four distinct values, 
# such that no integer repeats twice 
# consecutively among the first twenty entries.
distinct_elements=[]
def repition_checker(x):
    p=0
    for i in range(len(x)):
        if x[i] not in distinct_elements:
            distinct_elements.append(x[i])
        if p==x[i]:
            print("False")
            break
        p=x[i]  
    if len(distinct_elements)==4 and p==x[i]:
       print("True")
    if len(distinct_elements)!=4:
       print("False")

repition_checker([1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4])
