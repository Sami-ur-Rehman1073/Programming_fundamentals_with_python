# Write a Python program to create a new string 
# by taking a string, and word by word rearranging its characters 
# in ASCII order.

def order_arranger(string):
    unordred_list=[]
    for i in range(len(string)):
        if string[i]!=" ":
            unordred_list.append(ord(string[i]))
        if string[i]==" " or i==len(string)-1:
            unordred_list.sort()
            for j in range(len(unordred_list)):
                print(chr(unordred_list[j]),end='')
            print(" ",end='')         
            unordred_list=[]

order_arranger("maltos won")