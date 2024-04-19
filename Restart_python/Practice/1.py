def generators(n):
    for i in range(1,n+1):
        if i%5==0 and i%7==0:
            yield i
            
n=int(input("Enter your number:"))
values=[]
for i in generators(n):
    values.append(str(i))
print(",".join(values))