# Given a string consisting of whitespace andgroups of matched 
# parentheses, write a Python program to split it into 
# groups of perfectly matched parentheses 
# without any whitespace.


def white_space_remover(brackets):
    list_of_brackets = []
    temp=""
    opening_bracket = 0
    closing_bracket = 0
    for i in brackets:
        if i!=" ":
            if i=="(":
                opening_bracket += 1
            else:
                closing_bracket += 1 
            temp = temp + i
            if opening_bracket == closing_bracket:
                list_of_brackets.append(temp)
                opening_bracket = 0
                closing_bracket = 0
                temp = ""
    
    print(list_of_brackets)

white_space_remover("( ()) ((()()())) (()) ()")
        