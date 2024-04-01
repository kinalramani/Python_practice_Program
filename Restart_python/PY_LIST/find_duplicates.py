def find_duplicate(input_list):
    list=[]
    for i in input_list:
        if input_list.count(list) > 1 and i not in list:
            list.append(i)
    return list
input_list=[1,2,3,4,2,5,3]
f=find_duplicate(input_list)
print(f)