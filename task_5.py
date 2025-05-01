# Write a Python program to check the repition of atleast one character in the given list of strings
def proper_substring(x):
    n=x[0]
    for i in range(len(x)):
        if n not in x[i]:
            print("False")
            break
        if n in x[i] and i==(len(x))-1:
            print("True")
       
proper_substring(['a','abc','abc','abc'])