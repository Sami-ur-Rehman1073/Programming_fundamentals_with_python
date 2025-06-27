# write a program which returns true if there is a duplicate 
# in the string or an array and return false if there is no one 

def is_duplicate(a):
    if not a:
        return "string or list not given!"
    present = []
    for i in range(len(a)):
        if a[i] in present:
            return True 
        present.append(a[i])
    return False

print(is_duplicate("Misssipi"))