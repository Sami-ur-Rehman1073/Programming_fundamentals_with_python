# Write a Python program to split a string of words 
# separated by commas and spaces into 
# two lists, words and separators.
list_of_words=[]
list_of_punctuation=[]
def separator(x):
    string=''
    for i in range(len(x)):
        if x[i]!=' ' and x[i]!='.' and x[i]!=',':
            p=x[i]
            string=string+p
        if x[i]==' ' and string!='':
            list_of_words.append(string)
            if x[i] not in list_of_punctuation:
                list_of_punctuation.append(x[i])
            string=''
        if x[i]==',' or x[i]=='.':
            list_of_words.append(string)
            if x[i] not in list_of_punctuation:
                list_of_punctuation.append(x[i])
            string=''
    print(f'[{list_of_words},{list_of_punctuation}]')
separator('The party, ended happily.')