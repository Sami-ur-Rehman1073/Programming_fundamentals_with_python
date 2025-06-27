#  Write a Python program to find the vowels from each of 
# the original texts (y counts as a vowel at the end of the word) 
# from a given list of strings.

# by iterative approach

def vowel_finder(list):
    vowels=['a','A','e','E','i','I','o','O','u','U']
    vowels_list=[]
    for i in list:
        vowels_found = ""
        for j in i:
            if j in vowels:
                vowels_found += j
        vowels_list.append(vowels_found)
    print(vowels_list)   

vowel_finder(['w3resource', 'Python', 'Java', 'C++'])
