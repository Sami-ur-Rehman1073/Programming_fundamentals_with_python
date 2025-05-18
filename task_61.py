# write a python program which calculates the sum of the digits of the
# whether the number is piositive or negative

def sum_calculator(x):
    string=""
    sum=0
    p=str(x)
    if '-' in p:
        for i in range(len(p)):
            if p[i]=="-":
                string=p[i]+p[i+1]
                q=int(string)
                sum=sum+q
            if p[i]!="-" and i!=1:
                string+=p[i]
                q=int(string)
                sum=sum+q
            string=""
    if '-' not in p:
        for i in range(len(p)):
            string+=p[i]
            q=int(string)
            sum=sum+q
            string=""
    print(sum)
            
sum_calculator(-21)