L1 = [1, 9, 1, 6, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 2]
list=[]
for i in L1:
    if i not in list:
        list.append(i)
print(list)