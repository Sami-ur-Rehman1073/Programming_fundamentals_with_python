# write a program which counts each alphabet in the list of strings

def alphabet_counter(x):
    a=65
    for i in range(26):
        count=0
        for j in range(len(x)):
            p=x[j]
            for k in range(len(p)):
                if p[k]==chr(a) or p[k]==chr(a+32):
                    count+=1
        print(f'The letter {chr(a+32)} has repeated {count} times')
        a=a+1


alphabet_counter(['cat', 'dog', 'shatter', 'donut', 'at', 'todo'])