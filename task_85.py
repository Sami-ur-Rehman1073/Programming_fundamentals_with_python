# Write a Python program to find the closest 
# palindrome to a given string.

def paindrome_generator(string):

    def paindrome_checker(string):
        reverse_string = list(reversed(string))
        if string == reverse_string:
            return True
        else:
            return False
   
    s = list(string)
    j = len(string)-1
    for i in range(len(s)):
        if paindrome_checker(s):
            for k in s:
                print(k,end="")
            break
        s[j] = s[i]
        j -= 1

paindrome_generator("racecbr")