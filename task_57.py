# Write a Python program to find the dictionary key whose case 
# is different from all other keys.

def different_teller(x):
    upper_string=""
    lower_string=""
    upper_count=0
    lower_count=0
    for i in range(len(x)):
        p=x[i]
        if (65<=ord(p[0])<=90) or (97<=ord(p[0])<=122):
            if 65<=ord(p[0])<=90:
                upper_count+=1
                upper_string=p
            if 97<=ord(p[0])<=122:
                lower_count+=1
                lower_string=p
        else:
            for j in range(len(p)):
               if (65<=ord(p[j])<=90) or (97<=ord(p[j])<=122):
                if 65<=ord(p[j])<=90:
                    upper_count+=1
                    upper_string=p
                if 97<=ord(p[j])<=122:
                    lower_count+=1
                    lower_string=p
    if upper_count>lower_count:
        print(lower_string)
    if upper_count<lower_count:
        print(upper_string) 

different_teller(['RED', 'GREEN', 'orange', '#125GD'])