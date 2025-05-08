# Write a search Python program to find the set of distinct characters 
# in a given string, ignoring case.

def distincter(x):
    list=[]
    for i in range(len(x)):
        count=0
        for j in range(len(x)):
            if x[i]==x[j]:
                count+=1
        if count==1:
            q=x[i]
        if ord(x[i])>=65 and ord(x[i])<=90:
           p=chr(ord(q)+32)
        if ord(x[i])>=97 and ord(x[i])<=122:
           p=chr(ord(q)-32)
        if p not in list:
            list.append(p)
    for i in range(len(x)):
        if chr(ord(x[i])) and chr(ord(x[i])+32) not in list:
            q=x[i]
            if ord(x[i])>=65 and ord(x[i])<=90:
                p=chr(ord(q)+32)
                list.append(p) 
            if ord(x[i])>=97 and ord(x[i])<=122:
                p=chr(ord(q)-32)
                list.append(p)   
    print(list)

distincter("HELLO")