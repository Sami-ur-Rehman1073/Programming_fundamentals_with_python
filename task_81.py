# Write a Python program to calculate the 
# average of the numbers a through b 
# (b not included) rounded to the nearest integer, 
# in binary (or -1 if there are no such numbers).

def binary_average(num1, num2):

    def average_finder(num1,num2):
        import math 
        sum=0
        for i in range(num1,num2):
            sum += i
        avg = math.floor(sum/(num2-num1))
        print(avg)
        return avg

    def binary_finder(avg):
        bin = ""
        while avg>0:
            remainder = avg%2
            bin = str(remainder) + bin
            avg = avg//2
        print(bin)


    avg= average_finder(num1,num2)
    binary_finder(avg)

binary_average(11, 19)
        