#  Write a Python program to find the largest negative and 
# smallest positive numbers (or 0 if none).

# without sort function

def largest_negative_smallest_positive(nums):
    largest_negative = None
    smallest_positive = None
    for i in nums:
        if i < 0:
            if largest_negative is None or i > largest_negative:
                largest_negative = i
        if i > 0:
            if smallest_positive is None or i < smallest_positive:
                smallest_positive = i
    
    if largest_negative is None:
        largest_negative = 0
    if smallest_positive is None:
        smallest_positive = 0   

    print([largest_negative,smallest_positive])


largest_negative_smallest_positive([-1, -2, -3, -4])