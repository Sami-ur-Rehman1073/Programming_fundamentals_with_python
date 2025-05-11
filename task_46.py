# A python program which tells how much a highest 
# number is repeated consecutive 

def consecutive_number_teller(x):
    p=x[0]
    count=1
    max=0
    max_count=1
    for i in range(1,len(x)):
        if p==x[i]:
            count+=1
        if count>max_count:
            max=x[i] 
            max_count=count
        if p!=x[i]:
            count=1
        p=x[i]
    print(max)
    print(max_count)

consecutive_number_teller([3, 1, 4, 17, 5, 17, 2, 1, 41, 32, 2, 5, 5, 5, 5])