# Write a Python program to find the indices of three
# numbers that sum to 0 
# in a given list of numbers.

from itertools import combinations
def zero_sum_dectector(a):
    zero_sum_index=[]
    d=[]
    comb=combinations(a,3)
    b=list(comb)
    for i in range(len(b)):
        sum=0
        c=(b[i])
        for j in range(len(c)):
            sum+=c[j]
            if sum==0:
                for k in range(len(c)):
                    d.append(c[k])
    for i in range(len(a)):
        for j in range(len(d)):
            if a[i]==d[j]:
                p=i 
                if p not in zero_sum_index:
                    zero_sum_index.append(p)
    print(zero_sum_index)

zero_sum_dectector([12, -7, 3, -89, 14, 4, -78, -1, 2, 7])