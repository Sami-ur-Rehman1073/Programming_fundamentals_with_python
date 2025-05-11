# Write a Python program to find the product of the units digits
# in the numbers in a given list.

def unit_product_finder(x):
    product=1
    for i in range(len(x)):
        p=str(x[i])
        q=p[len(p)-1]
        r=int(q)
        product=product*r
    print(product)

unit_product_finder([1002, 2005])