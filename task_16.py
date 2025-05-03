# Write a Python program to find strings 
# in a given list starting with a given prefix
def string_checker(string,list):
    output_string=[]
    for k in range(len(string)):
        if k==0:
            m=string[k]
        if k==1:
            n=string[k]
    for i in range(len(list)):
        p=list[i]
        if p[0]==m and p[1]==n:
            output_string.append(p)
    print(output_string)

string_checker("ca",(('cat', 'car', 'fear', 'center', 'fisca')))