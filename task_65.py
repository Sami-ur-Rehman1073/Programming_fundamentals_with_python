#  Write a Python program to find the first 
# negative balance from a given list of numbers that 
# represent bank deposits and withdrawals.

def negative_balance_checker(withdrwals):
    sum=0
    negative_list=[]
    for i in range(len(withdrwals)):
        for j in range(len(withdrwals[i])):
            if withdrwals[i][0]<0:
                negative_list.append(withdrwals[i][0])
                break
            if withdrwals[i][0]>0:
                sum+=withdrwals[i][j]
                if sum<0:
                    negative_list.append(sum)
                    break
        if negative_list==[]:
            negative_list.append("None")
        sum=0
    print(negative_list)

negative_balance_checker([[-1200, 100, 1300], [100, 100, -2400]])