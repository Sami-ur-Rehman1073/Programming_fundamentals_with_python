# Write a Python program to find all n-digit 
# integers that start or end with 2.

def start_end_finder(n):
    def integer_size_finder(n): 
        integer_size = 1
        for i in range(n-1):
            integer_size = integer_size * 10 
        return integer_size

    integer_size =  integer_size_finder(n)

    for i in range(integer_size, integer_size*10):
        start = i//integer_size
        end = i%10
        if start == 2 or end == 2:
            print(i,end= ",")
    
start_end_finder(3)
