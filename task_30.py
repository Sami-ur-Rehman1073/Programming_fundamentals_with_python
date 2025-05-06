# Write a search Python program to rescale and shift numbers in
# a given list, 
# so that they cover the range [0, 1].
def ranger(x):
    range_list=[]
    max=0
    min=10000000000000000000000000000
    for i in range(len(x)):
        if x[i]>max:
            max=x[i]
        if min>x[i]:
            min=x[i]
    for i in range(len(x)):
        range_num=(x[i]-min)/(max-min)
        range_list.append(range_num)
    print(range_list)

ranger([13.0, 17.0, 17.0, 15.5, 2.94])