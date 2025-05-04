# Write a Python program to find the largest number where commas or 
# periods are decimal points.
def max_finder(x):
    max=0
    string=""
    for i in range(len(x)):
        p=x[i]
        for j in range(len(p)):
            if p[j]!=",":
               string=string+p[j]
            if p[j]==",":
               string=string+"."  
        num=float(string)
        if max<num:
            max=num
        string=""
    print(max)

max_finder(['100', '102,1', '101.1','103,1'])