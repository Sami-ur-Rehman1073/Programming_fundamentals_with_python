# A string is happy if every three consecutive characters are distinct.
# Write a Python program to find two indices associated with a 
# given string being unhappy.

def distinct_checker(string):
    con=None
    for i in range(len(string)):
        if string[i-1]==string[i]:
            print([i-1,i])
            con="True"
            break
    if con is None:
        print(con)


distinct_checker("Find")