n = 5
pre_num = 2
sum = 0

for i in range(0, n):
    print(pre_num, end=" + ")
    sum += pre_num
    
    pre_num = pre_num * 10 + 2
print(sum)