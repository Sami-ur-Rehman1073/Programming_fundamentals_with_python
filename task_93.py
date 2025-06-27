# write a python program to find the element which 
# occurs most times in an array

def most_occured(nums):
    counted = []
    num = 0
    max = 0
    for i in nums:
        if i not in counted:
            num_count = nums.count(i)
            if num_count > max:
                max = num_count
                num = i
        if i not in counted:
            counted.append(i)   
    return num

print(most_occured([1,2,3,1,2,3,1]))


# Finding the candidate using Boyer-Moore Voting Algorithm
# it is effective only when 
# (number of most repeating element)>len(nums)//2


def majority_element(nums):
    candidate = None
    count = 0
    for num in nums:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:     
            count -= 1
    return candidate

print(majority_element([2,2,2,2,1,1]))
        