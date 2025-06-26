#  Write a Python program to reorder numbers from a given array in increasing/decreasing order based on whether the 
# first plus last element is odd/even.

def list_sorter(nums):
    if (nums[0]+nums[len(nums)-1])%2==0:
        nums.sort()
        print(nums)
    if (nums[0]+nums[len(nums)-1])%2!=0:
        nums.sort(reverse=True)
        print(nums)
    

list_sorter([1, 5, 6, 7, 4, 2, 8])