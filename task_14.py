# Write a Python program to find the indexes of numbers in
# a given list below a given threshold.
def index_locater(threshold,list):
    index=0
    output_list=[]
    for i in range(len(list)):
        if list[i]<100:
            output_list.append(index)
        index+=1
    print(output_list)

index_locater(100,[0, 12, 45, 3, 4923, 322, 105, 29, 15, 39, 55])