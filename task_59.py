# Write a Python program to find the string consisting of 
# all the words whose lengths are prime numbers.

def prime_length_finder(x):
   string=""
   con=""
   for i in range(len(x)):
        if x[i]!=" " and x[i]!="." and x[i]!=",":
            string+=x[i]
        if x[i]==" " or x[i]=="." or x[i]==",":
            p=len(string)
            for j in range(2,p):
                if p%j==0:
                    con="false"
                    break
            if con!="false":
                print(string,end=" ")
            string=""
            con=""
prime_length_finder("The quick brown fox jumps over the lazy dog.")