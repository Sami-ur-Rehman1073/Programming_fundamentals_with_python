# Write a search Python program to find the indices
# of two numbers that sum to 0 
# in a given list of numbers.
def zero_sum_checker(x):
    index_1=0
    con="true"
    for i in range(len(x)):
        p=x[i]
        index_2=0
        for j in range(len(x)):
            if x[j]+p==0:
                con="true"
                print(index_1,index_2)
            index_2+=1
        index_1+=1
        if x[j]+p!=0:
            con="false"
        if con=="true":
            break
zero_sum_checker([1, -4, 6, 7, 4])