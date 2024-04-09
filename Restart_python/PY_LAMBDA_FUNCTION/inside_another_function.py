def my_func(n):
    return lambda a:n*a
x=my_func(5)
print(x(4))
