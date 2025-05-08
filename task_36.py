# Write a  Python program to determine which 
# triples sum to zero from a given list of lists.

def zero_sum_finder(x):
    list=[]
    for k in range(len(x)):
        sum=0
        for i in range(3):
            sum=sum+x[k][i]
        if sum==0:
            list.append("True")
        if sum!=0:
            list.append("False")    
    print(list)

zero_sum_finder([[1, 2, -3], [-4, 0, 4], [0, 1, -5], [1, 1, 1], [-2, 4, -1]])    