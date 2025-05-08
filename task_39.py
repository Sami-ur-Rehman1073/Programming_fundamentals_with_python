# Write a Python program to find all words 
# in a given string with n consonants.

def consonant_finder(x,n):
    max=0
    list=[]
    string=""
    consonant_count=0
    for i in range(len(x)):
        if  ord(x[i])!=97 and ord(x[i])!=101 and ord(x[i])!=105 and ord(x[i])!=111 and ord(x[i])!=117:
            consonant_count+=1
        if x[i]!=" ":
            string+=x[i]
        if consonant_count>max:
            max=consonant_count        
        if consonant_count==n:
            list.append(string)
        if x[i]==" ":
            consonant_count=0
            string=""
    print(list)

consonant_finder("this is our time",3)