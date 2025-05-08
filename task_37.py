# Write a search Python program to find strings that, 
# when case is flipped, give a target where vowels 
# are replaced by characters two later.

def case_flipper(x):
    p=""
    for i in range(len(x)):
        if ord(x[i])==65 or ord(x[i])==69 or ord(x[i])==73 or ord(x[i])==79 or ord(x[i])==85:
            r=ord(x[i])+2
            q=chr(r+32)
            p+=q
        elif ord(x[i])==97 or ord(x[i])==101 or ord(x[i])==105 or ord(x[i])==111 or ord(x[i])==117:
            r=ord(x[i])+2
            q=chr(r-32)
            p+=q
        elif ord(x[i])>=65 and ord(x[i])<=90:
            r=ord(x[i])+32
            q=chr(r)
            p+=q
        elif ord(x[i])>=97 and ord(x[i])<=122:
            r=ord(x[i])-32
            q=chr(r)
            p+=q
    print(p)

case_flipper("aeiou")