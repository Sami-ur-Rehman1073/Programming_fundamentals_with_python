# Given a string consisting of whitespace and 
# groups of matched parentheses, write a Python program to split it into 
# groups of 
# perfectly matched parentheses without any whitespace.
def without_spaces(x):
    count_1=0
    count_2=0
    string=''
    list=[]
    for i in range(len(x)):
        if x[i]=="(":
            string=string+x[i]
            count_1+=1
        if x[i]==')':
            string=string+x[i]
            count_2+=1
        if count_1==count_2 and string!='':
            list.append(string)
            count_1=0
            count_2=0
            string=''
    print(list)

without_spaces("( ) ( ()()() ) (( ))")