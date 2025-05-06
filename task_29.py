# Write a search Python program to find a list of strings that have 
# fewer total characters (including repetitions).
def character_count(x):
    count_1=0
    count_2=0
    for j in range(len(x[0])):
        p=x[0][j]
        for k in range(len(p)):
            if p[k]==" ":
                count_1+=0
            count_1+=1

    for j in range(len(x[1])):
        p=x[1][j]
        for k in range(len(p)):
            if p[k]==" ":
                count_2+=0
            count_2+=1
    if count_1>count_2:
        print(x[1])
    if count_2>count_1:
        print(x[0])


character_count([['this', 'list', 'is', 'narrow'], ['I', 'am', 'shorter but wider']])