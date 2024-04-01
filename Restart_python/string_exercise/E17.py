str1 = "Emma25 is Data scientist50 and AI Expert"
str1=str1.split()
for i in str1:
    for j in i:
        if j.isnumeric():
            print(i)
            break