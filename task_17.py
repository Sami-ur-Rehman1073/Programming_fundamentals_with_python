#  Write a Python program to find the length of a given 
# list of non-empty strings.
def length_teller(list):
    output_string=[]
    for i in range(len(list)):
        count=0
        for j in range(len(list[i])):
            count+=1
        output_string.append(count)
    print(output_string)

length_teller(['cat', 'dog', 'shatter', 'donut', 'at', 'todo', ''])