list=[1,2,3,4,5]
sum=0
number=0
for i in list:
    if i%2==0:
        sum+=i
    elif i%2!=0:
        number+=i
print("sum of even number!!",sum)
print("sum os odd number!!",number)