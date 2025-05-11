#  Write a Python program to reverse the case of all strings. 
# For those strings, which contain no letters, 
# reverse the strings.

def reverse_the_case(x):
    list=[]
    for i in range(len(x)):
        p=x[i]
        string=""
        if (ord(p[0])>=65 and ord(p[0])<=90) or (ord(p[0])>=97 and ord(p[0])<=122):
            for j in range(len(p)):
                if ord(p[j])>=65 and ord(p[j])<=90:
                    q=(ord(p[j]))+32
                    r=chr(q)
                    string+=r
                if ord(p[j])>=97 and ord(p[j])<=122:
                    q=(ord(p[j]))-32
                    r=chr(q)
                    string+=r
            list.append(string)
        else:
            for j in range(len(p)-1,-1,-1):
                string+=p[j]
            list.append(string)
    print(list)
            
reverse_the_case(['Hello', '!@#', '!@#$', '123#@!'])