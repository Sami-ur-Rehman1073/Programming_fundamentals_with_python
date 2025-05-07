#  Write a search Python program to compute the 
# product of the odd digits in a given number,
# or 0 if there aren't any.

def product_teller(x):
    product=1
    for i in range(len(x)):
        p=int(x[i])
        if p%2!=0:
            product=product*p
    if product==1:
        print(f'product: 0')
    else:
        print(f'product: {product}')

product_teller("123456789")