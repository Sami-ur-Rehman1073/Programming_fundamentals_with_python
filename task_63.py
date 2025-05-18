#  Write a Python program to find all 5's in integers less than n 
# that are divisible by 9 or 15.

def divisibilty_checker(n):
    final_list=[]
    for i in range(15,n+1):
        num_list=[]
        num=str(i)
        if "5" in num:
            if int(num)%9==0 or int(num)%15==0:
                num_list.append(int(num))
                for j in range(len(num)):
                    if num[j]=="5":
                        num_list.append(j) 
                final_list.append(num_list)  
    
    print(final_list)