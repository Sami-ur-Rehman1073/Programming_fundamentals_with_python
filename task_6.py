# Write a python program that tells 
# the reapeated words in the list of strings given
list=[]
list_2=[]
def word_repeat_teller(x):
    count=0
    for i in range(len(x)):
        p=x[i]
        for j in range(len(x[i])):
            list.append(p[j])
    print(list)
    for k in range(len(list)):
        count=0
        p=list[k]
        for l in range(len(list)):
            if p==list[l]:
                count+=1
        if p not in list_2:
            print(f'letter {p} is reapeated {count} times')
        list_2.append(p)
        
word_repeat_teller(['aaa','aaa'])