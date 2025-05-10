x="-103"
if "-" in x:
    for i in range(len(x)):
        if x[i]=="-":
            string=x[i]+x[i+1]
            p=int(string)
            print(p)
        if x[i]!="-" and i!=1:
            string=x[i]
            p=int(string)
            print(p)
        string=""


