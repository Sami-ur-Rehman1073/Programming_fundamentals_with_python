# Write a Python program to find four positive even 
# integers whose sum is a given integer.

def sum_finder(n):
    error_msg = "No combination found"
    final_list = [2, 2, 2]
    a = b = c = 2
    d = n - (a + b + c)
    if d>0 and d%2 == 0:
        final_list.append(d)
        return final_list
    else:
        return error_msg
        
print(sum_finder(100))