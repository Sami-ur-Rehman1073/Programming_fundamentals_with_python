#  Write a Python program to find a list of all numbers that 
# are adjacent to a prime number in the list, 
# sorted without duplicates.

def adjacent_digit_teller(x):
    list=[]
    for i in range(len(x)):
        p=x[i]
        con=""
        for j in range(2,p):
            if p%j==0:
                con="false"
                break
        if con!="false" and x[i]!=0 and x[i]!=1:
            if i==0:
                q=x[1]
                if q not in list:
                    list.append(q)
            elif i==len(x)-1:
                q=x[len(x)-2]
                if q not in list:
                    list.append(q)
            elif i!=0 and i!=len(x)-1:
                q=x[i-1]
                if q not in list:
                    list.append(q)
                r=x[i+1]
                if r not in list:
                    list.append(r)
        
    list.sort()
    print(list)

adjacent_digit_teller([1, 2, 3, 5, 1, 16, 7, 11, 4])