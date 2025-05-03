# Write a Python program to check whether the given 
# strings are palindromes or not.
# Return True otherwise False.
def string_return(list):
    output_list=[]
    for i in range(len(list)):
        if list[i]=='palindrome':
            output_list.append('true')
        if list[i]!='palindromes':
            output_list.append('false')
    print(output_list)

string_return(['palindrome', 'madamimadam', '', 'foo', 'eyes'])