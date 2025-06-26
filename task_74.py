# Write a Python program to calculate the average of the numbers 
# a through b (b not included) rounded to the nearest integer, 
# in binary (or -1 if there are no such numbers).

def convert_average_into_binary(a,b):
    sum=0
    def binary_converter(num):
        binary_number = ""
        while num >= 1:
           binary_number = str(num%2) + binary_number 
           num = num//2
        print(binary_number)

    for i in range(a,b):
        sum += i
    avg = round(sum/abs(a-b))
    binary_converter(avg)
    

convert_average_into_binary(11,19)