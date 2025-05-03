from random import *
length=10
x=[]
while len(x)<=length-1:
    p=randint(1,15)
    x.append(p)
print(x)
max_count=0
for i in range(len(x)):
    count=0
    for j in range(len(x)):
        if x[i]==x[j]:
            count+=1
        if count>max_count:
            max_count=count
            num=x[i]
print("The number",num,"has repeated maximunm times and it has repeated",max_count,"times")
