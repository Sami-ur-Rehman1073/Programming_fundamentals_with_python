# Write a Python program to find the longest string 
# in a given list of strings.
def longest_string_teller(list):
    max_count=0
    longest_string=""
    for i in range(len(list)):
        count=0
        for j in range(len(list[i])):
            count+=1
        if count>max_count:
            max_count=count
            longest_string=list[i]
    print(longest_string)

longest_string_teller(['cat', 'dog', 'shatter', 'donut', 'at', 'todo', ''])