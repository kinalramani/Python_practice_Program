my_list = [("apple", 50), ("banana", 10), ("cherry", 30)]
shorted_list=sorted(my_list,key=lambda x,:x[1])
print(shorted_list)