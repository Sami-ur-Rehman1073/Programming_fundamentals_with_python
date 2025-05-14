#  Write a Python program to find the sum of the magnitudes 
# of the elements in the array. 
# This sum should have a sign that is equal to 
# the product of the signs of the entries.

def sum_and_magnitude_finder(x):
    sum=0
    final_sign=1
    for i in range(len(x)):
        num=""
        p=str(x[i])
        if "-" in p:
            sign=-1
        else:
            sign=1
        for j in range(len(p)):
            if p[j]!="-":
                num+=p[j]
        q=int(num)
        final_sign=final_sign*sign
        sum+=q
    final_answer=final_sign*sum
    print(final_answer)
sum_and_magnitude_finder([-25, -12, -23])        