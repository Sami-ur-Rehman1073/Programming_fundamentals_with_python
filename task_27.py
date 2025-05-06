# Write a Python program to select a string from a given list 
# of strings with the most unique characters.

def unique_word_checker(x):
    max=0
    unique_word=""
    unique_count=0
    for i in range(len(x)):
        unique_letter_count=0
        p=x[i]
        for j in range(len(p)):
            q=p[j]
            for k in range(len(p)):
                if q==p[k]:
                    unique_count+=1
            if unique_count==1:
                    unique_letter_count+=1
            if unique_count>1:
                    unique_letter_count+=0
            unique_count=0
        if max<unique_letter_count:
                max=unique_letter_count
                unique_word=x[i]
    print(unique_word)
    print(max)

unique_word_checker(['Green', 'Red', 'Orange', 'Yellow', '', 'White'])