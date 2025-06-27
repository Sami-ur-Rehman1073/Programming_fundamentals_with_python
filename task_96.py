# Write a python program that returns the first letter that occur twice.

def first_twice_occur(string):
    seen_char = []
    for i in range(len(string)):
        if string[i] in string[i+1:len(string)-1]:
            return string[i]
    seen_char.append(i)

print(first_twice_occur("Missipi"))