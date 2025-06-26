# Write a Python program to round each 
# float in a given list of numbers up to the next integer and 
# return the running total of the integer squares.

def sum_of_squares(nums):
    final_list = []
    sum = 0
    for i in range(1 , len(nums)+1):
        rounded_num = (round(nums[i-1]))
        if rounded_num < nums[i-1]:
            rounded_num = rounded_num+1
        num = rounded_num**2
        sum += num
        final_list.append(sum)
    print(final_list)

sum_of_squares([301.1, 401.4, -23.1, 13554122.0, 10201.0101, 10000000.0])