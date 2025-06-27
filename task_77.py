#  Write a Python program to find the index of the
# matching parentheses for each 
# character in a given string.

def pair_checker(string):
    list_of_pairs = []
    for i in range(len(string)):
        for j in range(i,len(string)):
            if (string[i] == "(" and string[j] == ")") or (string[i] == ")" and string[j] =="("):
                if i not in list_of_pairs and j not in list_of_pairs:
                    list_of_pairs.append(i) ; list_of_pairs.append(j)
 
    print(list_of_pairs)

pair_checker("(()()()")
        