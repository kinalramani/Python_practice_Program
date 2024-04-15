def fibbonacci_no(n):
    a,b=0,1
    for i in range(n):
        a, b = b , a+b
        yield a
def square(num):
    for i in num:
        yield num**2
print(sum(square(fibbonacci_no(10))))
