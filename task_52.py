# write a program which tells whether a number is a paridrome or not.

def paridome_teller(x):
    string=""
    p=str(x)
    if "-" in p:
        print("The number is not a paridrome")
    else:
        for i in range(len(p)-1,-1,-1):
            string+=p[i]
        q=int(string)
        if q==x:
            print("The number is a paridrome")
        else:
            print("The number is not a paridrome")

paridome_teller(4)