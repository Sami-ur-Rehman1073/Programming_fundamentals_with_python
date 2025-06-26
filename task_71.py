# Write a Python program to find the two closest distinct numbers 
# in a given list of numbers.


# without sort function

def distinct_numbers(nums):
    min_sum = abs(nums[1] - nums[2])
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] != nums[j]:
                if min_sum > abs(nums[i] - nums[j]):
                    list = []
                    min_sum=abs(nums[i] - nums[j])
                    # for ascending arrangement
                    if nums[i] > nums[j]:
                        list.append(nums[j]) ; list.append(nums[i])
                    else:
                        list.append(nums[i]) ; list.append(nums[j])

    print(list)
            
distinct_numbers([5.24, 5.27, 0.89, 21.0, 5.27, 1.3])
    

# with sort function


def distinct_numbers(nums):
    min=10000000
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i]!=nums[i+1]:
            if abs(nums[i]-nums[i+1]) < min:
                min = abs(nums[i]-nums[i+1])
                list=[]
                list.append(nums[i])
                list.append(nums[i+1])

    print(list)
            
distinct_numbers([12.02, 20.3, 15.0, 19.0, 11.0, 14.99, 17.0, 17.0, 14.4, 16.8])
