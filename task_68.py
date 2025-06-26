# . Write a Python program to find a substring in a given string that 
# contains a vowel between two consonants.

def vowel_finder(string):
    vowels=["A","a","E","e","I","i","O","o","U","u"]
    for j in range(1,len(string)-1):
        if string[j] in vowels:
            if string[j-1] not in vowels and string[j+1] not in vowels:
                print(string[j-1],string[j],string[j+1],end=" ")

vowel_finder("Halal")