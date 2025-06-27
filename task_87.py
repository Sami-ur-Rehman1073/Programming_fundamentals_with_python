# Write a Python program to generate a 
# palindrome of a given length from a string.

def paindrome_generator(string, n):
    
    paindrome = ""
    half_length = n//2
    for i in range(half_length):
        paindrome += string[i]
    if (len(string))%2 == 1:
        paindrome += "a"
    paindrome += paindrome[::-1]
    print(paindrome)

paindrome_generator("madam" , 7)
