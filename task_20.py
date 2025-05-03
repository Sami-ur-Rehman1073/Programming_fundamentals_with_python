#  Write a Python program to split a given string (s) into strings if 
# there is a space in s, otherwise split on commas if there is a comma, 
# otherwise return 
# the list of lowercase letters in odd order
def splitter(x):
    list=[]
    if "," in x or " " in x:
        for i in range(len(x)):
            if x[i]!=" " and x[i]!=",":
                list.append(x[i])
    else:
        for j in range(len(x)):
            if j%2!=0:
                list.append(x[j])
    print(list)

splitter("abcd")