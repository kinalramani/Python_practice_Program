# list1=[10,20,30]
# list2=[10,20,30]
# reversed(list1)
# list2.reverse()
# print(list1)
# print(list2)

this_list=[35,30,50,45]
result=list(filter(lambda x: (x%15==0),this_list))
print(result)