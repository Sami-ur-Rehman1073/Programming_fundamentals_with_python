# Write a Python program to find all integers <= 1000 that are the 
# product of exactly three primes. 
# Each integer should be represented as a list of its three prime factors.

def three_primes(n):
    
    final_list=[]

    def prime_checker(n):
        for j in range(2,n):
            if n%j == 0:
                return False
        return True
    
    for i in range(8,n+1):
        prime_factors = []
        while i!=0:
            for k in range(2,i+1):
                if i%k == 0:                    
                    if prime_checker(k) is True:
                        prime_factors.append(k)
                        break
            i = i//k
        if len(prime_factors)==3:
            final_list.append(prime_factors)

    print(final_list)

three_primes(10000)