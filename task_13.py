# write a python program which gives 
# perfect order of pranthesis after accepting 
# an unarranged string of pranthesis.
def arranger(x):
    list=[]
    q=0
    count_right_brackets=0
    count_left_brackets=0
    for i in range(len(x)):
        if x[i]=="(":
            count_right_brackets+=1
        if x[i]==")":
            count_left_brackets+=1
    if count_right_brackets>count_left_brackets:
        p=count_left_brackets
        q=count_right_brackets-count_left_brackets
        r="("
    if count_left_brackets>count_right_brackets:
        p=count_right_brackets
        q=count_left_brackets-count_right_brackets
        r=")"
    if count_left_brackets==count_right_brackets:
        p=count_left_brackets
    for i in range(p):
        list.append("()")
    if q>=1:
        for j in range(q):
            list.append(r)
    print(list)

    
    

arranger("()(()()())(((())))(())((()")