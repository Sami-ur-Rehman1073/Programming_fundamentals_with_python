# A valid filename should end in .txt, .exe, .jpg, .png, or .dll, and should 
# have at most three digits, no additional periods. 
# Write a Python program to create a list of True/False that determine 
# whether candidate filename is valid or not.

def correct_filename_teller(x):
    con=""
    list=[]
    for i in range(len(x)):        
        if ".txt" in x[i] or ".exe" in x[i] or ".jpg" in x[i] or ".png" in x[i] or ".dll" in x[i]:
            r=x[i]
            p=len(x[i])
            q=p-4
            if q>=3:
                for j in range(q):
                    if r[j]==".":
                        con="No"
                        list.append(con)
                        break
                if con!="No":
                    list.append("Yes")
            if q<3:
                list.append("No")       
        elif ".txt" or ".exe" or ".jpg" or ".png" or ".dll" not in x[i]:
            list.append("No")
    print(list)

correct_filename_teller(['abc.txt', 'windows.dll', 'tiger.png', 'rose.jpg', 'test.py', 'win32.exe'])