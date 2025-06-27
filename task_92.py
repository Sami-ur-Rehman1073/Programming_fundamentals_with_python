# write a python program to find largest substring from a string 
# with distinct characters.

def substring_finder(string):  
    list_of_substring = []
    substring = ""
    if string == "":
        longest_substring = "empty string"
        return longest_substring
    for i in range(len(string)):  
        if string[i] in substring:
            list_of_substring.append(substring)
            substring = ""  
        substring += string[i]
        if i == len(string)-1:
            list_of_substring.append(substring)
    max = len(list_of_substring[0])
    longest_substring = list_of_substring[0]
    for i in range(1,len(list_of_substring)):
        if len(list_of_substring[i]) > max:
            longest_substring = list_of_substring[i]
    return longest_substring
    
print(substring_finder("Abdullah"))