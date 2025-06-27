# Write a Python program to find an increasing sequence consisting 
# of the elements of the original list

# by itrative approach

def increasing_order_sorter(nums):
    sorted_list=[]

    def min_finder(nums):
        min = nums[0]
        for i in nums:
            if i<min:
                min=i
        return min
    
    for i in range(len(nums)):
        if nums==[]:
            break
        min_num = min_finder(nums)
        sorted_list.append(min_num)
        nums.remove(min_num)
    
    print(sorted_list)

increasing_order_sorter([11, 31, 40, 68, 77, 93, 48, 1, 57])   


# by recursive approach

def increasing_order_sorter(nums,sorted_list = None):
    if nums == []:
        print(sorted_list)
        return 
    if sorted_list is None:
        sorted_list=[]

    def min_finder(nums):
        min = nums[0]
        for i in nums:
            if i<min:
                min=i
        return min
    
    min_num=min_finder(nums)
    sorted_list.append(min_num)
    nums.remove(min_num)
    increasing_order_sorter(nums,sorted_list)

increasing_order_sorter([11, 31, 40, 68, 77, 93, 48, 1, 57])