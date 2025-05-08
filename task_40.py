#  Write a search Python program to find which characters of 
# a hexadecimal number correspond to prime numbers.

def heexadecimal_checker(x):
    list=[]
    con=""
    q="BD"
    for i in range(len(x)):
        if ord(x[i])>=65:
            if x[i]=="B" or x[i]=="D":
                list.append("True")
            else:
                list.append("False")
        if ord(x[i])<65:
            p=int(x[i])
            if p==1:
                con="false"
            if p==2:
                con="true"
            if p>2:
                for j in range(2,p):
                    if p%j!=0:
                        con="true"
                    if p%j==0:
                        con="false"
                        break
            list.append(con)
    print(list)

heexadecimal_checker("FACE")