# Sqrt of an integer without any built-in function

# By using binary search algorithm 

def sqrt(num):
    l, r = 1, num
    while l<=r:
        mid = (l+r)//2
        print(mid)
        mid_squared = mid*mid
        if mid_squared == num:
            return mid
        elif mid_squared < num:
            l = mid + 1
        else:
            r = mid - 1 
    return r

print(sqrt(49))

