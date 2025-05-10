#  Write a Python program to find all even palindromes up to n.

def paindrome_finder(n):
    list=[]
    for i in range(n):
        if i<9:
            if i%2==0:
                list.append(i)
        if i>9:
            p=str(i)
            num=p[::-1]
            q=int(num)
            r=int(p)
            if num==p and q%2==0:
                list.append(r)
    print(list)

paindrome_finder(500)