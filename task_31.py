#  Write a search Python program to find the 
# positions of all uppercase vowels (not counting Y) 
# in even indices of a given string.

def position_finder(x):
    list=[]
    index=0
    for i in range(len(x)):
        if x[i]==chr(65) or x[i]==chr(69) or x[i]==chr(73) or x[i]==chr(79) or x[i]==chr(85):
            if index%2==0:
                list.append(index)
        index+=1
    print(list)
position_finder("AEIOUYW")  