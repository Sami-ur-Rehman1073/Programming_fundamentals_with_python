# Write a Python program to find the sublist of numbers 
# from a given list of numbers with only odd digits in increasing order

def sublist_of_odd(nums):
    odd_list=[]

    def odd_checker(num):
        if abs(num)%2 == 0:
            return False
        return True
    
    for i in nums:
        if odd_checker(i) is True:
            odd_list.append(i)

    odd_list.sort()
    print(odd_list)

sublist_of_odd([1, 3, 79, 10, 4, 2, 39])