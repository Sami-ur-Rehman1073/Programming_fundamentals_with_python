# Write a Python program to find a string such that, 
# when three or more spaces are compacted to a '-' and 
# one or two spaces are replaced by underscores, 
# leads to the target.

def space_generator(string):
    required_string = ""
    for i in string:
        if i == "-":
            for j in range(2):
                required_string += " "
        if i == "_":
            for k in range(3):
                required_string += " " 
        if i != "-" and i !="_":
            required_string += i
    print(required_string)

space_generator(" -Hello,_world!__This_is-so-easy!-")
