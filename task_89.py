#  Given a string consisting of groups of matched nested 
# parentheses separated by parentheses, write a Python program to 
# compute the depth of each group.

def depth_finder(brackets):
    final_list = []
    depth = 0
    bracket_groups = brackets.split()
    for j in bracket_groups:
        for k in j:
            if k=="(":
                depth += 1
            if k==")":
                final_list.append(depth)
                depth = 0
                break

    print(final_list)
depth_finder("(((((((()))))))) () (()) ((()()()))")