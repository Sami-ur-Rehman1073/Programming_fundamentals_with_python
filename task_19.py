# write a program which tells that whether a
# sequence is increasing or decreasing
def sequence_checker(list):
    p=list[0]
    for i in range(len(list)):
        if i>=1:
            if p<list[i]:
                sequence="increasing"
            if p>list[i] or p==list[i]:
                sequence=""
                break
            p=list[i]
    p=list[0]
    if sequence=="":
        for j in range(len(list)):
            if j>=1:
                if p>list[j]:
                    sequence="decreasing"
                if p<list[j] or p==list[j]:
                    sequence=""
                    break 
                p=list[i]        
    if sequence!="":
        print(sequence)
    if sequence=="":
        print("The numbers are not in monotonic order")

sequence_checker([1,2,3,4,5])
        