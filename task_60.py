# Write a Python program to find the indices of the 
# closest pair from a list of numbers.

def closest_number_finer(x):
    list=[]
    min=10000000000
    index_first_number=0
    index_second_number=0
    for i in range(len(x)):
        for j in range(len(x)):
            if x[i]>x[j]:
                p=x[i]-x[j]
            if x[i]<x[j]:
                p=x[j]-x[i]
            if x[i]==x[j]:
                p=0
            if p<min and p!=0:
                min=p
                index_first_number=i
                index_second_number=j
    list.append(index_first_number)
    list.append(index_second_number)
    print(list)

closest_number_finer([0.21, 11.3, 2.01, 8.0, 10.0, 3.0, 15.2])