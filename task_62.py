# Write a Python program to find a string which, 
# when each character is shifted (ASCII incremented) 
# by shift, gives the result.

def ascii_shifter(string,shift):
    p=""
    if shift>0:
        for i in range(len(string)):
            a=ord(string[i])-shift
            p+=chr(a)
        print(p)
    if shift<0:
        x=str(shift)
        q=x[1]
        r=int(q)
        for i in range(len(string)):
            a=ord(string[i])+r
            p+=chr(a)
        print(p)

ascii_shifter("Ascii character table",-1)