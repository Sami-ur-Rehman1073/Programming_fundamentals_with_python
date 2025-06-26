#  Write a Python program to find the index of the largest 
# prime in the list and the sum of its digits.

def largest_prime(nums):
    index=0
    list=[]
    sum=0
    max=-100
    def is_prime(n):
        for i in range(2,n):
            if n%i==0:
             return False
        return True
    
    for i in range(len(nums)):
        if is_prime(nums[i]) is True:
           if max<nums[i]:
                max=nums[i]
                index=i
    p=str(max)
    for j in range(len(p)):
        sum+=int(p[j])
    list.append(index)
    list.append(sum)
    print(list)
    
           
        
            
largest_prime([23, 17, 201, 14, 10473, 43225, 421, 423, 11, 10, 2022, 342157])