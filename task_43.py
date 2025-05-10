#  Write a search Python program to filter for numbers 
# in a given list whose sum of digits is > 0, 
# where the first digit can be negative.

def sum_finder(x):
    list=[]
    for i in range(len(x)):
        p=str(x[i])
        string=""
        sum=0
        for j in range(len(p)):
            if len(p)==1:
                 sum=int(p)
            if len(p)==2 and "-" in p:
                if p[j]=="-":
                    string=p[j]+p[j+1]
                    q=int(string)
                    sum=sum+q
                    string=""
            if len(p)==2 and "-" not in p:
                    string=p[j]
                    q=int(string)
                    sum=sum+q
                    string=""
            if len(p)==3 and "-" in p:
                    if p[j]=="-":
                        string=p[j]+p[j+1]
                        q=int(string)
                        sum=sum+q
                    if p[j]!="-":
                        if j!=1: 
                            string=p[j]
                            q=int(string)
                            sum=sum+q
                    string=""
            if len(p)==3 and "-" not in p:
                    string=p[j]
                    q=int(string)
                    sum=sum+q
                    string=""
            if len(p)>3 and "-" in p:
                    if p[j]=="-":
                        string=p[j]+p[j+1]
                        q=int(string)
                        sum=sum+q
                    if p[j]!="-":
                        if j!=1: 
                            string=p[j]
                            q=int(string)
                            sum=sum+q
                    string=""
            if len(p)>3 and "-" not in p:
                    string=p[j]
                    q=int(string)
                    sum=sum+q
                    string=""
        if sum>0:
            r=int(p)
            list.append(r)
    print(list)


sum_finder([11, -6, -103, -200])