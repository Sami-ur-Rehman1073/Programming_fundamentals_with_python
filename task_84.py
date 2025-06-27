#  Write a  Python program to start 
# with a list of integers, keep every other element in place 
# and otherwise sort the list.

def even_sorter(nums):
    no_of_passes = len(nums)//2
    for j in range(no_of_passes):
        for i in range(0,len(nums),2): 
            if i!= len(nums)-1 and i!= len(nums)-2:           
                if nums[i] > nums[i+2]:                 
                    nums[i], nums[i+2] = nums[i+2], nums[i]
    print(nums)

even_sorter([2, 5, 6, 3, 1, 4, 8, 43, 0])