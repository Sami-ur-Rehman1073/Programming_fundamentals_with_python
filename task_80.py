# Write a Python program to round each 
# float in a given list of numbers up to the next integer and 
# return the running total of the integer squares.

import math 

def rounded_squared_ints(nums):
    sum=0
    rounded_squared_list=[]
    for i in nums: 
        rounded_num = math.floor(i)+1
        squared_num = rounded_num**2
        sum+=squared_num
        rounded_squared_list.append(sum)
    print(rounded_squared_list)


rounded_squared_ints([2.6, 3.5, 6.7, 2.3, 5.6])



        
